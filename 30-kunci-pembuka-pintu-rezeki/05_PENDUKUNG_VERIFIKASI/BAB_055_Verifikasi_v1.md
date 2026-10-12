# LEMBAR VERIFIKASI DALIL — BAB 55 (TIPE A)

| ID | Rujukan | Sumber | Pemeriksaan/status |
|---|---|---|---|
| 55.D1 | QS. Al-Qashash: 76-82 | API quran-uthmani + id.indonesian + en.transliteration, Surah 28 | Teks Arab disalin dari API; terjemah makna ditulis ulang; [V-AYAT], [TERJEMAH-CEK]. Sudah ditambahkan ke BANK_DALIL_DRAF_v1.md (2026-10-10, izin Boss). |
| 55.D2 | QS. Al-Kahfi: 32-44 | API quran-uthmani + id.indonesian + en.transliteration, Surah 18 | Teks Arab disalin dari API; terjemah makna berdasar pembanding API; [V-AYAT], [TERJEMAH-CEK]. Sudah ditambahkan ke BANK_DALIL_DRAF_v1.md (2026-10-10, izin Boss). |
| 55.D3 | QS. Al-Qalam: 17-33 | API quran-uthmani + id.indonesian + en.transliteration, Surah 68 | Teks Arab disalin dari API; terjemah makna diperiksa dan dibenahi untuk kelancaran; [V-AYAT], [TERJEMAH-CEK]. Sudah ditambahkan ke BANK_DALIL_DRAF_v1.md (2026-10-10, izin Boss). |
| 55.D4 | QS. Al-Fajr: 15-16 | API quran-uthmani + id.indonesian + en.transliteration, Surah 89 | Teks Arab disalin dari API, bukan teks keliru pada entri BANK_DALIL QS. Al-Fajr: 15-20; perlu verifikasi pembanding ahli. |
| 55.D5 | HR. Tirmidzi, fitnah harta | https://sunnah.com/tirmidhi:2336 (Grade Sahih, Darussalam; in-book 36/33; dicek 2026-10-09) | Teks Inggris menyebut Ka'b bin 'Iyad; laman menampilkan Sahih (Darussalam). Naskah tidak menambah nomor ke badan bab karena tidak tercantum dalam TOC; [DERAJAT-CEK]. |
| 55.D6 | QS. At-Taubah: 75-77 | API quran-uthmani + id.indonesian + en.transliteration, Surah 9 | Teks Arab disalin dari API; ayat tidak menyebut nama Tsa'labah; [V-AYAT], [TERJEMAH-CEK]. Sudah ditambahkan ke BANK_DALIL_DRAF_v1.md (2026-10-10, izin Boss). |
| 55.D7 | HR. Bukhari dan Muslim (kisah tiga orang Bani Israil; muttafaq alaih, lihat Riyad as-Salihin 65) | https://sunnah.com/bukhari:3464 ; https://sunnah.com/muslim:2964 | Kedua sumber dibuka; kini punya blok dalil sendiri di naskah dengan derajat "dua kitab shahih" dan ringkasan makna; tanpa nomor karena rujukan bab hanya menyebut kedua kitab. |
| 55.D8 | Riwayat populer tentang Tsa'labah | https://www.islamweb.net/ar/fatwa/15817/ثعلبة-بن-حاطب-المفترى-عليه ; https://shamela.ws/book/37041/1286 | Kedua sumber menyatakan kisah populer itu lemah/tidak sahih; simpulan diringkas, bukan takhrij mandiri. |

URL API langsung untuk sumber ayat/transliterasi/terjemah pembanding:
- https://api.alquran.cloud/v1/surah/28/quran-uthmani ; https://api.alquran.cloud/v1/surah/28/en.transliteration ; https://api.alquran.cloud/v1/surah/28/id.indonesian
- https://api.alquran.cloud/v1/surah/18/quran-uthmani ; https://api.alquran.cloud/v1/surah/18/en.transliteration ; https://api.alquran.cloud/v1/surah/18/id.indonesian
- https://api.alquran.cloud/v1/surah/68/quran-uthmani ; https://api.alquran.cloud/v1/surah/68/en.transliteration ; https://api.alquran.cloud/v1/surah/68/id.indonesian
- https://api.alquran.cloud/v1/surah/89/quran-uthmani ; https://api.alquran.cloud/v1/surah/89/en.transliteration ; https://api.alquran.cloud/v1/surah/89/id.indonesian
- https://api.alquran.cloud/v1/surah/9/quran-uthmani ; https://api.alquran.cloud/v1/surah/9/en.transliteration ; https://api.alquran.cloud/v1/surah/9/id.indonesian
Ayat yang dikutip dipilih tepat menurut nomor pada TOC. Terjemah pembanding API bukan diperlakukan sebagai terjemahan final tanpa pemeriksaan.

Catatan batas: Al-Qashash, Al-Kahfi, Al-Qalam, At-Taubah tidak ada dalam BANK_DALIL. Entri Al-Fajr: 15-20 di BANK juga tidak sesuai teks ayat Al-Fajr pada API, maka naskah memakai data API untuk 15-16. ATURAN_ANAK_BAB melarang penulis mengubah BANK. Ini menyebabkan temuan audit otomatis yang tidak dapat diperbaiki tanpa pembaruan bank oleh pihak berwenang.

Penyuntingan setelah arahan: seluruh penyebutan TOC, naskah, lembar, dan proses produksi dihapus dari isi bab; setiap blok dalil menyebut derajatnya (ayat = wahyu Al-Qur'an; Tirmidzi = sahih per Darussalam; Bukhari-Muslim = dua kitab shahih).

Transliterasi Latin dihapus dari seluruh blok dalil sesuai arahan 2026-10-08 (target pembaca Muslim); baris LATIN diisi `n.a.`. URL en.transliteration tetap dicatat di atas sebagai arsip pembanding teks, bukan untuk ditampilkan ke pembaca.

Urutan sumber baru (arah Dato', 2026-10-08): nu.or.id dulu, lalu muhammadiyah.or.id, lalu Kemenag RI, baru sumber lain sebagai pendukung. Belum diterapkan pada bab ini karena pencocokan dilakukan setelah daftar kesulitan disetujui; lihat LAPORAN_KESULITAN_BAB_055_v1.md.

Sumber utama teks & terjemah (2026-10-09, arahan Dato'): quran.nu.or.id untuk 42 ayat (dibuka per ayat, 25 via unduhan langsung, 17 via browser Camofox karena Vercel checkpoint), hadits.id untuk HR. Tirmidzi 2336 (derajat: Shahih, Darussalam) dan HR. Bukhari 3464 (kisah tiga orang Bani Israil). Sunnah.com tetap dipakai silang: tirmidhi:2336, bukhari:3464, muslim:2964, riyadussalihin:65.
