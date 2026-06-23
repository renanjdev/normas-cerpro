#!/usr/bin/env python3
"""3 modelos de fluxograma do processo de análise/conexão BESS (Anexo I)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Ellipse, Rectangle
BLUE='#1F3864'; LBLUE='#EAF1FB'; RED='#C00000'; LRED='#FDE9E9'; YEL='#FFF3CC'; K='#1a1a1a'; GREY='#5b6677'
steps=[
 '1. Protocolo\n(≤ 5 dias úteis p/ conferência)','2. Análise preliminar\n(classificação A–D)','3. Parecer regulatório',
 '4. Parecer técnico\n(curto-circuito, fluxo,\ncoordenação, QEE, estabilidade)','5. Parecer operacional\n(telecomando, supervisão,\ncontingências)','6. Parecer jurídico\n(contratos, garantias, seguros)',
 '7. Comitê Interno BESS\n(aprova / condiciona /\ncomplementa / indefere)','8. Orçamento de Conexão (OC)','9. Formalização contratual\n(Acordo Operativo + aditivo CUSD\n+ Declaração de Não Exportação)',
 '10. Execução das adequações\n(acompanhada pela CERPRO)','11. Comissionamento\n(Anexo J)','12. Autorização para operação',
 '13. Monitoramento contínuo\n(eventos, alarmes, QEE)','14. Fiscalização\n(inspeções, auditorias)','15. Suspensão da operação\n(se risco/descumprimento)']
def arrow(ax,p,q,c='#444',lw=1.5):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=c,lw=lw,shrinkA=2,shrinkB=2))
def box(ax,x,y,w,h,txt,fc=LBLUE,ec=BLUE,fs=8,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.10',facecolor=fc,edgecolor=ec,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,color=K,fontweight='bold' if bold else 'normal')

# ===================== MODELO A — Vertical com faixas de fase =====================
fig,ax=plt.subplots(figsize=(7.8,13.8)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,19.8)
ax.text(5,19.4,'Modelo A — Fluxo vertical por fases',ha='center',fontsize=12.5,fontweight='bold',color=BLUE)
phases=[('SOLICITAÇÃO',[0],BLUE),('ANÁLISE',[1,2,3,4,5],BLUE),('DECISÃO',[6],RED),
        ('CONTRATAÇÃO',[7,8],BLUE),('IMPLANTAÇÃO',[9,10,11],BLUE),('OPERAÇÃO E FISCALIZAÇÃO',[12,13,14],BLUE)]
bx=1.5; bw=7.0; bh=0.74; gap=0.12; y=18.5; cen={}
for name,idxs,col in phases:
    ax.add_patch(Rectangle((bx,y-0.44),bw,0.44,facecolor=col,edgecolor='none'))
    ax.text(bx+bw/2,y-0.22,name,ha='center',va='center',fontsize=8.2,color='white',fontweight='bold')
    y-=0.52
    for j in idxs:
        fc=LRED if j==6 else (YEL if j==14 else LBLUE); ec=RED if j in(6,14) else BLUE
        box(ax,bx,y-bh,bw,bh,steps[j],fc=fc,ec=ec,fs=7.3); cen[j]=(bx+bw/2,y,y-bh)
        y-=bh+gap
    y-=0.16
for a,b in zip(range(15),range(1,15)):
    if (cen[a][2]-cen[b][0])<0.9:  # mesma fase (sem faixa entre eles)
        arrow(ax,(cen[a][0],cen[a][2]),(cen[b][0],cen[b][1]))
ax.text(5,0.25,'Fluxo de análise e conexão de sistemas BESS — Anexo I (Classes A–D, §13).',ha='center',fontsize=7.6,style='italic',color=GREY)
fig.savefig('img/anexoI-fluxo-A.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('A ok')

# ===================== MODELO B — Serpente horizontal por fases (cor) =====================
fig,ax=plt.subplots(figsize=(11,7.8)); ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(-0.9,12.4)
ax.text(6,12.0,'Modelo B — Fluxo horizontal (serpente) com fases por cor',ha='center',fontsize=12.5,fontweight='bold',color=BLUE)
phase_of={0:0,1:1,2:1,3:1,4:1,5:1,6:2,7:3,8:3,9:4,10:4,11:4,12:5,13:5,14:5}
pcol=['#DCE6F5','#EAF1FB','#FDE9E9','#E7F0E7','#EAF1FB','#FFF6DD']; pec=['#2E5596','#2E5596','#C00000','#3a7d44','#2E5596','#caa000']
cols=3; dx=4.0; dy=2.2; x0=0.5; y0=10.4; bw=3.5; bh=1.55; pos=[]
for i in range(15):
    r=i//cols; c=i%cols; cc=c if r%2==0 else (cols-1-c)
    x=x0+cc*dx; y=y0-r*dy; pos.append((x+bw/2,y-bh/2,x,y)); ph=phase_of[i]
    box(ax,x,y-bh,bw,bh,steps[i],fc=pcol[ph],ec=pec[ph],fs=7.3,bold=(i in(6,14)))
for i in range(14):
    (x1,y1,_,_),(x2,y2,_,_)=pos[i],pos[i+1]; same=(i//cols)==((i+1)//cols)
    if same: arrow(ax,(x1+(bw/2 if x2>x1 else -bw/2),y1),(x2+(-bw/2 if x2>x1 else bw/2),y2))
    else: arrow(ax,(x1,y1-bh/2),(x2,y2+bh/2))
names=['Solicitação','Análise','Decisão','Contratação','Implantação','Operação']
for k,(nm,cf,ce) in enumerate(zip(names,pcol,pec)):
    xx=0.6+k*1.95; ax.add_patch(Rectangle((xx,-0.7),0.3,0.3,facecolor=cf,edgecolor=ce)); ax.text(xx+0.4,-0.55,nm,fontsize=7.4,va='center',color=K)
fig.savefig('img/anexoI-fluxo-B.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('B ok')

# ===================== MODELO C — Fluxograma clássico com decisão =====================
fig,ax=plt.subplots(figsize=(8.0,15.2)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,21.6)
ax.text(5,21.2,'Modelo C — Fluxograma com ponto de decisão (Comitê)',ha='center',fontsize=12.5,fontweight='bold',color=BLUE)
cx=3.7; w=4.6; h=0.80; gap=0.36
def varrow(yb,yt): arrow(ax,(cx,yb),(cx,yt))
y=20.3
ax.add_patch(Ellipse((cx,y),2.4,0.7,facecolor='#E7F0E7',edgecolor='#3a7d44',lw=1.6)); ax.text(cx,y,'INÍCIO',ha='center',va='center',fontsize=9,fontweight='bold',color='#2c5e34')
prev_bottom=y-0.35; y-=0.35+gap
for j in [0,1,2,3,4,5]:
    box(ax,cx-w/2,y-h,w,h,steps[j],fc=LBLUE,ec=BLUE,fs=7.1); varrow(prev_bottom,y); prev_bottom=y-h; y-=h+gap
# diamante (Comitê)
dh=1.8; dw=4.4; dtop=prev_bottom-gap; dcy=dtop-dh/2
dia=Polygon([[cx,dtop],[cx-dw/2,dcy],[cx,dtop-dh],[cx+dw/2,dcy]],closed=True,facecolor=LRED,edgecolor=RED,lw=1.8); ax.add_patch(dia)
ax.text(cx,dcy,'7. Comitê Interno BESS\nAprovado?',ha='center',va='center',fontsize=7.4,fontweight='bold',color=K)
varrow(prev_bottom,dtop)
# ramo Não
ax.text(cx+dw/2+0.1,dcy+0.2,'Não',fontsize=7.5,color=RED,fontweight='bold')
box(ax,cx+1.55,dcy-0.45,2.9,0.9,'Indeferimento /\ncomplementação',fc='#f4f4f4',ec=RED,fs=7.1)
arrow(ax,(cx+dw/2,dcy),(cx+1.55,dcy),c=RED)
ax.text(cx+0.12,dtop-dh-0.02,'Sim',fontsize=7.5,color='#2c5e34',fontweight='bold',ha='left')
prev_bottom=dtop-dh; y=prev_bottom-gap
for j in [7,8,9,10,11,12,13]:
    box(ax,cx-w/2,y-h,w,h,steps[j],fc=LBLUE,ec=BLUE,fs=7.1); varrow(prev_bottom,y); prev_bottom=y-h; y-=h+gap
# fim
ax.add_patch(Ellipse((cx,prev_bottom-0.45),2.6,0.7,facecolor='#E7F0E7',edgecolor='#3a7d44',lw=1.6)); ax.text(cx,prev_bottom-0.45,'OPERAÇÃO',ha='center',va='center',fontsize=9,fontweight='bold',color='#2c5e34'); varrow(prev_bottom,prev_bottom-0.10)
# ramo de exceção 15 (suspensão) saindo de Monitoramento/Fiscalização
box(ax,cx+1.7,prev_bottom+0.5,2.7,0.92,steps[14],fc=YEL,ec=RED,fs=6.9)
arrow(ax,(cx+w/2,prev_bottom+1.0),(cx+1.7,prev_bottom+1.0),c=RED)
ax.text(5,0.3,'Fluxo simplificado — Anexo I (Classes A–D, §13). Ramo de exceção: suspensão.',ha='center',fontsize=7.4,style='italic',color=GREY)
fig.savefig('img/anexoI-fluxo-C.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('C ok')
