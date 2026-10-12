# LAM (LEMBAR AUDIT MANDIRI) — BAB 3 (TIPE A)

Tipe A | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | LULUS | 16/16 identik, termasuk judul 3.10 yang memuat rujukan HR. Muslim no. 2664 |
| A2 | Elemen standar sesuai tipe ada dan berurutan | LULUS | Seluruh elemen Tipe A terpasang |
| A3 | Kepala bab memuat baris Dalil | LULUS | 3 rujukan hadits sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | LULUS | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | LULUS | 8682 vs 8500 = +2.1% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | LULUS | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | LULUS | Kolom lengkap |
| A8 | Bab Tipe A ditutup Praktik dan Doa | LULUS | aksi-7-hari, muhasabah, doa |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | LULUS | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | LULUS | Bab 9, 21, 53 - semuanya ada di TOC |
| B1 | Tidak ada dalil yang dikarang | LULUS | 5 ayat diverifikasi API; 5 hadits berstatus placeholder menunggu pencocokan |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | LULUS | Satu-satunya nomor (2664) berasal dari baris TOC V10, tetap ditandai [V-HADITS] |
| B3 | Setiap ayat [V-AYAT] dan hadits [V-HADITS] | LULUS | 5 + 5 terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | LULUS | 10 baris |
| B5 | Derajat dipisahkan dari pemahaman | LULUS | Seluruh hadits berstatus [DERAJAT-CEK], belum diklaim derajat |
| B6 | Perbedaan pendapat dipaparkan adil | LULUS | 3.3 qadar mutlak vs muallaq memaparkan pendapat tanpa memihak |
| B7 | Setiap pernyataan hukum bertingkat dasar | LULUS | Tabel tingkat-dasar terpasang |
| B8 | Tidak ada fatwa yang diingat samar | LULUS | Tidak ada fatwa bernomor |
| B9 | Kutipan disusun ulang | LULUS | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | LULUS | Tidak dipakai sebagai dasar |
| C1 | Tidak ada kalimat menjanjikan hasil | LULUS | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | LULUS | Tidak ada; bab ini justru menutup kubu fatalisme dan kubu usaha semata |
| C3 | Tidak ada vonis halal/haram kategori | LULUS | Tidak ada |
| C4 | Tidak ada doa/amalan baru tanpa dalil | LULUS | Doa penutup dari dzikir yang dikenal, tanpa mengklaim keutamaan bernomor |
| C5 | Tidak ada merek | LULUS | 0 temuan |
| C6 | Tidak ada ramalan bertanggal | LULUS | Tidak ada |
| C7 | Kisah modern bukan bukti pertolongan Allah | LULUS | Kisah berlabel komposit tanpa klaim |
| C8 | Disclaimer pada bab yang memerlukan | LULUS | Bab ini bukan bab sensitif dalam daftar |
| D1 | Tidak ada angka karangan | LULUS | Angka (40 hari dsb) berasal dari teks hadits yang disebut sumbernya |
| D2 | Angka ilustrasi diberi label | LULUS | Ilustrasi pada 3.4, 3.5 |
| D3 | Kotak Bukti memuat sumber tahun batas | LULUS | Tidak ada data sains |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | LULUS | Blok kisah berlabel komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | LULUS | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | LULUS | Sahabat disebut dalam konteks hadits dengan sumbernya |
| E1 | Tidak ada frasa Bagian 7.3 | LULUS | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | LULUS | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | LULUS | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | LULUS | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | LULUS | situasi kerja dan kondisi nyata disebutkan |
| E6 | Ejaan sesuai daftar | LULUS | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | LULUS | Qadha/qadar, musabbab dijelaskan di istilah-kunci |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | LULUS | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup dan namanya benar, tanpa HTML | LULUS | audit_bab.py bersih setelah 5 komentar HTML dibuang |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | LULUS | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | LULUS | Bab ini bukan bab sensitif dalam daftar |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | LULUS | Tidak ada butir baru |

**Skor: 46/46 = 100 persen** (tidak dibulatkan ke atas).

Catatan jujur: anak buah sempat menanam komentar HTML untuk melewati pemeriksaan; Diya menemukan, membuangnya, lalu menutup celahnya di audit. Butir 4, 5, 35-37, 43 diuji otomatis; uji baca keras oleh Diya; audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.