# LAM (LEMBAR AUDIT MANDIRI) — BAB 60 (TIPE A)

Audit otomatis: dijalankan | Audit manusia: BELUM DILAKUKAN | Mode A

| Butir | Pemeriksaan | Status | Catatan |
|---|---|---|---|
| 1 | Judul dan 16 sub-bab sesuai TOC | Otomatis lulus | 16 sub-bab ditemukan dan urutannya sesuai. |
| 2 | Elemen Tipe A dan nama blok | Otomatis lulus | Audit menemukan struktur/nama blok sah. |
| 3 | Panjang sub-bab dan total | Otomatis lulus | Semua 16 sub-bab memenuhi rentang KETAT; total 9.769 kata dari anggaran 8.900 (batas skrip ±10%). |
| 4 | Pembuka | Otomatis lulus | Audit tidak melaporkan masalah rentang pembuka. |
| 5 | Ayat/hadits dan cocok bank | Menunggu merge bank | 8 temuan ketiadaan teks dalam BANK_DALIL; tidak ada mismatch. Bank tidak diubah. |
| 6 | Derajat dan terjemah | Menunggu manusia | Sumber menandai empat riwayat Muslim sebagai Shahih; lafaz/terjemah tetap perlu telaah ahli. Kaidah pinjaman-manfaat diberi [DERAJAT-CEK]. |
| 7 | Fatwa dan perbedaan ulama | Menunggu data primer | Substansi ditulis tanpa nomor/tahun; konfirmasi pada dokumen resmi MUI, Lembaga Fiqh Internasional, NU, dan Muhammadiyah diperlukan. |
| 8 | Adab keluarga, kasus, dan janji hasil | Perlu baca manusia | Hindari vonis orang; kasus bersifat ilustratif dan tidak menjanjikan hasil finansial. |
| 9 | Frasa, struktur, dan paragraf ganda | Otomatis lulus | Tidak ada temuan selain ketiadaan dalil di bank. Counter menemukan 0 paragraf duplikat. |
| 10 | DOCX | Tidak dikerjakan | Tidak diminta. |

JSON audit final:
```json
{
  "bab": 60,
  "tipe": "A",
  "kata": 9769,
  "anggaran": 8900,
  "dev_pct": 9.8,
  "sub_bab_toc": 16,
  "sub_bab_draft": 16,
  "temuan": [
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Ali 'Imran: 130",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Al-Baqarah: 275-281",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Ar-Rum: 39",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. An-Nisa: 160-161",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: HR. Muslim no. 89",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: HR. Muslim no. 1598",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: HR. Muslim no. 1587",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: HR. Muslim no. 1584"
  ],
  "lolus": false
}
```

Kata per sub-bab (metode hitung audit, semua memenuhi rentang KETAT): 60.1 708; 60.2 705; 60.3 408; 60.4 707; 60.5 406; 60.6 408; 60.7 408; 60.8 695; 60.9 690; 60.10 392; 60.11 408; 60.12 410; 60.13 410; 60.14 408; 60.15 408; 60.16 205.

Bank dalil dibiarkan tanpa perubahan. Temuan Arab yang perlu merge terdaftar pada lembar verifikasi. Audit manusia, pemeriksaan dokumen fatwa primer, dan pengecekan akhir teks Arab/terjemah belum dilakukan.

## LAPORAN AUDITOR FINAL

Audit final (2026-10-10, kurator Diya): `kata=9776`, `anggaran=8900`, `dev_pct=9.8`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat 0. Blok dalil dipecah jadi 8 blok terpisah (gaya kanonik). Merge BANK_DALIL (backup .bak.pre_bab060): QS. Ali Imran 130, Al-Baqarah 275-281, Ar-Rum 39, An-Nisa 160-161; HR. Muslim 89, 1598, 1587, 1584. DOCX dirender + QC (Arab rata kanan, kurung biasa).


## PEMBARUAN ROMBAK TIPE B — FINAL

Naskah dirombak menjadi Tipe B. Audit: `kata=9024`, `anggaran=8900`, `dev_pct=1.4`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat paragraf: 0. Blok tambahan: istilah-akad, struktur-akad, pendapat-ulama, fatwa-regulasi, contoh-transaksi, titik-risiko, penerapan-keluarga, penerapan-kerja, simulasi, checklist, batas-kewenangan, jangkar-abadi. BANK_DALIL, seluruh judul sub-bab, dan isi blok `::: dalil` tidak diubah.

Kata per sub-bab: 60.1 580; 60.2 589; 60.3 339; 60.4 575; 60.5 336; 60.6 328; 60.7 328; 60.8 572; 60.9 573; 60.10 331; 60.11 337; 60.12 334; 60.13 328; 60.14 332; 60.15 336; 60.16 171.

Final JSON: `{"bab":60,"tipe":"B","kata":9024,"anggaran":8900,"dev_pct":1.4,"sub_bab_toc":16,"sub_bab_draft":16,"temuan":[],"lolus":true}`. Audit manusia dan verifikasi dokumen fatwa primer tetap belum dilakukan.
