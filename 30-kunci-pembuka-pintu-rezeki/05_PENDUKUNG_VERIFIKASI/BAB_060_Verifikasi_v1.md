# LEMBAR VERIFIKASI DALIL — BAB 60 (TIPE A)

| ID | Rujukan | Sumber/URL | Status |
|---|---|---|---|
| 60.D1 | QS. Ali 'Imran: 130 | https://api.alquran.cloud/v1/ayah/3:130/quran-uthmani ; laman pembanding yang diminta: https://quran.nu.or.id/ali-imran/130 | Arab dari API quran-uthmani. [V-AYAT] [TERJEMAH-CEK]. Tidak cocokkan dengan BANK_DALIL. |
| 60.D2 | QS. Al-Baqarah: 275–281 | https://quran.nu.or.id/al-baqarah/275 ; https://api.alquran.cloud/v1/ayah/2:275/quran-uthmani hingga /2:281/quran-uthmani | Ayat 275 diperiksa juga pada laman NU; Arab ayat 275–281 bersumber API per ayat. [V-AYAT] [TERJEMAH-CEK]. |
| 60.D3 | QS. Ar-Rum: 39 | https://api.alquran.cloud/v1/ayah/30:39/quran-uthmani ; laman pembanding: https://quran.nu.or.id/ar-rum/39 | Arab dari API quran-uthmani. [V-AYAT] [TERJEMAH-CEK]. |
| 60.D4 | QS. An-Nisa: 160–161 | https://api.alquran.cloud/v1/ayah/4:160/quran-uthmani ; https://api.alquran.cloud/v1/ayah/4:161/quran-uthmani ; laman pembanding: https://quran.nu.or.id/an-nisa/160 dan /161 | Arab dari API per ayat. [V-AYAT] [TERJEMAH-CEK]. |
| 60.D5 | HR. Muslim no. 89 (tujuh dosa) | https://hadits.id/hadits/muslim/89 ; silang nomor/isi: https://sunnah.com/muslim:89 | Sumber hadits.id menandai Shahih; Sunnah.com memuat Sahih Muslim 89. Redaksi dan penomoran diperiksa; [DERAJAT-CEK]. |
| 60.D6 | HR. Muslim no. 1598 (laknat) | https://hadits.id/hadits/muslim/1598 ; https://sunnah.com/muslim:1598 | Hadits.id menandai Shahih; Sunnah.com menampilkan Sahih Muslim 1598, Kitab Musaqah, bab laknat atas pelaku riba. [DERAJAT-CEK]. |
| 60.D7 | HR. Muslim no. 1587 (enam komoditas) | https://hadits.id/hadits/muslim/1587 | Hadits.id menandai Shahih; matan Arab dan terjemah dibaca di halaman tersebut. [DERAJAT-CEK]. Tautan Sunnah.com Muslim 1587 dicoba melalui akses web namun gagal 403; jangan klaim silang berhasil. |
| 60.D8 | HR. Muslim no. 1584 (emas/perak) | https://hadits.id/hadits/muslim/1584 ; https://sunnah.com/muslim:1584 | Hadits.id menandai Shahih; Sunnah.com memberi nomor 1584a (Book 22, Hadith 93) dan teks sepadan. [DERAJAT-CEK]. |

## Catatan pemeriksaan

Arab ayat diambil dari edisi quran-uthmani API, lalu diberi nomor ayat dalam kurung Arab-Indic. Terjemah diringkas/diolah dari terjemah Indonesia dan perlu pemeriksaan editor/ahli. Hadits pada halaman hadits.id ditandai Shahih. Untuk tujuh dosa, nomor Muslim 89 dicantumkan terpisah dari Muslim 1598 yang berisi laknat para pihak dalam akad riba. Untuk enam komoditas, laman hadits.id mengidentifikasi riwayat Muslim 1587; jangan menyamakan matannya dengan Muslim 1584.

Audit `audit_bab.py` menyisakan 8 temuan `TEKS ARAB TIDAK ADA DI BANK_DALIL`. Ini temuan yang diizinkan; BANK_DALIL tidak disentuh. Ayat yang perlu Diya merge: QS. Ali 'Imran 130; QS. Al-Baqarah 275–281 (tujuh entri ayat); QS. Ar-Rum 39; QS. An-Nisa 160–161 (dua entri ayat). Hadits yang perlu Diya merge: HR. Muslim 89, 1598, 1587, 1584. Jumlah sumber dalil: 11 ayat + 4 hadits.

URL yang dipakai untuk substansi fatwa perlu dikumpulkan editor dari dokumen primer sebelum terbit. Tidak dicantumkan nomor/tahun fatwa yang belum dicocokkan.

## LAPORAN AUDITOR FINAL

Audit final (2026-10-10, kurator Diya): `kata=9776`, `anggaran=8900`, `dev_pct=9.8`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat 0. Blok dalil dipecah jadi 8 blok terpisah (gaya kanonik). Merge BANK_DALIL (backup .bak.pre_bab060): QS. Ali Imran 130, Al-Baqarah 275-281, Ar-Rum 39, An-Nisa 160-161; HR. Muslim 89, 1598, 1587, 1584. DOCX dirender + QC (Arab rata kanan, kurung biasa).


## PEMBARUAN ROMBAK TIPE B — FINAL

Naskah dirombak menjadi Tipe B. Audit: `kata=9024`, `anggaran=8900`, `dev_pct=1.4`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat paragraf: 0. Blok tambahan: istilah-akad, struktur-akad, pendapat-ulama, fatwa-regulasi, contoh-transaksi, titik-risiko, penerapan-keluarga, penerapan-kerja, simulasi, checklist, batas-kewenangan, jangkar-abadi. BANK_DALIL, seluruh judul sub-bab, dan isi blok `::: dalil` tidak diubah.

Kata per sub-bab: 60.1 580; 60.2 589; 60.3 339; 60.4 575; 60.5 336; 60.6 328; 60.7 328; 60.8 572; 60.9 573; 60.10 331; 60.11 337; 60.12 334; 60.13 328; 60.14 332; 60.15 336; 60.16 171.

Final JSON: `{"bab":60,"tipe":"B","kata":9024,"anggaran":8900,"dev_pct":1.4,"sub_bab_toc":16,"sub_bab_draft":16,"temuan":[],"lolus":true}`. Audit manusia dan verifikasi dokumen fatwa primer tetap belum dilakukan.
