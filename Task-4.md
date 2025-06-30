# 📦 Task 4: Implementasi Hardware

Perakitan dan pengujian awal perangkat keras untuk sistem pemantauan ketinggian air berbasis IoT.

---

## 1. Komponen yang Digunakan

| No | Nama Komponen              | Jumlah | Keterangan                              |
|----|----------------------------|--------|------------------------------------------|
| 1  | ESP32 DevKit V1            | 1      | Mikrokontroler dengan koneksi Wi-Fi      |
| 2  | Sensor Ultrasonik HC-SR04  | 1      | Mengukur jarak air ke permukaan          |
| 3  | Breadboard                 | 1      | Media perakitan sirkuit sementara        |
| 4  | Kabel Jumper               | ≥6     | Menghubungkan komponen                   |
| 5  | Resistor 1kΩ dan 2kΩ       | @1     | Untuk voltage divider (pin Echo)         |
| 6  | Power Supply (USB/baterai) | 1      | Sumber daya untuk ESP32                  |

---

## 2. Skema Rangkaian dan Wiring

### Wiring Teks:
| Sensor HC-SR04 | ESP32        |
|----------------|--------------|
| VCC            | 3V3          |
| GND            | GND          |
| TRIG           | GPIO 5       |
| ECHO           | GPIO 18 (via voltage divider) |

### Catatan Teknik:
Pin ECHO HC-SR04 memiliki output 5V, sedangkan ESP32 hanya menerima 3.3V. Untuk mencegah kerusakan, digunakan **voltage divider** menggunakan resistor 1kΩ dan 2kΩ untuk menurunkan tegangan.

### Ilustrasi Diagram:
Diagram wiring dapat dibuat menggunakan Fritzing atau simulator seperti Wokwi.

---

## 3. Langkah-Langkah Perakitan

1. Tempatkan ESP32 dan sensor HC-SR04 pada breadboard.
2. Hubungkan:
   - VCC → 3V3
   - GND → GND
   - TRIG → GPIO 5
   - ECHO → GPIO 18 (melalui voltage divider)
3. Sambungkan ESP32 ke laptop dengan kabel USB.
4. Pastikan koneksi kuat dan tidak longgar.
5. Siapkan perangkat lunak untuk pengujian awal.

---

## 4. Pengujian Awal Hardware

- ESP32 dihubungkan ke laptop dan dipantau melalui **Serial Monitor** di Arduino IDE.
- Program dasar diunggah untuk membaca jarak dari sensor.
- Hasil pembacaan tampil dalam satuan cm.
- Sensor menunjukkan respons dinamis saat objek mendekat/menjauh.

---


