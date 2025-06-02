# Judul
IoT Flood Monitoring System with ESP32 & HC-SR04
 # Deskripsi Singkat
 Proyek ini akan menghadirkan sistem pemantauan banjir sederhana berbasis ESP32 yang mengukur ketinggian air menggunakan sensor ultrasonik HC-SR04, mengirimkan data ke Blynk untuk visualisasi real-time, serta memberikan indikator lokal via LED dan buzzer. Sistem dirancang untuk memudahkan deteksi dini kenaikan air, mendukung aksi cepat, dan dapat diimplementasikan dengan komponen minimal.

 # SDGs yang Disasar
 1. SDG 11: Sustainable Cities and Communities – Meningkatkan ketahanan komunitas terhadap risiko banjir dengan teknologi IoT
 2. SDG 13: Climate Action – Mendukung mitigasi dampak perubahan iklim lewat sistem peringatan dini bencana banjir

# Gambar Skema Blok Sistem
![WhatsApp Image 2025-06-02 at 10 32 01](https://github.com/user-attachments/assets/6fda2b67-67c7-460f-977a-036b5c50d030)



 # Penjelasan Singkat Skema Blok Sistem
 
Input: HC-SR04 Ultrasonic Sensor
HC-SR04 menggunakan dua pin—Trig (D5) dan Echo (D18)—untuk menghitung jarak ke permukaan air 
. Sensor dipasang sedemikian rupa sehingga gelombang ultrasonik dipantulkan oleh permukaan air dan diterima kembali, memberikan pembacaan jarak dalam sentimeter 

Proses: ESP32 DevKit V1
ESP32 membaca sinyal Echo dari HC-SR04 dan mengonversi durasi pulsa menjadi jarak (cm) menggunakan rumus waktu × kecepatan suara/2 
. Setelah memperoleh nilai jarak, ESP32 membandingkannya dengan ambang: jika jarak ≥ 5 cm, itu dianggap kondisi "Aman" ; jika < 3 cm, dianggap bahaya banjir (“Banjir”); dan jika berada di antara 3 – 5 cm, statusnya “Rawan” (hanya LED/buzzer mati) 
. ESP32 juga dapat mem-publish data level air ke Blynk melalui koneksi Wi-Fi untuk monitoring jarak jauh 

Output: LED & Buzzer
LED (D 13): Menyala  di antara < 3 – 5 cm (nilai level air rendah) untuk menandakan kondisi "Rawan" 

Buzzer (D 12): Berbunyi ketika jarak < 3 cm (nilai level air sangat tinggi) untuk memberikan peringatan audio


# Daftar Komponen yang Diperlukan
1. ESP32-DevKitC
2. Ultrasonic Sensor HC-SR04
3. Resistor Divider
4. LED + Buzzer
5. Breadboard & Jumper Wires
6. USB-MicroUSB Cable
