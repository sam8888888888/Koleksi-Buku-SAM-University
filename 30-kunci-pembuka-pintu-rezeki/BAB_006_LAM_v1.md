# LAM (LEMBAR AUDIT MANDIRI) — BAB 6 (TIPE A)

Tipe A | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | LULUS | 17/17 identik |
| A2 | Elemen standar sesuai tipe ada dan berurutan | LULUS | Anatomi dinormalkan: 1 tiap elemen penutup, coba-sekarang 2, salah-paham 4 |
| A3 | Kepala bab memuat baris Dalil | LULUS | Sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | LULUS | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | LULUS | 7790 vs 8400 = -7.3% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | LULUS | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | LULUS | Kolom lengkap |
| A8 | Bab Tipe A ditutup Praktik dan Doa | LULUS | aksi-7-hari, muhasabah, doa |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | LULUS | Hanya 1 kotak, tanpa janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | LULUS | Bab 8, 45, 78 - semuanya ada di TOC |
| B1 | Tidak ada dalil yang dikarang | LULUS | 3 ayat diverifikasi API (1 cuplikan bagian doa, ditandai); 2 hadits placeholder |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | LULUS | Nomor 6412 dan 2965 berasal dari baris TOC V10 |
| B3 | Setiap ayat [V-AYAT] dan hadits [V-HADITS] | LULUS | Terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | LULUS | 5 baris |
| B5 | Derajat dipisahkan dari pemahaman | LULUS | [DERAJAT-CEK] pada kedua hadits |
| B6 | Perbedaan pendapat dipaparkan adil | LULUS | 6.15 membuka status klasifikasi wajah rezeki dengan jujur |
| B7 | Setiap pernyataan hukum bertingkat dasar | LULUS | Tabel tingkat-dasar 1 (dinormalisasi) |
| B8 | Tidak ada fatwa yang diingat samar | LULUS | Tidak ada fatwa bernomor |
| B9 | Kutipan disusun ulang | LULUS | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | LULUS | Tidak dipakai sebagai dasar |
| C1 | Tidak ada kalimat menjanjikan hasil | LULUS | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | LULUS | Tidak ada |
| C3 | Tidak ada vonis halal/haram kategori | LULUS | Tidak ada |
| C4 | Tidak ada doa/amalan baru tanpa dalil | LULUS | Doa penutup dari QS. Al-Baqarah: 201 |
| C5 | Tidak ada merek | LULUS | 0 temuan |
| C6 | Tidak ada ramalan bertanggal | LULUS | Tidak ada |
| C7 | Kisah modern bukan bukti pertolongan Allah | LULUS | 8 kasus berlabel komposit tanpa klaim |
| C8 | Disclaimer pada bab yang memerlukan | LULUS | Bab peta, bukan bab sensitif |
| D1 | Tidak ada angka karangan | LULUS | Tidak ada statistik |
| D2 | Angka ilustrasi diberi label | LULUS | Ilustrasi pada 6.10 |
| D3 | Kotak Bukti memuat sumber tahun batas | LULUS | Tidak ada data sains |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | LULUS | Fikri, Sinta, Farid, Dimas - sesuai Daftar Karakter |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | LULUS | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | LULUS | Hanya tokoh komposit |
| E1 | Tidak ada frasa Bagian 7.3 | LULUS | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | LULUS | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | LULUS | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | LULUS | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | LULUS | kota dan pekerjaan tokoh disebutkan |
| E6 | Ejaan sesuai daftar | LULUS | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | LULUS | Wajah rezeki dijelaskan sebagai kerangka penulis |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | LULUS | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | LULUS | audit_bab.py bersih; buka/tutup 43/43 |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | LULUS | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | LULUS | Bab peta, bukan bab sensitif |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | LULUS | Tidak ada butir baru |

**Skor: 46/46 = 100 persen** (tidak dibulatkan ke atas).

Catatan jujur: temuan terbesar bab ini adalah kelebihan elemen (18 satu-kalimat dsb) yang saya normalisasi; sebelum normalisasi audit otomatis TIDAK menangkapnya karena pemeriksa hanya cek keberadaan, bukan jumlah. Audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.