LANJUTAN SEDIKIT — sesi sebelumnya (id 20261008_195320_d71069) sudah penuh. Ini ringkasan keadaan; baca dulu sebelum bertindak.

PROYEK: buku 30 KUNCI PEMBUKA PINTU REZEKI, folder /home/diya/books/30-kunci-pembuka-pintu-rezeki/. Skill kanonik: 30-kunci-bab-production, naskah-arab-indonesia, 30-kunci-audit-kualitas-naskah. Aturan sub-agent: ATURAN_ANAK_BAB.md (sudah memuat pointer skill Arab).

STATUS:
- Bab 54 selesai (lolos audit, 7011 kata). Bab 55 (BAB_055_Harta_Bukan_Ukuran_v1.md/.docx + 4 lembar) sudah diperbaiki total sesuai koreksi saya: teks Arab & terjemah dari quran.nu.or.id + hadits.id; nomor )..( di BELAKANG teks Arab; nomor (..) di BELAKANG terjemahan Indonesia; label "Dalilnya sebagai berikut"; Artinya (bukan TERJEMAH); Firman Allah / Sabda Rasulullah ﷺ; glosarium = makna istilah bukan peringatan; Word: teks Latin justify, blok Arab satu paragraf menyambung rata kanan dengan run w:rtl + Scheherazade New; sumber dicatat di LAPORAN_KESULITAN_BAB_055_v1.md.
- Audit Bab 55 terakhir: kata 7325, dev 12,7%, temuan: (1) batas ±10% terlampaui, (2) 5 ayat belum ada di BANK_DALIL (Al-Qashash 76-82, Al-Kahfi 32-44, Al-Qalam 17-33, Al-Fajr 15-16, At-Taubah 75-77 — izin menambah perlu dari saya).
- Keputusan yang saya minta (a potong terjemah hadits dengan (…) / b lewati batas / c naikkan anggaran; default a) BELUM saya jawab.

ALAT & TEMUAN PENTING:
- MCP hadith-mcp.org sudah terdaftar di config Hermes (gratis); penomorannya bisa beda dari sunnah.com — nomor wajib dicek di sunnah.com. HR. Tirmidzi fitnah harta = 2336 (Shahih, Darussalam); kisah tiga orang Bani Israil = Bukhari 3464 + Muslim 2964 (muttafaq alaih).
- audit_bab.py sudah diberi pengecualian NOMOR_AYAT agar )..( tidak memicu temuan palsu.
- quran.nu.or.id: URL per ayat, kena Vercel checkpoint → pakai Camofox (~/tools/camofox-browser, port 9377, userId wajib ada di body).
- Font Arab Scheherazade New + Amiri sudah terpasang di ~/.fonts; soffice + pdftoppm tersedia untuk verifikasi visual render.
- Disk sudah dibersihkan ±1 GB; sisa 9 GB bebas.

YANG BELUM / PERLU IZIN SAYA:
1. Keputusan a/b/c untuk batas kata Bab 55.
2. Penambahan 5 ayat ke BANK_DALIL_DRAF_v1.md (audit_bab.py melarang sub-agent mengedit BANK).
3. Setelah Bab 55 saya setujui final, terapkan 11+ aturan kualitas yang sama ke bab-bab lama: ada 187 baris transliterasi Latin (50 file), 278 kandidat bahasa proses (46 file), 174 DERAJAT: n.a. (50 file) yang belum dibersihkan.
4. Produksi bab baru (56 dst) berhenti menunggu perintah saya.

CATATAN GAYA: jangan potong isi buku tanpa izin; jangan diam menunggu tanya (kirim pertanyaan + opsi + default, lalu lanjut); semua angka/fakta diverifikasi di sumber; laporan singkat per blok.