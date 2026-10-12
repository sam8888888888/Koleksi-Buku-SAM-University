# LAM (LEMBAR AUDIT MANDIRI) — BAB 19 (TIPE B)

Tipe B | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | L | 21/21 identik (audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | L | Semua elemen dalam batas |
| A3 | Kepala bab memuat baris Dalil | L | semua rujukan baris Dalil TOC tercantum |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | L | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | L | 8788 vs 9600 = -8.5% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | L | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | L | checklist + praktik terpasang |
| A8 | Bab Tipe A ditutup Praktik dan Doa | N/A | Bab Tipe B - ditutup praktik dan muhasabah |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | L | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | L | dicek terhadap TOC |
| B1 | Tidak ada dalil yang dikarang | L | semua ayat diverifikasi utuh dari API |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | L | hadits TOC tanpa nomor, tidak dikutip bila tak ada di Bank |
| B3 | Setiap ayat [V-AYAT] | L | terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | L | semua baris ada |
| B5 | Derajat dipisahkan dari pemahaman | L | n.a. pada ayat |
| B6 | Perbedaan pendapat dipaparkan adil | L | dipaparkan dengan atribusi |
| B7 | Setiap pernyataan hukum bertingkat dasar | L | tingkat dasar dicantumkan |
| B8 | Tidak ada fatwa yang diingat samar | L | [FATWA-CEK] pada bagian fatwa-regulasi |
| B9 | Kutipan disusun ulang | L | tanpa kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | L | tidak dipakai sebagai dasar |
| C1 | Tidak ada kalimat menjanjikan hasil | L | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | L | tidak ada |
| C3 | Tidak ada vonis halal/haram kategori | L | dibedah per akad, bukan vonis kategori |
| C4 | Tidak ada doa/amalan baru tanpa dalil | L | Muhasabah tanpa doa wajib (Tipe B) |
| C5 | Tidak ada merek | L | 0 temuan (dicek manual) |
| C6 | Tidak ada ramalan bertanggal | L | tidak ada |
| C7 | Kisah modern bukan bukti pertolongan Allah | L | contoh berlabel komposit/ilustrasi |
| C8 | Disclaimer pada bab yang memerlukan | L | blok batas-kewenangan terpasang |
| D1 | Tidak ada angka karangan | L | [DATA DIPERLUKAN] untuk angka yang belum tersumber |
| D2 | Angka ilustrasi diberi label | L | label pada simulasi |
| D3 | Kotak Bukti memuat sumber tahun batas | L | wajib bertahun |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | L | komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | L | tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | L | tidak ada |
| E1 | Tidak ada frasa Bagian 7.3 | L | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | L | yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | L | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | L | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | L | lokasi dan langkah konkret disebut |
| E6 | Ejaan sesuai daftar | L | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | L | istilah kunci dijelaskan |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | L | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | L | audit_bab.py bersih; HTML 0; ::: tidak menempel; tanpa tanda (—) |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | L | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | L | bagian sensitif diberi batas-kewenangan |
| F4 | Semua [TANYA DATO] jelas dengan usulan | L | tidak ada butir baru |

**Skor: 45/45 = 100 persen** (butir n/a dikeluarkan).

Catatan jujur: draf pertama menggabungkan Al-Maarij 24-25 dan Adz-Dzariyat 19 dalam satu blok, dan teks Arab Al-Maarij ternyata terpenggal serta mengulang frasa. Semua sudah Diya pisah dan ganti dengan teks API per ayat, lalu audit ulang sampai bersih. Audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.