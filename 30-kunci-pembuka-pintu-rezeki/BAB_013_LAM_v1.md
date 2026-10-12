# LAM (LEMBAR AUDIT MANDIRI) — BAB 13 (TIPE B)

Tipe B | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | L | 19/19 identik (audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | L | Lengkap; dalil 3, sisanya 1 - dalam batas |
| A3 | Kepala bab memuat baris Dalil | L | Sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | L | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | L | 7694 vs 8200 = -6.2% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | L | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | L | checklist + praktik terpasang |
| A8 | Bab Tipe A ditutup Praktik dan Doa | N/A | Bab Tipe B - ditutup praktik dan muhasabah |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | L | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | L | dicek terhadap TOC |
| B1 | Tidak ada dalil yang dikarang | L | 3 ayat diverifikasi utuh dari API |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | L | Dua rujukan hadits TOC ditulis tanpa nomor dan tidak dikutip sebagai teks |
| B3 | Setiap ayat [V-AYAT] | L | Terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | L | 3 baris + catatan hadits TOC |
| B5 | Derajat dipisahkan dari pemahaman | L | Tidak ada derajat yang diklaim |
| B6 | Perbedaan pendapat dipaparkan adil | L | 13.15 dan 13.16 membedah per kasus, bukan vonis kategori |
| B7 | Setiap pernyataan hukum bertingkat dasar | L | Tabel tingkat-dasar terpasang |
| B8 | Tidak ada fatwa yang diingat samar | L | [FATWA-CEK] pada bagian fatwa-regulasi |
| B9 | Kutipan disusun ulang | L | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | L | Tidak dipakai sebagai dasar |
| C1 | Tidak ada kalimat menjanjikan hasil | L | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | L | Tidak ada; fokus pada rambu transaksi, bukan pada orangnya |
| C3 | Tidak ada vonis halal/haram kategori | L | 0 frasa vonis kategori (dicek regex) |
| C4 | Tidak ada doa/amalan baru tanpa dalil | L | Muhasabah tanpa doa wajib (Tipe B) |
| C5 | Tidak ada merek | L | 0 temuan (dicek manual 20 kandidat merek) |
| C6 | Tidak ada ramalan bertanggal | L | Tidak ada |
| C7 | Kisah modern bukan bukti pertolongan Allah | L | Kisah berlabel komposit |
| C8 | Disclaimer pada bab yang memerlukan | L | blok batas-kewenangan terpasang |
| D1 | Tidak ada angka karangan | L | Simulasi memakai angka berlabel ilustrasi |
| D2 | Angka ilustrasi diberi label | L | Label pada simulasi |
| D3 | Kotak Bukti memuat sumber tahun batas | L | Bagian regulasi diberi tanggal dan [FATWA-CEK] |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | L | Blok kisah berlabel komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | L | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | L | Hanya tokoh komposit |
| E1 | Tidak ada frasa Bagian 7.3 | L | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | L | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | L | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | L | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | L | contoh pasar, warung, dan transaksi disebutkan |
| E6 | Ejaan sesuai daftar | L | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | L | gharar, maysir, tadlis, najasy dijelaskan |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | L | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | L | audit_bab.py bersih; HTML 0; tanpa tanda (—) |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | L | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | L | Riba di sini ringkasan peta, pembahasan lengkap di Bab 60-61 (dijelaskan) |
| F4 | Semua [TANYA DATO'] jelas dengan usulan | L | Tidak ada butir baru |

**Skor: 45/45 = 100 persen** (butir n/a dikeluarkan).

Catatan jujur: bab ini PERNAH ditolak. Draf pertama memuat 3 paragraf boilerplate diulang 49 kali sehingga angka kata 7.441 palsu (isi sebenarnya 4.297). Diya membongkar semuanya, lalu bab diperdalam ulang hingga 7.694 kata isi asli, 0 paragraf ganda, 3 ayat diverifikasi utuh. Audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.