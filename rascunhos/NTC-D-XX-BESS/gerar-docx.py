#!/usr/bin/env python3
"""Gera o .docx da NTC-D-XX no layout da norma original da CERPRO."""
import re
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# --- paleta da norma CERPRO ---
DBLUE = RGBColor(0x1F, 0x38, 0x64)   # H1/H2, capa
MBLUE = RGBColor(0x2E, 0x75, 0xB6)   # H3
RED   = RGBColor(0xEE, 0x00, 0x00)   # acento "SISTEMAS BESS"
GREY  = RGBColor(0x60, 0x60, 0x60)
CODE  = RGBColor(0x8A, 0x2A, 0x00)

FILES = ['NTC-D-XX-corpo-consolidado.md', 'NTC-D-XX-anexos.md']
OUT   = 'NTC-D-XX_BESS_CERPRO_consolidada_R1.docx'

doc = Document()

# Normal: Calibri (tema), 11pt
normal = doc.styles['Normal']
normal.font.name='Calibri'; normal.font.size=Pt(11)
normal.paragraph_format.space_after=Pt(6); normal.paragraph_format.line_spacing=1.15

# Headings iguais à norma: H1 16 / H2 13 (1F3864) ; H3 12 / H4 11 (2E75B6)
for i,(sz,col) in enumerate([(16,DBLUE),(13,DBLUE),(12,MBLUE),(11,MBLUE)], start=1):
    h=doc.styles[f'Heading {i}']
    h.font.name='Calibri'; h.font.size=Pt(sz); h.font.bold=True; h.font.color.rgb=col
    h.paragraph_format.space_before=Pt(12 if i<3 else 8); h.paragraph_format.space_after=Pt(4)
    h.paragraph_format.keep_with_next=True

# Página A4, margens da norma
for s in doc.sections:
    s.page_width=Cm(21.0); s.page_height=Cm(29.7)
    s.top_margin=Cm(3.17); s.bottom_margin=Cm(3.0); s.left_margin=Cm(2.54); s.right_margin=Cm(2.54)

def _hl(name):
    return {'yellow':WD_COLOR_INDEX.YELLOW,'cyan':WD_COLOR_INDEX.TURQUOISE,
            'magenta':WD_COLOR_INDEX.PINK}[name]

def shade(cell,hexc):
    tcPr=cell._tc.get_or_add_tcPr(); sh=OxmlElement('w:shd')
    sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),hexc); tcPr.append(sh)

def add_inline(p, text, base_bold=False):
    pat=r'(\*\*.+?\*\*|`[^`]+`|~~.+?~~|«[^»]*»|\[DECISÃO[^\]]*\]|\[VERIFICAR[^\]]*\])'
    for part in re.split(pat, text):
        if not part: continue
        r=p.add_run()
        if part.startswith('**') and part.endswith('**'): r.text=part[2:-2]; r.bold=True
        elif part.startswith('`') and part.endswith('`'):
            r.text=part[1:-1]; r.font.name='Consolas'; r.font.size=Pt(9.5); r.font.color.rgb=CODE
        elif part.startswith('~~') and part.endswith('~~'): r.text=part[2:-2]; r.font.strike=True
        elif part.startswith('«') and part.endswith('»'):
            r.text=part; r.font.color.rgb=RGBColor(0x70,0x50,0x00); r.font.highlight_color=_hl('yellow')
        elif part.startswith('[DECISÃO'): r.text=part; r.bold=True; r.font.highlight_color=_hl('cyan')
        elif part.startswith('[VERIFICAR'): r.text=part; r.bold=True; r.font.highlight_color=_hl('magenta')
        else: r.text=part
        if base_bold: r.bold=True

def flush_table(rows):
    rows=[r for r in rows if not re.match(r'^[\s:\-|]+$','|'.join(r))]
    if not rows: return
    ncol=max(len(r) for r in rows)
    t=doc.add_table(rows=0, cols=ncol); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for ri,r in enumerate(rows):
        cells=t.add_row().cells
        for ci in range(ncol):
            txt=r[ci] if ci<len(r) else ''
            cells[ci].text=''; p=cells[ci].paragraphs[0]; p.paragraph_format.space_after=Pt(2)
            add_inline(p, txt, base_bold=(ri==0))
            if ri==0:
                shade(cells[ci],'1F3864')
                for run in p.runs: run.font.color.rgb=RGBColor(0xFF,0xFF,0xFF); run.bold=True
    doc.add_paragraph().paragraph_format.space_after=Pt(2)

def ctr(size, text, color=None, bold=False, italic=False):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run(text); r.font.size=Pt(size); r.bold=bold; r.italic=italic
    if color is not None: r.font.color.rgb=color
    return p

# ---------- CAPA (réplica da norma) ----------
for _ in range(2): doc.add_paragraph()
ctr(32,'CERPRO',DBLUE,bold=True)
ctr(14,'Cooperativa de Eletrificação Rural da Região de Promissão',DBLUE)
doc.add_paragraph()
ctr(14,'NTC-D-XX',DBLUE,bold=True)
ctr(14,'NORMA TÉCNICA E PADRONIZAÇÃO',bold=True)
doc.add_paragraph()
ctr(15,'REQUISITOS E PROCEDIMENTOS PARA CONEXÃO DE',bold=True)
ctr(17,'SISTEMAS BESS',RED,bold=True)
ctr(12,'(Battery Energy Storage Systems)',RED)
ctr(15,'AO SISTEMA DE DISTRIBUIÇÃO DA CERPRO',bold=True)
doc.add_paragraph()
ctr(13,'Versão de trabalho R1 — Consolidada (corpo + anexos)',bold=True)
ctr(11,'Base: R0 da Engenharia CERPRO + NT-BESS-001/2026',GREY)
ctr(11,'Elaborado por Engenharia CERPRO',GREY)
ctr(11,'Aprovado pelo Grupo Técnico de Padronização',GREY)
for _ in range(2): doc.add_paragraph()
p=doc.add_paragraph(); r=p.add_run('Legenda dos marcadores editoriais:'); r.bold=True; r.font.color.rgb=DBLUE
for txt in ['«parâmetro» — valor a ser cravado pela Engenharia da CERPRO',
            '[DECISÃO CERPRO] — ponto que requer deliberação',
            '[VERIFICAR] — citação regulatória a confirmar antes da publicação']:
    pp=doc.add_paragraph(style='List Bullet'); add_inline(pp, txt)
doc.add_page_break()

# ---------- SUMÁRIO automático ----------
doc.add_heading('SUMÁRIO', level=1)
pটoc=doc.add_paragraph()
fld=OxmlElement('w:fldSimple')
fld.set(qn('w:instr'), r'TOC \o "1-3" \h \z \u')
run=OxmlElement('w:r'); t=OxmlElement('w:t'); t.set(qn('xml:space'),'preserve')
t.text='Atualize este campo no Word (clique direito ▸ Atualizar Campo) para gerar o sumário.'
run.append(t); fld.append(run); pটoc._p.append(fld)
doc.add_page_break()

# ---------- CABEÇALHO (réplica da norma: tabela 3x2) ----------
TITULO='Requisitos e Procedimentos para Conexão de Sistemas BESS (Battery Energy Storage Systems) ao Sistema de Distribuição da CERPRO'
def kv(cell, label, value, vbold=False):
    cell.text=''; p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0)
    if label:
        rl=p.add_run(label); rl.bold=True; rl.font.size=Pt(8.5); rl.font.color.rgb=DBLUE
    rv=p.add_run(value); rv.font.size=Pt(8.5); rv.bold=vbold

sec=doc.sections[0]
hdr=sec.header; hdr.is_linked_to_previous=False
ht=hdr.add_table(rows=3, cols=2, width=Cm(16.0)); ht.style='Table Grid'; ht.alignment=WD_TABLE_ALIGNMENT.CENTER
kv(ht.cell(0,0),'Tipo: ','Norma Técnica e Padronização')
kv(ht.cell(0,1),'', 'NTC-D-XX', vbold=True)
kv(ht.cell(1,0),'Área de Aplicação: ','Distribuição de Energia Elétrica')
kv(ht.cell(1,1),'Versão: ','R1/2026 (consolidada)')
c=ht.cell(2,0).merge(ht.cell(2,1)); kv(c,'Título: ',TITULO)

# ---------- RODAPÉ (réplica da norma: tabela 1x4) ----------
f=sec.footer; f.is_linked_to_previous=False
ft=f.add_table(rows=1, cols=4, width=Cm(16.0)); ft.style='Table Grid'; ft.alignment=WD_TABLE_ALIGNMENT.CENTER
kv(ft.cell(0,0),'Elaborado por: ','CERPRO')
kv(ft.cell(0,1),'Aprovado por: ','Grupo Técnico de Padronização')
kv(ft.cell(0,2),'Data de vigência: ','__/__/2026')
pc=ft.cell(0,3).paragraphs[0]; pc.paragraph_format.space_after=Pt(0)
rr=pc.add_run('Página '); rr.bold=True; rr.font.size=Pt(8.5); rr.font.color.rgb=DBLUE
fp=OxmlElement('w:fldSimple'); fp.set(qn('w:instr'),'PAGE'); pc._p.append(fp)
r2=pc.add_run(' de '); r2.font.size=Pt(8.5)
fn2=OxmlElement('w:fldSimple'); fn2.set(qn('w:instr'),'NUMPAGES'); pc._p.append(fn2)

# ---------- corpo ----------
def add_code_block(buf):
    p=doc.add_paragraph(); p.paragraph_format.left_indent=Cm(0.3)
    p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(6)
    pPr=p._p.get_or_add_pPr(); sh=OxmlElement('w:shd')
    sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),'F2F4F7'); pPr.append(sh)
    r=p.add_run('\n'.join(buf)); r.font.name='Consolas'; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor(0x22,0x33,0x44)

for fi,fn in enumerate(FILES):
    if fi>0: doc.add_page_break()
    tbl=[]; code=None
    for line in open(fn).read().split('\n'):
        s=line.rstrip()
        if s.strip().startswith('```'):
            if code is None: code=[]
            else: add_code_block(code); code=None
            continue
        if code is not None:
            code.append(line); continue
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
            left.set(qn('w:val'),'single'); left.set(qn('w:sz'),'18'); left.set(qn('w:space'),'8'); left.set(qn('w:color'),'2E75B6')
            pbdr.append(left); pPr.append(pbdr)
            add_inline(p, s.lstrip()[2:])
            for run in p.runs:
                if run.font.color.rgb is None: run.font.color.rgb=GREY
            continue
        mb=re.match(r'^(\s*)[-*]\s+(.*)', s)
        if mb:
            style='List Bullet' if len(mb.group(1))<2 else 'List Bullet 2'
            try: p=doc.add_paragraph(style=style)
            except KeyError: p=doc.add_paragraph(style='List Bullet')
            add_inline(p, mb.group(2)); continue
        mn=re.match(r'^(\s*)\d+\.\s+(.*)', s)
        if mn: p=doc.add_paragraph(style='List Number'); add_inline(p, mn.group(2)); continue
        p=doc.add_paragraph(); add_inline(p, s)
    if tbl: flush_table(tbl)

doc.save(OUT)
print('saved', OUT)
