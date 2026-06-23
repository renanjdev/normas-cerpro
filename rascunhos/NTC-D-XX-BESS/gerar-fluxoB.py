#!/usr/bin/env python3
"""Modelo B (final) — fluxo horizontal em serpente, Anexo I."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
BLUE='#1F3864'; K='#1a1a1a'
steps=[
 '1. Protocolo\n(≤ 5 dias úteis p/ conferência)','2. Análise preliminar\n(classificação A–D)','3. Parecer regulatório',
 '4. Parecer técnico\n(curto-circuito, fluxo, coordenação,\nQEE, estabilidade)','5. Parecer operacional\n(telecomando, supervisão,\ncontingências)','6. Parecer jurídico\n(contratos, garantias, seguros)',
 '7. Comitê Interno BESS\n(aprova / condiciona /\ncomplementa / indefere)','8. Orçamento de\nConexão (OC)','9. Formalização contratual\n(Acordo Operativo + aditivo CUSD\n+ Declaração de Não Exportação)',
 '10. Execução das adequações\n(acompanhada pela CERPRO)','11. Comissionamento\n(Anexo J)','12. Autorização para operação',
 '13. Monitoramento contínuo\n(eventos, alarmes, QEE)','14. Fiscalização\n(inspeções, auditorias)','15. Suspensão da operação\n(se risco/descumprimento)']
phase_of={0:0,1:1,2:1,3:1,4:1,5:1,6:2,7:3,8:3,9:4,10:4,11:4,12:5,13:5,14:5}
pcol=['#DCE6F5','#EAF1FB','#FDE9E9','#E7F0E7','#EAF1FB','#FFF6DD']
pec =['#2E5596','#2E5596','#C00000','#3a7d44','#2E5596','#C9A100']

fig,ax=plt.subplots(figsize=(11.5,7.4)); ax.axis('off')
cols=3; bw=3.6; bh=1.62; hgap=0.55; vgap=0.70
x0=0.35; y0=8.55
W=cols*bw+(cols-1)*hgap
ax.set_xlim(-0.1, x0+W+0.1)
rows=(len(steps)+cols-1)//cols
last_bottom=y0-(rows-1)*(bh+vgap)-bh
ax.set_ylim(last_bottom-1.0, y0+1.15)
ax.text(x0+W/2, y0+0.72, 'Anexo I — Fluxo de análise e conexão de sistemas BESS',
        ha='center', fontsize=13, fontweight='bold', color=BLUE)

def cell(i):
    r=i//cols; c=i%cols; cc=c if r%2==0 else (cols-1-c)
    x=x0+cc*(bw+hgap); y=y0-r*(bh+vgap)
    return x,y,x+bw,y-bh,x+bw/2,y-bh/2
def arrow(p,q,c='#5b6677'):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=c,lw=1.8,shrinkA=1,shrinkB=1))

for i,txt in enumerate(steps):
    x,yt,xr,yb,xcm,ycm=cell(i); ph=phase_of[i]
    ax.add_patch(FancyBboxPatch((x,yb),bw,bh,boxstyle='round,pad=0.02,rounding_size=0.10',
                 facecolor=pcol[ph],edgecolor=pec[ph],lw=1.8))
    ax.text(xcm,ycm,txt,ha='center',va='center',fontsize=8.0,color=K,
            fontweight='bold' if i in(6,14) else 'normal')
# setas seguindo a serpente
for i in range(len(steps)-1):
    _,_,_,_,x1,y1=cell(i); _,_,_,_,x2,y2=cell(i+1)
    same=(i//cols)==((i+1)//cols)
    if same: arrow((x1+(bw/2 if x2>x1 else -bw/2),y1),(x2-(bw/2 if x2>x1 else -bw/2),y2))
    else:    arrow((x1,y1-bh/2),(x2,y2+bh/2))
# legenda centralizada
names=['Solicitação','Análise','Decisão','Contratação','Implantação','Operação']
lx=x0; ly=last_bottom-0.62
import matplotlib.transforms as mt
seg=W/ len(names)
for k,(nm,cf,ce) in enumerate(zip(names,pcol,pec)):
    xx=x0+k*seg
    ax.add_patch(Rectangle((xx,ly),0.34,0.34,facecolor=cf,edgecolor=ce,lw=1.4))
    ax.text(xx+0.46,ly+0.17,nm,fontsize=8.2,va='center',color=K)
fig.savefig('img/anexoI-fluxo.png',dpi=200,bbox_inches='tight',pad_inches=0.12)
plt.close(fig); print('Modelo B final ok')
