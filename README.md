# THE SIGNAL TOWER — news-image-20261122 — Akun Final 3

Entry gambar berita dari @meleyotcok (Akun Final 3) untuk bounty
news-image-20261122 di make.fun, dibangun ulang pada gelombang 7.

## Gelombang 7

Gelombang ini memakai pool segar Minggu 22 Nov 2026: 15 kartu berita
utama ditambah 21 brief pendamping, total 36 cerita yang tersebar di
7 region. Angka-angka kunci tampil sebagai strip angka di bagian
bawah kanvas: 186 / 161 / 35% / $120bn / 720 / 9 / 50. Setiap kartu
melewati DATE CHECK — materi bertanggal basi dibuang dan diberi nama
jelas sebagai buangan bernama, bukan diselipkan diam-diam.

## Entry

- Dimensi: 1024x1024 piksel (pas di gerbang 1024x1024)
- Ukuran: 237176 byte
- SHA256: 58d033a9fd5b64a6e9bbbe70ed9b414bacf1e14b8da3c7b982c998334c59c671
- Margin checker: 13/13 lulus

`main.py` hanya memakai pustaka standar Python: ia memeriksa header
PNG, menolak sisi di atas 1024 piksel, menyalin `entry.png` apa adanya
ke folder keluaran, lalu membuktikan salinan itu byte-identik lewat
sha256 dan ukuran sebelum melaporkan hasilnya.
