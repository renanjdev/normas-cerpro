#!/usr/bin/env python3
"""Unifilares (single-line) com simbologia elétrica — Anexo A da NTC-D-XX."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc, FancyArrowPatch
import numpy as np

BLUE='#1F3864'; RED='#C00000'; K='#1a1a1a'
LW=1.7

def L(ax,x1,y1,x2,y2,c=K,lw=LW,ls='-'): ax.plot([x1,x2],[y1,y2],color=c,lw=lw,ls=ls,solid_capstyle='round',zorder=2)
def dot(ax,x,y,r=0.045): ax.add_patch(Circle((x,y),r,color=K,zorder=4))
def lbl(ax,x,y,t,ha='left',va='center',fs=9,c=K,b=False,it=False):
    ax.text(x,y,t,ha=ha,va=va,fontsize=fs,color=c,fontweight='bold' if b else 'normal',
            style='italic' if it else 'normal',zorder=5)

def busbar(ax,x,y,w,t,sub=None):
    L(ax,x-w/2,y,x+w/2,y,c=BLUE,lw=4)
    lbl(ax,x,y+0.22,t,ha='center',fs=10,c=BLUE,b=True)
    if sub: lbl(ax,x,y-0.24,sub,ha='center',fs=8,c=BLUE)

def meter(ax,x,y,t='Wh'):
    ax.add_patch(Circle((x,y),0.26,fill=True,facecolor='white',edgecolor=K,lw=LW,zorder=3))
    lbl(ax,x,y,t,ha='center',fs=8.5)
def ground(ax,x,y):
    L(ax,x,y,x,y-0.18); 
    for i,wd in enumerate([0.26,0.17,0.08]): L(ax,x-wd/2,y-0.18-0.07*i,x+wd/2,y-0.18-0.07*i)

def disconnect(ax,x,y,t='Seccionadora'):
    # bottom fixed contact, blade open to the right
    dot(ax,x,y-0.3); dot(ax,x,y+0.3)
    L(ax,x,y-0.3,x+0.28,y+0.22)        # blade angled
    lbl(ax,x+0.4,y,t,fs=8.5)
def breaker(ax,x,y,t='Disjuntor',num='52'):
    # disconnect-like with a filled square marker (utility CB)
    dot(ax,x,y-0.3); dot(ax,x,y+0.3)
    L(ax,x,y-0.3,x+0.28,y+0.22)
    ax.add_patch(Rectangle((x-0.085,y-0.085),0.17,0.17,facecolor=K,edgecolor=K,zorder=5))
    lbl(ax,x+0.4,y,f'{t} ({num})' if num else t,fs=8.5)
def recloser(ax,x,y,t='Religador'):
    dot(ax,x,y-0.3); dot(ax,x,y+0.3)
    L(ax,x,y-0.3,x+0.28,y+0.22)
    ax.add_patch(Circle((x,y),0.16,fill=True,facecolor=RED,edgecolor=RED,zorder=5))
    lbl(ax,x+0.4,y,t+' (R)',fs=8.5,c=RED)

def transformer(ax,x,y,prim='Δ',sec='Y',t='Trafo acoplamento'):
    r=0.26
    ax.add_patch(Circle((x,y+0.17),r,fill=False,edgecolor=K,lw=LW,zorder=3))
    ax.add_patch(Circle((x,y-0.17),r,fill=False,edgecolor=K,lw=LW,zorder=3))
    lbl(ax,x-0.42,y+0.17,prim,ha='center',fs=11,b=True)
    lbl(ax,x-0.42,y-0.17,sec,ha='center',fs=11,b=True)
    lbl(ax,x+0.5,y,t,fs=8.5)
    # neutral ground on secondary
    L(ax,x+0.18,y-0.30,x+0.45,y-0.30); ground(ax,x+0.45,y-0.30)

def inverter(ax,x,y,t='PCS (inversor)'):
    s=0.46
    ax.add_patch(Rectangle((x-s/2,y-s/2),s,s,fill=True,facecolor='white',edgecolor=K,lw=LW,zorder=3))
    L(ax,x-s/2,y+s/2,x+s/2,y-s/2)            # diagonal
    # DC side (upper-left): equal signs
    lbl(ax,x-0.13,y+0.12,'=',ha='center',fs=10)
    # AC side (lower-right): sine
    xx=np.linspace(x+0.03,x+0.18,20); yy=y-0.13+0.05*np.sin((xx-x-0.03)/0.15*2*np.pi)
    ax.plot(xx,yy,color=K,lw=1.2,zorder=4)
    lbl(ax,x+0.42,y,t,fs=8.5)
def battery(ax,x,y,t='Banco de baterias'):
    for i,(h,w) in enumerate([(0.16,0.34),(0.07,0.16),(0.16,0.34),(0.07,0.16)]):
        yy=y+0.18-i*0.12
        L(ax,x-w/2,yy,x+w/2,yy,lw=2.2)
    lbl(ax,x+0.4,y,t,fs=8.5)
def pv(ax,x,y,t='Gerador FV'):
    s=0.42
    ax.add_patch(Rectangle((x-s/2,y-s/2),s,s,fill=True,facecolor='white',edgecolor=K,lw=LW,zorder=3))
    L(ax,x-s/2,y-s/2,x+s/2,y+s/2); L(ax,x-s/2,y+s/2,x+s/2,y-s/2)
    lbl(ax,x+0.4,y,t,fs=8.5)
def relay(ax,x,y,side,text,c=BLUE):
    # CT/PT stub to a relay circle off the main line
    xr=x+side*0.9
    L(ax,x,y,xr-side*0.26,y,c=c,lw=1.3)
    ax.add_patch(Circle((xr,y),0.26,fill=False,edgecolor=c,lw=LW,zorder=3))
    lbl(ax,xr,y,'R',ha='center',fs=9,c=c,b=True)
    ha='left' if side>0 else 'right'
    lbl(ax,xr+side*0.34,y,text,ha=ha,fs=7.6,c=c)

def ansi(ax,x,y,code,c=BLUE,pending=False,r=0.17):
    # ANSI function circle (CERPRO Figura 2 style)
    ls='--' if pending else '-'
    ax.add_patch(Circle((x,y),r,fill=False,edgecolor=c,lw=1.4,ls=ls,zorder=4))
    fs=7.0 if len(code)<=4 else 6.0
    lbl(ax,x,y,code,ha='center',fs=fs,c=c,b=True)

def protbox(ax,x,y_top,codes,title='Relé de proteção\nmultifunção',side=-1):
    # CERPRO Figura 2: caixa de funções alimentada por TPs/TCs de proteção
    cols=4; cw=0.58; ch=0.58
    rows=(len(codes)+cols-1)//cols
    bw=cols*cw+0.2; bh=rows*ch+0.2
    bx=x+side*(1.15)            # right edge of box, com folga até a linha
    x0=bx-bw if side<0 else bx
    y0=y_top-bh
    ax.add_patch(Rectangle((x0,y0),bw,bh,fill=False,edgecolor=K,lw=1.4,ls=(0,(4,3)),zorder=2))
    lbl(ax,x0+bw/2,y_top+0.40,title,ha='center',fs=8,c=BLUE,b=True)
    for i,(code,pend) in enumerate(codes):
        r,cc=divmod(i,cols)
        cx=x0+0.1+cw/2+cc*cw; cy=y_top-0.1-ch/2-r*ch
        ansi(ax,cx,cy,code,pending=pend)
    # TP / TC proteção stubs from main line into box (rótulo no meio do trecho)
    ytp=y_top-0.1-ch/2; ytc=y_top-0.1-ch/2-ch; xmid=(x+(x0+bw))/2
    for yy,t in [(ytp,'TP proteção'),(ytc,'TC proteção')]:
        L(ax,x,yy,x0+bw,yy,c=BLUE,lw=1.0,ls='--')
        lbl(ax,xmid,yy+0.14,t,ha='center',fs=6.2,c=BLUE,it=True)
        ax.add_patch(Circle((x,yy),0.05,fill=True,color=BLUE,zorder=5))
    return y0

def invbox(ax,x,y_top,codes,title='Inversor / PCS —\nproteções internas'):
    ch=0.5; bh=len(codes)*ch+0.2; bw=0.8
    x0=x-bw-0.7; y0=y_top-bh
    ax.add_patch(Rectangle((x0,y0),bw,bh,fill=False,edgecolor=K,lw=1.3,ls=(0,(4,3)),zorder=2))
    lbl(ax,x0+bw/2,y_top+0.34,title,ha='center',fs=7.4,c=RED,b=True)
    for i,(code,pend) in enumerate(codes):
        cy=y_top-0.1-ch/2-i*ch
        ansi(ax,x0+bw/2,cy,code,c=RED,pending=pend,r=0.16)
        L(ax,x0+bw,cy,x,cy,c=RED,lw=1.0,ls='--')
    ax.add_patch(Circle((x,(y0+y_top)/2),0.05,fill=True,color=RED,zorder=5))
    return y0

def newfig(w,h,title):
    fig,ax=plt.subplots(figsize=(w,h)); ax.axis('off'); ax.set_aspect('equal')
    ax._title_txt=title
    return fig,ax
def put_title(ax,xc,y):
    ax.text(xc,y,ax._title_txt,ha='center',va='center',fontsize=11.5,fontweight='bold',color=BLUE)

# ===== A.1 — BT Zero-Grid =====
fig,ax=newfig(6.6,8.6,'A.1 — Unifilar: BESS sem GD em BT (P ≤ 75 kW) — Zero-Grid')
x=3.0; top=8.7
put_title(ax,x,top+0.7); busbar(ax,x,top,2.0,'Rede CERPRO — BT')
ys=[8.0,7.2,6.3,5.4,4.4,3.4,2.4]
L(ax,x,top,x,ys[-1]-0.4)
meter(ax,x,ys[0],'kWh')
lbl(ax,x+0.34,ys[0],'Medição SMF bidirecional',fs=8.5)
disconnect(ax,x,ys[1],'DSV travável (LOTO)')
breaker(ax,x,ys[2],'Elemento de interrupção  U≤0,7pu · ≤2,0s',num='')
relay(ax,x,ys[3],-1,'Anti-exportação\nANSI 32 + Hard Limit',c=RED)
dot(ax,x,ys[3])
inverter(ax,x,ys[4],'PCS bidirecional (INMETRO 515/2023)')
# branch to loads
L(ax,x,ys[4]+0.0,x,ys[4]); 
dot(ax,x,ys[4]+0.55)
L(ax,x,ys[4]+0.55,x+1.7,ys[4]+0.55); lbl(ax,x+1.8,ys[4]+0.55,'→ Cargas da UC',fs=8.5,it=True)
ax.add_patch(Rectangle((x-0.18,ys[5]-0.18),0.36,0.36,fill=False,edgecolor=K,lw=LW)); lbl(ax,x,ys[5],'BMS',ha='center',fs=6.5); lbl(ax,x+0.34,ys[5],'BMS',fs=8.5)
battery(ax,x,ys[6])
ax.set_xlim(0.2,6.4); ax.set_ylim(1.6,9.7)
fig.savefig('img/anexoA1.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('A1 ok')

# ===== A.2 — MT  (padronizado conforme NTC-D-09 Figura 2) =====
fig,ax=newfig(8.4,10.4,'A.2 — Unifilar: BESS sem GD em MT (P > 75 kW) — base NTC-D-09 Fig. 2')
x=4.6; top=10.4
put_title(ax,x,top+0.7); busbar(ax,x,top,2.2,'Rede elétrica MT da Distribuidora (CERPRO)')
# coluna principal: PR/FU -> medição -> proteção -> disjuntor tripolar -> TD -> trafo acopl.
y_pr=9.7; y_med=8.9; y_prot=7.9; y_cb=5.7; y_td=4.9; y_tr=3.9; y_pcs=2.7; y_bat=1.6
L(ax,x,top,x,y_pcs-0.2)
# para-raios + chave fusível
L(ax,x,y_pr,x+0.5,y_pr); ax.add_patch(Rectangle((x+0.5,y_pr-0.08),0.34,0.16,fill=False,edgecolor=K,lw=LW)); lbl(ax,x+0.95,y_pr,'PR (para-raios)',fs=8)
lbl(ax,x-0.12,y_pr,'FU',ha='right',fs=8)
# medição (M / TC / TP / CS)
meter(ax,x-0.95,y_med,'M'); L(ax,x-0.95,y_med,x,y_med); dot(ax,x,y_med)
lbl(ax,x-0.95,y_med+0.42,'Medição (M/TC/TP/CS)',ha='center',fs=7.6,c=BLUE)
# caixa de funções de proteção (estilo Figura 2)  — 78 marcada como PENDENTE (tracejada)
codes=[('27',0),('59',0),('59N',0),('81 O/U',0),
       ('25',0),('32',0),('46',0),('47',0),
       ('50/51',0),('50N/51N',0),('67',0),('51V',0),
       ('81 df/dt',0),('78',1),('21',0),('50BF',0)]
protbox(ax,x,y_prot,codes,side=-1)
lbl(ax,x-3.9,8.18,'(✱)',ha='left',fs=8,c=BLUE)
# disjuntor tripolar
breaker(ax,x,y_cb,'Disjuntor tripolar MT',num='52')
# TD + trafo de acoplamento  + ramo de Carga
lbl(ax,x+0.4,y_td,'TD (trafo de distribuição)',fs=8)
ax.add_patch(Circle((x,y_td),0.16,fill=False,edgecolor=K,lw=LW,zorder=3))
transformer(ax,x,y_tr,'Δ','Yn','Trafo de acoplamento · 59N')
dot(ax,x,y_tr+0.5); L(ax,x,y_tr+0.5,x+1.9,y_tr+0.5); L(ax,x+1.9,y_tr+0.5,x+1.9,y_tr); lbl(ax,x+2.0,y_tr+0.25,'Carga',fs=8.5)
# inversor + proteções internas (caixa lateral, estilo Figura 2)
invcodes=[('81 O/U',0),('59',0),('27',0),('25',0),('Anti-ilham.',0)]
invbox(ax,x,y_pcs+0.6,invcodes)
inverter(ax,x,y_pcs,'PCS bidirecional')
battery(ax,x,y_bat,'Banco de baterias (BESS)')
# legenda — em faixa própria abaixo do desenho, separada por linha (sem colidir)
leg=('FU: chave fusível · PR: para-raios · M: medidor 4 quadrantes\n'
     'TC/TP: transformadores de instrumentos · CS: chave seccionadora c/ abertura sem carga\n'
     'TD: trafo de distribuição\n'
     '(✱) função 78 (salto de vetor) tracejada = DECISÃO PENDENTE (ver §9.2.6)')
L(ax,0.3,0.30,8.5,0.30,c='#bbbbbb',lw=0.8)
lbl(ax,0.4,0.02,leg,ha='left',va='top',fs=6.5,c='#444',)
ax.set_xlim(0.2,8.7); ax.set_ylim(-1.0,11.4)
fig.savefig('img/anexoA2.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('A2 ok')

# ===== A.3 — Híbrido com LPI =====
fig,ax=newfig(7.4,8.8,'A.3 — Unifilar: BESS híbrido com MMGD (on-grid, LPI)')
x=3.5; top=8.8
put_title(ax,x,top+0.7); busbar(ax,x,top,2.2,'Rede CERPRO — BT ou MT')
y_m=8.1; y_b=7.2; y_pcc=6.3
L(ax,x,top,x,y_pcc)
meter(ax,x,y_m); lbl(ax,x+0.34,y_m,'Medição 4 quadrantes / SMF',fs=8.5)
breaker(ax,x,y_b,'Proteção de interface (§9.1/§9.2)',num='')
busbar(ax,x,y_pcc,2.4,'',sub=None); lbl(ax,x,y_pcc+0.33,'PCC — Ponto de Acoplamento Comum',ha='center',fs=10,c=BLUE,b=True)
# two feeders
lx,rx=x-1.6,x+1.6
L(ax,lx,y_pcc,lx,3.0); L(ax,rx,y_pcc,rx,3.4)
L(ax,x-1.2,y_pcc,lx,y_pcc); L(ax,x+1.2,y_pcc,rx,y_pcc)
inverter(ax,lx,5.4,'PCS BESS'); battery(ax,lx,4.2,'Baterias')
L(ax,lx,5.4,lx,4.2)
ax.add_patch(Rectangle((lx-0.18,3.0-0.18),0.36,0.36,fill=False,edgecolor=K,lw=LW)); lbl(ax,lx,3.0,'BMS',ha='center',fs=7)
inverter(ax,rx,5.4,'Inversor MMGD'); pv(ax,rx,4.0,'Gerador FV')
L(ax,rx,5.4,rx,4.0)
# SCRPI note box
ax.add_patch(Rectangle((x-3.05,2.0),6.1,0.6,fill=True,facecolor='#FBEAEA',edgecolor=RED,lw=LW))
lbl(ax,x,2.3,'SCRPI / EMS aplica LPI ≤ «limite do orçamento de conexão» (fail safe ≤ 15 s)',ha='center',fs=7.4,c=RED)
L(ax,lx,3.0-0.18,x-0.5,2.6,c=RED,lw=1.0,ls='--'); L(ax,rx,4.0-0.30,x+0.5,2.6,c=RED,lw=1.0,ls='--')
ax.set_xlim(0.2,7.6); ax.set_ylim(1.7,9.8)
fig.savefig('img/anexoA3.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('A3 ok')

# ===== Placa de advertência (DSV BESS — CERPRO) =====
from matplotlib.patches import Polygon, FancyBboxPatch
fig,ax=plt.subplots(figsize=(6.6,7.8)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,12.0)
ax.add_patch(Rectangle((0.15,0.15),9.7,11.7,fill=False,edgecolor=K,lw=3))
# faixa superior PERIGO
ax.add_patch(Rectangle((0.15,10.45),9.7,1.4,fill=True,facecolor='#C00000',edgecolor=K,lw=1))
ax.text(5,11.15,'PERIGO',ha='center',va='center',fontsize=27,fontweight='bold',color='white')
# triângulo de advertência
tri=Polygon([[5,10.0],[3.85,8.0],[6.15,8.0]],closed=True,facecolor='#FFD400',edgecolor=K,lw=2.2,zorder=3)
ax.add_patch(tri); ax.text(5,8.55,'!',ha='center',va='center',fontsize=30,fontweight='bold',color=K,zorder=4)
# riscos
ax.text(5,7.45,'RISCO ELÉTRICO · INCÊNDIO · EXPLOSÃO · QUÍMICO',ha='center',va='center',fontsize=8.0,fontweight='bold',color='#C00000')
# corpo
ax.text(5,6.55,'SISTEMA DE ARMAZENAMENTO DE\nENERGIA POR BATERIAS (BESS)',ha='center',va='center',fontsize=11.5,fontweight='bold',color=BLUE)
ax.add_patch(Rectangle((1.0,5.05),8.0,0.85,fill=True,facecolor='#FFF3CC',edgecolor=K,lw=1.2))
ax.text(5,5.48,'DISPOSITIVO DE SECCIONAMENTO VISÍVEL (DSV)',ha='center',va='center',fontsize=9.5,fontweight='bold',color=K)
ax.text(5,4.05,'Somente pessoal AUTORIZADO e TREINADO.\nProibido operar, abrir ou intervir sem autorização da CERPRO.\nVedada intervenção por pessoas não treinadas\nem caso de fuga térmica.',
        ha='center',va='center',fontsize=8.2,color=K,linespacing=1.4)
# faixa emergência
ax.add_patch(Rectangle((0.15,1.75),9.7,1.35,fill=True,facecolor='#1F3864',edgecolor=K,lw=1))
ax.text(5,2.72,'EMERGÊNCIA',ha='center',va='center',fontsize=10.5,fontweight='bold',color='#FFD400')
ax.text(5,2.18,'Acionar a CERPRO e o Corpo de Bombeiros (193)',ha='center',va='center',fontsize=9.2,color='white')
# rodapé CERPRO
ax.text(5,1.15,'CERPRO — Cooperativa de Eletrificação Rural\nda Região de Promissão',ha='center',va='center',fontsize=8.0,color=BLUE,fontweight='bold',linespacing=1.3)
ax.text(5,0.45,'Conforme NTC-D-14 (Anexos C e H) · NFPA 855',ha='center',va='center',fontsize=7.2,color='#555')
fig.savefig('img/placa-dsv-bess.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('placa ok')

# ===== Fluxograma do Anexo I (processo de análise BESS) =====
fig,ax=plt.subplots(figsize=(9.6,7.4)); ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,13)
steps=[
 '1. Protocolo\n(≤ 5 dias úteis p/ conferência)',
 '2. Análise preliminar\n(classificação A–D)',
 '3. Parecer regulatório',
 '4. Parecer técnico\n(curto-circuito, fluxo,\ncoordenação, QEE, estabilidade)',
 '5. Parecer operacional\n(telecomando, supervisão,\ncontingências)',
 '6. Parecer jurídico\n(contratos, garantias, seguros)',
 '7. Comitê Interno BESS\n(aprova / condiciona /\ncomplementa / indefere)',
 '8. Orçamento de Conexão (OC)',
 '9. Formalização contratual\n(Acordo Operativo + aditivo CUSD\n+ Declaração de Não Exportação)',
 '10. Execução das adequações\n(acompanhada pela CERPRO)',
 '11. Comissionamento\n(Anexo J)',
 '12. Autorização para operação',
 '13. Monitoramento contínuo\n(eventos, alarmes, QEE)',
 '14. Fiscalização\n(inspeções, auditorias)',
 '15. Suspensão da operação\n(se risco/descumprimento)',
]
cols=3; dx=4.0; dy=2.45; x0=0.5; y0=12.2; bw=3.5; bh=1.7
pos=[]
for i in range(len(steps)):
    r=i//cols; c=i%cols
    cc=c if r%2==0 else (cols-1-c)   # serpente
    x=x0+cc*dx; y=y0-r*dy; pos.append((x+bw/2,y-bh/2))
    fc='#FDE9E9' if i==6 else ('#FFF3CC' if i==14 else '#EAF1FB')
    ec=RED if i in(6,14) else BLUE
    ax.add_patch(FancyBboxPatch((x,y-bh),bw,bh,boxstyle='round,pad=0.04,rounding_size=0.18',
                 facecolor=fc,edgecolor=ec,lw=1.6))
    ax.text(x+bw/2,y-bh/2,steps[i],ha='center',va='center',fontsize=7.6,color=K)
# setas seguindo a serpente
def arrow(p,q):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color='#444',lw=1.4,shrinkA=2,shrinkB=2))
for i in range(len(steps)-1):
    (x1,y1),(x2,y2)=pos[i],pos[i+1]
    same_row=(i//cols)==((i+1)//cols)
    if same_row: arrow((x1+ (bw/2 if x2>x1 else -bw/2), y1),(x2+(-bw/2 if x2>x1 else bw/2),y2))
    else: arrow((x1,y1-bh/2),(x2,y2+bh/2))
ax.text(6,0.4,'Fluxo de análise e conexão de sistemas BESS — Anexo I (Classes A–D conforme §13).',
        ha='center',va='center',fontsize=8,style='italic',color='#555')
fig.savefig('img/anexoI-fluxo.png',dpi=200,bbox_inches='tight'); plt.close(fig); print('fluxo ok')
