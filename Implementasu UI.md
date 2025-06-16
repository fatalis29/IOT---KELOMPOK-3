# Pendahuluan
Bencana banjir merupakan salah satu permasalahan lingkungan yang sering terjadi di berbagai wilayah Indonesia. Banjir tidak hanya mengakibatkan kerugian material, tetapi juga berdampak serius terhadap keselamatan jiwa, kesehatan masyarakat, serta gangguan pada aktivitas sosial dan ekonomi. Oleh karena itu, diperlukan sistem peringatan dini yang efektif untuk memantau ketinggian air secara real-time dan memberikan peringatan cepat kepada masyarakat agar dapat mengambil langkah mitigasi yang tepat.

Seiring dengan berkembangnya teknologi Internet of Things (IoT), kini dimungkinkan untuk membangun sistem pemantauan banjir berbasis sensor yang terhubung ke internet dan dapat diakses dari mana saja. Teknologi ini memungkinkan pengukuran otomatis terhadap ketinggian air dan pengiriman data secara langsung ke dashboard digital yang dapat dimonitor oleh warga, relawan, maupun otoritas terkait.

Proyek ini mengusulkan implementasi sistem pemantauan banjir sederhana menggunakan ESP32 dan sensor ultrasonik HC-SR04. Sistem ini dirancang untuk mengukur level permukaan air, mengklasifikasikan statusnya (aman, rawan, atau banjir), serta mengirimkan informasi tersebut ke platform Blynk sebagai antarmuka pengguna (user interface). Selain itu, indikator lokal seperti LED dan buzzer turut digunakan untuk memberikan peringatan langsung di lokasi.

Melalui proyek ini, diharapkan dapat diwujudkan prototipe sistem monitoring banjir yang murah, mudah diterapkan, serta mendukung Sustainable Development Goals (SDGs) 13 (Climate Action).

2. Latar Belakang
Perubahan iklim yang ekstrem menyebabkan curah hujan yang tidak menentu dan meningkatnya risiko banjir, khususnya di daerah perkotaan yang memiliki sistem drainase terbatas. Sering kali banjir terjadi tanpa peringatan, dan informasi mengenai kondisi air tidak tersedia secara real-time.

Dalam beberapa tahun terakhir, teknologi IoT telah digunakan untuk mengatasi berbagai permasalahan lingkungan dan bencana. IoT memungkinkan perangkat-perangkat fisik seperti sensor dan mikrokontroler saling terhubung, mengumpulkan data, dan mengirimkannya ke cloud untuk diakses oleh pengguna. Dengan pendekatan ini, pemantauan banjir tidak lagi harus dilakukan secara manual, tetapi bisa dilakukan secara otomatis, akurat, dan cepat.

Salah satu perangkat mikrokontroler yang populer dalam pengembangan sistem IoT adalah ESP32, karena memiliki koneksi Wi-Fi bawaan dan mendukung pengolahan data secara lokal. Digabungkan dengan sensor HC-SR04, yang mampu mengukur jarak dengan gelombang ultrasonik, perangkat ini dapat memantau permukaan air dengan presisi yang cukup tinggi. Untuk visualisasi data, digunakan aplikasi Blynk yang memungkinkan pengguna melihat status ketinggian air dan menerima peringatan dalam waktu nyata.

3. Rumusan Masalah
Berdasarkan latar belakang tersebut, rumusan masalah dalam proyek ini adalah:

Bagaimana merancang sistem IoT yang dapat memantau ketinggian air secara real-time menggunakan sensor HC-SR04 dan ESP32?

Bagaimana cara mengirimkan data pemantauan level air ke platform cloud (Blynk) untuk visualisasi dan peringatan?

Bagaimana membedakan status kondisi air (aman, rawan, banjir) secara otomatis berdasarkan jarak air dari sensor?

Bagaimana memberikan indikator lokal (LED dan buzzer) sebagai peringatan dini di lokasi?

4. Tujuan
Tujuan dari proyek ini adalah:

Merancang dan mengimplementasikan sistem pemantauan banjir berbasis IoT menggunakan ESP32 dan sensor HC-SR04.

Mengukur ketinggian air secara otomatis dan mengirimkan data ke dashboard Blynk untuk pemantauan jarak jauh.

Memberikan notifikasi dan visualisasi real-time status air (aman, rawan, banjir) kepada masyarakat.

Menyediakan sistem indikator lokal menggunakan LED dan buzzer sebagai bentuk peringatan dini langsung di lapangan.

5. Manfaat
Adapun manfaat dari proyek ini adalah:

Bagi masyarakat: Meningkatkan kesadaran dan kesiapsiagaan terhadap potensi banjir melalui sistem peringatan dini berbasis teknologi.

Bagi pengembang teknologi: Memberikan referensi implementasi nyata IoT dalam solusi kebencanaan.

Bagi pemerintah/relawan: Mendukung pengambilan keputusan cepat dalam evakuasi dan mitigasi bencana.

Bagi pendidikan: Memberikan contoh aplikatif dari penerapan sensor, mikrokontroler, dan cloud IoT dalam kehidupan nyata.

#HARDWARE
![image](https://github.com/user-attachments/assets/6a8e7586-8d06-4094-93b7-275c2718f110)

