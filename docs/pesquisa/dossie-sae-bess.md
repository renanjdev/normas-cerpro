# Dossiê de Pesquisa Regulatória — Norma de Conexão de SAE/BESS (CERPRO)

> **Fase 1 (Pesquisa Regulatória) — consolidado das 4 frentes.** Data: **19/06/2026.**
> Frentes: A (marco ANEEL de SAE), B (PRODIST + Lei 14.300), C (benchmark de distribuidoras),
> D (normas técnicas e de segurança). Os outputs brutos estão em `frente-a/b/c/d-*.md`.
> A rastreabilidade requisito→fonte está em `matriz-rastreabilidade.md`.

---

## 1. Sumário executivo (o que a pesquisa mudou no desenho)

1. **Correção de premissa:** a **REN 1.059/2023 não é a norma de armazenamento** — é de
   micro/minigeração (MMGD/SCEE). O marco de SAE é **Lei 15.269/2025** (marco legal) + as **RNs
   aprovadas pela ANEEL em 02/06/2026** (encerrando a CP 39/2023). Nº de processo correto:
   `48500.904885/2020-63`.
2. **O acesso de SAE é direito legal expresso:** Lei 14.300/2022, **Art. 2º** — distribuidoras
   devem atender acesso de UC "com ou sem sistema de armazenamento, bem como sistemas híbridos".
   Esse é o **fundamento jurídico** da norma.
3. **A regulação técnica de conexão na distribuição NÃO está fechada** — duas camadas:
   - **SAE como MMGD/híbrido via conversor:** o **PRODIST Mód. 3 já impõe** ride-through,
     `df/dt`, anti-ilhamento, proibição de salto de vetor e ensaio de conformidade do conversor
     (itens 12.2/12.3, Tabelas 1/1-A/1-B/1-C). → **OBRIGATÓRIO ANEEL hoje.**
   - **SAE autônomo / front-of-meter:** requisitos técnicos delegados ao **ONS/Procedimentos de
     Rede** (NT-ONS DPL 0111/2025, com grid-forming) e, no futuro, ao PRODIST. → ainda em construção.
4. **Tensão×potência é CRITÉRIO DA DISTRIBUIDORA** (PRODIST Mód. 3, item 11) — a norma deve
   **publicar sua própria tabela**. Isso valida a decisão de **arcabouço parametrizado**.
5. **Estado da prática existe e é robusto:** a **CPFL GED-19397** é uma norma **dedicada a SAE**
   (v2.0, 09/12/2025); Neoenergia, Enel, Equatorial e Cemig já tratam BESS dentro das normas de GD.
   Temos modelo de estrutura, proteção, anti-ilhamento, zero-grid e documentação.

**Conclusão de desenho:** a norma da CERPRO será majoritariamente **derivada** (regime de
micro/minigeração + estado da prática + ABNT/IEC/IEEE), com um **núcleo OBRIGATÓRIO ANEEL** pequeno
porém firme, e ampla parcela de **CRITÉRIO DA DISTRIBUIDORA** explicitamente sinalizada.

---

## 2. Status do marco regulatório (o que é exigível hoje)

| Camada | Instrumento | Status (19/06/2026) | Efeito na norma |
|---|---|---|---|
| Legal | **Lei 14.300/2022** | Vigente | Direito de acesso de SAE/híbrido; definições micro/mini; FV+baterias |
| Legal | **Lei 15.269/2025** | Vigente | Reconhece armazenamento como atividade do setor elétrico |
| Regulatório ANEEL (SAE) | **RNs de 02/06/2026** (outorga + transversal) | Aprovadas pela Diretoria; **nº/DOU a confirmar** | Outorga/registro, acesso/uso de rede, tarifação, medição individualizada |
| Regulatório ANEEL (GD) | **REN 1.000/2021 + PRODIST Mód. 1/3/8** | Vigente | Etapas/prazos de acesso, proteção, medição, ride-through do conversor, qualidade |
| Técnico (transmissão) | **Procedimentos de Rede / NT-ONS DPL 0111/2025** | Em elaboração | Grid-forming e requisitos técnicos de SAE (referência prospectiva) |

---

## 3. Obrigatório ANEEL × Critério da distribuidora (o eixo do QA)

**Núcleo OBRIGATÓRIO ANEEL (a norma reproduz/observa, não inventa):**
- Direito de acesso de SAE/híbrido e formulário-padrão (Lei 14.300 Art. 2º).
- Limites de potência micro/mini (Lei 14.300 Art. 1º).
- Etapas e **prazos** do processo de acesso (REN 1.000 Arts. 56, 64, 83, 88, 91).
- Interface mínima por faixa e **funções de proteção** (PRODIST Mód. 3 Tab. 1/1-A).
- **Ride-through** do conversor, `df/dt` ≤ 2,0 Hz/s, **anti-ilhamento**, proibição de salto de
  vetor (PRODIST Mód. 3 Tab. 1-B/1-C, itens 13-A a 13-D).
- **Ensaio de conformidade** do conversor do SAE (PRODIST Mód. 3 itens 12.2/12.3).
- **Medição** bidirecional / 4 quadrantes (PRODIST Mód. 3 Tab. 1; Mód. 5).
- **Qualidade** conforme Módulo 8 (PRODIST Mód. 3 item 16).
- Outorga/registro e medição individualizada do SAE autônomo (RNs 02/06/2026 — confirmar).

**CRITÉRIO DA DISTRIBUIDORA (a norma decide, ancorada em técnica):**
- **Tabela tensão×potência** (Mód. 3 item 11).
- Ajustes de proteção e **tempo de reconexão** (Mód. 3 Tab. 1-A nota 4).
- Modalidades aceitas e regras de **zero-grid / limitação de injeção** (estado da prática).
- Requisitos de **segurança/incêndio**, **ambientais** e de **comissionamento/O&M** (não há norma
  ANEEL específica → ancorar em NFPA 855/UL 9540/IEC 62933-5-2/62619/63056 e CONAMA/PNRS).
- Telemetria/supervisão (fora do escopo v1).

---

## 4. Insumos por seção da norma

| Seção da norma | Principais insumos (fonte) |
|---|---|
| Objetivo / campo de aplicação | Lei 14.300 Art. 2º; REN 1.000 Art. 19; CPFL GED-19397 (escopo) |
| Definições/siglas | PRODIST Mód. 1; Lei 14.300 Art. 1º; IEC 62933-1 (criar verbete de SAE) |
| Modalidades de SAE | CPFL GED-19397 (SAE sem GD/zero-grid; híbrido on-grid; off-grid); Frente A (BTM/FTM/autônomo/colocalizado) |
| Requisitos por porte/tensão | PRODIST Mód. 3 Tab. 1 (faixas 75/500/5.000 kW); tabela tensão×potência própria (modelo CERVAM) |
| Proteção e controle (incl. anti-ilhamento) | PRODIST Mód. 3 Tab. 1-A; CPFL (ANSI 50/51/67/27/59/81/25; ≤2 s; intertravamento 0,7 pu); IEEE 1547 |
| FRT + controle P/Q (4 quadrantes) | PRODIST Mód. 3 Tab. 1-B/1-C; IEEE 1547 Cl.5/6 (Volt-VAR/Volt-Watt, LVRT/HVRT, droop) |
| Qualidade de energia | PRODIST Mód. 8 (transcrever valores); IEEE 519/1453; injeção CC <0,5% |
| Medição | PRODIST Mód. 3 Tab. 1 + Mód. 5; bidirecional/4 quadrantes; medição individualizada (SAE autônomo) |
| Segurança e incêndio | NFPA 855 (afastamento 3 ft), UL 9540/9540A, IEC 62933-5-2:2025, IEC 62619/63056; CPFL 6.3 (BMS/PCS/EMS) |
| Exigências ambientais | CONAMA 237/1997 (licenciamento, em regra estadual); Lei 12.305/2010 + Dec. 10.936/2022 + CONAMA 401/2008 (logística reversa) |
| Comissionamento, ensaios e O&M | IEEE 1547.1-2020; IEC 62933-2-2/3-1; ensaio de conformidade do conversor (Mód. 3 12.2) |
| Solicitação de acesso (etapas/prazos) | REN 1.000 Arts. 56/64/83/88/91; estrutura Cemig ND-5.31 / Equatorial NT.020 |
| Documentação exigida | ART/TRT; unifilar; memorial; formulário de dados do SAE; certificação/registro INMETRO; declaração zero-grid (CPFL Anexo B; Neoenergia Termo Zero Grid) |
| Responsabilidades / acordo operativo | Lei 14.300 Arts. 4º/8º; CPFL (Responsabilidades Adicionais / Relacionamento Operacional) |
| Anexos | Diagramas de paralelismo bateria/rede BT/MT (Enel Anexos C/E); formulários; placas (CPFL Anexo C); matriz de rastreabilidade |

---

## 5. Estado da prática (benchmark — síntese)

- **CPFL GED-19397** (dedicada a SAE): modalidades **SAE sem GD (zero-grid)** e **híbrido on-grid**;
  proteção por porte (>75 kW trafo de acoplamento; >300 kW religador); **anti-ilhamento ≤2 s**,
  intertravamento a **0,7 pu**; segurança (BMS/PCS/EMS, DPS, aterramento); formulário de dados da
  bateria; referências IEC 62619/62620/62933-5-1.
- **Neoenergia DIS-NOR-031:** subseção **7.13 SCRPI** (controle de redução de injeção com BESS) +
  **Termo Zero Grid**.
- **Enel:** diagramas de **paralelismo permanente bateria/rede** (BT e MT).
- **Cemig / Equatorial:** bateria como atributo do projeto de GD (FV despachável, modulação ≥20%).
- **Convergências:** base REN 1.000 + PRODIST 1/3/8; etapas de acesso padronizadas; ART + unifilar +
  memorial + formulário; proteção escalonada por porte; anti-ilhamento obrigatório; medição
  bidirecional; INMETRO de inversores.
- **Estrutura consolidada sugerida:** ver `frente-c-benchmark-distribuidoras.md` (seções 1–18).

---

## 6. Lacunas e itens a verificar manualmente (antes de publicar)

| # | Item | Caminho de verificação |
|---|---|---|
| 1 | Número/DOU das RNs de SAE de 02/06/2026 | in.gov.br (DOU Seção 1, 03–18/06/2026); cedoc/ANEEL |
| 2 | Texto integral da NT 03/2026 e da Lei 15.269/2025 | gov.br/aneel; planalto.gov.br |
| 3 | **NT-ONS DPL 0111/2025** (grid-forming/requisitos técnicos) | ons.org.br |
| 4 | PRODIST **Mód. 1 v12 (REN 1.137/2025)** e **Mód. 8 v11** (valores de qualidade) | cedoc/git.aneel (estavam fora do ar) |
| 5 | Texto literal REN 1.000 Arts. 56/83/88 (obtidos via LegisWeb) | PDF oficial ANEEL |
| 6 | Cláusulas/edições 2026: NFPA 855, UL 9540A 6ª ed.; ROCOF e curva de FP do IEEE 1547 | textos integrais adquiridos IEEE/IEC/NFPA/UL |
| 7 | Energisa (NDU-013/015) e Copel (NTC 905200) — bloqueados | download manual |

> **Regra de citação:** nenhum número de RN, artigo de lei ou cláusula técnica entra na minuta sem
> verificação humana sobre fonte primária. Itens [NÃO CONFIRMADO] na matriz não podem virar texto
> normativo definitivo até serem fechados.

---

## 7. Recomendações para as próximas fases

1. **Materiais da CERPRO (necessários p/ a Fase 3):** normas internas existentes e seu **padrão de
   numeração**; **níveis de tensão e características da rede** (BT/MT, curto-circuito, capacidade de
   hospedagem); padrões de medição; modelos de ART/acordo operativo.
2. **Fechar as lacunas críticas** #1 e #3 (RNs de SAE + NT-ONS) — são as que mais mudam o conteúdo.
3. **Adotar a estrutura consolidada** da Frente C como esqueleto da minuta.
4. **Parametrizar** todos os valores que são critério da distribuidora (tabela tensão×potência,
   ajustes/tempos de reconexão, afastamentos de segurança) como campos a cravar pela engenharia.

---

## 8. Fontes primárias-chave
- Lei 14.300/2022 — planalto.gov.br/.../l14300.htm
- PRODIST Mód. 3 (REN 956/2021, consolid. 11/2024) — espelho cooperluz.com.br
- PRODIST Mód. 1 (Rev. 9) — espelho light.com.br
- REN 1.000/2021 — legisweb id=490988
- NT Conjunta 13/2025-ANEEL — apine.com.br/.../NI1415a08.pdf
- ANEEL, notícias 02/06/2026 e 02/04/2026 — gov.br/aneel
- GESEL/UFRJ TDSE-155 — gesel.ie.ufrj.br
- CPFL GED-19397 — sites.cpfl.com.br/documentos-tecnicos/GED-19397.pdf
- IEEE 1547-2018/.1-2020; IEC 62933 (série); NFPA 855; UL 9540/9540A; IEC 62619/63056
- CONAMA 237/1997 e 401/2008; Lei 12.305/2010 + Decreto 10.936/2022

(URLs completas e status de verificação nos arquivos `frente-*.md` e na matriz.)
