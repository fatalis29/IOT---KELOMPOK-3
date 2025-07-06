# main.py – FloodGuard

import network
import urequests
import time
from machine import Pin, PWM, I2C, time_pulse_us

# lcd_api.py (in-line) 
class LcdApi:
    LCD_CLR        = 0x01
    LCD_HOME       = 0x02
    LCD_ENTRY_MODE = 0x04
    LCD_DISPLAY_CTL= 0x08
    LCD_FUNCTION   = 0x20
    LCD_SET_DDRAM  = 0x80

    def __init__(self, num_lines, num_columns):
        self.num_lines   = num_lines
        self.num_columns = num_columns
        time.sleep_ms(20)
        self._init_lcd()

    def _init_lcd(self):
        # 4-bit, 2 lines, display on, backlight on
        self.hal_command(self.LCD_FUNCTION | 0x08)
        time.sleep_ms(5)
        self.hal_command(self.LCD_DISPLAY_CTL | 0x04)
        time.sleep_ms(5)
        self.clear()
        self.hal_command(self.LCD_ENTRY_MODE | 0x02)
        time.sleep_ms(5)

    def clear(self):
        self.hal_command(self.LCD_CLR)
        time.sleep_ms(2)

    def move_to(self, col, row):
        addr = col + 0x40 * row
        self.hal_command(self.LCD_SET_DDRAM | addr)

    def putstr(self, text):
        for ch in text:
            self.hal_data(ord(ch))

    # abstract methods
    def hal_command(self, cmd):
        raise NotImplementedError()

    def hal_data(self, data):
        raise NotImplementedError()

# i2c_lcd.py (in-line)
from time import sleep_ms
MASK_RS        = 0x01
MASK_RW        = 0x02
MASK_E         = 0x04
MASK_BACKLIGHT = 0x08

class I2cLcd(LcdApi):
    def __init__(self, i2c, addr, rows, cols):
        self.i2c       = i2c
        self.addr      = addr
        self.backlight = MASK_BACKLIGHT
        # init sequence
        self.i2c.writeto(addr, bytearray([0]))
        sleep_ms(20)
        for _ in range(3):
            self._write_init_nibble(self.LCD_FUNCTION)
            sleep_ms(5)
        super().__init__(rows, cols)

    def _write_init_nibble(self, nibble):
        data = nibble & 0xF0
        self.i2c.writeto(self.addr, bytearray([data | MASK_E]))
        self.i2c.writeto(self.addr, bytearray([data]))

    def hal_write4(self, data):
        # send high nibble then low nibble
        self.i2c.writeto(self.addr, bytearray([data | self.backlight | MASK_E]))
        self.i2c.writeto(self.addr, bytearray([data | self.backlight]))

    def hal_command(self, cmd):
        self.hal_write4(cmd & 0xF0)
        self.hal_write4((cmd << 4) & 0xF0)

    def hal_data(self, data):
        self.hal_write4(MASK_RS | (data & 0xF0))
        self.hal_write4(MASK_RS | ((data << 4) & 0xF0))

# Konfigurasi & Inisialisasi
SSID       = "Kuota anda habis???"
PASSWORD   = "raikirixryuusei"
BLYNK_AUTH = "s-DceF79DKZ5mg7dH-mOGykPPf0_V6nz" # token authentic blynk
BLYNK_API  = "https://sgp1.blynk.cloud/external/api/update"  

TH_SAFE, TH_FLOOD = 5.0, 3.0

TRIG_PIN, ECHO_PIN = 5, 18
LED_PIN, BUZZER_PIN = 2, 15
I2C_SDA, I2C_SCL = 21, 22

trig   = Pin(TRIG_PIN, Pin.OUT)
echo   = Pin(ECHO_PIN, Pin.IN)
led    = Pin(LED_PIN, Pin.OUT)
buzzer = PWM(Pin(BUZZER_PIN), freq=2000)
buzzer.duty(0)

i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

#  Fungsi Utama 
def connect_wifi(timeout=15):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    t0 = time.time()
    while not wlan.isconnected():
        if time.time() - t0 > timeout:
            print("⚠ Wi-Fi timeout")
            return False
        time.sleep(0.1)
    print("✔ Wi-Fi:", wlan.ifconfig()[0])
    return True

def read_distance():
    trig.value(0); time.sleep_us(2)
    trig.value(1); time.sleep_us(10)
    trig.value(0)
    dur = time_pulse_us(echo, 1, 30000)
    return None if dur < 0 else (dur * 0.0343) / 2

def send_blynk(pin, val):
    try:
        url = "{}?token={}&{}={}".format(BLYNK_API, BLYNK_AUTH, pin, val)
        r = urequests.get(url)
        r.close()
    except Exception as e:
        print("⚠ Blynk error:", e)

def update_lcd(dist, status):
    lcd.clear()
    if dist is None:
        lcd.putstr("No echo!")
    else:
        lcd.putstr("Lv:{:.1f}cm".format(dist))
        lcd.move_to(0,1)
        lcd.putstr(status)

def main():
    if not connect_wifi():
        lcd.clear(); lcd.putstr("Wi-Fi Fail"); return

    lcd.clear(); lcd.putstr("FloodGuard Ready"); time.sleep(1)

    while True:
        d = read_distance()
        print("DEBUG distance =", d)
        if d is None:
            status = "NoEcho"; led.value(0); buzzer.duty(0)
        else:
            send_blynk("V0", round(d,1))
            if d >= TH_SAFE:
                status = "Aman"; led.value(1); buzzer.duty(0)
            elif d < TH_FLOOD:
                status = "Banjir"; led.value(0); buzzer.duty(768)
            else:
                status = "Rawan"; led.value(0); buzzer.duty(0)
            send_blynk("V1", status)
        update_lcd(d, status)
        print("Lv={:.1f}cm → {}".format(d if d else 0, status))
        time.sleep(5)

if __name__ == "__main__":
    main()

