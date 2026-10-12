# HANDOFF — 30 KUNCI PEMBUKA PINTU REZEKI (sesi baru, lanjut Bab 63)

Tempel ini sebagai pesan pertama di sesi baru. Diya akan langsung tahu posisi dan melanjutkan.

## POSISI SEKARANG
- **Selesai & lolos audit: Bab 1–62** (semua `temuan: []`, `lolus: true` di audit terakhir). Bab 61 (8.538 kata, dev 6,8%) dan Bab 62 (9.231 kata, dev 1,5%) baru saja tuntas — keduanya Tipe B, 12 blok B lengkap, DOCX + QC lolos.
- **Berikutnya: Bab 63** (baca blok TOC `### Bab 63.` untuk judul, sub-bab, dalil).
- Kerja **per dua bab (63+64)**, tidak lanjut 65 sebelum 63–64 lulus audit + izin Boss.

## ATURAN UTAMA (sudah teruji, jangan dilanggar)
1. **Kurung ayat nomor: `(..)` biasa. `﴿..﴾` DILARANG** (Boss: "salah besar"). Nomor ayat Arab-Indic `(١٢)` di belakang teks Arab; nomor Latin `(12)` di belakang terjemah.
2. Label kanonik blok `::: dalil`: `ARAB:` / `QS. Nama: nomor` / `Artinya:` / `DERAJAT:` / `RUJUKAN:` / `STATUS:`. Tidak ada transliterasi Latin (`LATIN: n.a. (transliterasi tidak dipakai; teks Arab dibaca langsung)`).
3. Teks Arab/hadits HANYA dari sumber: quran.nu.or.id per ayat (fallback `https://api.alquran.cloud/v1/ayah/<n>:<v>/quran-uthmani`), hadits.id + silang sunnah.com. **Jangan pernah dari ingatan; nomor beda antar basis data.** Kalau ragu → tulis tanpa nomor + `[DERAJAT-CEK]`.
4. Frasa terlarang: di era digital, tidak dapat dipungkiri, penting untuk dicatat, mari kita selami, pada akhirnya, sebagai kesimpulan, mengupas tuntas, komprehensif, holistik, krusial, esensial, paradigma, lanskap, sinergi, transformasi, tanda `—`. Bahasa proses produksi (TOC/naskah/penerbit/audit/sub-bab/Bank Dalil) dilarang di prosa. Tanpa merek fintech/bank/platform (deskripsi generik).
5. **BANK_DALIL_DRAF_v1.md: hanya kurator (Diya) yang edit**, selalu backup dulu (`.bak.pre_bab0XX`). Ayat/hadits baru dicatat di lembar Verifikasi lalu di-merge kurator.
6. Stage gate: setelah 2 bab lulus → **lapor Boss + PAUSE**, tunggu izin sebelum bab berikutnya.

## CARA MENULIS BAB (PELAJARAN PALING PENTING — 3 agent gagal karena ini)
- **JANGAN tulis bab penuh sekali jalan** — agent konsisten berhenti dini (Bab 61 pernah cuma 761 kata; Bab 62 cuma 3.582). Pecah jadi **batch kecil 4–7 sub-bab per agent, serial per file**, baru batch final (blok Tipe B + penutup + lembar).
- Aturan keras agent: **panggilan pertama WAJIB langsung `write_file`** (jangan riset dulu).
- Hitung target kata presisi SEBELUM dispatch: rentang ketat per penanda `●560-840`, `◐320-480`, `○160-240`; total bab = anggaran ±10% (cek ANGGARAN_KATA_V10_Usulan.md; tipe B bila bab 10–19, 60–62, 66–91, sisanya A).
- Kurator WAJIB verifikasi sendiri: audit ulang, baca bagian kritis, cek teks Arab vs sumber, QC DOCX (semua paragraf Arab `right` + `rtl`).

## ALAT
- Audit: `cd /home/diya/books/30-kunci-pembuka-pintu-rezeki && python3 audit_bab.py <file.md> <nomor> <A|B>` → wajib `temuan: []`, `lolus: true` (temuan BANK diperbolehkan).
- Render: `python3 render_bab_docx.py <file.md>`; QC: cek `word/document.xml` (semua paragraf berhuruf Arab harus `<w:jc w:val="right"/>` + `<w:rtl/>`; `soffice --headless --convert-to pdf` → `pdftotext` untuk jumlah halaman).
- Skill kanonik: `30-kunci-bab-production`, `naskah-arab-indonesia`, `30-kunci-audit-kualitas-naskah`.
- `audit_bab.py` sudah punya pengecualian `NOMOR_AYAT`; TOC path permanen di folder proyek (jangan pakai cache).

## FILE PROYEK (folder `/home/diya/books/30-kunci-pembuka-pintu-rezeki/`)
- Kanonik: `TOC_V10_30_Kunci_Pembuka_Pintu_Rezeki.md`, `PROMPT_MASTER_DIYA_30_KUNCI.md`, `ANGGARAN_KATA_V10_Usulan.md`, `PENANDA_KEDALAMAN_V10_Usulan.md`, `BANK_DALIL_DRAF_v1.md`, `audit_bab.py`, `render_bab_docx.py`.
- Naskah: `BAB_0XX_*_v1.md/.docx` + 4 lembar pendamping (`_Verifikasi`, `_Data`, `_LAM`, `_Serah_Terima`).
- Backup: `_BACKUP_pre_audit60/` + per-file `.bak.pre_*`.

## PEKERJAAN TERTUNDA (setelah batch 63–64, atau bila Boss perintah)
- Penanda tersisa lintas Bab 1–60: 93 `[TERJEMAH-CEK]` + 87 `[DERAJAT-CEK]` + 18 `[FATWA-CEK]` + 10 `[DATA DIPERLUKAN]` + 10 `[KONTAK-CEK]` (daftar per bab di lembar masing-masing; mayoritas terjemah ayat butuh terjemah resmi + riwayat tanpa nomor). Bab 61: 3; Bab 62: 5.
- Bab 66 "Anatomi Akad" sudah ada & lolos (10.527 kata) — di luar batch.
- Bab 63–105 belum ditulis.

## PERINTAH TERAKHIR BOSS
"lanjut ke penulisan bab 63, kerjakan per dua bab. tidak boleh lanjut ke bab berikutnya sebelum dua bab beres dan lulus audit."
