#!/usr/bin/env python3
"""Render lampiran (markdown tabel-heavy) ke DOCX.
Standar sama dengan render_bab_docx.py: Calibri 11 justify; heading bold;
tabel markdown dengan header bold; teks Arab di sel tabel = Scheherazade New + rtl.
Pemakaian: python3 render_lampiran_docx.py LAMPIRAN_X_....md"""
import re, sys
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

AR = re.compile(r'[\u0600-\u06FF]')

def ar_run(p, text, size=13):
    r = p.add_run(text); r.font.name = 'Scheherazade New'; r.font.size = Pt(size)
    rPr = r._r.get_or_add_rPr()
    rPr.append(rPr.makeelement(qn('w:rtl'), {})); rPr.append(rPr.makeelement(qn('w:cs'), {qn('w:val'): '1'}))
    return r

def add_text(p, text, bold=False, size=9):
    if AR.search(text):
        ar_run(p, text, size=13)
    else:
        r = p.add_run(text); r.bold = bold; r.font.size = Pt(size)

def render(md_path, out_path):
    t = open(md_path, encoding='utf-8').read()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.27); sec.page_height = Inches(11.69)  # A4
    st = doc.styles['Normal']
    st.font.name = 'Calibri'; st.font.size = Pt(10.5)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    lines = t.split('\n')
    i = 0
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith('# '):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(l[2:].strip()); r.bold = True; r.font.size = Pt(18)
        elif l.startswith('## '):
            p = doc.add_paragraph(); r = p.add_run(l[3:].strip()); r.bold = True; r.font.size = Pt(13)
        elif l.startswith('### '):
            p = doc.add_paragraph(); r = p.add_run(l[4:].strip()); r.bold = True; r.font.size = Pt(11.5)
        elif l.startswith('```'):
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                p = doc.add_paragraph(); add_text(p, lines[i], size=10); i += 1
        elif l.startswith('|'):
            tbl_lines = []
            while i < len(lines) and lines[i].startswith('|'):
                tbl_lines.append(lines[i]); i += 1
            rows_raw = [x for x in tbl_lines if not re.match(r'^\|[\s\-:|]+\|$', x)]
            if not rows_raw: continue
            ncols = max(len(x.split('|')) - 2 for x in rows_raw)
            table = doc.add_table(rows=0, cols=ncols)
            table.style = 'Table Grid'; table.alignment = WD_TABLE_ALIGNMENT.CENTER
            for k, rl in enumerate(rows_raw):
                cells = [c.strip() for c in rl.strip().strip('|').split('|')]
                tr = table.add_row()
                for j in range(ncols):
                    txt = cells[j] if j < len(cells) else ''
                    tp = tr.cells[j].paragraphs[0]
                    add_text(tp, txt, bold=(k == 0), size=9)
            doc.add_paragraph()
        else:
            p = doc.add_paragraph()
            txt = l.strip()
            bold = False
            m = re.match(r'^\*\*(.+?)\*\*:?\s*(.*)$', txt)
            if m:
                r0 = p.add_run(m.group(1) + (':' if ':' in txt[:len(m.group(1))+2] else '')); r0.bold = True; r0.font.size = Pt(10.5)
                txt = m.group(2)
            for seg in re.split(r'(\*\*.+?\*\*)', txt):
                if not seg: continue
                if seg.startswith('**'):
                    add_text(p, seg[2:-2], bold=True, size=10.5)
                else:
                    add_text(p, seg, size=10.5)
        i += 1
    doc.save(out_path)
    print('OK', out_path)

if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else sys.argv[1][:-3] + '.docx')
