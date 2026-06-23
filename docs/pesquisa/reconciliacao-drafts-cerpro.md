# Reconciliação — Drafts reais da CERPRO × Estrutura NRM-0001

| Campo | Conteúdo |
|---|---|
| **Data** | 2026-06-19 |
| **Fontes novas** | `docs/fontes-cerpro/NTC-D-XX_BESS_v01-2026_R0.md` · `docs/fontes-cerpro/NT-BESS-001-2026_normas-internas.md` |
| **Comparado com** | `rascunhos/NRM-0001-conexao-sae-bess/NRM-0001-estrutura-anotada.md` |

## 1. O que chegou
A CERPRO já possui **dois documentos próprios e avançados**, que passam a ser a **linha de base** (substituem o pressuposto de "seguir com placeholders genéricos"):

1. **`NTC-D-XX` (v01/2026 R0)** — *norma técnica*. Tom explicativo/didático. Seções 1–9 redigidas:
   apresentação, hierarquia **ESS×BESS** (escopo restrito a baterias eletroquímicas), campo de
   aplicação, objetivo, referências **comentadas** (ANEEL, ABNT, IEC, IEEE, NFPA/UL, NRs),
   responsabilidades, ~60 definições, critérios BT/MT, modos on/off-grid, requisitos
   ambientais/segurança/QEE/O&M/descarte, fluxo de acesso (13 etapas) e **proteção** com tabelas
   ANSI, FRT (LVRT/frequência), transformador de acoplamento, anti-ilhamento, aterramento.
   → **Inacabada**: termina em 9.2.9; faltam tabelas preenchidas (3,4,5,6) e os Anexos A–K citados.

2. **`NT-BESS-001/2026`** — *norma regulatória/administrativa* em formato de **artigos**, com:
   Acordo Operativo (modelo), **Anexo IV** (proteções mínimas — lista ANSI 27/59/81/50/51/67/32/25/46/47/50N-51N/64),
   **Matriz de Responsabilidades**, **Procedimentos de Emergência** (thermal runaway, incêndio,
   ambiental), e **Manual MP-BESS-001** (classificação **Classe A–D**, comitê interno, 10 etapas de
   análise com pareceres técnico/regulatório/operacional/jurídico).

## 2. Como se relacionam (e com o NRM-0001)
Há **três artefatos cobrindo o mesmo tema** → risco de sobreposição e conflito. Recomendação de papéis:

| Papel | Documento | Observação |
|---|---|---|
| **Norma técnica** (corpo principal) | NTC-D-XX | Mais completa e melhor estruturada. Deve ser a **base do corpo**. |
| **Camada administrativa/jurídica + anexos operativos** | NT-BESS-001 + MP-BESS | Vira **anexos/processo** da norma técnica (Acordo Operativo, Matriz de Responsabilidades, fluxo interno, emergências). |
| **Esqueleto/checklist de cobertura** | NRM-0001 (nosso) | Deixa de ser "minuta paralela": vira **mapa de conformidade** para auditar lacunas do NTC-D-XX. |

> **Decisão de método:** parar de redigir uma minuta nova do zero. Passar a **completar e revisar o
> NTC-D-XX**, usando o NRM-0001 como checklist e a matriz de rastreabilidade para validar fontes.

## 3. NTC-D-XX cobre o que faltava no nosso esqueleto — e vice-versa
**Pontos fortes do NTC-D-XX (adotar):**
- Distinção ESS×BESS e recorte de escopo explícito (resolve a indefinição de "porte/front-of-meter").
- Referências comentadas, com a **NBR 17153:2023** como espinha dorsal (não tínhamos destacado).
- Tabelas de proteção ANSI por BT/MT, FRT, transformador Dyn, anti-ilhamento por função 78.
- Fluxo de acesso já com prazos concretos (5 du análise; 15/30/45 d OC; vistoria 5/10 du).

**Lacunas a fechar no NTC-D-XX (do nosso checklist + leitura):**
1. **Tabelas vazias** — Tab. 3 (interface BT), Tab. 4 (ANSI MT), Tab. 5 (LVRT), Tab. 6 (frequência), Tab. do 9.1.1 (ajustes BT). *Parâmetros da CERPRO.*
2. **Anexos citados e ausentes** — A (arranjos), B (memorial/dados), C (placas), D (certificações), H (placa DSV), K (coordenação). O NT-BESS-001 já traz **modelos** de vários (Acordo Operativo, checklist, declaração de não exportação) → migrar.
3. **Seção 9 incompleta** (corta em 9.2.9) — faltam QEE detalhada, medição, comissionamento/ensaios e disposições finais/vigência como articulado normativo.
4. **Numeração de seções duplicada** no R0 (vários "7.4"; "9.1/9.2" ok) — corrigir.
5. **Erros de redação** a sanear: "BESS cem Geração" (7.2 título); definição **6.35-A** diz "BESS é equivalente de ESS" mas escreve BESS (troca SAE↔BESS) — **revisar toda a dualidade SAE/ESS/BESS**, hoje inconsistente.
6. **Conflito de exigência** entre os dois docs a resolver:
   - NTC-D-XX: anti-ilhamento por **função 78 (salto de vetor)** como primário em MT.
     ⚠️ Mas o nosso dossiê/benchmark aponta **vedação de salto de vetor** em conversores (CPFL) — **checar com a engenharia** qual regra a CERPRO adota.
   - NT-BESS-001 lista **ANSI 78 não**, mas exige **anti-exportação dedicada com redundância**; NTC-D-XX fala em "não injeção"/Zero-Grid. Alinhar terminologia (anti-exportação × LPI/SCRPI × Zero-Grid).
   - Retenção de registros: NT-BESS-001 diz **60 meses**; Acordo Operativo diz **5 anos**. (Equivalente, padronizar texto.)

## 4. Itens do NT-BESS-001/MP-BESS a incorporar (não existiam no NTC-D-XX nem no NRM-0001)
- **Classificação de complexidade A–D** e **Comitê Interno BESS** (governança de aprovação).
- **Matriz de Responsabilidades** detalhada (projeto, equipamentos, operação, ambiental, trabalhista, regulatório).
- **Procedimentos de Emergência** (passos 1–7; thermal runaway; comunicação a Bombeiros/Defesa Civil; investigação de incidentes em 30 d; **seguro** obrigatório).
- **Acordo Operativo** como instrumento obrigatório de energização.
- **Critérios de indeferimento técnico** da conexão.

## 5. Pontos que exigem verificação humana (não cravar sozinho)
- Regra de **anti-ilhamento** (salto de vetor permitido vs. vedado).
- **Valores das tabelas** de ajuste (BT/MT/FRT) — parâmetros da CERPRO.
- Exigência de **seguro** e de **AVCB** (NT-BESS-001) — confirmar se entram como obrigatório geral.
- Citações regulatórias a confirmar: **REN ANEEL 956/2021** ("Procedimentos de Distribuição" — verificar nº, no NTC-D-XX), RN de SAE de 2026, **Lei 15.269/2025**.
