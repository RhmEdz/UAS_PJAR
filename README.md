Network Programming Project

Proyek ini merupakan aplikasi jaringan sederhana berbasis Python yang mengimplementasikan beberapa fitur komunikasi socket dan autentikasi pengguna.

 Status Fitur

 Berhasil / Sudah Terimplementasi
- ✅ Transfer file menggunakan TCP
  - Upload file ke server
  - Download file dari server
  - Melihat daftar file yang tersimpan
- ✅ Registrasi dan verifikasi akun melalui OTP Gmail
  - Proses registrasi mengirim OTP ke email pengguna
  - Verifikasi akun dilakukan melalui kode OTP



 Tujuan Proyek

Proyek ini dibuat untuk mempelajari dan mengimplementasikan konsep jaringan komputer, antara lain:
- Socket programming
- TCP communication
- Authentication dan OTP
- File transfer
- Penggunaan database MySQL

## Struktur Folder

```text
client/           # client untuk menguji koneksi TCP/UDP/auth/media
config/           # konfigurasi database dan SMTP
server/           # server TCP, UDP, auth, dan media
database/         # file SQL database
storage/          # folder penyimpanan file dan media
web/              # aplikasi web Flask
```

## Persyaratan

Pastikan sistem Anda sudah menginstall:
- Python 3.x
- MySQL Server
- pip

 Instalasi Dependency

Jalankan perintah berikut:

```bash
pip install flask mysql-connector-python opencv-python
```

 Persiapan Database

1. Buat database MySQL dengan nama `pjar`
2. Import file SQL berikut:

```bash
mysql -u root -p pjar < database/pjar.sql
```

## Konfigurasi

Buka file konfigurasi berikut:

```text
config/config.py
```

Sesuaikan pengaturan database dan SMTP sesuai lingkungan Anda.

## Cara Menjalankan

### 1. Jalankan server TCP

```bash
cd server
python tcp_server.py
```

### 2. Jalankan aplikasi web

```bash
cd web
python app.py
```

### 3. Akses aplikasi

Buka browser dan akses:

```text
http://localhost:8080
```

 Catatan Penting

- Fitur TCP, upload/download file, serta proses verify OTP Gmail adalah bagian yang paling relevan dan dapat digunakan pada proyek ini.

## Penulis

Proyek ini dibuat untuk kebutuhan tugas jaringan dan pemrograman jaringan.
