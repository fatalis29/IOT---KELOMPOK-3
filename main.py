# main.py – IoT Flood Monitoring (tanpa LCD), safe for Thonny introspection

import network
import urequests
import time
from machine import Pin, PWM, time_pulse_us, reset

# — Konfigurasi Wi-Fi & Blynk —
SSID       = "Kuota anda habis???"
PASSWORD   = "raikirixryuusei"
BLYNK_AUTH = "Your_Blynk_Token"
BLYNK_API  = "http://blynk.cloud/external/api/update"

# — Ambang Banjir (cm) —
TH_SAFE   = 5.0   # ≥5 cm → Aman
TH_FLOOD  = 3.0   # <3 cm → Banjir

# — Pin Setup —
TRIG_PIN   = 5    # HC-SR04 Trig
ECHO_PIN   = 18   # HC-SR04 Echo
LED_PIN    = 2    # LED
BUZZER_PIN = 15   # Buzzer

# Global handles (injeksi di fungsi init)
trig = echo = led = buzzer = None

def init_hardware():
    """Inisialisasi semua GPIO dan PWM; tidak ada side-effect di import."""
    global trig, echo, led, buzzer

    # Ultrasonik
    trig = Pin(TRIG_PIN, Pin.OUT)
    echo = Pin(ECHO_PIN, Pin.IN)

    # LED + Buzzer
    led    = Pin(LED_PIN, Pin.OUT)
    buzzer = PWM(Pin(BUZZER_PIN), freq=1000)
    buzzer.duty(0)

    print("Hardware siap: TRIG, ECHO, LED, Buzzer diinisialisasi")

def connect_wifi(timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > timeout:
            raise RuntimeError("Gagal koneksi Wi-Fi")
        time.sleep(0.1)
    print("Wi-Fi OK, IP:", wlan.ifconfig()[0])

def read_distance():
    """Kembalikan jarak dalam cm atau None jika timeout."""
    trig.value(0); time.sleep_us(2)
    trig.value(1); time.sleep_us(10)
    trig.value(0)
    dur = time_pulse_us(echo, 1, 30000)
    if dur < 0:
        return None
    return (dur * 0.0343) / 2

def send_blynk(pin, value):
    try:
        url = "{}?token={}&pin={}&value={}".format(BLYNK_API, BLYNK_AUTH, pin, value)
        res = urequests.get(url)
        res.close()
        if res.status_code != 200:
            print("Blynk HTTP error:", res.status_code)
    except Exception as e:
        print("Blynk error:", e)

def main():
    """Fungsi utama: inisialisasi → koneksi → loop pengukuran & pengiriman."""
    init_hardware()

    try:
        connect_wifi()
    except Exception as e:
        print(e)

    while True:
        d = read_distance()
        if d is None:
            print("No echo")
        else:
            if   d >= TH_SAFE:   status, led_val, buz_duty = "Aman", 1,   0
            elif d <  TH_FLOOD:  status, led_val, buz_duty = "Banjir", 0, 512
            else:                status, led_val, buz_duty = "Rawan",  0,   0

            led.value(led_val)
            buzzer.duty(buz_duty)
            print("Jarak: {:.1f} cm → {}".format(d, status))
            send_blynk("V0", round(d,1))
            send_blynk("V1", {"Aman":0,"Rawan":1,"Banjir":2}[status])

        time.sleep(5)

# **Tidak ada** pemanggilan main() di level modul:
# Agar Thonny tidak langsung menjalankan loop saat import/get_globals.