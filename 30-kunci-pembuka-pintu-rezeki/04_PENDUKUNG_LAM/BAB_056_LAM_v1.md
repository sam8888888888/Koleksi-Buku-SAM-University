# LAM (LEMBAR AUDIT MANDIRI) — BAB 56 (TIPE A)

Audit otomatis: dijalankan; hasil awal gagal | Audit manusia: belum dilakukan | Status: DRAF, BELUM LULUS

| Butir | Pemeriksaan | Status awal |
|---|---|---|
| Judul dan subbab | 19 judul cocok dengan Bab 56 TOC | Otomatis cocok |
| Struktur Mode A | Blok utama tersedia | Periksa ulang urutan/kelengkapan |
| Pembuka | Pemeriksaan kata audit | Lulus pada audit awal |
| Rentang kata | 56.1 serta banyak subbab di bawah rentang; total 5,473/8,500 | Gagal; perlu ekspansi substansial |
| Dalil | Empat ayat, belum ada pada Bank Dalil saat audit | Gagal; butuh persetujuan/penambahan bank dan audit ulang |
| Janji hasil | Kalimat “pasti lunas” ditandai | Perlu penyuntingan kalimat |
| PHK, utang, hukum, bantuan, penagihan | Detail tidak terverifikasi diberi [DATA DIPERLUKAN]/[KONTAK-CEK] | Audit ahli dan cek sumber resmi diperlukan |
| Perlindungan korban | KDRT dan penipuan tanpa menyalahkan korban | Tetap perlu review keselamatan dan hukum |
| Duplikat paragraf | Belum diaudit ulang pasca finalisasi | Jalankan checker dan catat hasil |
| DOCX | Perlu dibuat dan dicek bila konverter tersedia | Belum diverifikasi |

Audit awal `python3 audit_bab.py BAB_056_Bangkit_dari_Krisis_v1.md 56 A`: `kata=5473`, `anggaran=8500`, `dev_pct=-35.6`, 19 subbab ditemukan, `lolus=false`. Temuan: panjang subbab/total, frasa janji hasil, dan tiga teks ayat belum ada di BANK_DALIL. Jangan menyatakan lulus sebelum semua diperbaiki dan diperiksa ulang.

Perlu pemeriksaan manusia: teks/terjemah ayat, tafsir dan penerapan QS At-Talaq:7, hukum ketenagakerjaan, PKPU/kepailitan, praktik penagihan, bantuan resmi, dan keselamatan KDRT. Skor akhir tidak ditetapkan.

## Pembaruan setelah ekspansi
Naskah diperluas dan diperiksa ulang. Audit final: 8.847 kata, anggaran 8.500, deviasi +3,7%, 19 sub-bab dikenali, `temuan: []`, `lolus: true`. Pemeriksaan paragraf dengan `collections.Counter` menghasilkan 0 duplikat.
