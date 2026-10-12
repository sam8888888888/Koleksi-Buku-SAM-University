# LAM (LEMBAR AUDIT MANDIRI) — BAB 2 (TIPE A)

Tipe A | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | LULUS | 16/16 sub-bab identik (dicek audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | LULUS | Seluruh elemen Tipe A terpasang |
| A3 | Kepala bab memuat baris Dalil | LULUS | 4 rujukan dari baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | LULUS | audit_bab.py: 0 sub-bab di luar rentang |
| A5 | Total bab dalam toleransi plus minus 10 persen | LULUS | 8510 vs 8600 = -1.0% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | LULUS | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | LULUS | Kolom lengkap |
| A8 | Bab Tipe A ditutup Praktik dan Doa | LULUS | aksi-7-hari, muhasabah, doa |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | LULUS | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | LULUS | Bab 1, Bab 27, Bab 28 - semuanya ada di TOC |
| B1 | Tidak ada dalil yang dikarang | LULUS | 12 blok ayat diverifikasi 12/12 terhadap API |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | LULUS | 1 sebutan hadits memakai placeholder + [DERAJAT-CEK] |
| B3 | Setiap ayat [V-AYAT] | LULUS | 12 [V-AYAT] + 1 [V-HADITS] |
| B4 | Lembar Verifikasi memuat semua dalil | LULUS | 13 baris |
| B5 | Derajat dipisahkan dari pemahaman | LULUS | Bab ini tanpa derajat yang diklaim |
| B6 | Perbedaan pendapat dipaparkan adil | LULUS | 2.9 membedakan budi pekerti vs permohonan pertolongan, tanpa melabeli kalangan |
| B7 | Setiap pernyataan hukum bertingkat dasar | LULUS | Tabel tingkat-dasar terpasang |
| B8 | Tidak ada fatwa yang diingat samar | LULUS | Tidak ada fatwa |
| B9 | Kutipan disusun ulang | LULUS | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | LULUS | 2.10 menyatakan teks hadits belum dicocokkan |
| C1 | Tidak ada kalimat menjanjikan hasil | LULUS | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | LULUS | 2.9 justru menutup dengan pengertian atas yang tertekan |
| C3 | Tidak ada vonis halal/haram kategori | LULUS | Tidak ada |
| C4 | Tidak ada doa/amalan baru tanpa dalil | LULUS | Doa penutup dari bank dalil |
| C5 | Tidak ada merek | LULUS | 0 temuan |
| C6 | Tidak ada ramalan bertanggal | LULUS | Tidak ada |
| C7 | Kisah modern bukan bukti pertolongan Allah | LULUS | Contoh berlabel ilustrasi/komposit |
| C8 | Disclaimer pada bab yang memerlukan | LULUS | Bab ini bukan bab sensitif dalam daftar |
| D1 | Tidak ada angka karangan | LULUS | Semua angka berlabel ilustrasi (Lembar Data) |
| D2 | Angka ilustrasi diberi label | LULUS | Label pada 2.10 |
| D3 | Kotak Bukti memuat sumber tahun batas | LULUS | Tidak ada data sains dikutip |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | LULUS | Blok kisah berlabel komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | LULUS | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | LULUS | Hanya tokoh komposit dan Nabi/sahabat |
| E1 | Tidak ada frasa Bagian 7.3 | LULUS | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | LULUS | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | LULUS | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | LULUS | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | LULUS | warung Semarang, pekerja lepas Yogyakarta, tok Semarang |
| E6 | Ejaan sesuai daftar | LULUS | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | LULUS | Nama Allah dijelaskan dalam prose |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | LULUS | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup dan namanya benar | LULUS | audit_bab.py bersih |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | LULUS | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | LULUS | Bab ini bukan bab sensitif dalam daftar |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | LULUS | Tidak ada butir baru |

**Skor: 46/46 = 100 persen** (tidak dibulatkan ke atas).

Catatan jujur: butir 4, 5, 35-37, 43 diuji otomatis; uji baca keras (42) oleh Diya; audit manusia/Claude belum berjalan. Seluruh ayat diverifikasi terhadap API, bukan ingatan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.