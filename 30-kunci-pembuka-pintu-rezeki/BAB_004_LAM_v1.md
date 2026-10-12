# LAM (LEMBAR AUDIT MANDIRI) — BAB 4 (TIPE A)

Tipe A | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | LULUS | 13/13 identik (audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | LULUS | Seluruh elemen Tipe A terpasang |
| A3 | Kepala bab memuat baris Dalil | LULUS | sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | LULUS | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | LULUS | 6977 vs 7300 = -4.4% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | LULUS | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | LULUS | Kolom lengkap |
| A8 | Bab Tipe A ditutup Praktik dan Doa | LULUS | aksi-7-hari, muhasabah, doa |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | LULUS | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | LULUS | dicek terhadap TOC |
| B1 | Tidak ada dalil yang dikarang | LULUS | 4 ayat diverifikasi API; 2 hadits tanpa nomor, berstatus placeholder |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | LULUS | Kedua hadits ditulis "tanpa nomor hadits" |
| B3 | Setiap ayat [V-AYAT] dan hadits [V-HADITS] | LULUS | 4 + 2 pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | LULUS | 6 baris |
| B5 | Derajat dipisahkan dari pemahaman | LULUS | [DERAJAT-CEK] pada kedua hadits |
| B6 | Perbedaan pendapat dipaparkan adil | LULUS | 4.9 dan 4.10 memuat pendapat lembaga tanpa memihak |
| B7 | Setiap pernyataan hukum bertingkat dasar | LULUS | Tabel tingkat-dasar terpasang |
| B8 | Tidak ada fatwa yang diingat samar | LULUS | Fatwa kontemporer ditandai [FATWA-CEK] dan diberi tanggal bila perlu |
| B9 | Kutipan disusun ulang | LULUS | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | LULUS | Tidak dipakai |
| C1 | Tidak ada kalimat menjanjikan hasil | LULUS | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | LULUS | Tidak ada |
| C3 | Tidak ada vonis halal/haram kategori | LULUS | Produk dinilai lewat struktur akad dan rujukan, bukan vonis kategori (4.6-4.10) |
| C4 | Tidak ada doa/amalan baru tanpa dalil | LULUS | Basmalah dan adab makan dirujukkan umum |
| C5 | Tidak ada merek | LULUS | 0 temuan; contoh produk ditulis tanpa merek |
| C6 | Tidak ada ramalan bertanggal | LULUS | Data diberi tanggal penutupan, tanpa ramalan |
| C7 | Kisah modern bukan bukti pertolongan Allah | LULUS | Kisah berlabel komposit |
| C8 | Disclaimer pada bab yang memerlukan | LULUS | Bab ini menyebut status produk tanpa menjatuhkan vonis pribadi |
| D1 | Tidak ada angka karangan | LULUS | Tidak ada angka statistik yang dikutip |
| D2 | Angka ilustrasi diberi label | LULUS | Ilustrasi ditandai |
| D3 | Kotak Bukti memuat sumber tahun batas | LULUS | Kebutuhan data ditandai di Lembar Data |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | LULUS | Blok kisah berlabel komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | LULUS | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | LULUS | Hanya tokoh komposit |
| E1 | Tidak ada frasa Bagian 7.3 | LULUS | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | LULUS | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | LULUS | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | LULUS | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | LULUS | warung, dapur, dan meja makan disebutkan |
| E6 | Ejaan sesuai daftar | LULUS | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | LULUS | thayyib, israf, syubhat dijelaskan di istilah-kunci |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | LULUS | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | LULUS | audit_bab.py bersih |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | LULUS | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | LULUS | Bagian 8 tidak memuat bab ini; bab 103 (mitos) masih tersendiri |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | LULUS | Tidak ada butir baru |

**Skor: 46/46 = 100 persen** (tidak dibulatkan ke atas).

Catatan jujur: dua blok hadits awalnya memakai label di luar standar Prompt (TEKS:/MAKNA:), sudah Diya tata ulang; 4 ayat diverifikasi ke API; audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.