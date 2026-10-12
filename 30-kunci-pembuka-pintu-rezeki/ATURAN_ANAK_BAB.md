# ATURAN ANAK-AGENT — PENULISAN SATU BAB (buku 30 Kunci Pembuka Pintu Rezeki)

Berlaku untuk semua agent penulis bab. Diya (auditor) memeriksa ulang SEMUA hasil dan mengoreksi; jadi jangan menyimpang diam-diam. Kalau ada konflik aturan vs TOC: TOC menang, catat di laporan.

## 1. Berkas yang ditulis (per bab)
- `BAB_0NN_JudulPendek_v1.md` — naskah Mode A.
- `BAB_0NN_Verifikasi_v1.md`, `BAB_0NN_Data_v1.md`, `BAB_0NN_LAM_v1.md`, `BAB_0NN_Serah_Terima_v1.md` — ikuti format persis 4 lembar Bab 34 (baca dulu).
- JANGAN menyentuh: `BANK_DALIL_DRAF_v1.md`, `audit_bab.py`, TOC, naskah bab lain, lembar bab lain.

## 2. Alur kerja (urut)
1. Baca spek bab (TOC block + penanda + anggaran) yang diberikan Diya.
2. Baca `audit_bab.py` (SEMUA aturan keras ada di sana), `ATURAN_ANAK_BAB.md` ini, dan `BAB_034_Menolong_Sesama_v1.md` + 4 lembar Bab 34 sebagai exemplar.
3. Baca `KARAKTER_TOKOH_v1.md` (tokoh komposit yang boleh dipakai) dan `DAFTAR_EJAAN_dan_ISTILAH_v1.md`.
4. TULIS FILE NASKAH DULU (jangan riset berlarut-larut), lalu iterasi audit sampai lulus.
5. Tulis 4 lembar pendamping.
6. Cek duplikat paragraf + kirim laporan.

## 3. Struktur naskah (Tipe A)
- Baris 1: `# Bab NN. {judul persis TOC}`.
- `::: kepala-bab` berisi: `Bab NN | Kunci NN | Tipe A` (Kunci sesuai TOC).
- Sub-bab: `## NN.x {judul persis TOC}` — HURUF, tanda kutip, dan angka persis TOC.
- Blok wajib Tipe A (urut): kepala-bab, pembuka-masalah, pertanyaan-utama, ringkasan, istilah-kunci, dalil, tingkat-dasar, janji-nyata, salah-paham, fiqh-praktis, kasus, kisah, coba-sekarang, aksi-7-hari, lihat-juga, muhasabah, doa, satu-kalimat. Penanda `::: nama` dan `:::` penutup HARUS baris sendiri (tidak menempel di teks).
- Pembuka-masalah: 120–180 kata. aksi-7-hari: tepat 7 baris tabel. muhasabah: tepat 1 kali per bab.
- `::: lihat-juga` isi: daftar bab dari spek + `[QR: /bab-NN]`.

## 4. Dalil (SANGAT KRITIS)

- **Seluruh tata penulisan teks Arab (sumber, nomor ayat, terjemahan bernomor, tampilan Word) mengikuti skill kanonik `naskah-arab-indonesia`** — quran.nu.or.id + hadits.id; nomor )..( di BELAKANG teks Arab; nomor (..) di BELAKANG terjemahan Indonesia; blok Arab rata kanan satu paragraf menyambung; teks Latin rata kanan-kiri.
- Satu blok `::: dalil` per rujukan (baris Dalil di TOC).
- Format tiap entri 7 baris urut: ARAB, LATIN, TERJEMAH, PERAWI, DERAJAT, RUJUKAN, STATUS.
- **TEKS ARAB AYAT: WAJIB salin persis dari `BANK_DALIL_DRAF_v1.md`** (baris ref sudah disediakan Diya). Jangan pernah menulis Arab dari ingatan. Kalau ref tidak ada di BANK, ambil dari `https://api.alquran.cloud/v1/ayah/{surah}:{ayat}/quran-uthmani` lalu LAPOR di laporan akhir (jangan mengubah BANK).
- Ayat: `PERAWI: n.a. (ayat, bukan hadits)`, `DERAJAT: Wahyu Al-Qur'an (kitabullah); bukan hadits, sehingga tidak dinilai derajat perawinya`, `RUJUKAN: QS. ...`, `STATUS: [V-AYAT]`.
- **LATIN**: ditulis `LATIN: n.a. (transliterasi tidak dipakai; teks Arab dibaca langsung)` untuk ayat, `LATIN: n.a.` untuk hadits. Transliterasi latin ayat DITIADAKAN — pembaca target muslim sanggup membaca Arab (keputusan Dato', 2026-10-08); syarat rasio ≥ 0,7 TIDAK berlaku lagi, jangan dikembalikan tanpa izin Dato'.
- **TERJEMAH**: terjemah maknanya sendiri, diakhiri `[TERJEMAH-CEK]`.
- Hadits: `ARAB: n.a. (...)` (TIDAK dikutip Arab, TIDAK dikarang), nomor hadis BOLEH hanya kalau ada di baris Dalil TOC (tulis `sebagaimana tercantum pada TOC`), isi hadits diverifikasi di sunnah.com / hadits.id (catat URL di lembar Verifikasi), derajat ditandai `[DERAJAT-CEK]`.
- **DERAJAT wajib menyebut jenis sumber dan derajatnya (Dato': fatal bila tidak jelas)**: ayat → `DERAJAT: Wahyu Al-Qur'an (kitabullah); bukan hadits, sehingga tidak dinilai derajat perawinya` (dilarang `DERAJAT: n.a.`); hadits → derajatnya eksplisit + `[DERAJAT-CEK]`. Kutipan hadits di narasi tanpa blok `::: dalil` wajib diberi blok dalil sendiri (audit tidak membatasi jumlah blok dalil).
- Potongan ayat: tulis `(sebagian, bagian ...)` di RUJUKAN dan teksnya HARUS substring persis dari ayat penuh.

## 5. Panjang (audit menghukum di luar batas)
- Hitungan sub-bab = teks luar blok `:::`; total = seluruh file.
- Rentang penanda: ● 560–840, ◐ 320–480, ○ 160–240.
- Total ±10% terhadap anggaran. Targetkan rentang TENGAH-ATAS; kalau total meleset, naik/turunkan SEMUA sub-bab proporsional lalu audit ulang.

## 6. Konten dilarang (audit menandai)
- Frasa: di era digital*, tidak dapat dipungkiri, penting untuk dicatat, mari kita selami, pada akhirnya, sebagai kesimpulan, mengupas tuntas, komprehensif, holistik, krusial, esensial, paradigma, lanskap, sinergi, transformasi. (*kecuali muncul persis sebagai judul sub-bab TOC — audit mengecualikan judul `## `.)
- Tanda `—` (em dash) dan `%`: dilarang di seluruh file.
- **Bahasa proses produksi dilarang di isi naskah (Dato', 2026-10-08)**: `TOC`, `naskah`, `Lembar`/`lembar Verifikasi`, `penerbit`, `penulis`, `audit`, `sub-bab`, `Bank Dalil`. Catatan proses diletakkan di 4 lembar pendamping, bukan di bab.
- Nol: merek/jenama, statistik rekaan, nomor hadis karangan, vonis halal/haram kategori, janji hasil/rumus, menyalahkan orang miskin, sapaan "kamu" (kecuali di TERJEMAH ayat), sapaan "Anda".
- Frasa terlarang lain: cek daftar di `audit_bab.py`.
- Maksimum 2 grup daftar per sub-bab (audit memeriksanya).
- Kisah wajib label `*Kisah komposit.*`; tokoh hanya dari `KARAKTER_TOKOH_v1.md`.
- Tidak ada tag HTML; tidak ada paragraf identik antar sub-bab (cek `collections.Counter`, harus 0 duplikat).
- Jangan mengarang isi yang tidak ada di TOC; jangan mengubah urutan sub-bab.

## 7. Audit
`python3 audit_bab.py BAB_0NN_....md NN A` → wajib `"temuan": []` dan `"lolus": true`. ULANGI sampai bersih. (Tipe B: ganti A dengan B.)

## 8. Laporan akhir ke Diya
JSON audit final persis; jumlah kata per sub-bab; hasil cek duplikat; daftar file yang ditulis; daftar URL sumber hadits yang dibuka; keputusan yang butuh perhatian auditor (mis. konflik aturan vs TOC).
