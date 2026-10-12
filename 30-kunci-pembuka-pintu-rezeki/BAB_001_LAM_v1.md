# LAM (LEMBAR AUDIT MANDIRI) — BAB 1 (TIPE A)

Tipe A | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | LULUS | 17/17 sub-bab identik (dicek audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | LULUS | Seluruh elemen Tipe A terpasang termasuk doa dan coba-sekarang |
| A3 | Kepala bab memuat baris Dalil dan keterangan TOC | LULUS | 3 dalil + baris keterangan dari TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | LULUS | audit_bab.py: 0 sub-bab di luar rentang |
| A5 | Total bab dalam toleransi plus minus 10 persen | LULUS | 9501 vs 9500 = +0.0% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | LULUS | tokoh Dimas, kantor di Surabaya |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | LULUS | Kolom lengkap pada aksi-7-hari |
| A8 | Bab Tipe A ditutup Praktik dan Doa | LULUS | aksi-7-hari, muhasabah, doa |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | LULUS | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | LULUS | Bab 2, Bab 4, Bab 9 - semuanya ada di TOC |
| B1 | Tidak ada dalil yang dikarang | LULUS | 4 ayat dari baris Dalil TOC; tanpa nomor hadits karangan |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | LULUS | Satu rujukan salaf ditulis sebagai rujukan umum + [DERAJAT-CEK] |
| B3 | Setiap ayat [V-AYAT] | LULUS | 4 [V-AYAT] pada 4 blok dalil |
| B4 | Lembar Verifikasi memuat semua dalil | LULUS | 5 baris |
| B5 | Derajat dipisahkan dari pemahaman | LULUS | Seluruh derajat ditandai |
| B6 | Perbedaan pendapat dipaparkan adil | LULUS | 1.15 memaparkan jalur teologi dan tasawuf tanpa memihak |
| B7 | Setiap pernyataan hukum bertingkat dasar | LULUS | Tabel tingkat-dasar 6 pernyataan |
| B8 | Tidak ada fatwa yang diingat samar | LULUS | Tidak ada fatwa dikutip |
| B9 | Kutipan disusun ulang | LULUS | Tidak ada kutipan panjang dari sumber lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | LULUS | Tidak ada riwayat tanpa sanad yang dipakai |
| C1 | Tidak ada kalimat menjanjikan hasil | LULUS | audit_bab.py: 0 temuan janji/rumus |
| C2 | Tidak ada kalimat menyalahkan orang miskin | LULUS | Tidak ada |
| C3 | Tidak ada vonis halal/haram kategori | LULUS | Bab ini konsep, tanpa vonis produk |
| C4 | Tidak ada doa/amalan baru tanpa dalil | LULUS | Doa penutup dari QS. Al-Baqarah: 172 |
| C5 | Tidak ada merek | LULUS | 0 temuan |
| C6 | Tidak ada ramalan bertanggal | LULUS | Tidak ada tahun |
| C7 | Kisah modern bukan bukti pertolongan Allah | LULUS | Dua kisah berlabel komposit tanpa klaim |
| C8 | Disclaimer pada bab yang memerlukan | LULUS | Bab ini bukan bab investasi/pajak/waris |
| D1 | Tidak ada angka karangan | LULUS | Seluruh angka berlabel ilustrasi (Lembar Data) |
| D2 | Angka ilustrasi diberi label | LULUS | Label ilustrasi pada 1.1 dan 1.7 |
| D3 | Kotak Bukti memuat sumber tahun batas | LULUS | Tidak ada data sains dikutip; kebutuhan data ditandai |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | LULUS | Dimas, Rina, Pak Har sesuai KARAKTER_TOKOH |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | LULUS | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | LULUS | Hanya tokoh komposit dan Nabi/sahabat secara umum |
| E1 | Tidak ada frasa Bagian 7.3 | LULUS | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | LULUS | Kalimat lebih dari 55 kata hanya baris tabel, bukan prosa |
| E3 | Maksimal dua daftar per sub-bab | LULUS | audit_bab.py: 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | LULUS | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | LULUS | kantor Surabaya, Bekasi, Semarang, catatan bulanan |
| E6 | Ejaan sesuai daftar | LULUS | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | LULUS | Kosakata Arab dijelaskan di istilah-kunci |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | LULUS | Uji baca mandiri Diya; belum dibaca manusia |
| F1 | Mode A: blok ::: tertutup dan namanya benar | LULUS | audit_bab.py: buka/tutup seimbang, nama sah |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | LULUS | Naskah + 4 lembar pendamping |
| F3 | Bab sensitif memenuhi Bagian 8 | LULUS | Bab ini bukan bab sensitif dalam daftar |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | LULUS | Tidak ada butir baru; 4 butir lama sudah dijawab Dato |

**Skor: 46/46 = 100 persen** (tidak dibulatkan ke atas).

Catatan jujur: butir 4, 5, 35-37, 43 diuji otomatis; uji baca keras (42) baru oleh Diya; audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.