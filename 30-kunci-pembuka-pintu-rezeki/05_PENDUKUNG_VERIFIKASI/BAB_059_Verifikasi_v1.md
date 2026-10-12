# LEMBAR VERIFIKASI DALIL — BAB 59 (TIPE A)

| ID dalil | Rujukan | Sumber/URL | Status |
|---|---|---|---|
| 59.D1 | QS. Asy-Syura: 30 | https://quran.nu.or.id/asy-syura/30 (dibuka, HTTP 200); teks Arab diambil dari https://api.alquran.cloud/v1/ayah/42:30/quran-uthmani | [V-AYAT]; teks cocok dengan entri BANK_DALIL_DRAF_v1.md (baris QS. Asy-Syura: 30). Terjemah ditulis ulang dengan kata sendiri, [TERJEMAH-CEK]. |
| 59.D2 | QS. Ar-Rum: 41 | https://quran.nu.or.id/ar-rum/41 (dibuka, HTTP 200); teks Arab diambil dari https://api.alquran.cloud/v1/ayah/30:41/quran-uthmani | [V-AYAT]; teks cocok dengan entri BANK_DALIL_DRAF_v1.md (baris QS. Ar-Rum: 41). Terjemah [TERJEMAH-CEK]. |
| 59.D3 | QS. At-Tahrim: 8 | https://quran.nu.or.id/at-tahrim/8 (dibuka, HTTP 200); teks Arab diambil dari https://api.alquran.cloud/v1/ayah/66:8/quran-uthmani | [V-AYAT]; teks tidak ditemukan di BANK_DALIL_DRAF_v1.md sehingga audit menyisakan satu temuan `TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. At-Tahrim: 8`; menunggu merge oleh Diya. Terjemah [TERJEMAH-CEK]. |

Catatan sumber: halaman NU dapat dibuka tanpa 403, tetapi penulisan Arabnya memakai ejaan yang berbeda dari gaya quran-uthmani yang dipakai BANK_DALIL (misalnya wasla ٱ berganti alef biasa). Naskah mengikuti gaya quran-uthmani dari API agar konsisten dengan entri bank yang sudah terverifikasi; halaman NU tetap dicatat sebagai rujukan pembuka.

Hadits pada sub-bab 59.1 tidak dikutip dengan nomor. Bunyi riwayat "seseorang terhalang dari rezekinya karena dosa yang dilakukannya" disampaikan dengan status yang jujur: diriwayatkan dengan beberapa sanad; sebagian ulama menilainya lemah, sebagian mengamalkannya dengan kehati-hatian. Penanda [DERAJAT-CEK] dibiarkan agar pemeriksa manusia menutup poin ini; tidak ada klaim sahih dan tidak ada nomor hadits yang ditulis. Pencarian di koleksi hadits tersedia tidak menemukan padanan berbahasa Indonesia maupun Arab yang bisa dikutip dengan yakin.

BANK_DALIL_DRAF_v1.md tidak diubah. Pemeriksaan teks Arab, terjemah, tafsir, dan fiqh oleh manusia tetap diperlukan sebelum terbit.

## LAPORAN AUDITOR FINAL

Audit final (2026-10-10, kurator Diya): `kata=6018`, `anggaran=5800`, `dev_pct=3.8`, 11/11 sub-bab, `temuan: []`, `lolus: true`. Duplikat 0. Merge BANK_DALIL (backup .bak.pre_bab059): QS. At-Tahrim 8 (Asy-Syura 30 & Ar-Rum 41 sudah ada). Hadits 59.1 tanpa nomor, status jujur (sanad diperdebatkan) + [DERAJAT-CEK]. DOCX dirender + QC (Arab rata kanan, kurung biasa).
