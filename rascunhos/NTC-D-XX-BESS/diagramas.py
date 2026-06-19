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

# ===== A.2 — MT =====
fig,ax=newfig(7.0,9.6,'A.2 — Unifilar: BESS sem GD em MT (P > 75 kW)')
x=3.2; top=9.7
put_title(ax,x,top+0.7); busbar(ax,x,top,2.2,'Rede CERPRO — MT (13,8 / 34,5 kV)')
ys=[9.0,8.1,7.2,6.2,5.0,3.9,2.9]
L(ax,x,top,x,ys[-1]-0.4)
recloser(ax,x,ys[0],'Religador telecom. (P>300 kW → COS)')
disconnect(ax,x,ys[1],'Seccionadora tripolar (Kirk)')
breaker(ax,x,ys[2],'Disjuntor MT (vácuo/SF6)',num='52')
relay(ax,x,ys[3],+1,'Relé multifunção\n27/59/59N/81/25/32/46/47\n50/51/50N/51N/67 — SEM 78',c=BLUE); dot(ax,x,ys[3])
transformer(ax,x,ys[4],'Δ','Yn','Trafo Dyn11/Dyn1 · 59N')
inverter(ax,x,ys[5],'PCS')
battery(ax,x,ys[6])
lbl(ax,x-1.7,ys[5]+0.4,'Med. 4 quadrantes\nFonte aux. ≥2 h\nAterr. ≤10 Ω + DPS',ha='left',fs=7.4,c='#555')
ax.set_xlim(0.2,6.9); ax.set_ylim(2.0,10.7)
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
