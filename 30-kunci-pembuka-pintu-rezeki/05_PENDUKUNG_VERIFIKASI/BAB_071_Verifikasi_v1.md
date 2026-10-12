# Verifikasi Bab 71

- Dua ayat dalil: QS. An-Nisa: 29 dan QS. Al-Ma'idah: 1, teks Arab dari baris BANK (sumber quran.nu.or.id, verified batch sebelumnya). Status [V-AYAT] x2. Terjemah dari API id.indonesian, perlu dicocokkan dengan terjemah resmi [TERJEMAH-CEK].
- Fatwa terkait transaksi elektronik disebut di kepala-bab dengan penanda [FATWA-CEK] (merujuk Lampiran L).
- CATATAN BANK: ditemukan duplikat baris QS. Al-Ma'idah: 1 (versi dengan & tanpa basmalah); disamakan ke satu versi kanonik (dengan basmalah). Bab 66 dan 68 disesuaikan ulang + backup .bak.pre_dedup71, audit ulang keduanya lolos.
- Audit: `python3 audit_bab.py BAB_071_...md 71 B` -> temuan [], lolus true, 7667 kata, dev -0,4% terhadap anggaran 7700.
- QC DOCX: 2 paragraf Arab right+rtl; PDF 24 halaman.
- Waktu pemeriksaan: 2026-10-12 02:19 +08.
