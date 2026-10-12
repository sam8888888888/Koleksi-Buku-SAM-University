# LAM (LEMBAR AUDIT MANDIRI) — BAB 16 (TIPE B)

Tipe B | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | L | 14/14 identik (audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | L | Semua elemen dalam batas; dalil 2, pendapat-ulama 2, checklist 2, titik-risiko 2 |
| A3 | Kepala bab memuat baris Dalil | L | Sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | L | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | L | 6599 vs 6900 = -4.4% |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | L | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | L | checklist + praktik terpasang |
| A8 | Bab Tipe A ditutup Praktik dan Doa | N/A | Bab Tipe B - ditutup praktik dan muhasabah |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | L | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | L | dicek terhadap TOC |
| B1 | Tidak ada dalil yang dikarang | L | 2 ayat diverifikasi utuh dari API |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | L | Rujukan HR. Ahmad/Tirmidzi TOC ditulis tanpa nomor dan tidak dikutip |
| B3 | Setiap ayat [V-AYAT] | L | Terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | L | 2 baris + catatan hadits TOC |
| B5 | Derajat dipisahkan dari pemahaman | L | Tidak ada derajat yang diklaim |
| B6 | Perbedaan pendapat dipaparkan adil | L | 16.4-16.7 membedakan peran negara dan batasnya |
| B7 | Setiap pernyataan hukum bertingkat dasar | L | Tingkat dasar disebut pada bagian yang muatan hukumnya kuat |
| B8 | Tidak ada fatwa yang diingat samar | L | [FATWA-CEK] pada bagian fatwa-regulasi |
| B9 | Kutipan disusun ulang | L | Tidak ada kutipan panjang pihak lain |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | L | Tidak dipakai sebagai dasar |
| C1 | Tidak ada kalimat menjanjikan hasil | L | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | L | 16.14 justru menimbang akses yang benar-benar terpakai |
| C3 | Tidak ada vonis halal/haram kategori | L | Tidak ada |
| C4 | Tidak ada doa/amalan baru tanpa dalil | L | Muhasabah tanpa doa wajib (Tipe B) |
| C5 | Tidak ada merek | L | 0 temuan (dicek manual 21 kandidat merek; platform dan bank disebut umum) |
| C6 | Tidak ada ramalan bertanggal | L | Kripto/uang digital dibaca tanpa prediksi harga |
| C7 | Kisah modern bukan bukti pertolongan Allah | L | Contoh berlabel ilustrasi/komposit |
| C8 | Disclaimer pada bab yang memerlukan | L | blok batas-kewenangan terpasang |
| D1 | Tidak ada angka karangan | L | Tidak ada statistik di bab ini; angka ilustrasi dilabeli |
| D2 | Angka ilustrasi diberi label | L | Label pada simulasi |
| D3 | Kotak Bukti memuat sumber tahun batas | L | Bila perlu data makro ditandai [DATA DIPERLUKAN] dengan tahun |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | L | Contoh komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | L | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | L | Tidak ada |
| E1 | Tidak ada frasa Bagian 7.3 | L | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | L | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | L | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | L | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | L | pengadaan, kuitansi, verifikasi dokumen, tiket aduan disebut |
| E6 | Ejaan sesuai daftar | L | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | L | inklusi keuangan, modal sosial, algoritma dijelaskan |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | L | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | L | audit_bab.py bersih; HTML 0; ::: tidak menempel; tanpa tanda (—) |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | L | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | L | Korupsi (16.6) fokus pada dampak dan jalur aduan, tanpa menuduh pihak tertentu |
| F4 | Semua [TANYA DATO] jelas dengan usulan | L | Tidak ada butir baru |

**Skor: 45/45 = 100 persen** (butir n/a dikeluarkan).

Catatan jujur: draf awal anak buah lolos audit tapi mepet di batas bawah (-10,0%); Diya menambah 5 paragraf unik agar menjadi -4,4% sambil mempertahankan semua sub-bab dalam rentang. Audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI.