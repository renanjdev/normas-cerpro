# Plano de execução — Norma de Conexão de SAE/BESS

Projeto coordenado por um **orquestrador** com um time de agentes especializados para produzir uma **Norma de Conexão de Sistemas de Armazenamento de Energia (SAE/BESS)** para a CERPRO, a partir de pesquisa regulatória profunda + materiais da CERPRO.

## Time de agentes

| Papel | Função |
|-------|--------|
| **Orquestrador** | Consolida os produtos, mantém a matriz de rastreabilidade (requisito → fonte) e o estado entre fases. |
| **Pesquisador Regulatório** | Varre ANEEL (REN 1.059/2023, PRODIST Mód. 1 e 3, Lei 14.300), arcabouço de SAE e normas técnicas (ABNT/IEC/IEEE). |
| **Analista Técnico** | Converte regulação em requisitos de conexão (tensão, proteção, anti-ilhamento, qualidade, medição, modos de operação). |
| **Especialista CERPRO** | Encaixa na realidade da permissionária (estrutura/numeração das normas e características da rede). |
| **Redator Normativo** | Escreve no estilo regulatório. |
| **Revisor de Conformidade (QA)** | Lacunas, contradições e separação obrigatório-ANEEL vs. critério-da-distribuidora. |

## Decisões travadas

- **Faseamento:** checkpoint após a Fase 1 (pesquisa) antes de redigir.
- **Materiais da CERPRO:** entram antes da fase de redação.
- **Profundidade:** arcabouço parametrizado (valores como parâmetros justificados pela fonte).
- **Módulos BESS no escopo:** exigências ambientais · segurança e incêndio · FRT + controle P/Q (4 quadrantes) · comissionamento + O&M.
- **Fora do escopo da v1:** Comunicação/SCADA + Cibersegurança (revisão futura).

## Fases

1. **Pesquisa Regulatória** → dossiê + matriz de rastreabilidade. **[checkpoint com o cliente]**
2. **Análise Técnica** → requisitos parametrizados por porte/tensão.
3. **Encaixe CERPRO** (com materiais da permissionária).
4. **Redação Normativa** → minuta `NRM-XXXX` em `rascunhos/`.
5. **QA de Conformidade** → relatório de lacunas/contradições.

## Estrutura prevista da norma

objetivo · campo de aplicação · referências · definições/siglas · modalidades de SAE · requisitos técnicos por porte/tensão · proteção e controle (incl. FRT, anti-ilhamento) · controle P/Q e qualidade de energia · medição · segurança e incêndio · exigências ambientais · comissionamento, ensaios e O&M · solicitação de acesso (etapas/prazos) · documentação exigida (ART, diagramas, certificados) · responsabilidades · disposições transitórias/vigência · anexos (formulários, unifilares de referência, matriz de rastreabilidade).

## Princípio de rastreabilidade

Cada requisito da norma deve apontar para sua **fonte** e ser classificado como **Obrigatório (ANEEL/lei)** ou **Critério da distribuidora**. Citações só entram após verificação humana.
