# FRENTE B — PRODIST + Lei 14.300/2022: acesso e requisitos por porte/tensão

> Data: **19/06/2026**. Fontes primárias baixadas e extraídas (PDF→texto / HTML→texto). Onde o
> host oficial da ANEEL estava sob Cloudflare (HTTP 403), usou-se espelho idêntico do mesmo
> documento (Light/CooperLuz) ou o texto consolidado da LegisWeb, sempre indicado.

> **CONCLUSÃO CENTRAL:** o arcabouço atual (PRODIST Mód. 1 e 3 + REN 1.000/2021 + Lei 14.300/2022)
> **não trata o armazenamento como categoria autônoma de acesso**. O SAE/BESS aparece de forma
> incidental: (a) Lei 14.300 art. 2º (acesso "com ou sem sistema de armazenamento... híbridos") e
> art. 1º IX (FV+baterias para enquadrar "despachável"); (b) PRODIST Mód. 3 itens 12.2/12.3 (ensaio
> de conformidade do conversor) e Tabelas 1-B/1-C (ride-through do conversor). Não há tabela
> tensão×potência nem prazos específicos de BESS — a norma da distribuidora deve **derivar** os
> requisitos do regime de micro/minigeração e marcar o que é critério próprio.

## A.1 — PRODIST Módulo 1 (Glossário) [VERIFICADO via PDF, Rev. 9; confirmar Rev. 10]
Definições literais aplicáveis: **2.2 Acessada**, **2.3 Acessantes**, **2.4 Acesso**, **2.44 Central
geradora**, **2.311 Ponto de conexão**, **2.319 Potência instalada em central geradora**.
- **Lacuna:** o glossário **não define** "armazenamento/bateria/BESS" nem "ponto de acoplamento"
  como verbete. A norma deverá criar definição própria (ancorar em Lei 14.300 e IEC 62933).
- **Ressalva:** a definição de minigeração no Mód. 1 Rev. 9 está **desatualizada** (≤3 MW híd./≤5 MW
  demais) — prevalece a **Lei 14.300** (≤5 MW despacháveis / ≤3 MW não despacháveis).

## A.2 — PRODIST Módulo 3 (REN 956/2021, consolidado 11/2024) [VERIFICADO via PDF]

**Tabela 1 — interface por faixa (≤75 / >75–500 / >500–5.000 kW):** acoplamento (nenhum / trafo
com isolação galvânica), seccionamento (disjuntor / chave acessível), interrupção automática,
proteção, **medição bidirecional (≤75 kW) → 4 quadrantes (>75 kW)**.

**Tabela 1-A — funções de proteção (ANSI) por faixa:** 27, 59, 81U, 81O, 25, 62 e **anti-ilhamento**
em todas; 46/47 só p/ máquina síncrona (dispensadas p/ conversor); 50/50N, 51/51N nas faixas.
Tempo de reconexão = **critério da distribuidora** (nota 4).

**Itens 12.2 / 12.2.1 / 12.3 — ÚNICO tratamento direto de SAE no PRODIST:** micro/mini que usa
conversor eletrônico, **incluindo sistema de armazenamento de energia elétrica**, exige **relatório
de ensaio** de conformidade com normas técnicas brasileiras (lab. acreditado Inmetro/ILAC-MRA); na
ausência de norma BR, admite-se norma internacional. [VERIFICADO — transcrição literal]

**Ride-through do conversor (Tabelas 1-B/1-C, REN 1.076/2023):**
- Frequência: **58,5–62,5 Hz → tempo ilimitado**; 57,5–58,5 → 20 s; 57,0–57,5 → 5 s; 62,5–63,0 → 10 s.
- Tensão (pu no ponto CA do conversor): **0,80–1,10 → tempo ilimitado**; 0,5–0,8 → 2,5 s; 0,2–0,5 → 0,5 s; 1,10–1,18 → 1 s.
- **df/dt até 2,0 Hz/s** (item 13-C); **proibida função anti-ilhamento por salto de vetor** para conversores (13-C.2).

**Item 16 — qualidade:** remete ao **Módulo 8** (tensão regime permanente, FP, harmônicos,
desequilíbrio, flutuação, variação de frequência).

**Item 11 — tensão×potência:** "nº de fases e nível de tensão **definidos pela distribuidora** em
função da rede" → **critério da distribuidora**.

**Tabela 2 — proteções de central geradora** (faixas <10 / 10–500 / >500 kW): aplicável se o SAE
for tratado como central geradora (standalone de maior porte).

## A.4 — REN 1.000/2021 — prazos do acesso [VERIFICADO via LegisWeb id=490988]
- Orçamento Estimado: **30 dias** (Art. 56).
- Orçamento Prévio/Parecer: **15 dias** micro <69 kV sem obras; **30 dias** micro com obras; **45
  dias** demais (mini, ≥69 kV) — Art. 64 I/II/III.
- Aprovação pelo consumidor: **10 dias úteis** (Art. 83). Execução de obras rede aérea ≤2,3 kV:
  **60 dias** (Art. 88, I).
- Vistoria + medição: **5 dias úteis** (<2,3 kV) / **10 dias úteis** (≥2,3 e <69 kV) — Art. 91.
- **Art. 19:** a distribuidora deve tratar em suas normas técnicas a conexão de micro/mini,
  observado o Mód. 3 e a REN 1.000 — **base jurídica da nossa norma**.

## A.5 — Lei 14.300/2022 [VERIFICADO via Planalto, curl HTTP 200]
- **Art. 1º:** XI micro ≤75 kW; XIII mini >75 kW (≤5 MW despacháveis / ≤3 MW não despacháveis); **IX
  fontes despacháveis** (FV ≤3 MW **com baterias**, modulação ≥**20%** da geração mensal); **XII
  microrrede** (inclui armazenamento, opera conectada e isolada); I/II autoconsumo local/remoto; X
  geração compartilhada; XIV SCEE.
- **Art. 2º (CHAVE):** distribuidoras/permissionárias **devem atender solicitações de acesso de UC
  com micro/minigeração, COM OU SEM SISTEMA DE ARMAZENAMENTO, bem como sistemas híbridos**. §3º
  formulário-padrão ANEEL; §4º saneamento de vício em **30 dias**.
- **Art. 4º:** garantia de fiel cumprimento (mini): 2,5% (500–<1.000 kW), 5% (≥1.000 kW); micro
  dispensada. **Art. 8º:** responsabilidades financeiras de medição (micro = distribuidora; mini = interessado).

## Lacunas (a fechar antes da norma final)
1. Definição de SAE/BESS inexistente no PRODIST → criar própria.
2. Confirmar Mód. 1 Rev. 10 e Mód. 1 **v12 (REN 1.137/2025)** — hosts ANEEL bloqueados.
3. **Módulo 8** (valores de qualidade) não extraído — transcrever para a seção Qualidade.
4. Texto literal de Arts. 56/83/88 da REN 1.000 (obtidos via LegisWeb) — conferir no PDF oficial.
5. Reclassificar requisitos quando a(s) RN(s) de SAE de 02/06/2026 forem publicadas (ver Frente A).

## Contradições / ressalvas
- Mód. 1 Rev. 9 (espelho) vs Rev. 10/v12 (oficial) — citar a vigente.
- Limite de minigeração: prevalece a **Lei 14.300** sobre o glossário desatualizado.
- Nomenclatura: REN 1.000 "Orçamento Estimado/Prévio" ≡ PRODIST/Lei "parecer de acesso" — padronizar.

## Fontes
Lei 14.300 (planalto.gov.br/.../l14300.htm); PRODIST Mód. 3 (espelho cooperluz.com.br); PRODIST
Mód. 1 Rev. 9 (espelho light.com.br); REN 1.000 (legisweb id=490988); NTC-D-09 CERVAM
(cervam.com.br); PRODIST Mód. 8 v11 (ANEEL, não extraído).
