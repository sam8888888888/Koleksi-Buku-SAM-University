#!/usr/bin/env python3
"""Audit otomatis satu bab buku 30 Kunci. Pemakaian: python3 audit_bab.py BAB_001_....md 1 A
Menghasilkan daftar temuan + skor LAM (butir yang bisa diuji otomatis)."""
import re, sys, json, collections

D = '/home/diya/books/30-kunci-pembuka-pintu-rezeki/'
TOC = '/home/diya/books/30-kunci-pembuka-pintu-rezeki/TOC_V10_30_Kunci_Pembuka_Pintu_Rezeki.md'  # kanonik permanen; jangan pakai cache (ter-prune 24 jam)
BANNED = ['di era digital', 'tidak dapat dipungkiri', 'penting untuk dicatat', 'mari kita selami',
          'pada akhirnya', 'sebagai kesimpulan', 'mengupas tuntas', 'komprehensif', 'holistik',
          'krusial', 'esensial', 'paradigma', 'lanskap', 'sinergi', 'transformasi', '—']
ELEM_A = ['kepala-bab', 'pembuka-masalah', 'pertanyaan-utama', 'ringkasan', 'istilah-kunci', 'dalil',
          'tingkat-dasar', 'janji-nyata', 'salah-paham', 'fiqh-praktis', 'kasus', 'kisah',
          'aksi-7-hari', 'muhasabah', 'satu-kalimat', 'lihat-juga']
ELEM_B_EXTRA = ['istilah-akad', 'struktur-akad', 'pendapat-ulama', 'fatwa-regulasi', 'contoh-transaksi',
                'titik-risiko', 'penerapan-keluarga', 'penerapan-kerja', 'simulasi', 'checklist',
                'batas-kewenangan', 'jangkar-abadi']
ALLOWED = set('''kepala-bab pembuka-masalah pertanyaan-utama ringkasan istilah-kunci dalil tingkat-dasar
kriteria-kunci janji-nyata salah-paham fiqh-praktis kasus kisah jangkar-abadi aksi-7-hari muhasabah doa
satu-kalimat pull-quote lihat-juga pagar-editorial coba-sekarang kotak-jujur kotak-bukti disclaimer
istilah-akad struktur-akad pendapat-ulama fatwa-regulasi contoh-transaksi titik-risiko penerapan-keluarga
penerapan-kerja simulasi checklist batas-kewenangan produk-contoh kisah-pembuka peta-jilid penegasan
jeda-refleksi'''.split())
BR = {'●': (560, 840), '◐': (320, 480), '○': (160, 240)}


def prose(seg):
    return len(re.findall(r'[A-Za-z]+', re.sub(r'(?ms)^::: \S+.*?^:::\s*$', '', seg)))


def main(path, bab, tipe):
    t = open(path, encoding='utf-8').read()
    toc = open(TOC, encoding='utf-8').read()
    i = toc.find(f'### Bab {bab}.'); j = toc.find(f'### Bab {bab+1}.')
    sec = toc[i:j if j > 0 else len(toc)]
    subs = [x[2:] for x in re.findall(rf'^- {bab}\.\d+ .*$', sec, re.M)]
    find = []
    # 1 judul sub-bab persis TOC
    if tipe == 'C':  # FAQ: heading = pertanyaan tanpa kurung rujukan TOC; nomor saja yang diverifikasi
        _nums_draft = set(re.findall(rf'(?m)^## ({bab}\.\d+) ', t))
        _nums_toc = set(re.findall(rf'^- ({bab}\.\d+) ', sec, re.M))
        for n in sorted(_nums_toc - _nums_draft, key=lambda x: int(x.split('.')[1])):
            find.append(f'SUB-BAB FAQ HILANG: {n}')
    else:
        for s in subs:
            if '## ' + s not in t:
                find.append(f'JUDUL SUB-BAB HILANG/BERBEDA: {s[:70]}')
    # 2 blok seimbang + nama sah
    buka = re.findall(r'(?m)^::: (\S+)', t); tutup = len(re.findall(r'(?m)^:::\s*$', t))
    if len(buka) != tutup:
        find.append(f'BLOK TIDAK SEIMBANG: buka {len(buka)} tutup {tutup}')
    for n in set(buka):
        if n not in ALLOWED:
            find.append(f'NAMA BLOK TIDAK SAH: {n}')
    # 3 frasa terlarang
    _tl = '\n'.join(_l for _l in t.splitlines() if not (_l.startswith('## ') or _l.startswith('# '))).lower()
    for b in BANNED:
        c = _tl.count(b.lower())
        if c:
            find.append(f'FRASA TERLARANG "{b}" x{c}')
    # 4 pembuka masalah 120-180
    m = re.search(r'(?s)::: pembuka-masalah\n(.*?)\n:::', t)
    if not m:
        find.append('BLOK pembuka-masalah TIDAK ADA')
    else:
        w = len(re.findall(r'\w+', m.group(1)))
        if not (120 <= w <= 180):
            find.append(f'PEMBUKA {w} kata (syarat 120-180)')
    # 5 elemen tipe
    if tipe == 'C':  # bab FAQ: hanya blok pembungkus; jawaban = heading + paragraf
        need = ['kepala-bab', 'pembuka-masalah', 'muhasabah', 'satu-kalimat', 'lihat-juga']
    elif tipe == 'A':
        need = ELEM_A
    else:
        need = ['kepala-bab', 'pembuka-masalah', 'pertanyaan-utama', 'ringkasan', 'dalil',
                'muhasabah', 'satu-kalimat', 'lihat-juga'] + ELEM_B_EXTRA
    need = list(need)
    # 'dalil' hanya wajib bila baris *Dalil:* ada di blok TOC bab ini
    if 'dalil' in need:
        try:
            _i = toc.find(f'### Bab {bab}.')
            _j = toc.find('### Bab ', _i + 1)
            _seg = toc[_i: _j if _j > 0 else len(toc)]
            if '*Dalil:' not in _seg:
                need = [x for x in need if x != 'dalil']
                # INFO: TOC tanpa baris Dalil -> 'dalil' tidak diwajibkan (bukan temuan)
        except Exception:
            pass
    for e in need:
        if f'::: {e}' not in t:
            find.append(f'ELEMEN KURANG: {e}')
    if tipe == 'A' and '::: doa' not in t:
        find.append('TIPE A TANPA blok doa')
    # 6 penanda per sub-bab
    pen = {}
    if tipe == 'C':
        pass  # FAQ tanpa penanda kedalaman
    for l in open(D + 'PENANDA_KEDALAMAN_V10_Usulan.md', encoding='utf-8').read().split('\n') if tipe != 'C' else []:
        mm = re.match(rf'\| {bab} \| ([\d.]+) \| .* \| (●|◐|○) \|$', l)
        if mm:
            pen[mm.group(1)] = mm.group(2)
    heads = [(mm.start(), mm.group(1)) for mm in re.finditer(r'(?m)^## (\d+\.\d+) ', t)]
    out_of = []
    for k, (pos, code) in enumerate(heads):
        end = heads[k+1][0] if k+1 < len(heads) else len(t)
        w = prose(t[pos:end]); dp = pen.get(code)
        if not dp:
            continue
        lo, hi = BR[dp]
        if not (lo <= w <= hi):
            out_of.append(f'{code} {w} kata penanda {dp} (rentang {lo}-{hi})')
    if out_of:
        find.append('SUB-BAB DI LUAR TOLERANSI ±20%: ' + '; '.join(out_of))
    # 7 total bab vs anggaran
    total = len(re.findall(r'[A-Za-z]+', t))
    ang = None
    if tipe == 'C' and bab == 105:
        ang = 10500  # 68 jawaban FAQ x 120-200 kata (baris ANGGARAN 66)
    for l in open(D + 'ANGGARAN_KATA_V10_Usulan.md', encoding='utf-8').read().split('\n'):
        if l.startswith(f'| {bab} |') and ang is None:
            ang = int(l.split('|')[6].strip())
    dev = (total - ang) / ang * 100 if ang else 0
    if abs(dev) > 10:
        find.append(f'TOTAL BAB {total} vs anggaran {ang} = {dev:+.1f}% (batas ±10%)')
    # 8 penanda verifikasi ayat/hadits
    if re.search(r'<!--|-->', t) or re.search(r'<[a-z]+[ >]', t):
        find.append('KOMENTAR/TAG HTML TERSISA (Mode A tanpa HTML)')
    if '{{ARAB-AYAT' in t:
        find.append(f'PLACEHOLDER ARAB AYAT TERSISA: x{t.count("{{ARAB-AYAT")}')
    # placeholder hadits dibiarkan: teks hadits hanya dari pemeriksa manusia (catatan, bukan temuan)
    ayat_blocks = len(re.findall(r'(?m)^RUJUKAN: QS\.', t))
    if tipe in 'AB' and ayat_blocks and t.count('[V-AYAT]') < ayat_blocks:
        find.append(f'[V-AYAT] kurang dari jumlah blok ayat ({t.count("[V-AYAT]")} vs {ayat_blocks})')
    # 9 daftar per sub-bab maks 2 grup
    for k, (pos, code) in enumerate(heads):
        end = heads[k+1][0] if k+1 < len(heads) else len(t)
        seg = t[pos:end]; g = 0; prev = False
        for line in seg.split('\n'):
            b = line.startswith('- ')
            if b and not prev:
                g += 1
            prev = b
        if g > 2:
            find.append(f'{code}: {g} grup daftar (maks 2)')
    # 10 lihat-juga minimal 2 + nomor valid
    lj = re.search(r'(?s)::: lihat-juga\n(.*?)\n:::', t)
    if not lj:
        find.append('BLOK lihat-juga TIDAK ADA')
    else:
        nums = [int(x) for x in re.findall(r'Bab (\d+)', lj.group(1))]
        if len(set(nums)) < 2:
            find.append('lihat-juga kurang dari 2 rujukan')
        for n in nums:
            if not (1 <= n <= 105) or f'### Bab {n}.' not in toc:
                find.append(f'lihat-juga nomor salah: Bab {n}')
    # 11 janji hasil / vonis (deteksi sederhana)
    NEG = ('bukan', 'jangan', 'tidak', 'tanpa', 'menyombongkan', 'meyakinkan', 'apakah', 'berbohong',
           'antara', 'menyebut', 'dijamin rizq', 'salah paham', 'salah-paham', 'kesalahpahaman', 'pembacaan', 'muncul pembacaan', 'keliru')
    # 'rumus' hanya dianggap janji hasil bila berpasangan dengan kata hasil/kaya;
    # TOC memakai 'Rumus' sebagai konsep mis. 'Rumus Niat Tiga Lapis' (bab 22) yang sah.
    RUMUS_AMAN = ('niat', 'baca', 'tulis', 'langkah', 'kerangka', 'pola', 'tiga lapis', 'daftar', 'cek')
    for mm in re.finditer(r'[^.\n]*(pasti (kaya|datang|lunas|berhasil)|dijamin |rumus )[^.\n]*', t, re.I):
        frag = mm.group(0)
        if frag.lstrip().startswith('#'):  # judul sub-bab dari TOC
            continue
        _ln = t[t.rfind('\n', 0, mm.start())+1: t.find('\n', mm.end())]
        if _ln.lstrip().startswith('## ') or _ln.lstrip().startswith('# '):  # frag dari baris heading (titik nomor memotong regex)
            continue
        low = frag.lower()
        if any(n in low for n in NEG):
            continue
        if '---' in frag or '|' in frag:  # baris tabel
            continue
        if 'rumus' in low and not any(k in low for k in ('kaya', 'rezeki', 'rezek', 'untung', 'berhasil',
                                                         'sukses', 'pasti', 'dijamin', 'cepat datang')):
            continue  # rumus dipakai sebagai konsep, bukan janji hasil
        find.append('KALIMAT JANJI HASIL/RUMUS: ' + frag.strip()[:120])
    # 12 angka ilustrasi tanpa label: angka % atau 'persen' di luar blok tabel
    persen = [x for x in re.findall(r'[^.\n]*\b\d+[,.]?\d*\s*(?:persen|%)[^.\n]*', t)]
    unl = [x.strip()[:90] for x in persen if 'ilustrasi' not in x.lower() and '---' not in x]
    if unl:
        find.append(f'ANGKA PERSEN TANPA LABEL ilustrasi: {unl[:3]}')
    # jumlah elemen per bab (Prompt Bagian 6): satu-kalimat/muhasabah/doa/lihat-juga/tingkat-dasar/janji-nyata/aksi-7-hari = 1; coba-sekarang <=2; salah-paham <=4
    BATAS = {'satu-kalimat':1,'muhasabah':1,'doa':1,'lihat-juga':1,'tingkat-dasar':1,'janji-nyata':1,
             'aksi-7-hari':1,'ringkasan':1,'pertanyaan-utama':1,'kepala-bab':1,'pembuka-masalah':1,'coba-sekarang':2,'salah-paham':4,'kisah':2,
             'istilah-akad':3,'struktur-akad':1,'pendapat-ulama':2,'fatwa-regulasi':1,'contoh-transaksi':1,
             'titik-risiko':4,'produk-contoh':1,'penerapan-keluarga':1,'penerapan-kerja':1,'simulasi':1,
             'checklist':2,'batas-kewenangan':1,'jangkar-abadi':1}
    import re as _re
    for _n,_b in BATAS.items():
        _c=len(_re.findall(rf'(?m)^::: {_n}\b', t))
        if _c > _b:
            find.append(f'ELEMEN BERLEBIH: ::: {_n} x{_c} (maks {_b})')
    if re.search(r'\S:::', t) or re.search(r':::\S', t):
        find.append('TANDA ::: MENEMPEL pada teks lain (harus baris sendiri)')

    # paragraf identik muncul >1 (pola boilerplate)
    import collections as _c
    _par = [x.strip() for x in re.split(r'\n\s*\n', t) if len(x.split()) > 12 and not x.strip().startswith(':::') and 'ARAB:' not in x[:40]]
    _dup = [k[:70] for k, v in _c.Counter(_par).items() if v > 1]
    if _dup:
        find.append(f'PARAGRAF GANDA: {len(_dup)} paragraf berulang, contoh: {_dup[:3]}')

    # 13 kecocokan teks Arab ke BANK_DALIL (teks API yang sudah diverifikasi) — audit tanpa jaringan
    try:
        _bank = open(D + 'BANK_DALIL_DRAF_v1.md', encoding='utf-8').read()
        _bmap = {}
        for _l in _bank.splitlines():
            if _l.startswith('| QS. ') or _l.startswith('| HR. '):
                _c = [x.strip() for x in _l.strip().strip('|').split('|')]
                if len(_c) >= 2:
                    _bmap[re.sub(r'[^0-9a-z]', '', _c[0].replace('’', "'").lower().split('(')[0])] = _c[1]
    except Exception:
        _bmap = {}
    if _bmap:
        _lines = t.splitlines()
        for _i, _l in enumerate(_lines):
            if _l.startswith('ARAB: '):
                _arab = _l[6:].strip()
                if _arab.startswith('n.a') or '{{' in _arab:
                    continue
                _ref = None
                for _j in range(_i + 1, min(_i + 8, len(_lines))):
                    if _lines[_j].startswith('RUJUKAN: '):
                        _ref = _lines[_j][9:].strip()
                        break
                if not _ref or not (_ref.startswith('QS.') or _ref.startswith('HR.')):
                    find.append(f'ARAB TIDAK PUNYA RUJUKAN QS/HR JELAS (baris {_i + 1})')
                    continue
                _key = _ref.split(';')[0].split('(')[0].strip().replace('’', "'")
                _nkey = re.sub(r'[^0-9a-z]', '', _key.lower())
                _canon = _bmap.get(_nkey)
                # NOMOR_AYAT: penomoran ayat diabaikan saat membandingkan isi.
                # Boss (2026-10-10): kurung wajib bentuk (..); bentuk ﴿..﴾ DILARANG.
                def NOMOR_AYAT(x):
                    # nomor diganti spasi lalu spasi dirapikan, supaya "... (٢٨٦)" == "...ilah"
                    return ' '.join(re.sub(r'[()\uFD3E\uFD3F\u06DD\u0660-\u06690-9]+', ' ', x).split())
                if _canon is None:
                    find.append(f'TEKS ARAB TIDAK ADA DI BANK_DALIL: {_key}')
                elif '(' in _ref:
                    if NOMOR_AYAT(_arab) not in NOMOR_AYAT(_canon):
                        find.append(f'POTONGAN AYAT BUKAN SUBSTRING BANK: {_key}')
                elif NOMOR_AYAT(_arab) != NOMOR_AYAT(_canon):
                    find.append(f'ARAB TIDAK COCOK DENGAN BANK/API: {_key}')

    print(json.dumps({'bab': bab, 'tipe': tipe, 'kata': total, 'anggaran': ang,
                      'dev_pct': round(dev, 1), 'sub_bab_toc': len(subs),
                      'sub_bab_draft': len(heads), 'temuan': find,
                      'lolus': len(find) == 0}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
