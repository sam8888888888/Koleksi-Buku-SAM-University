# LAM (LEMBAR AUDIT MANDIRI) — BAB 58 (TIPE A)

Audit otomatis: dijalankan | Audit manusia: BELUM DILAKUKAN | Mode A

Skor akhir tidak ditetapkan. Kecocokan otomatis tidak menggantikan pemeriksaan teks Arab, terjemah, tafsir, fiqh, data, dan mutu editorial.

| Butir | Pemeriksaan | Status | Catatan |
|---|---|---|---|
| 1 | Judul dan delapan sub-bab sesuai TOC | Otomatis lulus | Urutan sesuai daftar aktif. |
| 2 | Elemen Tipe A dan nama blok | Otomatis lulus | Struktur diperiksa audit_bab.py. |
| 3 | Panjang sub-bab dan total | Otomatis lulus | 58.1–58.8 masing-masing memenuhi ambang skrip; total 4.784 kata dari anggaran 4.500. |
| 4 | Pembuka | Otomatis lulus | Rentang 120–180 kata. |
| 5 | Ayat dan kecocokan bank | Menunggu merge bank | Audit menyisakan 4 temuan TEKS ARAB TIDAK ADA DI BANK_DALIL; 155 cocok bank. Tidak ada mismatch atau temuan lain. |
| 6 | Terjemah dan tafsir | Menunggu manusia | Terjemah makna ditandai [TERJEMAH-CEK]; telaah ahli diperlukan. |
| 7 | Hak atas bantuan dan zakat | Menunggu manusia | Penerapan mustahik dan penyaluran dana perlu telaah fiqh/amil. |
| 8 | Tidak menyalahkan korban | Menunggu manusia | Naskah menolak vonis hukuman atas korban; tetap perlu pembacaan editorial. |
| 9 | Angka dan fakta | Otomatis lulus | Tidak ada statistik spesifik atau kontak tak terverifikasi. |
| 10 | Frasa terlarang, struktur dan blok | Otomatis lulus | Audit final tidak mencatat temuan selain ketiadaan ayat di bank. |
| 11 | Duplikat paragraf | Otomatis lulus | collections.Counter: 0 paragraf duplikat. |
| 12 | DOCX | Tidak dikerjakan | Tidak diminta pada tugas ini. |

JSON audit final:
```json
{
  "bab": 58,
  "tipe": "A",
  "kata": 4784,
  "anggaran": 4500,
  "dev_pct": 6.3,
  "sub_bab_toc": 8,
  "sub_bab_draft": 8,
  "temuan": [
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Al-Baqarah: 156",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Al-Baqarah: 157",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. Al-Hadid: 22–23",
    "TEKS ARAB TIDAK ADA DI BANK_DALIL: QS. At-Taghabun: 11"
  ],
  "lolus": false
}
```

Audit menandai hanya ayat yang belum tersedia di bank; Diya perlu merge ayat tersebut ke BANK_DALIL dan menjalankan audit ulang. Pemeriksaan manusia belum dilakukan.
