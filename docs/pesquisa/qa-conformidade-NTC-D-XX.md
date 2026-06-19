# QA de Conformidade — NTC-D-XX (R1 consolidada)

| Campo | Conteúdo |
|---|---|
| **Data** | 2026-06-19 |
| **Documento avaliado** | `rascunhos/NTC-D-XX-BESS/NTC-D-XX-corpo-consolidado.md` + `…-anexos.md` |
| **Referências de QA** | `rascunhos/NRM-0001-…/NRM-0001-estrutura-anotada.md` (checklist) · `docs/pesquisa/matriz-rastreabilidade.md` (48 IDs) · `docs/pesquisa/reconciliacao-drafts-cerpro.md` |
| **Método** | Cobertura seção-a-seção do checklist → status no consolidado; verificação de fontes; varredura de pendências `«»`/`[DECISÃO]`/`[VERIFICAR]`; conflitos. |

## 1. Veredito
**Cobertura estrutural: ~92%.** Todas as 18 seções do checklist NRM-0001 têm correspondência no
consolidado. As pendências restantes são **parâmetros de engenharia** (valores) e **2 anexos a
desenhar** — não são lacunas de escopo. **Apto a circular internamente** como R1 de trabalho; **não
publicável** até fechar os `[DECISÃO]`/`[VERIFICAR]` e cravar os `«»`.

## 2. Matriz de cobertura (checklist NRM-0001 → consolidado)
| # Checklist | Tema | Seção no consolidado | Status |
|---|---|---|---|
| 1 | Objetivo | §3 | ✅ |
| 2 | Campo/âmbito | §2 (+ não aplicação) | ✅ |
| 3 | Referências | §4 | ✅ (⚠ REN 956 a verificar) |
| 4 | Definições/siglas | §6 (+ R0) | ✅ saneado SAE/ESS/BESS |
| 5 | Responsabilidades | §5 + Anexo G | ✅ |
| 6 | Modalidades | §1.2, §7.1.2, §7.2 | ✅ |
| 7 | Requisitos por porte/tensão | §7.1.1, §9 | ⚠ tabelas com `«»` |
| 8 | Proteção/seccionamento | §9.1, §9.2 + Anexo K | ✅ |
| 9 | FRT + P/Q | §9.2.5 (Tab.5/6) | ⚠ valores `«»` |
| 10 | Qualidade de energia | §7.5, §10.1 | ⚠ transcrever Mód.8 |
| 11 | Medição | §10.2 | ✅ |
| 12 | Segurança/incêndio | §7.4, §12 + Anexo H | ✅ (afastamento `«3,0 m»`) |
| 13 | Ambiental | §7.3 | ✅ |
| 14 | Comissionamento/O&M | §11 + Anexo J | ✅ |
| 15 | Etapas/prazos de acesso | §8 + Anexo I | ✅ |
| 16 | Documentação exigida | §8.2 + Anexos B/C/E | ✅ |
| 17 | Resp. adicionais/Acordo Operativo | §7.7, §12 + Anexo F | ✅ |
| 18 | Disposições finais/vigência | §14 | ⚠ `«vigência»` |
| — | Governança (classes/comitê) | §13 + Anexo I | ✅ (ganho do NT-BESS-001) |

## 3. Conformidade de fontes (amostragem da matriz)
- **OK e rastreado:** faixas de potência 75 kW/5 MW (R-04/R-05); fluxo e prazos de acesso
  (R-24–R-28); ensaio do conversor PRODIST M3 (R-14); medição M5 (R-19); logística reversa
  (R-42/R-43); proteção/anti-ilhamento (R-13/R-17/R-23) — todos refletidos.
- **Decisão divergente do R0, documentada:** anti-ilhamento por **df/dt** com **salto de vetor
  vedado** (§9.2.6) — alinhado ao benchmark (R-30/Frente C); diverge do R0 e está anotado como nota
  de mudança. ✅ rastreável.
- **A confirmar (não cravar):** valores PRODIST Mód.8 (R-20 marcado NC na matriz); RN de SAE 2026
  (R-45/R-48); número da **REN 956/2021** citada no R0 (verificar se corresponde aos Procedimentos de
  Distribuição). Todos já sinalizados com `[VERIFICAR]`.

## 4. Pendências abertas (consolidado)
### 4.1 `[DECISÃO CERPRO]` (5)
1. **AVCB obrigatório** como documento geral? (§8.2)
2. **Seguro** obrigatório (incêndio/explosão/ambiental/RC/rede)? (§8.2, §12, Anexo H)
3. **Matriz classe × estudo** exigível (A–D) (§13).
4. Limiar de potência para função **67** (Tab.4).
5. Função **64** conforme arranjo (Tab.4).

### 4.2 `[VERIFICAR]` (4 famílias)
REN 956/2021 (nº/objeto) · RN de SAE 2026 (nº/DOU) · Lei 15.269/2025 · valores PRODIST Mód.8.

### 4.3 `«parâmetros»` a cravar (engenharia) — principais
Ajustes BT (27/59/81 e tempos) · LVRT (Tab.5) e frequência (Tab.6) · afastamento (`«3,0 m»`) ·
injeção CC (`«0,5%»`) · limiar telemetria (`«300 kW»`) · retenção (`«60»` meses) · vigência ·
e-mail de protocolo · resistência de aterramento (já fixa em ≤10 Ω).

### 4.4 Anexos a produzir
- ~~**Anexo A** — arranjos de conexão BT/MT~~ → ✅ **esboçado** (A.1 BT Zero-Grid, A.2 MT, A.3 híbrido
  com LPI); faltam apenas os **diagramas cotados** (engenharia).
- ~~**Anexo D** — certificações por componente~~ → ✅ **consolidado** (tabela por componente).

> **Atualização 2026-06-19 (pós-QA):** fechados sem depender da engenharia — (a) mini-glossário
> Zero-Grid/LPI/Anti-exportação/SCRPI/Hard Limit em **§6.1**; (b) **Anexo A** esboçado; (c) **Anexo D**
> consolidado. Conflito terminológico do item 5 passa a **✅ resolvido**.

## 5. Conflitos/inconsistências — status
| Item | Origem | Resolução no R1 |
|---|---|---|
| SAE = BESS (def. 6.35-A trocada) | R0 | ✅ corrigido (SAE = ESS família) |
| Numeração "7.4" repetida | R0 | ✅ renumerado |
| "BESS cem Geração" | R0 | ✅ corrigido (§7.2) |
| Salto de vetor primário vs. vedado | R0 × benchmark | ✅ decidido: vedado (§9.2.6) |
| Retenção 60 meses × 5 anos | NT-BESS-001 × Acordo | ✅ padronizado 60 meses |
| Anti-exportação × Zero-Grid × LPI | terminologia | ⚠ parcial — termos unificados no texto; **recomenda-se glossário único** em §6 ligando os três |

## 6. Recomendações priorizadas
1. **Engenharia:** preencher Tabelas 3–6 e ajustes (maior bloqueio para publicação).
2. **Regulação/Jurídico:** fechar os 5 `[DECISÃO]` e os 4 `[VERIFICAR]`.
3. **Redação:** adicionar em §6 um mini-glossário **Zero-Grid / LPI / Anti-exportação / SCRPI** para
   eliminar ambiguidade remanescente.
4. **Desenho:** produzir Anexos A e D.
5. Após (1)–(4): revisão final e mudança de estado para **R1 publicável** + atualizar Controle de Revisões.

## 7. Conclusão
O consolidado **incorpora integralmente** os dois drafts da CERPRO, resolve as inconsistências do R0,
fecha o escopo do checklist e mantém rastreabilidade às fontes. O caminho crítico até a publicação é
**parametrização de engenharia + decisões regulatórias**, não redação de novo conteúdo.
