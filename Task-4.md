# 📦 Task 4: Implementasi Hardware

## 🎯 Milestone
Perakitan dan pengujian awal perangkat keras untuk sistem pemantauan ketinggian air berbasis IoT dengan koneksi ke platform **Blynk**.

---

## 1. Komponen yang Digunakan

| No | Nama Komponen              | Jumlah | Keterangan                              |
|----|----------------------------|--------|------------------------------------------|
| 1  | ESP32 DevKit V1            | 1      | Mikrokontroler utama dengan Wi-Fi        |
| 2  | Sensor Ultrasonik HC-SR04  | 1      | Mengukur jarak permukaan air             |
| 3  | LED Merah                  | 1      | Indikator lokal status bahaya            |
| 4  | Buzzer                     | 1      | Memberikan peringatan suara lokal        |
| 5  | Resistor 220Ω              | 2      | Untuk LED dan buzzer                     |
| 6  | Breadboard                 | 1      | Perakitan sirkuit                        |
| 7  | Kabel Jumper               | ≥8     | Menghubungkan antar komponen             |
| 8  | Power Supply (USB/baterai) | 1      | Menyalakan ESP32                         |
| 9  | Aplikasi Blynk IoT         | 1      | Visualisasi data dan pengiriman notifikasi|

---

## 2. Skema Rangkaian dan Wiring

### Wiring Teks:
| Komponen           | Terhubung ke ESP32     |
|--------------------|------------------------|
| HC-SR04 VCC        | 3V3                    |
| HC-SR04 GND        | GND                    |
| HC-SR04 TRIG       | GPIO 5                 |
| HC-SR04 ECHO       | GPIO 18 (via voltage divider jika perlu) |
| LED Anoda (+)      | GPIO 4 (via resistor 220Ω) |
| Buzzer Positif (+) | GPIO 2 (via resistor 220Ω) |
| LED & Buzzer GND   | GND Breadboard (sama dengan ESP32) |

---

### Ilustrasi Diagram:
![Wiring Diagram]![image](https://github.com/user-attachments/assets/37be26c8-87f1-4492-b07a-ef495285b96a)



> Diagram ini menunjukkan koneksi antara ESP32, sensor HC-SR04, LED, dan buzzer. Semua komponen dihubungkan dengan jalur ground bersama dan siap untuk terintegrasi dengan sistem Blynk.

---

## 3. Langkah-Langkah Perakitan

1. Tempatkan ESP32 dan HC-SR04 di breadboard.
2. Lakukan koneksi TRIG dan ECHO ke GPIO 5 dan 18.
3. Pasang LED ke GPIO 4, dan buzzer ke GPIO 2 menggunakan resistor pembatas arus.
4. Pastikan semua GND terhubung dengan baik.
5. Siapkan koneksi Wi-Fi pada ESP32 sebagai persiapan integrasi dengan **Blynk**.
6. Unduh aplikasi **Blynk IoT**, buat project baru, dan siapkan:
   - Auth Token (nanti dipakai di kode program)
   - Virtual Pin (misal: V0 untuk nilai jarak, V1 untuk status banjir)
   - Widget: Value Display, Notification, Gauge

---

## 4. Pengujian Awal Hardware

- Perangkat dihubungkan ke laptop melalui USB.
- Sensor HC-SR04 dapat membaca jarak dan menampilkannya di Serial Monitor.
- LED menyala dan buzzer berbunyi saat kondisi jarak < 20 cm.
- Tes awal koneksi Wi-Fi berhasil dilakukan melalui sketch sederhana `WiFi.begin(...)`.
- Koneksi awal dengan Blynk telah dicoba menggunakan Auth Token (akan diperluas di Task 5).

---

## 5. Dokumentasi

- Wiring diagram telah dibuat (lihat gambar di atas).
- Rangkaian diuji dan berhasil mendeteksi perubahan ketinggian air.
- Persiapan untuk koneksi cloud (Blynk) sudah dimulai.
- Data dan status perangkat disiapkan untuk dihubungkan ke Virtual Pin.

---
