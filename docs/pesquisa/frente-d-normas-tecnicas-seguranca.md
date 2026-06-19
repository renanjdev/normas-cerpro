# FRENTE D — Normas técnicas e de segurança aplicáveis à CONEXÃO de SAE/BESS

> Data: **19/06/2026**. Alimenta os módulos: **ambiental, segurança/incêndio, FRT+controle P/Q,
> comissionamento/O&M**.
>
> **Nota de método:** páginas de produto IEEE/IEC/NFPA/UL confirmam título, edição, ano e escopo,
> mas raramente o texto das cláusulas (paywall). Valores numéricos do IEEE 1547 foram extraídos
> verbatim do **NRECA Guide to IEEE 1547-2018 (mar/2019)** — fonte secundária autorizada que cita
> as cláusulas/tabelas do standard. Marcados como tal.

---

## 1) IEEE 1547-2018 e IEEE 1547.1-2020

**IEEE Std 1547-2018** — *Interconnection and Interoperability of DER* (06/04/2018).
**IEEE Std 1547.1-2020** — *Conformance Test Procedures* (21/05/2020).

- **Categorias de regulação de tensão/reativos: A e B** (B = alta penetração/saída variável → caso BESS). [NREL/NRECA Cl.5].
- **Categorias de ride-through: I, II, III** (II alinhada à NERC PRC-024-2; III p/ redes de baixa inércia). [NRECA Cl.6.4].
- **Tensão (LVRT/HVRT):** proíbe trip na região de operação contínua; **faixa contínua 0,88–1,10 pu**; zonas contínua/mandatory/permissive/momentary cessation/trip. [NRECA Cl.6.4].
- **Frequência (ride-through, iguais p/ as 3 categorias) — setpoints de trip default:** OF2 **62,0 Hz** (0,16 s); OF1 **61,2 Hz** (300 s); UF1 **58,5 Hz** (300 s); UF2 **56,5 Hz** (0,16 s). Exige **ride-through de ROCOF** e de **salto de ângulo de fase**; **frequency droop** (resposta P–f) obrigatório. [NRECA Cl.6.5]. Valor de ROCOF (Hz/s) [NÃO CONFIRMADO].
- **Controle P/Q e FP (4 quadrantes):** capacidade de constant power factor, **Volt-VAR**, **Volt-Watt** e constant reactive power; default = FP unitário. [NREL/Keentel + NRECA Cl.5]. Faixa exata de FP / curva de reativos [NÃO CONFIRMADO].
- **Qualidade:** injeção CC **< 0,5% da corrente nominal** [VERIFICADO]; harmônicos por **IEEE 519**, flicker por **IEEE 1453**.
- **Anti-ilhamento:** detectar e desenergizar ilha não intencional em **≤ 2 s**. [VERIFICADO verbatim].
- **Comissionamento/ensaios:** **IEEE 1547.1-2020** define ensaios type/production/commissioning/periodic. [VERIFICADO].

Fontes: standards.ieee.org/ieee/1547/5915; docs.nrel.gov/docs/fy20osti/75436.pdf; NRECA Guide
(cooperative.com); ieeexplore 9097534; keentelengineering.com (injeção CC/IEEE 519).
**Alimenta:** FRT, controle P/Q e FP, qualidade, comissionamento/O&M.

## 2) Série IEC 62933 — Electrical Energy Storage (EES) Systems

| Parte | Título | Ed./Ano | Cobre |
|---|---|---|---|
| 62933-1 | Vocabulary | 2018 (subst. por 2024) | Terminologia (parâmetros, ensaios, planejamento, instalação, segurança, ambiental) |
| 62933-2-1 | Unit parameters and testing – General | 2017/2018 (+Cor.1:2019) | Parâmetros de unidade; medição no POC |
| 62933-2-2 (TS) | Application and performance testing | 2022 | Ensaios de aplicação/desempenho, duty cycles |
| 62933-3-1 | Planning and performance assessment | 2025 | Planejamento, dimensionamento, operação, manutenção |
| 62933-5-1 (TS) | Safety – General | 2017 | Segurança geral de EES integrado à rede |
| **62933-5-2** | **Safety – Electrochemical systems** | **Ed.2.0 2025 (09/12/2025)** | **Segurança específica de BESS eletroquímico** (núcleo da seção de segurança) |

**Alimenta:** definições (62933-1), comissionamento/desempenho (2-1, 2-2, 3-1), **segurança** (5-1, **5-2**).

## 3) ABNT NBR 16690:2019
*Instalações elétricas de arranjos fotovoltaicos — Requisitos de projeto* (out/2019). Cobre o
**lado CC do arranjo FV** (condutores CC, fusíveis de string, seccionamento, aterramento, DPS,
1500 Vcc). **Exclui explicitamente** dispositivos de armazenamento/inversor. Relevante para
**PV+BESS DC-coupled** (barramento CC do gerador), **não cobre o BESS**. Correlatas: NBR 5410,
5419, 16149/16150 (interface FV à rede). [VERIFICADO via fontes técnicas; cláusulas NÃO CONFIRMADAS].
**Alimenta:** segurança elétrica CC / comissionamento (PV+armazenamento).

## 4) Segurança/incêndio de BESS

- **NFPA 855** — *Installation of Stationary Energy Storage Systems*. Ed. **2023** [VERIFICADO
  verbatim, TIA]; **ed. 2026** vigente (corroborada). Requisitos verbatim (ed. 2023): **separação
  mínima de 3 ft (914 mm) entre unidades ESS** salvo justificativa por UL 9540A (§15.3.1);
  avaliação por pessoa qualificada (§15.12). HMA, detecção/supressão, controle de explosão,
  ventilação, sinalização, siting [NÃO CONFIRMADO valores].
- **UL 9540** — *Energy Storage Systems and Equipment*. Ed.3, 28/06/2023 (rev. 03/2025).
  **Certificação no nível de sistema**. Exclui a instalação (regida pelo NFPA 855). [VERIFICADO].
- **UL 9540A** — *Test Method for Thermal Runaway Fire Propagation in BESS*. **5ª ed., 12/03/2025**
  [VERIFICADO]; 6ª ed. (2026) [NÃO CONFIRMADO]. Multinível célula→módulo→unidade→instalação;
  **subsidia as distâncias do NFPA 855**.
- **IEC 62619:2022** — segurança de células/baterias de lítio industriais (inclui EES). [VERIFICADO].
- **IEC 63056:2020 (+Cor.1:2021)** — *product safety* de baterias de lítio para EES, máx. 1500 Vcc;
  requisitos adicionais sobre a base da 62619. [VERIFICADO]. Cláusulas detalhadas [NÃO CONFIRMADO].

**Alimenta:** segurança/incêndio (afastamentos, supressão, ventilação, sinalização) e comissionamento/O&M.

## 5) Exigências AMBIENTAIS no Brasil

- **Licenciamento — Res. CONAMA 237/1997** (verbatim): prévio licenciamento (Art. 2º); **LP → LI →
  LO** (Art. 8º); competência **federal/IBAMA** (Art. 4º) só em impacto nacional/regional/UC
  federal/terra indígena; caso contrário **estadual** (Art. 5º). → BESS conectado é em regra
  **licenciamento estadual**; consultar órgão ambiental estadual. [VERIFICADO verbatim].
- **Logística reversa — Lei 12.305/2010 (PNRS):** **Art. 33, II** obriga fabricantes/importadores/
  distribuidores/comerciantes de **pilhas e baterias** a estruturar logística reversa. Regulamento:
  **Decreto 10.936/2022**. [VERIFICADO verbatim].
- **Res. CONAMA 401/2008** (verbatim): limites de Pb/Cd/Hg, recebimento pelo comércio (Art. 4º),
  destinação de responsabilidade do fabricante/importador (Art. 6º), proibição de disposição
  inadequada (Art. 22); alterada pela **CONAMA 424/2010** (conteúdo NÃO CONFIRMADO). [VERIFICADO verbatim].

**Alimenta:** ambiental (licenciamento da instalação; logística reversa/descarte das baterias).

## Mapa "tema técnico → norma de referência" (para a seção Referências)

| Tema | Norma(s) |
|---|---|
| Interconexão DER / categorias | IEEE 1547-2018 |
| LVRT/HVRT | IEEE 1547-2018 Cl.6.4 |
| Ride-through de freq. + ROCOF + droop | IEEE 1547-2018 Cl.6.5 |
| Controle P/Q, FP, Volt-VAR/Volt-Watt | IEEE 1547-2018 Cl.5 |
| Anti-ilhamento (≤ 2 s) | IEEE 1547-2018 |
| Qualidade (harmônicos/flicker/CC) | IEEE 1547-2018 + IEEE 519 + IEEE 1453 |
| Comissionamento/ensaios | IEEE 1547.1-2020 |
| Terminologia EES | IEC 62933-1 |
| Parâmetros/ensaios/planejamento | IEC 62933-2-1 / -2-2 / -3-1 |
| Segurança EES (geral / BESS) | IEC 62933-5-1 / **62933-5-2:2025** |
| Segurança baterias de lítio | IEC 62619:2022 / IEC 63056:2020 |
| Instalação/incêndio (afastamentos, supressão, siting) | **NFPA 855** |
| Certificação do sistema BESS | UL 9540 (Ed.3:2023) |
| Propagação de thermal runaway (ensaio) | UL 9540A (5ª ed.:2025) |
| Projeto CC do arranjo FV (PV+BESS) | ABNT NBR 16690:2019 (+ 5410, 5419) |
| Conexão FV à rede (interface/ensaios) | ABNT NBR 16149 / 16150 |
| Licenciamento ambiental (LP/LI/LO) | Res. CONAMA 237/1997 (em regra estadual) |
| Logística reversa / descarte de baterias | Lei 12.305/2010 (Art. 33, II) + Decreto 10.936/2022 + CONAMA 401/2008 |

**Recomendação:** números de cláusula, ROCOF/curva de FP e edições 2026 (NFPA 855 / UL 9540A 6ª
ed.) devem ser confirmados sobre os textos integrais adquiridos antes da publicação da norma.

## Lacunas
1. Números de cláusula das IEC 62619/63056, 62933-5-x, NFPA 855 (exceto §15.3.1/15.12), NBR 16690.
2. IEEE 1547: valor de ROCOF (Hz/s); faixa exata de FP/curva de reativos; faixa contínua de frequência.
3. Edição vigente NFPA 855 (2026) e UL 9540A 6ª ed. — texto não extraído.
4. IEC 62933-2-1 (confirmado via search, não fetch).
5. CONAMA 424/2010 (alteração da 401); texto da Lei 15.269/2025 e número da REN de SAE.
