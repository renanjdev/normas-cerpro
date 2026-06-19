# NTC-D-XX — ANEXOS (consolidação a partir do NT-BESS-001/2026 e MP-BESS-001)

> Conteúdo migrado de `docs/fontes-cerpro/NT-BESS-001-2026_normas-internas.md`, formatado como anexos
> da NTC-D-XX. `«»` = a cravar · `[DECISÃO CERPRO]` = deliberar.

---

## ANEXO E — Checklist de Documentação *(do NT-BESS-001 Anexo I / MP-BESS Etapa 1)*
- [ ] Requerimento formal
- [ ] Projeto executivo completo + diagramas unifilares e funcionais
- [ ] ART/TRT dos responsáveis técnicos (+ CREA/CFT atualizada)
- [ ] Memorial descritivo (empreendimento, baterias, PCS, BMS, EMS, HVAC, memória de cálculo,
      Plano de Segurança, de Emergência e de Descomissionamento)
- [ ] Planta baixa (implantação, acessos, rotas de fuga, FDC, afastamentos, áreas de segurança)
- [ ] Estudo de proteção e aterramento
- [ ] Catálogos/*datasheets* e manuais técnicos
- [ ] Certificados de conformidade (IEC/UL) + **certificação INMETRO** (baterias e inversores)
- [ ] AVCB ou equivalente `[DECISÃO CERPRO]`
- [ ] Licenças ambientais exigíveis
- [ ] **Declaração de finalidade operacional** + **Declaração de Não Exportação** (Anexo C)
- [ ] Comprovação de seguro `[DECISÃO CERPRO]`
- [ ] Cronograma físico-financeiro

## ANEXO B — Formulário de Solicitação + Dados Técnicos *(NT-BESS-001 Anexo II + R0)*
Campos mínimos: identificação do acessante/UC; localização; classe de tensão; demanda/geração
associada; **tecnologia da bateria** (química — recomenda-se LFP), capacidade nominal (kWh), potência
(kW), tensão, corrente, C-rate, RTE; **PCS** (potência, faixas, controle P/Q, modos); **BMS/EMS**;
**HVAC**; **finalidade** (backup / compensação reativa / arbitragem); parâmetros operacionais (FP a
manter; janelas de carga/descarga); modos habilitados (on/off-grid, Zero-Grid/LPI).

## ANEXO C — Declaração de Não Exportação e Placas de Advertência *(NT-BESS-001 Anexo III + R0)*
**Declaração de Não Exportação:** o titular declara que o BESS opera com **não injeção de potência
ativa (Zero-Grid)** / **LPI** conforme arranjo aprovado, comprovada por ensaio ou declaração do
fornecedor.
**Placas (mín. 2, material resistente a intempéries/UV):**
- "CUIDADO — RISCO DE CHOQUE ELÉTRICO — BATERIAS" (BESS sem GD)
- "CUIDADO — RISCO DE CHOQUE ELÉTRICO — SISTEMA HÍBRIDO" (BESS com GD)
Locais: caixa de medição/cabine primária e ponto de entrega (postinho/fachada/duto, voltada à via
pública); edificações coletivas: ponto de entrega do edifício e caixa de distribuição.

## ANEXO F — Acordo Operativo (modelo) *(NT-BESS-001 Anexo V)*
**ACORDO OPERATIVO Nº `«__/20__»`** entre CERPRO e `«consumidor»`.
- **Objeto:** condições técnicas e operacionais de conexão e operação do BESS.
- **Responsabilidades da CERPRO:** disponibilizar o ponto de conexão; fiscalizar; determinar medidas
  corretivas; solicitar informações técnicas.
- **Responsabilidades do consumidor:** operar dentro do aprovado; manter proteções; **impedir
  exportação não autorizada**; disponibilizar registros; comunicar ocorrências; manutenção.
- **Limites operacionais:** Potência máx. `«__ MW»`; Capacidade `«__ MWh»`; Tensão `«__ kV»`; Demanda
  contratada `«__ kW»`; Operação ilhada ( ) permitida ( ) não; Exportação ( ) mediante autorização ( ) vedada.
- **Eventos de contingência:** falha de proteção/sincronismo; injeção indevida; oscilações; distorções
  harmônicas; risco operacional.
- **Direito de intervenção da CERPRO:** redução de potência, limitação, paralisação, desligamento
  emergencial.
- **Responsabilidade por danos:** consumidor responde por danos à rede, a equipamentos da CERPRO, a
  terceiros e custos de reparação/interrupção.
- **Registro de dados:** retenção mínima de **`«60»` meses** (operação, carga/descarga, alarmes,
  eventos de proteção, ocorrências). *(Padronizado — o R0 falava "5 anos".)*
- **Vigência:** enquanto o sistema permanecer conectado. Alterações dependem de nova análise.

## ANEXO G — Matriz de Responsabilidades *(NT-BESS-001 Anexo VII)*
**Princípio:** a aprovação da conexão **não** implica homologação técnica, certificação de segurança,
nem assunção de responsabilidade operacional/ambiental/civil pela CERPRO.

| Domínio | Responsável | Inclui |
|---|---|---|
| Projeto e engenharia | Consumidor | dimensionamento, seleção de equipamentos, parametrização de proteção |
| Equipamentos | Consumidor | baterias, inversores, trafos internos, cabines, supervisão, proteção |
| Operação | Consumidor | carga/descarga, peak shaving, arbitragem, ilhamento, controle energético |
| Segurança operacional | Consumidor | prevenção/combate a incêndio, evacuação, controle de acesso |
| Ambiental | Consumidor | licenciamento, resíduos, descarte, vazamentos, contaminação |
| Trabalhista | Consumidor | empregados, terceirizados, acidentes |
| Regulatório | Consumidor | autorizações, registros, cadastros, certificações ANEEL |
| Sistema de distribuição | CERPRO | operação/manutenção/proteção da rede; continuidade |
| Fiscalização da conexão | CERPRO | análise documental e técnica; acompanhamento das condições |

**Eventos de responsabilidade exclusiva do consumidor:** incêndio/explosão/*thermal runaway*; falha
de inversores/módulos/controle/anti-exportação/sincronismo/aterramento/manutenção; degradação; perda
financeira; indisponibilidade.

## ANEXO H — Placa "DSV BESS — CERPRO" + Procedimentos de Emergência *(R0 + NT-BESS-001 Anexo VIII)*
**Placa DSV:** identificação "DSV BESS — CERPRO" no dispositivo de seccionamento visível travável (LOTO).
**Procedimento imediato (situação de emergência):** 1) interromper operação; 2) acionar proteções
automáticas; 3) isolar a área; 4) comunicar a CERPRO; 5) acionar o Corpo de Bombeiros; 6) acionar RTs;
7) registrar a ocorrência. **Comunicação imediata:** CERPRO, Bombeiros, Defesa Civil e órgão ambiental
(quando aplicável).
**Incêndio em baterias:** interromper, isolar, impedir aproximação, aguardar Bombeiros, seguir
fabricante; **vedada intervenção por pessoas não treinadas**.
**Fuga térmica (*thermal runaway*):** desligar, ampliar isolamento, impedir religamento, monitorar
temperatura, comunicar a CERPRO.
**Investigação:** ocorrências Nível 3/4 geram relatório + causa raiz + planos corretivo/preventivo em
**≤ 30 dias**. **Treinamento anual**; simulados para empreendimentos críticos. **Seguro** compatível
com incêndio/explosão/dano ambiental/RC/dano à rede `[DECISÃO CERPRO: obrigatório?]`.

## ANEXO I — Fluxo / Manual de Procedimentos (MP-BESS-001)
**Classificação:** A (baixa) · B (média) · C (alta) · D (estratégico).
**Etapas:** 1) Protocolo (≤ 5 du conferência) → 2) Análise preliminar (classificação) → 3) Parecer
regulatório → 4) Parecer técnico (curto-circuito, fluxo, coordenação, QEE, harmônicos, estabilidade,
confiabilidade, impacto) → 5) Parecer operacional (telecomando, supervisão, contingências) → 6)
Parecer jurídico (responsabilidades, contratos, Acordo Operativo, garantias, seguros) → 7) **Comitê
Interno BESS** (aprovação / com condicionantes / complementação / indeferimento) → 8) Orçamento de
Conexão → 9) Formalização contratual (Acordo Operativo + aditivo CUSD + Declaração de Não Exportação
+ seguro + termo de responsabilidade) → 10) Execução das adequações (acompanhada pela CERPRO).

## ANEXO J — Procedimento de Testes e Comissionamento *(NT-BESS-001 Anexo VI / Cap. X)*
Testes obrigatórios antes da operação: anti-ilhamento; anti-exportação/LPI; proteção; desligamento de
emergência; comunicação; supervisão; teste funcional do sistema. A CERPRO pode acompanhar
presencialmente. Registro de eventos (RDP, cronológico, alarmes, atuações de proteção), retenção **≥
60 meses**.

## ANEXO K — Requisitos Mínimos de Proteção e Critérios de Indeferimento *(NT-BESS-001 Anexo IV)*
**Proteções elétricas mínimas (ANSI):** 27, 59, 81U, 81O, 50, 51, 67, 32, 25, 46, 47, 50N/51N, 64.
*(Salto de vetor — 78 — **vedado** como método de anti-ilhamento, ver corpo §9.2.6.)*
**Anti-ilhamento:** certificado; desligamento automático na perda da rede; operação ilhada não
autorizada proibida.
**Anti-exportação:** quando sem autorização de exportação, sistema dedicado que impeça **física e
logicamente** o fluxo reverso; CERPRO pode exigir redundância.
**Desligamento de emergência:** botão dedicado; CERPRO pode determinar desligamento imediato por risco
à segurança/rede, falha de proteção/sincronismo, exportação indevida, risco ambiental/incêndio.
**Critérios de indeferimento técnico:** ausência dos estudos exigidos; impossibilidade de mitigar
riscos; incompatibilidade técnica com a rede; descumprimento regulatório; inexistência de condições
mínimas de segurança.

---

## ANEXOS A e D — pendentes de desenho
- **A (Arranjos de conexão BT/MT):** diagramas a elaborar (referência: arranjos do R0 e modelos de
  benchmark) — `«engenharia»`.
- **D (Lista de certificações exigidas):** consolidar a partir do §4 do R0 (IEC/UL/INMETRO por
  componente) — próxima rodada.
