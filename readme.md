# Instagram Bruteforce - Educational Purpose Only

🚨 **Disclaimer:** Proyek ini dibuat hanya untuk tujuan edukasi dan penelitian keamanan. Penyalahgunaan alat ini untuk tujuan ilegal merupakan tindakan yang melanggar hukum. Pengembang tidak bertanggung jawab atas segala bentuk penyalahgunaan.

## 📌 Deskripsi

Proyek ini adalah alat brute force untuk menguji keamanan akun Instagram dalam konteks pembelajaran keamanan siber. Tujuan utama adalah memahami bagaimana mekanisme autentikasi bekerja dan bagaimana sistem pertahanan dapat diperkuat.

## ⚠️ Peringatan

Instagram memiliki sistem keamanan yang sangat kuat, termasuk rate-limiting dan proteksi anti-bot. Menggunakan alat ini pada akun yang bukan milik Anda atau tanpa izin dapat menyebabkan akun diblokir atau tindakan hukum.

## 🛠️ Fitur

- Multi-threading untuk kecepatan optimal
- Dukungan user-agent random
- Simulasi login menggunakan Requests
- Log hasil percobaan
- **Bypass SSL Pinning** untuk menghindari proteksi keamanan tambahan

## 🚀 Cara Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/KenXinDev/BruteForceIG.git
cd BruteForceIG
```

### 2. Install Dependensi

```bash
pkg update -y && pkg upgrade -y
pkg install clang python-pip libffi openssl libsodium binutils build-essential rust
apt install python-cryptography
SODIUM_INSTALL=system pip install pynacl
pip install -r requirements.txt
```

### 3. Jalankan Skrip

```bash
python3 run.py
```

## 📄 Catatan

- Alat ini hanya untuk tujuan edukasi dan penelitian.
- Gunakan secara bertanggung jawab untuk memahami dan meningkatkan keamanan.

## 🤝 Kontribusi
Kami sangat menghargai kontribusi dari komunitas! Jika Anda ingin membantu mengembangkan alat ini, silakan buka [Issues](https://github.com/KenXinDev/BruteForceIG/issues) atau buat [Pull Requests](https://github.com/KenXinDev/BruteForceIG/pulls).

## 📜 Lisensi
Proyek ini bukan open source. Semua hak cipta dari kode sumber dimiliki oleh pengembang. Anda diberikan hak untuk menggunakan alat ini, tetapi tidak diperbolehkan untuk memodifikasi, mendistribusikan, atau menjual ulang kode sumber tanpa izin.


