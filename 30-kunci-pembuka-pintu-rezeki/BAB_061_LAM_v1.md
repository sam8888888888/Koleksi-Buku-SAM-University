# LAM — Lembar Audit Mandiri — Bab 61 (Tipe B)

Audit otomatis dijalankan dengan `python3 audit_bab.py BAB_061_Riba_di_Zaman_Kita_v1.md 61 B`. Telaah manusia belum dilakukan.

| Butir | Pemeriksaan | Status/catatan |
|---|---|---|
| Struktur dan TOC | 16 sub-bab; blok seimbang | Lulus otomatis; 23 pembuka dan 23 penutup. |
| Batas audit | Tipe B, jumlah kata dan penanda sub-bab | Lulus otomatis; 8.541 kata, 16/16 judul ditemukan. |
| 61.1 | Perluasan sub-bab ● | 695 kata menurut fungsi hitung `prose()` pada `audit_bab.py`, dalam target 680-710. |
| Teks Arab | QS. Al-Baqarah 275-279 | Exact-string sama dengan kolom Arab bank. |
| Frasa/format | Em dash dan penutup blok | Tidak ada em dash; jumlah ::: seimbang. |
| Fatwa/angka simulasi | Data dan batas klaim | Angka ditandai ilustrasi; nomor fatwa belum diverifikasi dan diberi `[FATWA-CEK]`. |
| QS. Ghafir: 7 | Ketidakcocokan sumber | Lafaz instruksi tidak ditemukan di bank dan bukan lafaz ayat; blok memakai lafaz ayat yang diverifikasi API. Catatan pada lembar Verifikasi. |
| Terjemah, fiqh, kontrak | Telaah substantif | Perlu pemeriksaan editor/ahli sebelum terbit. |

```json
{"bab":61,"tipe":"B","kata":8541,"anggaran":8000,"dev_pct":6.8,"sub_bab_toc":16,"sub_bab_draft":16,"temuan":[],"lolus":true}
```

Kata per sub-bab (fungsi `prose()`): 61.1 695; 61.2 403; 61.3 406; 61.4 404; 61.5 403; 61.6 409; 61.7 400; 61.8 417; 61.9 707; 61.10 399; 61.11 400; 61.12 402; 61.13 406; 61.14 409; 61.15 397; 61.16 213.

Audit otomatis lulus; ini bukan pengesahan fatwa, audit hukum kontrak, ataupun pengganti telaah ahli atas terjemah dan dalil.
