# NTC-D-XX — Requisitos e Procedimentos para Conexão de Sistemas BESS ao Sistema de Distribuição da CERPRO

| Campo | Conteúdo |
|---|---|
| **Documento** | NTC-D-XX — Norma Técnica e Padronização |
| **Versão de trabalho** | R1-consolidada (a partir do R0 da Engenharia + NT-BESS-001/2026) |
| **Estado** | Rascunho em consolidação |
| **Base** | `docs/fontes-cerpro/NTC-D-XX_BESS_v01-2026_R0.md` · `docs/fontes-cerpro/NT-BESS-001-2026_normas-internas.md` · `docs/pesquisa/` |

> **Convenções desta consolidação**
> `«PARÂMETRO»` = valor a ser cravado pela Engenharia da CERPRO · `[DECISÃO CERPRO]` = ponto que
> requer deliberação · `[VERIFICAR]` = citação regulatória a confirmar antes da publicação.
> Numeração de seções refeita (o R0 tinha "7.4" repetido e saltos). Terminologia ESS/SAE/BESS
> saneada conforme item 1.1.

---

## CONTROLE DE REVISÕES
| Rev. | Data | Descrição | Responsável |
|---|---|---|---|
| R0 | 01/2026 | Versão inicial da Engenharia (seções 1–9, incompleta) | Engenharia CERPRO |
| R1 | `«data»` | Consolidação: §9 completada, tabelas, anexos migrados do NT-BESS-001, terminologia e numeração saneadas, anti-ilhamento alinhado | Squad de Normas |

## SUMÁRIO
1. Apresentação · 2. Campo de Aplicação · 3. Objetivo · 4. Referências Normativas e Documentais ·
5. Responsabilidades · 6. Termos e Definições · 7. Critérios Básicos de Conexão · 8. Etapas e
Documentos para Viabilização do Acesso · 9. Forma de Conexão e Sistema de Proteção · 10. Qualidade
de Energia, Medição e Telemetria · 11. Comissionamento, Operação, Manutenção e Descomissionamento ·
12. Segurança, Emergência e Responsabilidades · 13. Governança da Análise (Classificação e Comitê) ·
14. Disposições Finais e Vigência · Anexos A–K.

---

## 1. APRESENTAÇÃO
A CERPRO — Cooperativa de Eletrificação Rural da Região de Promissão, permissionária do serviço
público de distribuição regulada pela ANEEL, consolida neste documento as diretrizes técnicas,
procedimentais, ambientais e de segurança para a conexão de Sistemas BESS (*Battery Energy Storage
Systems*) ao seu sistema de distribuição.

### 1.1 ESS, SAE e BESS — hierarquia conceitual *(terminologia saneada)*
- **ESS (*Energy Storage System*)** — **família geral** de sistemas que armazenam energia para uso
  posterior, qualquer que seja a forma física. Inclui PHES, CAES, *flywheels*, TES, hidrogênio/célula
  a combustível, capacitores/supercapacitores, SMES e **BESS**.
- **SAE (Sistema de Armazenamento de Energia)** — **termo equivalente em português de ESS** (a
  família geral). *(Correção: o R0 confundia SAE com BESS; SAE = ESS, não = BESS.)*
- **BESS (*Battery Energy Storage System*)** — **subconjunto eletroquímico** (por baterias) da
  família ESS/SAE. Sistema completo: módulos de bateria, BMS, PCS, EMS, HVAC, proteções e gabinete.

Esta NTC-D-XX disciplina **exclusivamente os sistemas BESS**. Demais tecnologias da família ESS/SAE
ficam fora do escopo e serão tratadas caso a caso, em regulamentação específica.

### 1.2 Modalidades contempladas
- **BESS junto à carga** (*behind-the-meter*), sem MMGD associada;
- **BESS híbrido**, em conjunto com micro/minigeração distribuída (MMGD).

## 2. CAMPO DE APLICAÇÃO
### 2.1 Aplicação
Unidades consumidoras conectadas (ou com pedido protocolado) ao sistema da CERPRO, em **BT** (< 2,3
kV) ou **MT** (2,3 kV ≤ Un < 69 kV), que instalem, ampliem, substituam ou operem BESS, com ou sem GD.
Aplicações cobertas: *backup*/UPS; integração de renováveis (*peak-shifting*, *smoothing*,
*firming*); compensação reativa; arbitragem tarifária (*load shifting*, *peak shaving*); operação
ilhada intencional de microrredes/sistemas críticos.

### 2.2 Não aplicação
- Demais tecnologias ESS (PHES, CAES, *flywheel*, TES, hidrogênio, capacitores, SMES) — caso a caso;
- Fotovoltaico sem BESS (ver NTC-D-09);
- Baterias automotivas/veiculares não estacionárias (EV, V2G, V2H, V2X móveis);
- BESS *off-grid* permanente, sem interface com a rede;
- Conexões em AT (≥ 69 kV) — regulamentação específica em conjunto com o ONS.

## 3. OBJETIVO
Estabelecer critérios técnicos, procedimentos, documentação mínima, requisitos de segurança e
ambientais e obrigações das partes — observando a regulação dos órgãos competentes quando existente,
e prevalecendo esta norma quando não houver regulação específica — para que o acessante possa
projetar, protocolar, instalar, comissionar, operar e descomissionar BESS conectados ao sistema da
CERPRO, preservando a segurança de pessoas, instalações e meio ambiente e a qualidade e continuidade
do serviço.

## 4. REFERÊNCIAS NORMATIVAS E DOCUMENTAIS
*(Mantém-se o capítulo comentado do R0 — ver `docs/fontes-cerpro/NTC-D-XX_BESS_v01-2026_R0.md` §4.
Destaques e correções:)*
- **Espinha dorsal técnica:** ABNT NBR 17153:2023 (BESS).
- **INMETRO:** Portarias 140/2022, 515/2023, 17/2016.
- **ANEEL:** REN 1.000/2021; **REN 956/2021 [VERIFICAR número — confirmar se é a dos Procedimentos de
  Distribuição/PRODIST]**; **RN de SAE de 2026 [VERIFICAR nº/DOU]**; **Lei 15.269/2025 [VERIFICAR]**;
  Lei 14.300/2022; REN 616/2014; PRODIST Mód. 1/3/5/8.
- **ABNT:** 5410, 14039, 5419, 14519, 15479/15688/15751, 16149/16150, IEC 62116, 16690, 16767,
  16975/16976, 10151, 17240, 14725.
- **IEC:** 60364, 60896, 61140, 61439, 61850, 62040, 62109-2, 62116, 62133, 62619, 62620, 62933
  (-2-1, -4-2, -4-3, -5-1, -5-2), 62443.
- **IEEE:** 242, 519, 1547/1547.1/1547.4, 2030.3.
- **NFPA/UL:** NFPA 855:2023, 68, 69, 70, 72, 1; UL 9540, 9540A, 1973, 1974.
- **NRs:** NR-10 (+ SEP), NR-33, NR-35.
- **Ambiental:** CONAMA 237/1997 e 401/2008; Lei 12.305/2010 (PNRS) + Dec. 10.936/2022; IN Ibama 8/2012.

## 5. RESPONSABILIDADES
Compete aos órgãos de mercado, planejamento, operação, automação, proteção, atendimento e ligação da
CERPRO cumprir e fazer cumprir esta norma. A **segregação detalhada** acessante × CERPRO consta do
**Anexo G — Matriz de Responsabilidades** (migrada do NT-BESS-001).

## 6. TERMOS E DEFINIÇÕES
Aplicam-se as definições da NTC-D-09 e do PRODIST Módulo 1, além dos termos do R0 (ver fonte). 
**Correções aplicadas:**
- **SAE** — Sistema de Armazenamento de Energia: equivalente em português de **ESS** (família geral).
  *(Removida a definição 6.35-A do R0, que igualava SAE a BESS.)*
- **BESS** — subconjunto eletroquímico (baterias) da família ESS/SAE; objeto exclusivo desta NTC.
- Mantidas as definições operacionais: BMS, PCS, EMS, HVAC, SoC/SoH, C-rate, DoD, RTE, FRT/LVRT/HVRT,
  Zero-Grid, LPI, SCRPI, *thermal runaway*, *off-gassing*, *hard limit*, *fail safe*, DSV, etc.

### 6.1 Mini-glossário — controle de fluxo de potência *(novo — elimina ambiguidade apontada no QA)*
Os termos abaixo **não são sinônimos** e devem ser empregados com precisão ao longo da norma:

| Termo | Significado nesta NTC | Como se comprova |
|---|---|---|
| **Zero-Grid** | Estado operacional em que a **injeção de potência ativa na rede é nula** (exportação = 0). É o *objetivo* do BESS sem GD. | Ensaio/declaração do fornecedor (§7.2, Anexo C) |
| **Anti-exportação** | **Função/dispositivo** que impede física e logicamente o fluxo reverso de ativa para a rede, garantindo o Zero-Grid. Pode exigir redundância. | Função 32 + lógica dedicada; teste de comissionamento (Anexo J/K) |
| **LPI — Limitação de Potência Injetada** | **Limite máximo** de injeção (não necessariamente zero) aplicado a BESS híbrido com MMGD, conforme orçamento de conexão. | Ensaio/declaração de atuação da limitação (§7.2) |
| **SCRPI — Sistema de Controle de Redução da Potência Injetável** | **Sistema** que executa a LPI, reduzindo a potência ao valor-limite (modo *fail safe* em ≤ 15 s). | Memorial do EMS + ensaio |
| **Hard Limit** | Limite **em hardware**, independente de software, como camada redundante do anti-exportação/LPI. | Projeto do PCS/proteção |

> Resumo: **Zero-Grid** (estado, injeção = 0) é garantido pela função **Anti-exportação**; **LPI**
> (limite > 0) é executada pelo **SCRPI**; o **Hard Limit** é a camada redundante de ambos.

## 7. CRITÉRIOS BÁSICOS DE CONEXÃO
### 7.1 BESS sem Geração Distribuída
**Princípio:** não pode injetar potência ativa na rede (**Zero-Grid** quanto à exportação). Funções
permitidas: *backup*/UPS, compensação de reativos local, arbitragem/*peak shaving*.

**7.1.1 Requisitos por porte:**
- **BT (P ≤ 75 kW):** atender NTC-D04; interface conforme §9.1.
- **MT / P > 75 kW:** atender NTC-D03; **transformador de acoplamento**, **disjuntor de MT** e **relé
  de proteção** (funções da Tabela 4).
- **P > 300 kW:** adicionalmente **religador telecomandado** no ponto de paralelismo e equipamento
  com **supervisão remota** integrável ao COS, participando do cálculo de proporcionalidade.

**7.1.2 Modos de operação:**
- **On-Grid:** paralelo com a rede; **sem injeção de ativa**; serviços ancilares (reativo, QEE) e
  arbitragem permitidos. Funcionalidades habilitadas declaradas no formulário (Anexo B).
- **Off-Grid (ilhado):** isolado, tipicamente *backup*; **ilhamento interno seguro** restrito à UC;
  desacoplamento automático na ausência da rede. Inversores certificados INMETRO (Port. 140/2022)
  dispensam chave de intertravamento; demais arranjos exigem dispositivo de desconexão/intertravamento.

### 7.2 BESS com Geração Distribuída (Sistemas Híbridos) *(título corrigido)*
Documentação de MMGD (NTC-D09) **mais** os complementos do Anexo B. Para *on-grid*, apresentar
ensaios/declaração do fornecedor comprovando atuação da **Limitação de Potência Injetada (LPI)** e,
quando Zero-Grid, da **não injeção de ativa**.

### 7.3 Requisitos Ambientais
Implantação compatível com as condições do sítio (IEC 62933-4-3:2025; -5-1:2024): proteção contra
descargas atmosféricas, sismo, inundação, umidade, corrosão, poeira, fauna/flora; drenagem/contenção
de efluentes; avaliação documentada de impacto de falha de célula/módulo; **logística reversa e
descarte** (Lei 12.305/2010; CONAMA 401/2008; IN Ibama 8/2012). Licenciamento ambiental conforme
órgão estadual competente (CONAMA 237/1997).

### 7.4 Requisitos de Segurança
Conformidade a NFPA 855, NFPA 70/1, IEC 62933-5-1/-5-2; certificação/listagem do sistema e
componentes críticos (UL 9540/1973/1741); proteção e monitoramento por BMS (+EMS); desligamento
seguro, intertravamentos, sinalização, aterramento; ventilação/climatização, detecção e mitigação de
gases, detecção/controle/supressão de incêndio; proteção contra *thermal runaway* baseada em ensaio
(UL 9540A); FDS disponíveis (NBR 14725).
**Afastamentos:** definidos pela configuração efetiva, relatórios de ensaio (UL 9540A), instruções do
fabricante e autoridade competente, adotando-se **o critério mais restritivo**. O valor de **`«3,0 m»`**
da NFPA 855 é referência mínima ao tempo, ampliável conforme ensaio de propagação térmica. Redução só
com comprovação por ensaio/barreira corta-fogo/parede incombustível. Exaustão não pode descarregar
sobre rotas de fuga, passagens ou tomadas de ar.

### 7.5 Requisitos de Qualidade de Energia
Atendimento integral ao **PRODIST Módulo 8**: tensão em regime permanente, fator de potência,
distorções harmônicas, desequilíbrio, *flicker*, variação de frequência e VTCD. Não conformidade →
medidas corretivas a cargo do acessante. Detalhamento em §10.

### 7.6 Requisitos de Operação, Manutenção e Descarte
Conexão só autorizada se não houver risco técnico/segurança e sem prejuízo à qualidade/continuidade.
Consumidor responde civil e criminalmente por manobras/interligações indevidas e pela manutenção.
**Suspensão imediata e sem aviso** em risco iminente. **Proibido energizar a rede desenergizada da
CERPRO** (ilhamento não intencional). Sinalização: ≥ 2 placas (Anexo C). Descarte conforme PNRS/CONAMA 401.

### 7.7 Responsabilidades Adicionais
Cumprimento integral dos requisitos; a CERPRO pode exigir estudos de impacto (custeados pelo
acessante); injeção sem anuência é irregularidade grave (sanções: suspensão, perda de enquadramento
GD, desconsideração da energia injetada, demais penalidades).

### 7.8 Forma de protocolo
Documentação por **`«cerpro@cerpro.com.br»`** ou presencialmente na sede; protocolo inicia a
contagem de prazos.

## 8. ETAPAS E DOCUMENTOS PARA VIABILIZAÇÃO DO ACESSO
**8.1 Fluxo processual** (alinhado ao MP-BESS — ver Anexo I):
1. *(Facultativa)* Consulta de Acesso / Orçamento Estimado.
2. Solicitação de Orçamento de Conexão (formulário Anexo B + docs do 8.2).
3. **Análise documental — até 5 du.**
4. **Classificação de complexidade (Classe A–D)** e estudos técnicos (§13).
5. **Emissão do Orçamento de Conexão:** 15 d (com/sem micro, sem reforço) · 30 d (com reforço) · 45 d (demais).
6. Aceite/assinatura do OC + **Relacionamento Operacional / Acordo Operativo** (Anexo F).
7. Execução das obras (prazo Art. 88 REN 1.000).
8. Comissionamento prévio + relatório (Anexo J).
9. Solicitação de Vistoria.
10. **Vistoria técnica:** 5 du (BT) · 10 du (MT); laudo em 3 du.
11. **Primeiro paralelismo PRESENCIAL** com vistoriador CERPRO.
12. Energização e operação comercial.
13. Cadastro ANEEL (quando aplicável) — até 5 du.

**8.2 Documentação mínima:** identificação do titular/RT; ART/TRT + CREA/CFT; Memorial Descritivo
(dados do empreendimento, baterias, PCS, BMS, EMS, HVAC, memória de cálculo, Plano de Segurança,
Plano de Emergência, Plano de Descomissionamento); diagrama unifilar; planta baixa (implantação,
acessos, rotas de fuga, FDC, afastamentos, áreas de segurança); estudo de proteção e aterramento;
sistema de intertravamento; *datasheets* e manuais; **certificação INMETRO** (baterias e inversores);
cronograma físico-financeiro; **declaração de não exportação/LPI** (Anexo C); **AVCB ou equivalente
[DECISÃO CERPRO — confirmar obrigatoriedade geral]**; licenças ambientais exigíveis; **comprovação de
seguro [DECISÃO CERPRO]**.

## 9. FORMA DE CONEXÃO E SISTEMA DE PROTEÇÃO

### 9.1 Requisitos em Baixa Tensão (BT) — P ≤ 75 kW
**Tabela 3 — Elementos mínimos na interface de conexão em BT**

| Elemento | Exigência |
|---|---|
| Acoplamento | Direto em BT, conforme NTC-D04 |
| Seccionamento visível (DSV) | Travável em LOTO, placa "DSV BESS — CERPRO" (Anexo H) |
| Elemento de interrupção | Atua com **U ≤ 0,7 p.u. de Un**, atraso **≤ 2,0 s** |
| Proteções do PCS/inversor | Certificadas INMETRO (Port. 515/2023; NBR 16149/16150) |
| Anti-ilhamento | Ensaio IEC 62116 / NBR IEC 62116 (comissionamento) |
| Medição | Bidirecional / SMF conforme §10 |

**Tabela do item 9.1.1 — Ajustes mínimos de proteção em BT** *(Port. INMETRO 515/2023 e NBR 16149)*

| Função | Grandeza | Ajuste | Tempo |
|---|---|---|---|
| 27 | Subtensão | `«0,80 p.u.»` | `«s»` |
| 59 | Sobretensão | `«1,10 p.u.»` | `«s»` |
| 81U | Subfrequência | `«57,5 Hz»` | `«s»` |
| 81O | Sobrefrequência | `«62,0 Hz»` | `«s»` |
| 81 df/dt | ROCOF | `«2,0 Hz/s»` | — |
| Anti-ilhamento | — | desconexão **≤ 2,0 s** | — |

> Valores entre `«»` a confirmar pela Engenharia com base na Port. 515/2023 vigente.

**9.1.2 DSV e Elemento de Interrupção:** DSV visível e travável (LOTO), placa do Anexo H; interrupção
com U ≤ 0,7 p.u., atraso ≤ 2,0 s.

### 9.2 Requisitos em Média Tensão (MT) — P > 75 kW
**9.2.1 Transformador de acoplamento:** obrigatório; isolação galvânica; **Dyn11 ou Dyn1**; em 13,8/
34,5 kV, enrolamento dedicado para **59N**; impedância e TAPs conforme estudo.

**9.2.2 Chave seccionadora:** tripolar, manual + motorizada (telecomando para P > 300 kW);
intertravamento Kirk; indicação OPEN/CLOSED; abertura visível.

**9.2.3 Disjuntor geral de MT:** tripolar, vácuo ou SF6 (**óleo mineral vedado**); molas com
carregamento motorizado; bobina de abertura com dupla alimentação (CC + CA aux.); indicação mecânica
e elétrica; bloqueio Kirk; cores I-vermelho/O-verde; Icc compatível (informado no OC).

**9.2.4 Relé digital multifuncional — Tabela 4 — Funções ANSI mínimas obrigatórias**

| ANSI | Função | BT (≤75 kW) | MT (>75 kW) | Obs. |
|---|---|---|---|---|
| 27 | Subtensão | ✔ | ✔ | |
| 59 | Sobretensão | ✔ | ✔ | |
| 59N | Sobretensão de neutro | — | ✔ | enrol. dedicado |
| 81O/81U | Sobre/subfrequência | ✔ | ✔ | |
| 81 df/dt | ROCOF | ✔ | ✔ | redundância anti-ilhamento |
| 25 | Verificação de sincronismo | — | ✔ | |
| 32 | Direcional de potência | — | ✔ | apoio ao Zero-Grid/LPI |
| 46/47 | Desequilíbrio corrente/tensão | `«opc»` | ✔ | |
| 50/51 | Sobrecorrente inst./temp. | — | ✔ | |
| 50N/51N | Falta à terra | — | ✔ | |
| 64 | Proteção de aterramento | — | `«conf. arranjo»` | |
| 67 | Sobrecorrente direcional | — | `«P > «valor» kW»` | |
| ~~78~~ | ~~Salto de vetor~~ | ❌ | ❌ | **VEDADO** — ver 9.2.6 |

**9.2.5 Ride-through (FRT):**

**Tabela 5 — Suportabilidade a afundamentos de tensão (LVRT) em MT**
| Tensão no PCC (p.u.) | Tempo mínimo de permanência |
|---|---|
| ≥ 0,90 | regime permanente |
| 0,80 – 0,90 | `«s»` |
| 0,50 – 0,80 | `«s»` |
| < 0,50 | desconexão conforme `«ms»` |

**Tabela 6 — Suportabilidade a desvios de frequência**
| Faixa (Hz) | Tempo mínimo |
|---|---|
| 58,5 – 62,5 | `«ilimitado / valor»` |
| < 58,5 ou > 62,5 | desconexão |
| df/dt | ≤ `«2,0 Hz/s»` |

> Faixas-base do dossiê; valores finais a cravar pela Engenharia (alinhar a IEEE 1547 e PRODIST).

**9.2.6 Anti-ilhamento em MT — [decisão aplicada: salto de vetor VEDADO]**
- Desconexão em **≤ 2,0 s** após detecção; limiar **U ≤ 0,7 p.u.**
- **Método primário: passivo por df/dt (ROCOF)** + monitoramento de tensão/frequência, **vedado o
  uso de salto de vetor (função 78)** como método em conversores, por suscetibilidade a atuação
  indevida e *nuisance tripping* (alinhado ao benchmark de distribuidoras).
- Redundância para **P > 500 kW**: método ativo de detecção compatível com IEC 62116 + telecomando.
- **Proibido** ajuste de subfrequência ≥ 58,5 Hz para fins de anti-ilhamento.
> *Nota de mudança em relação ao R0:* o R0 previa a função 78 como primário; substituída por df/dt +
> método ativo conforme decisão da CERPRO de 2026-06-19.

**9.2.7 Proteção auxiliar:** fonte auxiliar com autonomia ≥ 2 h (no-break + banco + retificador);
no-break ≥ 1000 VA; iluminação de emergência na sala de proteção.

**9.2.8 Religador telecomandado:** obrigatório P > 300 kW; integração ao COS via **DNP3 ou IEC 61850**.

**9.2.9 Aterramento:** NBR 5410/14039/15751/15479; resistência **≤ 10 Ω** (em regra);
equipotencialização de gabinetes/racks/estruturas; **DPS** conforme NBR 5419 (incl. DPS CC).

## 10. QUALIDADE DE ENERGIA, MEDIÇÃO E TELEMETRIA *(seção nova — completa a §9 do R0)*
### 10.1 Qualidade de Energia
Limites do **PRODIST Módulo 8** `[transcrever valores vigentes]`; injeção CC < `«0,5 %»`; harmônicos
conforme IEEE 519; *flicker* IEEE 1453/NBR. Medições de comprovação a cargo do acessante quando exigido.

### 10.2 Medição
SMF conforme **PRODIST Módulo 5** e NBR 14519: medição **bidirecional** (BT ≤ 75 kW) ou **4 quadrantes**
(> 75 kW); medição dedicada/anti-exportação quando exigida; **registro de eventos retido por `«60»`
meses** (padronizado com o Acordo Operativo — Anexo F).

### 10.3 Telemetria e Supervisão
Para P > `«300 kW»` (e a critério da CERPRO): integração ao COS com potência ativa/reativa instantânea,
tensão, corrente, frequência, SoC, ciclos, temperatura de módulos e alarmes críticos; sincronismo
horário; **IEC 61850 obrigatória para P > 500 kW** ou integração a subestação; **IEC 62443** para
EMS/SCADA de P > 500 kW.

## 11. COMISSIONAMENTO, OPERAÇÃO, MANUTENÇÃO E DESCOMISSIONAMENTO *(seção nova)*
- **Ensaio de conformidade do conversor:** PRODIST Mód. 3 (12.2/12.3), laboratório acreditado (ILAC/
  Inmetro); anti-ilhamento por IEC 62116/NBR IEC 62116.
- **Comissionamento em campo (Anexo J):** anti-ilhamento, anti-exportação/LPI, proteção, desligamento
  de emergência, comunicação/supervisão, teste funcional; CERPRO pode acompanhar presencialmente.
- **O&M:** plano de manutenção preventiva/corretiva; condições de desconexão/religamento (IEC
  62933-2-2/3-1); registros retidos `«60»` meses.
- **Descomissionamento:** desativação, coleta, logística reversa e destinação final (PNRS/CONAMA 401).

## 12. SEGURANÇA, EMERGÊNCIA E RESPONSABILIDADES *(consolida NT-BESS-001)*
- **Matriz de Responsabilidades:** Anexo G.
- **Procedimentos de Emergência:** Anexo H-EMG (passos 1–7; *thermal runaway*; incêndio; risco
  ambiental; comunicação imediata a CERPRO/Bombeiros/Defesa Civil/órgão ambiental; investigação de
  incidentes Nível 3/4 em ≤ 30 d; treinamento anual; **seguro** compatível com incêndio/explosão/
  dano ambiental/RC/dano à rede — **[DECISÃO CERPRO: tornar obrigatório?]**).
- **Suspensão cautelar** da operação até eliminação dos riscos, com retomada por autorização formal.

## 13. GOVERNANÇA DA ANÁLISE — CLASSIFICAÇÃO E COMITÊ *(consolida MP-BESS)*
- **Classificação de complexidade:** Classe A (baixa) · B (média) · C (alta) · D (estratégico),
  segundo potência, capacidade, tensão, tipo de conexão, GD associada e impacto na rede.
- **Estudos exigíveis por classe** `[DECISÃO CERPRO — definir matriz classe × estudo]`: curto-circuito,
  fluxo de potência, coordenação/seletividade, estabilidade, QEE/harmônicos, transitórios,
  contingência, impacto sistêmico (custeados pelo acessante).
- **Comitê Interno BESS** (Diretoria, Engenharia, Operação, Jurídico, Regulação): delibera aprovação /
  aprovação com condicionantes / complementação / **indeferimento técnico fundamentado** (critérios
  do Anexo K).
- **Pareceres:** técnico, regulatório, operacional e jurídico (fluxo MP-BESS, Anexo I).

## 14. DISPOSIÇÕES FINAIS E VIGÊNCIA *(seção nova)*
- Requisitos são **mínimos**; a CERPRO pode exigir adicionais conforme características do empreendimento,
  da rede ou da regulamentação.
- **Revisão** quando houver alteração regulatória, determinação da ANEEL, necessidade operacional ou
  novos riscos sistêmicos.
- **Vigência:** `«prazo, ex.: 120 dias após publicação»`; **regime de transição:** `«definir»`.

---

## ANEXOS (estrutura — conteúdo em arquivo próprio)
| Anexo | Título | Origem |
|---|---|---|
| A | Arranjos de conexão permitidos (BT/MT) | ✔ esboçado (diagramas cotados pendentes) |
| B | Formulário de solicitação + dados técnicos do BESS | NT-BESS-001 Anexo II + R0 |
| C | Declaração de Não Exportação / Placas de advertência | NT-BESS-001 Anexo III |
| D | Lista de certificações exigidas | ✔ consolidado (§4 R0) |
| E | Checklist de documentação | NT-BESS-001 Anexo I / MP-BESS Etapa 1 |
| F | Acordo Operativo (modelo) | NT-BESS-001 Anexo V |
| G | Matriz de Responsabilidades | NT-BESS-001 Anexo VII |
| H | Placa "DSV BESS — CERPRO" + Procedimentos de Emergência | R0 + NT-BESS-001 Anexo VIII |
| I | Fluxo/Manual de Procedimentos (classes, comitê, etapas) | MP-BESS-001 |
| J | Procedimento de Testes e Comissionamento | NT-BESS-001 Anexo VI |
| K | Critérios de indeferimento + Requisitos mínimos de proteção | NT-BESS-001 Anexo IV |

> Os modelos de texto dos anexos estão em `docs/fontes-cerpro/NT-BESS-001-2026_normas-internas.md`
> e serão formatados em `NTC-D-XX-anexos.md` na próxima rodada.
