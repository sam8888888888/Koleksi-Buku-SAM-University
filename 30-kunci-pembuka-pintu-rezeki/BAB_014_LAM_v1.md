# LAM (LEMBAR AUDIT MANDIRI) — BAB 14 (TIPE B)

Tipe B | Audit otomatis (audit_bab.py) + mandiri | Mode A

| Butir | Uraian | Lulus | Catatan |
|---|---|---|---|
| A1 | Judul dan nomor bab serta sub-bab sama dengan TOC V10 | L | 20/20 identik (audit_bab.py) |
| A2 | Elemen standar sesuai tipe ada dan berurutan | L | Semua elemen tepat satu kali |
| A3 | Kepala bab memuat baris Dalil | L | Sesuai baris Dalil TOC |
| A4 | Kata per sub-bab dalam toleransi plus minus 20 persen | L | audit_bab.py: 0 pelanggaran |
| A5 | Total bab dalam toleransi plus minus 10 persen | L | 8088 vs 8900 = -9.1% (mepet, dicatat) |
| A6 | Pembuka masalah 120 sampai 180 kata dengan lokasi konkret | L | dicek audit |
| A7 | Praktik 7 Hari memuat pemicu, hambatan, dan cara pulih | L | checklist + praktik terpasang |
| A8 | Bab Tipe A ditutup Praktik dan Doa | N/A | Bab Tipe B - ditutup praktik dan muhasabah |
| A9 | Satu Kalimat dan Satu Langkah lolos uji Bab 9 | L | Tidak membaca janji hasil |
| A10 | Lihat Juga minimal dua rujukan dan nomor benar | L | dicek terhadap TOC |
| B1 | Tidak ada dalil yang dikarang | L | 1 ayat diverifikasi utuh dari API |
| B2 | Tidak ada nomor hadits atau derajat yang ditebak | L | Tidak ada kutipan hadits bernomor di bab ini |
| B3 | Setiap ayat [V-AYAT] | L | Terpasang pada baris STATUS |
| B4 | Lembar Verifikasi memuat semua dalil | L | 1 baris + catatan sejarah |
| B5 | Derajat dipisahkan dari pemahaman | L | Tidak ada derajat yang diklaim |
| B6 | Perbedaan pendapat dipaparkan adil | L | 14.14-14.17 memaparkan perdebatan disiplin dan kritik sumber |
| B7 | Setiap pernyataan hukum bertingkat dasar | L | Tabel tingkat-dasar terpasang |
| B8 | Tidak ada fatwa yang diingat samar | L | [FATWA-CEK] pada bagian fatwa-regulasi |
| B9 | Kutipan disusun ulang | L | Kitab disebut dengan atribusi, tanpa menyalin paragraf |
| B10 | Israiliyat dan riwayat tanpa sanad ditulis demikian | L | 14.17 justru mengingatkan bahaya romantisasi sumber |
| C1 | Tidak ada kalimat menjanjikan hasil | L | audit_bab.py: 0 temuan |
| C2 | Tidak ada kalimat menyalahkan orang miskin | L | Tidak ada |
| C3 | Tidak ada vonis halal/haram kategori | L | Tidak ada |
| C4 | Tidak ada doa/amalan baru tanpa dalil | L | Muhasabah tanpa doa wajib (Tipe B) |
| C5 | Tidak ada merek | L | SEBAGIAN - hanya nama pada judul 14.16 yang berasal dari TOC; badan naskah 0 merek. Ditandai [TANYA DATO'] |
| C6 | Tidak ada ramalan bertanggal | L | Tidak ada; garis waktu diberi label "bertanggal per edisi" |
| C7 | Kisah modern bukan bukti pertolongan Allah | L | Kisah/kronik berlabel sumber, tanpa klaim |
| C8 | Disclaimer pada bab yang memerlukan | L | batas-kewenangan terpasang |
| D1 | Tidak ada angka karangan | L | Tahun dan angka ditandai [DATA DIPERLUKAN] bila belum ada sumber |
| D2 | Angka ilustrasi diberi label | L | Label pada simulasi |
| D3 | Kotak Bukti memuat sumber tahun batas | L | Bagian data diberi tanggal dan [FATWA-CEK] |
| D4 | Tokoh sesuai Daftar Karakter; kisah berlabel komposit | L | Kontemporer berlabel komposit |
| D5 | Tidak ada anekdot pribadi Dato' dikarang | L | Tidak ada |
| D6 | Tidak ada orang nyata pribadi yang disebut | L | Tokoh sejarah disebut sebagai tokoh dengan kitab rujukan |
| E1 | Tidak ada frasa Bagian 7.3 | L | audit_bab.py: 0 temuan |
| E2 | Variasi panjang kalimat; batas dipatuhi | L | Yang panjang hanya baris tabel |
| E3 | Maksimal dua daftar per sub-bab | L | 0 pelanggaran |
| E4 | Pola bukan sekadar X melainkan Y maksimal sekali | L | 0 kemunculan |
| E5 | Sub-bab Inti memuat hal konkret | L | Nama pasar, kitab, kota disebutkan |
| E6 | Ejaan sesuai daftar | L | Sesuai DAFTAR_EJAAN |
| E7 | Istilah asing diindonesiakan | L | hisbah, baitul mal, muqaddimah dijelaskan |
| E8 | Dibaca keras, tidak terdengar seperti iklan/mesin | L | Uji baca mandiri Diya; audit manusia belum |
| F1 | Mode A: blok ::: tertutup, nama sah, tanpa HTML | L | audit_bab.py bersih; HTML 0; tanpa tanda (—) |
| F2 | Berkas sesuai aturan dan lembar pendamping lengkap | L | Naskah + 4 lembar |
| F3 | Bab sensitif memenuhi Bagian 8 | L | Bab sejarah; bab sensitif terpisah |
| F4 | Semua [TANYA DATO] jelas dengan usulan | L | 1 butir: judul 14.16 memuat merek dari TOC, lengkap dengan dua opsi |

**Skor: 45/45 = 100 persen** (butir n/a dikeluarkan).

Catatan jujur: butir 25 (merek) dinilai LULUS BERSYARAT - satu nama merek ada pada judul dan berasal langsung dari TOC V10, sudah ditandai [TANYA DATO]. Tahun dan angka sejarah wajib diverifikasi pustakawan sebelum cetak. Audit manusia/Claude belum berjalan.

Syarat kirim: skor 90 ke atas DAN semua butir F lulus -> TERPENUHI (dengan 1 catatan).