# Verifikasi Bab 69

- QS. Al-Baqarah: 282: teks Arab diambil persis dari baris BANK_DALIL_DRAF_v1.md (terverifikasi API + quran.nu.or.id). Status [V-AYAT].
- QS. Al-Baqarah: 283 dan QS. Al-Qashash: 26-27: teks Arab langsung dari quran.nu.or.id (al-baqarah/283, al-qashash/26), dicocokkan dengan api.alquran.cloud; ditambahkan ke BANK_DALIL (backup .bak.pre_bab69nu). Status [V-AYAT] x2.
- Kisah sahabat meruqyah dengan Al-Fatihah pada 69.2: diriwayatkan Muslim (kitab as-Salam) dari Abu Said al-Khudri; teks Arab dari hadith-mcp id 12863, silang Bukhari. Ditulis dalam prosa tanpa nomor sesuai kaidah; catatan sumber di lembar ini.
- Audit: `python3 audit_bab.py BAB_069_Akad_Jasa_Jaminan_dan_Pinjaman_v1.md 69 B` -> temuan [], lolus true, 6770 kata, dev +5,8% terhadap anggaran 6400.
- QC DOCX: 3 paragraf Arab right+rtl; PDF 22 halaman. Kata 'naskah' dibersihkan dari prosa.
- Waktu pemeriksaan: 2026-10-12 01:25 +08.
