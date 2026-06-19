# Matriz de Rastreabilidade — Norma de Conexão de SAE/BESS (CERPRO)

> Cada requisito previsto da norma → **fonte** → **tipo** (Obrigatório ANEEL / Critério da
> distribuidora / Referência técnica) → **status de verificação** → **seção da norma**.
> Atualize a cada fase. Itens **[NÃO CONFIRMADO]** não podem virar texto normativo definitivo sem
> verificação humana sobre fonte primária.

**Legenda — Tipo:** `OBR` = Obrigatório ANEEL/lei · `CRIT` = Critério da distribuidora · `REF` =
Referência técnica (ABNT/IEC/IEEE/NFPA/UL).
**Legenda — Verificação:** `V` = verificado via fetch de fonte primária/espelho idêntico ·
`P` = parcial (paráfrase/secundária) · `NC` = não confirmado.

| ID | Requisito / tema | Fonte | Tipo | Verif. | Seção |
|----|------------------|-------|------|:-----:|-------|
| R-01 | Direito de acesso de UC com/sem SAE e sistemas híbridos | Lei 14.300/2022, Art. 2º, caput | OBR | V | Objetivo / Campo de aplicação |
| R-02 | Formulário-padrão; vedado exigir docs além do formulário | Lei 14.300, Art. 2º §3º | OBR | V | Documentação |
| R-03 | Saneamento de vício formal em 30 dias | Lei 14.300, Art. 2º §4º | OBR | V | Solicitação de acesso |
| R-04 | Limite micro ≤ 75 kW | Lei 14.300, Art. 1º XI | OBR | V | Modalidades / Porte |
| R-05 | Limite mini > 75 kW (≤5 MW despach. / ≤3 MW não despach.) | Lei 14.300, Art. 1º XIII | OBR | V | Modalidades / Porte |
| R-06 | FV "despachável" = +baterias, modulação ≥ 20% geração mensal | Lei 14.300, Art. 1º IX | OBR | V | Modalidades |
| R-07 | Microrrede (GD + armazenamento + cargas; conectada/isolada) | Lei 14.300, Art. 1º XII | OBR | V | Modalidades |
| R-08 | Garantia de fiel cumprimento (mini): 2,5% / 5% | Lei 14.300, Art. 4º | OBR | V | Responsabilidades |
| R-09 | Responsabilidades financeiras de medição (micro/mini) | Lei 14.300, Art. 8º §§4–6 | OBR | V | Medição / Responsabilidades |
| R-10 | Definições de acessante, ponto de conexão, central geradora | PRODIST Mód. 1, verbetes 2.2/2.3/2.44/2.311 | OBR | V | Definições |
| R-11 | Inexistência de verbete de SAE → criar definição própria | PRODIST Mód. 1 (ausência) + IEC 62933-1 | CRIT/REF | V | Definições |
| R-12 | Interface mínima por faixa (acopl./seccion./interrup./proteção/medição) | PRODIST Mód. 3, Tab. 1 | OBR | V | Requisitos por porte |
| R-13 | Funções de proteção (ANSI) por faixa (27/59/81/25/62/anti-ilh.; 50/51 etc.) | PRODIST Mód. 3, Tab. 1-A | OBR | V | Proteção e controle |
| R-14 | Ensaio de conformidade do conversor do SAE (lab. Inmetro/ILAC) | PRODIST Mód. 3, itens 12.2/12.2.1/12.3 | OBR | V | Documentação / Comissionamento |
| R-15 | Ride-through de frequência (58,5–62,5 Hz tempo ilimitado etc.) | PRODIST Mód. 3, Tab. 1-B | OBR | V | FRT |
| R-16 | Ride-through de tensão (0,80–1,10 pu tempo ilimitado etc.) | PRODIST Mód. 3, Tab. 1-C | OBR | V | FRT |
| R-17 | Suportabilidade a df/dt ≤ 2,0 Hz/s | PRODIST Mód. 3, item 13-C | OBR | V | FRT / Proteção |
| R-18 | Proibição de anti-ilhamento por salto de vetor (conversores) | PRODIST Mód. 3, item 13-C.2 | OBR | V | Proteção (anti-ilhamento) |
| R-19 | Medição bidirecional (≤75 kW) / 4 quadrantes (>75 kW) | PRODIST Mód. 3, Tab. 1 + Mód. 5 | OBR | V | Medição |
| R-20 | Qualidade conforme Módulo 8 (tensão, FP, harmônicos, etc.) | PRODIST Mód. 3, item 16 → Mód. 8 | OBR | P (valores NC) | Qualidade |
| R-21 | Nível de tensão/nº de fases definidos pela distribuidora | PRODIST Mód. 3, item 11 | CRIT | V | Requisitos por porte/tensão |
| R-22 | Tabela tensão×potência própria (modelo CERVAM NTC-D-09) | Norma de distribuidora (exemplo) | CRIT | V | Requisitos por porte/tensão |
| R-23 | Tempo de reconexão definido pela distribuidora | PRODIST Mód. 3, Tab. 1-A nota 4 | CRIT | V | Proteção e controle |
| R-24 | Orçamento Estimado em 30 dias | REN 1.000/2021, Art. 56 | OBR | P | Solicitação de acesso (prazos) |
| R-25 | Orçamento Prévio/Parecer: 15/30/45 dias | REN 1.000/2021, Art. 64 I/II/III | OBR | V | Solicitação de acesso (prazos) |
| R-26 | Aprovação pelo consumidor: 10 dias úteis | REN 1.000/2021, Art. 83 | OBR | P | Solicitação de acesso (prazos) |
| R-27 | Execução de obras (rede aérea ≤2,3 kV): 60 dias | REN 1.000/2021, Art. 88, I | OBR | P | Solicitação de acesso (prazos) |
| R-28 | Vistoria + medição: 5/10 dias úteis | REN 1.000/2021, Art. 91 I/II | OBR | V | Vistoria / efetivação |
| R-29 | Dever da distribuidora de ter norma própria de conexão | REN 1.000/2021, Art. 19 | OBR | V | Objetivo / base normativa |
| R-30 | Anti-ilhamento ≤ 2 s; intertravamento a 0,7 pu; vedada operação em ilha | CPFL GED-19397 (estado da prática) + IEEE 1547 | CRIT/REF | V | Proteção (anti-ilhamento) |
| R-31 | Modalidades SAE sem GD (zero-grid) / híbrido on-grid / off-grid | CPFL GED-19397 | CRIT | V | Modalidades |
| R-32 | Controle de redução de injeção com BESS / Termo Zero Grid | Neoenergia DIS-NOR-031 (7.13) | CRIT | V | Controle de injeção / Documentação |
| R-33 | Diagramas de paralelismo permanente bateria/rede (BT/MT) | Enel GRI-EDBR-CNC-0005 (Anexos C/E) | REF | V | Anexos |
| R-34 | Controle P/Q 4 quadrantes (Volt-VAR/Volt-Watt, FP, droop) | IEEE 1547-2018, Cl. 5/6.5 | REF | P | Controle P/Q |
| R-35 | LVRT/HVRT (faixa contínua 0,88–1,10 pu) | IEEE 1547-2018, Cl. 6.4 | REF | P | FRT |
| R-36 | Injeção CC < 0,5%; harmônicos IEEE 519; flicker IEEE 1453 | IEEE 1547-2018 + 519 + 1453 | REF | P | Qualidade |
| R-37 | Comissionamento/ensaios (type/production/commissioning/periodic) | IEEE 1547.1-2020 | REF | V | Comissionamento e O&M |
| R-38 | Terminologia / planejamento / desempenho de EES | IEC 62933-1/-2-2/-3-1 | REF | V | Definições / O&M |
| R-39 | Segurança de BESS eletroquímico (ciclo de vida) | IEC 62933-5-2:2025; IEC 62619/63056 | REF | V | Segurança e incêndio |
| R-40 | Instalação/incêndio (afastamento 3 ft; supressão; ventilação; siting) | NFPA 855; UL 9540/9540A | REF | P | Segurança e incêndio |
| R-41 | Projeto elétrico CC do arranjo FV (PV+BESS) | ABNT NBR 16690:2019 (+5410/5419) | REF | P | Segurança elétrica / Comissionamento |
| R-42 | Licenciamento ambiental (LP/LI/LO; em regra estadual) | Res. CONAMA 237/1997 | OBR | V | Exigências ambientais |
| R-43 | Logística reversa / descarte de baterias | Lei 12.305/2010 Art. 33 II + Dec. 10.936/2022 + CONAMA 401/2008 | OBR | V | Exigências ambientais |
| R-44 | Documentação núcleo (ART/TRT, unifilar, memorial, formulário, INMETRO) | Benchmark (CPFL/Cemig/Equatorial/Neoenergia/Enel) + INMETRO Port. 140/2022 | CRIT/REF | V | Documentação |
| R-45 | Outorga/registro e medição individualizada do SAE autônomo | RNs ANEEL de 02/06/2026 (a confirmar) | OBR | NC | Modalidades / Medição |
| R-46 | Dois modelos de tarifação de uso da rede (coordenado-ONS / independente) | RNs 02/06/2026 + NT 13/2025 | OBR | P | (contexto comercial — fora do escopo técnico) |
| R-47 | Requisitos técnicos de SAE autônomo / grid-forming | Procedimentos de Rede / NT-ONS DPL 0111/2025 | OBR (prospec.) | NC | FRT / Controle (referência prospectiva) |
| R-48 | Base legal do armazenamento como atividade do setor | Lei 15.269/2025 | OBR | P | Objetivo / base normativa |

## Itens críticos a fechar (NC/P) antes da publicação
- **R-45, R-46, R-47, R-48:** dependem do número/DOU das RNs de SAE, da NT-ONS DPL 0111/2025 e do
  texto da Lei 15.269/2025 — ver lacunas #1–#3 do dossiê.
- **R-20:** transcrever valores do PRODIST Módulo 8.
- **R-24, R-26, R-27:** confirmar texto literal no PDF oficial da REN 1.000.
- **R-34, R-35, R-36, R-40, R-41:** confirmar cláusulas/edições sobre os textos integrais
  IEEE/IEC/NFPA/UL adquiridos.
