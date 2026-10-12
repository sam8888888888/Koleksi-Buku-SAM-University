# SERAH TERIMA — BAB 60

Status: draf selesai; audit otomatis menyisakan 8 temuan `TEKS ARAB TIDAK ADA DI BANK_DALIL` saja. Naskah belum siap terbit sebelum Diya merge dalil ke bank (bila dikehendaki) dan telaah manusia menyelesaikan pemeriksaan teks/terjemah serta fatwa primer.

Berkas dibuat:
- `BAB_060_Riba_Dalil_Jenis_Hikmah_v1.md`
- `BAB_060_Verifikasi_v1.md`
- `BAB_060_Data_v1.md`
- `BAB_060_LAM_v1.md`
- `BAB_060_Serah_Terima_v1.md`

Audit akhir: 9.769 kata; anggaran 8.900, deviasi 9,8% (di bawah batas skrip ±10%); 16 sub-bab sesuai TOC; semua sub-bab memenuhi rentang KETAT; 0 paragraf duplikat. JSON dan hitungan ada di lembar LAM.

Temuan bank yang menunggu merge:
- Ayat: QS. Ali 'Imran: 130; QS. Al-Baqarah: 275–281; QS. Ar-Rum: 39; QS. An-Nisa: 160–161.
- Hadits: HR. Muslim no. 89, 1598, 1587, dan 1584.

URL sumber dalil: halaman API Quran per ayat dan URL hadits.id/Sunnah.com dicatat rinci pada `BAB_060_Verifikasi_v1.md`. Sunnah.com Muslim 1598 dan 1584 berhasil diperiksa lewat ekstraksi web; akses langsung HTTP untuk keduanya sempat 403, tetapi ekstraksi web memuat isi. Sunnah.com 1587 tidak berhasil diakses (403), sehingga tidak diklaim sebagai silang terverifikasi. Tidak ada nomor/tahun fatwa yang belum diverifikasi; rincian fatwa ditandai [DATA DIPERLUKAN] pada lembar Data.

`BANK_DALIL_DRAF_v1.md` dan bab lain tidak diubah. Tidak dibuat DOCX.

## LAPORAN AUDITOR FINAL

Audit final (2026-10-10, kurator Diya): `kata=9776`, `anggaran=8900`, `dev_pct=9.8`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat 0. Blok dalil dipecah jadi 8 blok terpisah (gaya kanonik). Merge BANK_DALIL (backup .bak.pre_bab060): QS. Ali Imran 130, Al-Baqarah 275-281, Ar-Rum 39, An-Nisa 160-161; HR. Muslim 89, 1598, 1587, 1584. DOCX dirender + QC (Arab rata kanan, kurung biasa).


## PEMBARUAN ROMBAK TIPE B — FINAL

Naskah dirombak menjadi Tipe B. Audit: `kata=9024`, `anggaran=8900`, `dev_pct=1.4`, 16/16 sub-bab, `temuan: []`, `lolus: true`. Duplikat paragraf: 0. Blok tambahan: istilah-akad, struktur-akad, pendapat-ulama, fatwa-regulasi, contoh-transaksi, titik-risiko, penerapan-keluarga, penerapan-kerja, simulasi, checklist, batas-kewenangan, jangkar-abadi. BANK_DALIL, seluruh judul sub-bab, dan isi blok `::: dalil` tidak diubah.

Kata per sub-bab: 60.1 580; 60.2 589; 60.3 339; 60.4 575; 60.5 336; 60.6 328; 60.7 328; 60.8 572; 60.9 573; 60.10 331; 60.11 337; 60.12 334; 60.13 328; 60.14 332; 60.15 336; 60.16 171.

Final JSON: `{"bab":60,"tipe":"B","kata":9024,"anggaran":8900,"dev_pct":1.4,"sub_bab_toc":16,"sub_bab_draft":16,"temuan":[],"lolus":true}`. Audit manusia dan verifikasi dokumen fatwa primer tetap belum dilakukan.
