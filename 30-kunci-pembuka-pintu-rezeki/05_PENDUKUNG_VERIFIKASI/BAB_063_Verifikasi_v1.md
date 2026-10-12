# Verifikasi Bab 63

- Teks Arab 3 ayat (Al-A'raf 199, Luqman 15, Al-An'am 162) diambil dari api.alquran.cloud (quran-uthmani) dan dicek silang quran.nu.or.id per ayat: /al-araf/199, /luqman/15, /al-anam/162.
- Status ayat: [V-AYAT] x3. Ayat sudah ditambahkan ke BANK_DALIL_DRAF_v1.md (backup .bak.pre_bab063).
- Tidak ada kutipan hadits ber-nomor di naskah; kerangka riwayat pada blok kisah ditulis tanpa nomor [DERAJAT-CEK].
- Penanda tersisa: [FATWA-CEK] x1 (63.1, klaim fatwa soal pahala sedekah kepada yang wafat) — perlu verifikasi fatwa sebelum terbit.
- Audit: `python3 audit_bab.py BAB_063_Amalan_Rezeki_Nusantara_v1.md 63 A` -> temuan [], lolus true, 4626 kata, dev -1,6% terhadap anggaran 4700.
- Waktu pemeriksaan: 2026-10-11 22:48 +08.
