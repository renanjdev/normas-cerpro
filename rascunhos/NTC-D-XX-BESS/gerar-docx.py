#!/usr/bin/env python3
"""Gera o .docx formatado da NTC-D-XX a partir dos Markdown consolidados."""
import re
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY   = RGBColor(0x14, 0x3A, 0x5A)   # institucional
BLUE   = RGBColor(0x1F, 0x6F, 0xB2)
GREY   = RGBColor(0x60, 0x60, 0x60)
CODE   = RGBColor(0x8A, 0x2A, 0x00)
PARAM_HL = 'yellow'      # «»
DEC_HL   = 'cyan'        # [DECISÃO]
VER_HL   = 'magenta'     # [VERIFICAR]

FILES = ['NTC-D-XX-corpo-consolidado.md', 'NTC-D-XX-anexos.md']
OUT   = 'NTC-D-XX_BESS_CERPRO_consolidada_R1.docx'

doc = Document()

# ---- base styles ----
normal = doc.styles['Normal']
normal.font.name = 'Calibri'; normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(6); normal.paragraph_format.line_spacing = 1.12

for i,(sz,col) in enumerate([(18,NAVY),(14,NAVY),(12,BLUE),(11,BLUE)], start=1):
    h = doc.styles[f'Heading {i}']
    h.font.name='Calibri'; h.font.size=Pt(sz); h.font.bold=True; h.font.color.rgb=col
    h.paragraph_format.space_before=Pt(12 if i<3 else 8); h.paragraph_format.space_after=Pt(4)
    h.paragraph_format.keep_with_next=True

# ---- page margins ----
for s in doc.sections:
    s.top_margin=Cm(2.2); s.bottom_margin=Cm(2.0); s.left_margin=Cm(2.4); s.right_margin=Cm(2.0)

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),hexcolor)
    tcPr.append(sh)

def add_inline(p, text, base_bold=False):
    # split keeping markers: **bold** `code` ~~strike~~ «param» [DECISÃO...] [VERIFICAR...]
    pat = r'(\*\*.+?\*\*|`[^`]+`|~~.+?~~|«[^»]*»|\[DECISÃO[^\]]*\]|\[VERIFICAR[^\]]*\])'
    for part in re.split(pat, text):
        if not part: continue
        r = p.add_run()
        if part.startswith('**') and part.endswith('**'):
            r.text=part[2:-2]; r.bold=True
        elif part.startswith('`') and part.endswith('`'):
            r.text=part[1:-1]; r.font.name='Consolas'; r.font.size=Pt(9.5); r.font.color.rgb=CODE
        elif part.startswith('~~') and part.endswith('~~'):
            r.text=part[2:-2]; r.font.strike=True
        elif part.startswith('«') and part.endswith('»'):
            r.text=part; r.font.highlight_color.__class__  # noop
            r.font.color.rgb=RGBColor(0x70,0x50,0x00)
            r.font.highlight_color = _hl(PARAM_HL)
        elif part.startswith('[DECISÃO'):
            r.text=part; r.bold=True; r.font.highlight_color=_hl(DEC_HL)
        elif part.startswith('[VERIFICAR'):
            r.text=part; r.bold=True; r.font.highlight_color=_hl(VER_HL)
        else:
            r.text=part
        if base_bold: r.bold=True

from docx.enum.text import WD_COLOR_INDEX
def _hl(name):
    return {'yellow':WD_COLOR_INDEX.YELLOW,'cyan':WD_COLOR_INDEX.TURQUOISE,
            'magenta':WD_COLOR_INDEX.PINK}[name]

def flush_table(rows):
    rows=[r for r in rows if not re.match(r'^[\s:\-|]+$','|'.join(r))]
    if not rows: return
    ncol=max(len(r) for r in rows)
    t=doc.add_table(rows=0, cols=ncol); t.style='Light Grid Accent 1'
    t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=True
    for ri,r in enumerate(rows):
        cells=t.add_row().cells
        for ci in range(ncol):
            txt=r[ci] if ci<len(r) else ''
            cells[ci].text=''
            p=cells[ci].paragraphs[0]; p.paragraph_format.space_after=Pt(2)
            add_inline(p, txt, base_bold=(ri==0))
            if ri==0:
                shade(cells[ci],'143A5A')
                for run in p.runs: run.font.color.rgb=RGBColor(0xFF,0xFF,0xFF); run.bold=True
    doc.add_paragraph().paragraph_format.space_after=Pt(2)

# ---------- COVER ----------
def cover():
    for _ in range(3): doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('CERPRO'); r.bold=True; r.font.size=Pt(26); r.font.color.rgb=NAVY
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('Cooperativa de Eletrificação Rural da Região de Promissão'); r.font.size=Pt(12); r.font.color.rgb=GREY
    for _ in range(2): doc.add_paragraph()
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('NTC-D-XX'); r.bold=True; r.font.size=Pt(20); r.font.color.rgb=BLUE
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('Requisitos e Procedimentos para Conexão de Sistemas BESS\nao Sistema de Distribuição da CERPRO')
    r.bold=True; r.font.size=Pt(15); r.font.color.rgb=NAVY
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('(Battery Energy Storage Systems)'); r.italic=True; r.font.size=Pt(12); r.font.color.rgb=GREY
    for _ in range(6): doc.add_paragraph()
    # info box
    t=doc.add_table(rows=0, cols=2); t.style='Light List Accent 1'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for k,v in [('Versão de trabalho','R1 consolidada (corpo + anexos)'),
                ('Base','R0 da Engenharia CERPRO + NT-BESS-001/2026'),
                ('Estado','Rascunho em consolidação — para revisão'),
                ('Data de geração','19/06/2026')]:
        c=t.add_row().cells; c[0].text=''; c[1].text=''
        rp=c[0].paragraphs[0]; rr=rp.add_run(k); rr.bold=True; rr.font.color.rgb=NAVY
        add_inline(c[1].paragraphs[0], v)
    # legenda dos marcadores
    doc.add_paragraph()
    p=doc.add_paragraph(); r=p.add_run('Legenda dos marcadores editoriais'); r.bold=True; r.font.color.rgb=NAVY
    for txt in ['«parâmetro» — valor a ser cravado pela Engenharia da CERPRO',
                '[DECISÃO CERPRO] — ponto que requer deliberação',
                '[VERIFICAR] — citação regulatória a confirmar antes da publicação']:
        pp=doc.add_paragraph(style='List Bullet'); add_inline(pp, txt)
    doc.add_page_break()

# ---------- footer w/ page numbers ----------
def add_footer():
    sec=doc.sections[0]
    f=sec.footer; f.is_linked_to_previous=False
    p=f.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run('NTC-D-XX — BESS — CERPRO  |  Página ')
    r.font.size=Pt(8); r.font.color.rgb=GREY
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); p._p.append(fld)
    r2=p.add_run(' de '); r2.font.size=Pt(8); r2.font.color.rgb=GREY
    fld2=OxmlElement('w:fldSimple'); fld2.set(qn('w:instr'),'NUMPAGES'); p._p.append(fld2)

cover()
add_footer()

# ---------- body ----------
for fi,fn in enumerate(FILES):
    if fi>0: doc.add_page_break()
    tbl=[]
    for line in open(fn).read().split('\n'):
        s=line.rstrip()
        if s.strip().startswith('|') and s.strip().endswith('|'):
            tbl.append([c.strip() for c in s.strip().strip('|').split('|')]); continue
        elif tbl: flush_table(tbl); tbl=[]
        if not s.strip(): continue
        m=re.match(r'^(#{1,6})\s+(.*)', s)
        if m: doc.add_heading(m.group(2), level=min(len(m.group(1)),4)); continue
        if s.strip()=='---': continue
        if s.lstrip().startswith('> '):
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Cm(0.6)
            p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(3)
            pPr=p._p.get_or_add_pPr(); pbdr=OxmlElement('w:pBdr'); left=OxmlElement('w:left')
            left.set(qn('w:val'),'single'); left.set(qn('w:sz'),'18'); left.set(qn('w:space'),'8'); left.set(qn('w:color'),'1F6FB2')
            pbdr.append(left); pPr.append(pbdr)
            add_inline(p, s.lstrip()[2:]); 
            for run in p.runs:
                if run.font.color.rgb is None: run.font.color.rgb=GREY
            continue
        mb=re.match(r'^(\s*)[-*]\s+(.*)', s)
        if mb:
            ind=len(mb.group(1)); style='List Bullet' if ind<2 else 'List Bullet 2'
            try: p=doc.add_paragraph(style=style)
            except KeyError: p=doc.add_paragraph(style='List Bullet')
            add_inline(p, mb.group(2)); continue
        mn=re.match(r'^(\s*)\d+\.\s+(.*)', s)
        if mn: p=doc.add_paragraph(style='List Number'); add_inline(p, mn.group(2)); continue
        p=doc.add_paragraph(); add_inline(p, s)
    if tbl: flush_table(tbl)

doc.save(OUT)
print('saved', OUT)
