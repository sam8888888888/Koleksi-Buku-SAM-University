#!/usr/bin/env python3
"""Gabung front matter + 105 bab + 34 lampiran jadi satu master DOCX."""
import json, os
from docx import Document
from docxcompose.composer import Composer

P = '/home/diya/books/30-kunci-pembuka-pintu-rezeki/'
lst = json.load(open('/home/diya/.hermes/cache/scratch/merge_list.json'))
composer = Composer(Document(lst[0]))
for p in lst[1:]:
    composer.append(Document(p), add_page_break=True)
out = P + 'MASTER_30_KUNCI_PEMBUKA_PINTU_REZEKI_v1.docx'
composer.save(out)
print('OK', out, os.path.getsize(out) // 1024, 'KB', 'file:', len(lst))
