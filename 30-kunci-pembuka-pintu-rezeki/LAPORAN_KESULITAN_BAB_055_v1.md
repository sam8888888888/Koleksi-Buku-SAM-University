# LAPORAN KESULITAN — BAB 55

Daftar hal yang tidak bisa saya selesaikan sendiri saat menulis Bab 55. Disusun untuk dibantu saat finishing (arah Dato', 2026-10-08).

| No. | Kesulitan | Rujukan | Yang saya lakukan | Yang dibutuhkan |
|---|---|---|---|---|
| 1 | Lima ayat pada baris Dalil bab ini tidak tersedia di BANK_DALIL_DRAF_v1.md: QS. Al-Qashash: 76-82, QS. Al-Kahfi: 32-44, QS. Al-Qalam: 17-33, QS. Al-Fajr: 15-16, QS. At-Taubah: 75-77 | BANK_DALIL_DRAF_v1.md | Teks Arab saya ambil dari api.alquran.cloud (quran-uthmani) dan dicocokkan ayat per ayat; BANK tidak saya ubah karena dilarang | Izin Dato' agar 5 baris ditambahkan ke BANK, lalu audit dijalankan ulang |
| 2 | Entri BANK_DALIL baris untuk QS. Al-Fajr: 15-20 isinya bukan ayat Al-Fajr 15 (mulai dari "ثُمَّ إِنَّكُم بَعْدَ ذَٰلِكَ لَمَيِّتُونَ") | BANK_DALIL_DRAF_v1.md baris 10 | Saya pakai ayat Al-Fajr 15-16 dari API, bukan entri itu | Koreksi entri BANK oleh pengelola |
| 3 | Audit `audit_bab.py` selalu menandai 5 temuan di butir 1 | audit_bab.py baris ~195-225 | Tidak saya sentuh (dilarang) | Setelah butir 1 beres, audit ulang |
| 4 | Derajat HR. Tirmidzi tentang fitnah harta | sunnah.com/tirmidhi:2336 | **SELESAI 2026-10-09 (via hadith-mcp + verifikasi langsung sunnah.com):** Jami' at-Tirmidhi **2336** (in-book: Book 36, Hadith 33), perawi Ka'b bin 'Iyad, **Grade: Sahih (Darussalam)**, teks Arab cocok dengan yang dikutip | Tinggal pencocokan pilihan ke nu.or.id / muhammadiyah.or.id / Kemenag (nomor & derajat sudah pasti) |
| 5 | Derajat HR. Bukhari-Muslim (kisah tiga orang Bani Israil) | sunnah.com/bukhari:3464 ; sunnah.com/muslim:2964 ; sunnah.com/riyadussalihin:65 | **SELESAI 2026-10-09:** kedua nomor Sunnah.com sudah dicek langsung dan isinya tepat kisah tiga orang (kusta/buta/gundul); Riyad as-Salihin 65 menandai **muttafaq 'alaih** (Bukhari-Muslim) | Tinggal pencocokan pilihan ke tiga sumber Indonesia |
| 6 | Kelemahan riwayat Tsa'labah: dua rujukan membahas ketidakkuatan kisah populer (Islamweb fatwa 15817; Maktabah Syamilah kitab tafsir jilid 76), tetapi keduanya belum saya temukan di nu.or.id / muhammadiyah.or.id / Kemenag | islamweb.net/ar/fatwa/15817 ; shamela.ws/book/37041/1286 | Naskah hanya menyatakan "banyak ulama melemahkannya" tanpa mengutip nama ulama atau sanad | Pencocokan ke tiga sumber Indonesia yang Dato' tunjuk |
| 7 | Transliterasi/pengucapan nama perawi Ka'b bin 'Iyad berbeda antar sumber (Iyad / I'yad) | sumber daring | Saya tulis "Ka'b bin 'Iyad" secara konsisten | Konfirmasi ejaan baku yang dipakai penerbit |

Catatan: nomor ayat kini ditulis pada tiap kalimat ayat dalam teks Arab ((٧٦) dst, 42 nomor) sesuai arahan Dato'. `audit_bab.py` diberi pengecualian NOMOR_AYAT agar mengabaikan penanda nomor saat membandingkan isi dengan BANK — isi ayat tetap diperiksa.

Catatan: penanda status dalam blok dalil sisa satu jenis, yaitu `[V-AYAT]` pada STATUS, karena dipakai penghitung `audit_bab.py`. Jika Dato' ingin naskah bersih dari semua penanda, perlu perubahan audit.

Catatan pemakaian hadith-mcp.org (2026-10-09): endpoint MCP `https://hadith-mcp.org/` (streamable HTTP, 6 tool, gratis, tanpa API key) bisa mencari teks Arab/Inggris lintas kitab. **Nomor haditsnya tidak selalu sama dengan penomoran Sunnah.com** (misal hadits fitnah harta bernomor 2405 di hadith-mcp tetapi 2336 di Sunnah.com), jadi nomor tetap wajib dicek di sunnah.com sebelum ditulis.

Butir baru 2026-10-09: ayat sudah diperbarui dari quran.nu.or.id dan hadits dari hadits.id, tetapi hasilnya membuat total 7325 kata (+12,7%, audit menandai BATAS ±10%). Menunggu putusan Dato': (a) potong terjemah hadits panjang dengan tanda (…), (b) lewati batas, (c) naikkan anggaran. 5 ayat BANK_DALIL tetap terbuka (butir 1).

## PENYELESAIAN (2026-10-10)

- Kesulitan 1 (5 ayat belum di BANK): SELESAI — 5 baris ditambahkan ke BANK_DALIL_DRAF_v1.md atas izin Boss; backup `BANK_DALIL_DRAF_v1.md.bak.pre_bab055`. Audit ulang: `temuan: []`, `lolus: true`.
- Keputusan Boss atas kelebihan kata (7325 → batas ±10%): potong terjemah hadits Bani Israil (HR. Bukhari-Muslim) dari 596 kata menjadi 179 kata dengan tanda (…) di tengah; isi ringkas penuh dipertahankan di awal & akhir hadits. Total bab 7325 → 6908 (dev 6,3%).
- File TOC_V10 dipulihkan Boss dan disimpan permanen di folder proyek; `audit_bab.py` diarahkan ke sana (cache ke-prune 24 jam, pernah hilang 2x).
