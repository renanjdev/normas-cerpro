# NRM-0001 — Norma de Conexão de Sistemas de Armazenamento de Energia (SAE/BESS) — ESTRUTURA ANOTADA

| Campo | Conteúdo |
|---|---|
| **Identificador** | NRM-0001 |
| **Versão** | 0.1 (estrutura anotada — pré-redação) |
| **Estado** | Rascunho |
| **Responsável** | Squad de Normas — CERPRO |
| **Base** | `docs/pesquisa/dossie-sae-bess.md` + `matriz-rastreabilidade.md` |

> **O que é este documento:** o **esqueleto anotado** da futura minuta. Cada seção traz: *objetivo*,
> *conteúdo previsto*, *fontes* (IDs `R-xx` da matriz de rastreabilidade), *classificação*
> (🟦 OBR = obrigatório ANEEL/lei · 🟨 CRIT = critério da distribuidora · ⬜ REF = referência técnica)
> e **`«PARÂMETRO»`** = valor a ser cravado pela engenharia da CERPRO. Aprovado este índice, redige-se
> o corpo. Nada marcado `[NÃO CONFIRMADO]` na matriz vira texto definitivo sem verificação humana.

---

## 1. Objetivo  🟦
- **Conteúdo:** estabelecer critérios e procedimentos para conexão de SAE/BESS ao sistema de
  distribuição da CERPRO, em BT e MT, isolados ou associados a geração.
- **Fontes:** R-01 (Lei 14.300 Art. 2º), R-29 (REN 1.000 Art. 19).

## 2. Campo / Âmbito de Aplicação  🟦🟨
- **Conteúdo:** a quem se aplica (acessantes com SAE, com/sem GD, sistemas híbridos); o que fica de
  fora (`«definir: SAE de grande porte / front-of-meter como central geradora?»`); faixas de
  potência cobertas.
- **Parâmetros:** `«faixa de potência/porte coberta pela norma»`.
- **Fontes:** R-01, R-04, R-05, R-07.

## 3. Referências  🟦⬜
- **Conteúdo:** Lei 14.300/2022; Lei 15.269/2025 `[verificar]`; REN ANEEL de SAE de 02/06/2026
  `[nº/DOU a confirmar — R-45/R-48]`; REN 1.000/2021; PRODIST Mód. 1/3/5/8; ABNT NBR 16690/16149/16150/5410/5419;
  IEC 62933 (série), IEC 62619, IEC 63056; IEEE 1547/1547.1, IEEE 519/1453; NFPA 855; UL 9540/9540A;
  CONAMA 237/1997 e 401/2008; Lei 12.305/2010 e Dec. 10.936/2022; Procedimentos de Rede/NT-ONS DPL
  0111/2025 `[prospectivo]`.
- **Fontes:** mapa "tema → norma" em `frente-d` e `dossie §8`.

## 4. Definições e Siglas  🟦🟨
- **Conteúdo:** importar verbetes do PRODIST Mód. 1 (acessante, acessada, ponto de conexão, central
  geradora); **criar definição própria de SAE/BESS** (ancorar em Lei 14.300 Art. 1º IX/XII e IEC
  62933-1) — não existe verbete no PRODIST. Siglas: SAE, BESS, BMS, PCS, EMS, PCC, SoC, etc.
- **Fontes:** R-10, R-11.

## 5. Responsabilidades  🟦🟨
- **Conteúdo:** acessante, responsável técnico (RT), distribuidora; garantias e responsabilidades
  financeiras de medição.
- **Fontes:** R-08, R-09; benchmark (CPFL "Responsabilidades Adicionais").

## 6. Modalidades de SAE  🟨
- **6.1 SAE sem GD ("junto à carga" / zero-grid)** — back-up, UPS, reativos, arbitragem; **injeção
  ativa proibida** salvo arranjo autorizado.
- **6.2 SAE híbrido on-grid (SAE + MMGD)** — injeção conforme orçamento de conexão.
- **6.3 Modos operacionais** — on-grid / off-grid (ilha interna com intertravamento).
- **Parâmetros:** `«modalidades aceitas pela CERPRO»`, `«limites de injeção por modalidade»`.
- **Fontes:** R-06, R-07, R-31, R-32 (CPFL GED-19397; Neoenergia SCRPI/Termo Zero Grid).

## 7. Requisitos técnicos por porte e tensão  🟦🟨
- **7.1 Faixas de potência** (limites legais): micro ≤75 kW; mini >75 kW (≤5 MW despach./≤3 MW não
  despach.) — **OBR**.
- **7.2 Tabela tensão×potência da CERPRO** — **CRIT**: publicar tabela própria (modelo CERVAM).
  - **Parâmetros:** `«kW → nº de fases / nível de tensão BT/MT»`, `«limite de potência por ponto»`,
    `«capacidade de hospedagem por alimentador»`.
- **7.3 Interface mínima por faixa** (acoplamento/seccionamento/interrupção/proteção/medição) — Tab. 1.
- **Fontes:** R-04, R-05, R-12, R-19, R-21, R-22.

## 8. Proteção, seccionamento e manobra  🟦🟨⬜
- **8.1 Funções de proteção (ANSI) por faixa** — Tab. 1-A (27/59/81O/81U/25/62/anti-ilhamento; 50/51,
  50N/51N, 67, 32, 59N conforme porte).
- **8.2 Anti-ilhamento e intertravamento** — desconexão ≤ `«2 s»`; intertravamento a `«0,7 pu»`;
  **proibido salto de vetor** (conversores); vedada operação em ilha da rede.
- **8.3 Acoplamento e manobra por porte** — trafo de interface >75 kV; religador acima de
  `«300 kW»`; DSV lacrável.
- **Parâmetros:** `«ajustes de proteção»`, `«tempo de reconexão»` (CRIT — Tab. 1-A nota 4).
- **Fontes:** R-13, R-17, R-18, R-23, R-30; IEEE 1547; CPFL.

## 9. Suportabilidade (FRT) e controle P/Q  🟦⬜
- **9.1 Ride-through** — frequência (58,5–62,5 Hz tempo ilimitado) e tensão (0,80–1,10 pu) por
  Tab. 1-B/1-C; `df/dt ≤ 2,0 Hz/s`.
- **9.2 Controle de potência ativa/reativa (4 quadrantes)** — Volt-VAR, Volt-Watt, FP, frequency
  droop — IEEE 1547 Cl. 5/6 (REF; ajustes a `«definir»`).
- **Parâmetros:** `«modos P/Q exigidos por porte»`, `«faixa de FP»`.
- **Fontes:** R-15, R-16, R-34, R-35.

## 10. Qualidade de energia  🟦⬜
- **Conteúdo:** valores do **PRODIST Módulo 8** (tensão regime permanente, FP, DTT/harmônicos,
  desequilíbrio, flutuação, variação de frequência) `[transcrever — R-20 NC]`; injeção CC <0,5%;
  harmônicos IEEE 519, flicker IEEE 1453.
- **Fontes:** R-20, R-36.

## 11. Medição  🟦🟨
- **Conteúdo:** bidirecional (≤75 kW) / 4 quadrantes (>75 kW); PRODIST Mód. 5; medição
  individualizada (SAE autônomo) `[R-45 a confirmar]`; medição direta/indireta (TC) por porte.
- **Parâmetros:** `«padrão de medição da CERPRO por porte»`.
- **Fontes:** R-19, R-45.

## 12. Segurança e prevenção/combate a incêndio  🟨⬜
- **Conteúdo:** BMS/monitoramento e alarme; PCS/EMS; afastamentos (NFPA 855 — `«3 ft / valor»`);
  detecção/supressão; ventilação/controle de explosão; sinalização/placas; aterramento (NBR
  5410/15751) e DPS (NBR 5419). Referências IEC 62933-5-2:2025, IEC 62619/63056, UL 9540/9540A.
- **Parâmetros:** `«afastamentos»`, `«requisitos de sala/abrigo»`, `«exigência de ensaio UL 9540A»`.
- **Fontes:** R-39, R-40, R-41; CPFL 6.3.

## 13. Exigências ambientais  🟦
- **Conteúdo:** licenciamento ambiental (LP/LI/LO — em regra estadual; consultar órgão estadual);
  logística reversa/descarte das baterias (Lei 12.305/2010 Art. 33 II + Dec. 10.936/2022 + CONAMA
  401/2008).
- **Fontes:** R-42, R-43.

## 14. Comissionamento, ensaios e O&M  🟦⬜
- **Conteúdo:** ensaio de conformidade do conversor (PRODIST Mód. 3 12.2/12.3 — lab. Inmetro/ILAC);
  ensaios de comissionamento (IEEE 1547.1); vistoria para energização; requisitos de O&M e
  condições de desconexão/religamento (IEC 62933-2-2/3-1).
- **Parâmetros:** `«roteiro de comissionamento/vistoria da CERPRO»`.
- **Fontes:** R-14, R-37, R-38.

## 15. Solicitação de acesso — etapas e prazos  🟦
- **Conteúdo:** fluxo consulta → orçamento estimado (30 d) → solicitação → orçamento prévio/parecer
  (15/30/45 d) → aprovação (10 du) → contrato/acordo operativo → obras (60 d) → vistoria+medição
  (5/10 du) → energização. Saneamento de vício: 30 d.
- **Fontes:** R-03, R-24, R-25, R-26, R-27, R-28; estrutura Cemig ND-5.31 / Equatorial NT.020.

## 16. Documentação exigida  🟦🟨
- **Conteúdo:** ART/TRT (projeto e execução); diagrama unifilar; memorial descritivo; **formulário
  de dados do SAE** (tecnologia, kW, kWh, tensão, finalidade, carga/descarga); certificação/registro
  INMETRO (Port. 140/2022); declaração zero-grid / limitação de injeção; placas de advertência;
  formulário-padrão (vedado exigir além — Lei 14.300 Art. 2º §3º).
- **Parâmetros:** `«formulário/anexos oficiais da CERPRO»`.
- **Fontes:** R-02, R-14, R-44.

## 17. Responsabilidades adicionais / Acordo Operativo / Relacionamento Operacional  🟨
- **Conteúdo:** instrumentos pós-aprovação por modalidade/porte (espelho CPFL/Cemig).
- **Fontes:** benchmark (Frente C).

## 18. Disposições transitórias e vigência  🟨
- **Conteúdo:** vigência (`«prazo, ex.: 120 dias»`), regras de transição, revisão e revogação.
- **Parâmetros:** `«vigência e regime de transição»`.

## Anexos
- **A.** Arranjos e diagramas de referência (BT/MT; paralelismo permanente bateria/rede) — modelo Enel.
- **B.** Formulário de solicitação / dados técnicos do SAE — modelo CPFL Anexo B.
- **C.** Placas de advertência — modelo CPFL Anexo C.
- **D.** Lista de normas técnicas e de segurança de referência.
- **E.** Matriz de rastreabilidade (`docs/pesquisa/matriz-rastreabilidade.md`).

---

## Lista de parâmetros a cravar (resumo para a engenharia da CERPRO)
1. Tabela tensão×potência (kW → fases/tensão BT-MT) e capacidade de hospedagem.
2. Modalidades aceitas e limites de injeção por modalidade.
3. Ajustes de proteção e tempo de reconexão.
4. Limiar de potência para religador/trafo de acoplamento.
5. Modos de controle P/Q exigidos por porte e faixa de FP.
6. Padrão de medição por porte.
7. Afastamentos e requisitos de abrigo/segurança; exigência de ensaio UL 9540A.
8. Roteiro de comissionamento/vistoria.
9. Formulários e anexos oficiais.
10. Vigência e regime de transição.

## Itens regulatórios a fechar (verificação humana)
Número/DOU das RNs de 02/06/2026 (R-45/R-48) · NT-ONS DPL 0111/2025 (R-47) · valores do PRODIST
Módulo 8 (R-20) · cláusulas/edições 2026 NFPA 855/UL 9540A (R-40).
