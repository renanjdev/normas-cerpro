# FRENTE C — Benchmark de Normas de Conexão/Acesso de Distribuidoras (GD e Armazenamento)

> Pesquisa regulatória para subsidiar a **Norma de Conexão de SAE/BESS da CERPRO**.
> Data da pesquisa: **19/06/2026**. Autor: Pesquisador Regulatório/Benchmark.
>
> **Regras de citação:** só constam documentos efetivamente acessados e lidos via extração de
> texto (PyMuPDF) sobre o PDF da fonte primária. Cada ficha traz distribuidora, código, versão,
> data e URL, com marcação **[VERIFICADO via fetch]** ou **[NÃO CONFIRMADO]**.
>
> **Nota de método:** vários sites de distribuidora bloqueiam download direto (HTTP 403 Akamai –
> ex.: Energisa) ou movem URLs (404 – ex.: links antigos da Equatorial). Quando o PDF foi obtido
> e o texto extraído, marcou-se [VERIFICADO via fetch]. Quando só houve acesso a metadados de
> busca/portal sem leitura do corpo do PDF, marcou-se [NÃO CONFIRMADO].

---

## DESTAQUE — Norma de armazenamento já publicada por distribuidora

**SIM, existe.** A **CPFL** já possui norma técnica **dedicada** a Sistemas de Armazenamento de
Energia (SAE):

- **CPFL — GED-19397 — "Critérios de Acesso ao Sistema Elétrico da CPFL com Sistemas de
  Armazenamento de Energia"** — Código `DIST-19397-2025-RE-NOR`, **Versão 2.0, publicada
  09/12/2025**. **A v1.0 é de 19/12/2022.** **[VERIFICADO via fetch]**

Além dela, **Neoenergia, Enel, Equatorial e Cemig** já trataram de armazenamento/baterias
**dentro de suas normas de conexão de GD** (não como norma separada). Detalhes nas fichas.

Estado regulatório federal (contexto, não é norma de distribuidora): a **ANEEL** publicou em
**10/10/2025 orientações** para conexão de SAE associado a centrais geradoras e mantém em
tramitação a minuta de Resolução Normativa de SAE (origem na Consulta Pública nº 39/2023). O
arcabouço federal de SAE para GD/distribuição ainda **não estava consolidado em REN** na data
desta pesquisa — o que torna as normas de distribuidora (sobretudo a GED-19397) a principal
referência de **estado da prática**.

---

# FICHAS POR DISTRIBUIDORA/DOCUMENTO

## 1. CPFL — GED-19397 — Critérios de Acesso com Sistemas de Armazenamento de Energia (SAE) ★ NORMA DE ARMAZENAMENTO

**[VERIFICADO via fetch]**

| Campo | Valor |
|---|---|
| Distribuidora | Grupo CPFL Energia (CPFL Paulista, CPFL Piratininga, CPFL Santa Cruz, RGE) |
| Código | `DIST-19397-2025-RE-NOR` (N. Documento 19397) |
| Tipo/Categoria | Norma Técnica / Operacional |
| Versão | **2.0** (v1.0 = 19/12/2022) |
| Data publicação | **09/12/2025** |
| Aprovador | Eduardo Henrique da Silva |
| Páginas | 37 |
| URL | https://sites.cpfl.com.br/documentos-tecnicos/GED-19397.pdf |

**Escopo:** critérios e requisitos para conexão de SAE, no modelo **híbrido** (baterias + micro/
minigeração distribuída) **ou junto à carga** (sem GD), para UCs de BT e MT. Foco em baterias
eletroquímicas **behind-the-meter** ("atrás do medidor").

### Estrutura (sumário transcrito)
```
1  OBJETIVO
2  ÂMBITO DE APLICAÇÃO
3  CONCEITOS E DEFINIÇÕES
4  DOCUMENTOS DE REFERÊNCIA
5  RESPONSABILIDADES
6  REGRAS BÁSICAS
   6.1  Sistemas de Armazenamento de Energia (SAE) sem Geração Distribuída
   6.2  Sistemas On-Grid com Bateria (Híbridos)
   6.3  Aspectos de Segurança
   6.4  Requisitos de Proteção, Seccionamento e Manobra do SAE
   6.5  Requisitos de Qualidade da Energia Elétrica
   6.6  Requisitos de Operação, Manutenção e Descarte
   6.7  Canais de Atendimento ao Consumidor
   6.8  Responsabilidades Adicionais
7  CONTROLE DE REGISTROS
8  ANEXOS
   8.1  Anexo A: Arranjos Permitidos
   8.2  Anexo B: Formulário para solicitação de conexão de sistemas on-grid com bateria
   8.3  Anexo C: Placas de Advertência
   8.4  Anexo D: Documentação Técnica e de Segurança (Referências)
9  REGISTRO DE ALTERAÇÕES
```

### Modalidades de conexão
- **SAE sem GD** (junto à carga): funções back-up, UPS, compensação de reativos e arbitragem;
  **proibida injeção de potência ativa** na rede — deve ser **"zero-grid"**.
- **On-Grid Híbrido** (SAE + MMGD): integra renováveis (atende art. 73 da REN 1.000/2021);
  **despacho/injeção de potência à rede só é permitido em arranjos SAE+GD**, respeitando o
  Orçamento de Conexão.
- Modos operacionais exigidos em ambos: **On-Grid** (sem injeção ativa; serviços ancilares e
  arbitragem permitidos) e **Off-Grid** (back-up ilhado, com chave de intertravamento).

### Requisitos por porte/tensão
- SAE/central **> 75 kW** → conexão por **transformador de acoplamento** + proteção por disjuntor
  em MT com funções no relé.
- **> 300 kW** (mesmo sem exportação) → **religador** (ET CPFL 15197) com supervisão remota.
- BT: funções de proteção embarcadas no inversor (certificado INMETRO Portaria 140/2022).

### Proteção / anti-ilhamento
- **Tabela 6.1 (≤ 75 kW)** com colunas "inversor COM certificado INMETRO" vs "SEM": exige
  elemento de desconexão, elemento de interrupção (só p/ sem certificado), sub/sobretensão,
  sub/sobrefrequência, relé de sincronismo, **anti-ilhamento**.
- MT: relé digital multifuncional com **ANSI 50/51, 50N/51N/51GS, 67, 27, 59, 59N, 32, 81 O/U, 25**;
  chave seccionadora tripolar (bloqueio Kirk); disjuntor de interconexão.
- **Anti-ilhamento:** desconexão automática em **≤ 2 s**; intertravamento aciona quando tensão da
  rede ≤ **70% (0,7 p.u.)**. Vedada operação em ilha da rede da distribuidora.
- Chaves de intertravamento eletromecânicas **ou** estáticas (não se aceita só controle direcional).

### Medição / qualidade / segurança
- Conexão física segue NT CPFL nº 13 (BT) / nº 2855 e 33 (MT).
- Qualidade: PRODIST Módulo 8 (DTT, DTC, fator de potência, variação de tensão/frequência).
- Segurança (6.3): sistema de monitoramento/alarme da bateria; supressão automática de condição
  perigosa; **PCS** (Power Conversion System) com interface de controle local (BT) e integração a
  **EMS** com controle remoto (MT); aterramento revisado (NBR 5410/15751); **DPS** (NBR 5419).
- Descarte (6.6): responsabilidade do acessante.

### Documentação exigida
- **Documento de responsabilidade técnica (ART)** de projeto e execução (Anexo B, item 2.1).
- **Memorial descritivo + diagrama unifilar**.
- **Certificação INMETRO** de durabilidade/desempenho das baterias (**opcional**).
- Datasheet/manuais/certificações IEC da **chave de intertravamento**.
- **Ensaio ou declaração do fornecedor** comprovando operação **Zero Grid** (sem injeção ativa)
  ou **Limitação de Potência Injetada** (Anexo I da NT 15303).
- **Formulário Anexo B** (dados técnicos da bateria: tecnologia, potência kW, tensão, capacidade
  kWh, finalidade, características de carga/descarga p/ arbitragem).
- **Placas de advertência** (Anexo C) em locais especificados.
- Anexo D lista normas: NBR 5410/5419/15751, **IEC 62619/62620/62933-5-1**, IEC 60947, IEC
  62310/62040 (chaves STS/ATS), NBR 16149/16150/IEC 62116 (inversores).

### Saída do processo
- Após aprovação: emissão de **"Responsabilidades Adicionais"** (SAE sem GD) ou
  **"Relacionamento Operacional"/"Acordo Operativo"** (híbrido, conforme o tipo de conexão).

---

## 2. CPFL — GED-15303 — Conexão de Micro e Minigeração Distribuída (SCEE)

**[VERIFICADO via fetch]** (cópia lida: versão antiga)

| Campo | Valor |
|---|---|
| Distribuidora | Grupo CPFL Energia |
| Código | GED-15303 (N. Documento 15303) |
| Tipo/Categoria | Norma Técnica / Instrução |
| Versão lida | **1.7** (publicação 31/12/2020) — cópia analisada referencia REN 482/2012¹ |
| URL | http://sites.cpfl.com.br/documentos-tecnicos/GED-15303.pdf |

¹ A cópia obtida via busca é a v1.7/2020 (base REN 482); a CPFL mantém o mesmo código GED-15303
para a versão vigente sob REN 1.000/2021 — a **GED-19397 v2.0 (2025) referencia a NT 15303
vigente e seu "Anexo I" de Limitação de Potência Injetada**, indicando versão mais nova em uso.
**[Versão vigente: NÃO CONFIRMADO — recomenda-se baixar a edição atual da GED-15303]**

### Estrutura (sumário transcrito)
```
1  OBJETIVO
2  ÂMBITO DE APLICAÇÃO
3  DEFINIÇÕES
4  DOCUMENTOS DE REFERÊNCIA
5  RESPONSABILIDADES
6  REGRAS BÁSICAS
   - Sistema de Compensação de Energia Elétrica
   - Demonstração de Créditos; Fatura
   - Tensão de Conexão; Potência Instalada
   - Cogeração Qualificada
   - Contrato; Acordo Operativo; Relacionamento Operacional
   - Contatos do Acessante
   - Solicitação de Acesso
   - Consulta e Informação de Acesso
   - Parecer de Acesso
   - Vistoria; Relatório de Vistoria; Aprovação da Conexão
   - Segurança
   - Requisitos Específicos
   - Ponto de Conexão
   - Diagramas Unifilares
   - Padrão de Entrada
   - Proteção; Secionamento; Manobra
   - Sistema de Medição de Faturamento
   - Qualidade da Energia Elétrica
   - Requisitos para Operação em Paralelo
   - Acordo Operativo; Relacionamento Operacional
7  CONTROLE DE REGISTROS
8  ANEXOS
9  REGISTRO DE ALTERAÇÕES
```

### Pontos relevantes
- **Proteção por faixa de potência** (tabela com código ANSI x P ≤ 75 / 75–500 / 500–5000 kW):
  27/59, 81 U/O, 25 e anti-ilhamento exigidos em todas as faixas; 67, 50/51, 50N/51N/51G, 59N, 32,
  78, 81 df/dt acrescidos nas faixas maiores. BT via inversor (NBR 16149/16150).
- **Anti-ilhamento:** cessar injeção ativa em **≤ 0,2 s** ao sair da faixa; reconexão após **180 s**;
  corrente CC ≤ 0,5% e cessação em 1 s sem transformador de isolamento. ANSI 79 bloqueado.
- **MT:** dispositivo de seccionamento visível (DSV) lacrável; **> 300 kW** → religador (ET 15197).
- **Documentação:** **ART** de projeto e execução; **diagrama unifilar** (CAD, do ponto de conexão);
  **Anexo F** preenchido (equivale ao **memorial descritivo**); identificação/localização da UC;
  planta do padrão de entrada; fotos do padrão e do dispositivo de proteção geral.
- **Medição:** medidor bidirecional fornecido pela CPFL; direta ou indireta (com TCs).
- **Armazenamento/BESS:** **NÃO** há tratamento de SAE nesta versão (as 2 ocorrências de
  "armazenamento" referem-se a agrotóxicos; "acumulado" refere-se a créditos de energia). O SAE
  está na GED-19397 (ficha 1).

---

## 3. Cemig D — ND-5.31 — Conexão de Acessantes Produtores em Média Tensão

**[VERIFICADO via fetch]**

| Campo | Valor |
|---|---|
| Distribuidora | Cemig Distribuição (Cemig D) |
| Código | ND-5.31 |
| Título | Requisitos para Conexão de Acessantes Produtores de Energia Elétrica ao Sistema de Distribuição da Cemig D – Média Tensão |
| Revisão lida | **Revisão g** (vigência 24/JUN/2024); o PDF obtido (upload 2025/10) traz histórico até rev. g. Há referência a edição posterior **[a versão de outubro/2025 deve ser baixada para confirmar]** |
| Páginas | 171 |
| URL | https://www.cemig.com.br/wp-content/uploads/2025/10/ND_5.31_Conexao-em-MT-.pdf |
| Norma irmã (BT) | **ND-5.30** – Conexão em BT (URL com 404 na data; ver lacunas) |

### Estrutura (índice transcrito — resumido)
```
1  INTRODUÇÃO
   1.1 Objetivos e Escopo · 1.2 Terminologia · 1.3 Disposições Gerais
   1.4 Normas, Legislação e Regulação
2  PRODUTORES INDEPENDENTES E AUTOPRODUTORES DE ENERGIA ELÉTRICA
   2.1 Procedimentos para Viabilização do Acesso
       2.1.1 Consulta e Entrega de Orçamento Estimado
       2.1.2 Pedido de Conexão
       2.1.3 Aceite/Rejeição do Pedido e Entrega de Protocolo
       2.1.4 Análise Distribuidora (Alternativas) – Orçamento de Conexão Técnico-Comercial
       2.1.5 Aprovação do Orçamento de Conexão
       2.1.6 Assinatura de Contrato e Pagamento
       2.1.7 Obras
   2.2 Critérios Técnicos – Produtores Independentes e Autoprodutores
       2.2.1 Características do Sistema de Distribuição em MT · 2.2.2 Forma da Conexão
       2.2.3 Critérios para Estudos de Conexão · 2.2.4 Requisitos e Padrões Técnicos
3  MICROGERAÇÃO E MINIGERAÇÃO DISTRIBUÍDA ADERENTES AO SCEE
   3.1 Procedimento de Acesso (3.1.1 Projeto Elétrico · 3.1.2 Responsabilidade Técnica ·
       3.1.3 Acordo Operativo e Relacionamento Operacional · 3.1.4 Obras de Conexão ·
       3.1.5 Vistoria e Comissionamento)
   3.2 Critérios Técnicos – Micro e Minigeração Distribuída
4  QUALIDADE DA ENERGIA ELÉTRICA
   4.1 (Tensão) · 4.2 Fator de Potência · 4.3 Distorções Harmônicas · 4.4 Desequilíbrios de
   Tensão · 4.5 Flutuações de Tensão · 4.6 Variações de Tensão · 4.7 Variações de Frequência
   4.8 Requisitos de Qualidade do Serviço
5  BIBLIOGRAFIA
6  ANEXOS
```

### Pontos relevantes
- Norma **abrangente** que separa **Produtores Independentes/Autoprodutores** de **MMGD/SCEE**,
  com etapas completas de acesso (consulta → orçamento estimado → pedido de conexão →
  protocolo → orçamento de conexão → contrato → obras → vistoria/comissionamento).
- **Armazenamento (17 menções) / bateria (10):** tratado como **atributo do projeto de GD**, não
  como norma separada. Exige que projetos de MMGD **associados a SAE por baterias** detalhem
  **características técnicas do sistema e forma de operação em conjunto com a geração**. Cita a
  definição de FV despachável (modulação por baterias ≥ **20%** da geração diária — REN 1.000).
- Documentação: **projeto elétrico**, **responsabilidade técnica (ART)**, Acordo Operativo/
  Relacionamento Operacional.

---

## 4. Equatorial — NT.00020.EQTL — Conexão de Micro e Minigeração Distribuída

**[VERIFICADO via fetch]**

| Campo | Valor |
|---|---|
| Distribuidora | Grupo Equatorial Energia |
| Código | NT.00020.EQTL |
| Revisão | **06 – 2025** (Homologado em **26/12/2025**) |
| Páginas | 89 |
| URL | https://ceee.equatorialenergia.com.br/wp-content/uploads/2026/01/NT.00020.EQTL-06-Conexao-de-Micro-e-Minigeracao-Distribuida-ao-Sistema-de-Distribuicao.pdf |

### Estrutura (sumário transcrito — resumido)
```
1  CAMPO DE APLICAÇÃO
2  RESPONSABILIDADES
3  DEFINIÇÕES
4  REFERÊNCIAS
5  CONDIÇÕES GERAIS
   5.1 Atendimento ao Cliente · 5.2 Generalidades · 5.3 Aluguel de Telhado
   5.4 Sistema de Compensação de Energia Elétrica
   5.5 Responsabilidades por Danos e Acesso à Revelia · 5.6 Garantia de Fiel Cumprimento
   5.7 Participação Financeira · 5.8 Responsabilidade em Obras · 5.9 Contratos
   5.10 Etapas de Conexão · 5.11 Orçamento Estimado · 5.12 Aprovação Prévia de Projeto
   5.13 Solicitação de Orçamento de Conexão · 5.14 Orçamento de Conexão
   5.15 Inversão de Fluxo · 5.16 Vistoria e Aprovação do Ponto de Conexão
   5.17 Solicitação de Vistoria · 5.18 Prazos · 5.19 Casos Omissos
6  CARACTERÍSTICAS TÉCNICAS E PADRÕES CONSTRUTIVOS
   6.1 Requisitos Técnicos e Operacionais
   6.2 Requisitos da Conexão com a Rede Elétrica para SFV (sistema fotovoltaico)
   6.3 Características Construtivas
7  ANEXOS
8  TABELAS
9  DESENHOS
10 CONTROLE DE REVISÕES
11 APROVAÇÃO
```

### Pontos relevantes
- Vigência integral após **120 dias** da publicação (Art. 20 REN 1.000), cancelando versões
  anteriores.
- **Armazenamento (9 menções) / bateria (4):** integrado à GD. Exige no **formulário de
  Solicitação de Orçamento de Conexão** indicar se há **armazenamento** e, para FV
  **despachável**, comprovação de atendimento ao **art. 655-B da REN 1.000/2021** (modulação por
  baterias ≥ 20% da geração mensal). Prevê **suprimento ilhado de cargas internas a partir do
  armazenamento** (qualidade sob responsabilidade do acessante). No controle de potência
  injetável, exige declarar **se haverá instalação de SAE**.
- Documentação: memorial técnico descritivo; dados da central geradora; comprovação de
  propriedade; (e demais conforme PRODIST Mód. 3). Há seção **5.18 Prazos** específica.

---

## 5. Neoenergia — DIS-NOR-031 — Conexão de Microgeradores ao Sistema de Distribuição

**[VERIFICADO via fetch]**

| Campo | Valor |
|---|---|
| Distribuidora | Grupo Neoenergia (Coelba, Pernambuco, Cosern, Elektro, Brasília) |
| Código | DIS-NOR-031 |
| Revisão | **02** — Aprovado **16/05/2025** (aprovador Ricardo Prado Pina) |
| Páginas | 41 |
| URL | https://www.neoenergia.com/documents/d/sp/dis-nor-031-pdf?download=true |
| Normas irmãs | DIS-NOR-033 (Minigeração/MT), DIS-NOR-067 (Acesso/Conexão e Uso – 72 pgs, abril/2024) |

### Estrutura (sumário transcrito)
```
1  CONTROLE DE ALTERAÇÕES
2  DOCUMENTOS ANTECESSORES
3  OBJETIVO
4  CAMPO DE APLICAÇÃO
5  RESPONSABILIDADES
6  DEFINIÇÕES
7  CONDIÇÕES GERAIS
   7.1 Condições Gerais · 7.2 Regulamentação
   7.3 Responsabilidade e Atribuições Profissionais · 7.4 Ponto de Conexão
   7.5 Padrão de Entrada · 7.6 Potência Máxima Instalada e Desequilíbrio entre Fases
   7.7 Critérios Adicionais e Pontos de Atenção · 7.8 Requisitos de Projetos
   7.9 Requisitos para Conexão de Central Geradora · 7.10 Sistema de Medição de Energia Elétrica
   7.11 Sinalização de Segurança · 7.12 Sistema de Controle de Exportação
   7.13 Sistema de Controle de Redução da Potência Injetável com BESS
8  REFERÊNCIAS
9  ANEXOS  (Anexo I – TERMO DE RESPONSABILIDADE TÉCNICA ZERO GRID)
```

### Pontos relevantes
- **BESS (4 menções) / bateria (15) / armazenamento (11):** Neoenergia **integrou o BESS** como
  mecanismo de controle de injeção. Subseção dedicada **7.13 "Sistema de Controle de Redução da
  Potência Injetável com BESS" (SCRPI)**, com **diagrama esquemático** e **perfil de resposta
  dinâmica** para rejeição completa de carga local.
- Há **7.12 Sistema de Controle de Exportação** (limitação de injeção) e um **Termo de
  Responsabilidade Técnica Zero Grid** como Anexo I — o RT declara o funcionamento do controle.
- Documentação: **responsabilidade técnica (ART)**, requisitos de projeto, diagrama unifilar.
- Referências: NBR 16149/16150, NBR IEC 60947, normas Neoenergia (DIS-NOR-012/030/053),
  REN 1.000/2021.

---

## 6. Enel Grids Brasil — GRI-EDBR-CNC-GRI-0005 — Conexão de Micro e Minigeração Distribuída

**[VERIFICADO via fetch]**

| Campo | Valor |
|---|---|
| Distribuidora | Enel Grids Brasil (Enel CE, RJ, SP) |
| Código | GRI-EDBR-CNC-GRI-0005 (Especificação Técnica nº 0005) |
| Versão | **05** — data **30/07/2024** |
| Páginas | 52 |
| URL | https://www.eneldistribuicao.com.br/rj/documentos/Conexao%20de%20Micro%20e%20Minigera%C3%A7ao%20Distribu%C3%ADda%20ao%20Sistema%20El%C3%A9trico%20da%20Enel%20Grids%20Brasil_3.0.pdf |

### Estrutura (índice transcrito — resumido)
```
1  OBJETIVOS DO DOCUMENTO E ÁREA DE APLICAÇÃO
2  GESTÃO DA VERSÃO DO DOCUMENTO
3  UNIDADES RESPONSÁVEIS PELO DOCUMENTO
4  REFERÊNCIAS
5  POSIÇÃO DO PROCESSO COM RELAÇÃO À ESTRUTURA ORGANIZACIONAL
6  SIGLAS E PALAVRAS-CHAVE
7  DESCRIÇÃO DO PROCESSO
   7.2 Procedimento de Conexão · 7.3 Solicitação de Conexão · 7.4 Tipos de Conexão
   7.5 Medição · 7.6 Proteção · 7.7 Sinalização · 7.8 Índice de tabelas e figuras
8  ANEXOS
   8.1 Anexo A – Formulário de Solicitação de Orçamento de Conexão
   8.2 Anexo B – Diagrama Unifilar de Conexão à Rede de BT
   8.3 Anexo C – Diagrama – Paralelismo Permanente Rede/Sistema de Baterias na BT
   8.4 Anexo D – Diagrama Unifilar Conexão à Rede de MT
   8.5 Anexo E – Diagrama Paralelismo Permanente Rede/Sistema de Baterias na MT
   8.6 Anexo F – Padrão de Medição de BT  (...)
```

### Pontos relevantes
- **Bateria/armazenamento:** Enel **fornece diagramas unifilares de referência** para
  **"Paralelismo Permanente Rede/Sistema de Baterias"** em **BT (Anexo C)** e **MT (Anexo E)** —
  abordagem de "storage integrado ao padrão de conexão de GD".
- Proteção (7.6): chave de desconexão visível/acessível, elemento de interrupção automático,
  transformador de interface UC↔rede.
- Referências citam Portaria INMETRO de "Avaliação da Conformidade para Equipamentos de
  Geração, Condicionamento e **Armazenamento** de Energia Elétrica em Sistemas FV".

---

## 7. Energisa — NDU-013 (BT) e NDU-015 (MT) — Conexão de Acessantes de GD

**[NÃO CONFIRMADO via fetch]** — site Energisa retorna **HTTP 403** (bloqueio Akamai) a
WebFetch e a curl com user-agent de navegador; corpo do PDF não pôde ser lido. Metadados
abaixo vêm de busca/portal.

| Campo | Valor (de busca) |
|---|---|
| Distribuidora | Grupo Energisa |
| NDU-013 | Critérios para a Conexão em **Baixa Tensão** de Acessantes de GD — versão referida **8 (dez/2024)**; aplica a microgeração ≤ 75 kW no SCEE |
| NDU-015 | Critérios para a Conexão em **Média Tensão** de Acessantes de GD — edição referida **dez/2025** |
| URL NDU-013 | https://www.energisa.com.br/sites/energisa/files/media/documents/2025-02/NDU%20013%20-%20Crit%C3%A9rios%20para%20a%20Conex%C3%A3o%20em%20Baixa%20Tens%C3%A3o%20de%20Acessantes%20de%20Gera%C3%A7%C3%A3o%20Distribu%C3%ADda%20ao%20Sistema%20de%20Distribui%C3%A7%C3%A3o.pdf |
| URL NDU-015 | https://www.energisa.com.br/sites/energisa/files/media/documents/2025-12/NDU%20015%20-%20...pdf |

> **Ação recomendada:** baixar manualmente (navegador) NDU-013 e NDU-015 para verificação humana;
> verificar se a Energisa já incorporou SAE/BESS (não confirmado nesta pesquisa).

---

## 8. Copel — NTC 905200 — Acesso de Micro e Minigeração Distribuída

**[NÃO CONFIRMADO via fetch]** — fonte oficial www.copel.com/normas; corpo não lido
(disponível em repositórios terceiros — Scribd/Studocu/SlideShare — não usados como fonte
primária). Metadados de busca:

| Campo | Valor (de busca) |
|---|---|
| Distribuidora | Copel Distribuição |
| Código | NTC 905200 — Acesso de Micro e Minigeração Distribuída |
| Histórico | emitida desde fev/2014; revisão referida **jan/2024** |
| Escopo | micro/minigeração SCEE sob REN 1.000/2021 (até 3 MW não-despacháveis / 5 MW despacháveis) |
| Portal | https://www.copel.com/normas (verificar URL direta do PDF) |

> **Ação recomendada:** localizar o PDF oficial em copel.com/normas e verificar tratamento de SAE.

---

# SEÇÃO COMPARATIVA

## CONVERGÊNCIAS (o que quase todas exigem)
1. **Base regulatória comum:** REN ANEEL **1.000/2021** + **PRODIST Módulos 1, 3 e 8**; muitas ainda
   citam o histórico REN 482/2012 e seguintes.
2. **Etapas de acesso padronizadas:** consulta/orçamento estimado → solicitação/pedido de conexão
   → orçamento de conexão → contrato/Acordo Operativo ou Relacionamento Operacional → obras →
   **vistoria/comissionamento** → aprovação/energização.
3. **Documentação núcleo:** **ART/documento de responsabilidade técnica** (projeto e execução);
   **diagrama unifilar**; **memorial descritivo** (às vezes via formulário próprio); **formulário de
   solicitação**; identificação/localização da UC; fotos/plantas do padrão de entrada.
4. **Proteção mínima escalonada por porte** (faixas tipicamente ≤ 75 / 75–500 / 500–5.000 kW),
   com funções **ANSI 27/59, 81 O/U, 25 (sincronismo) e anti-ilhamento** sempre presentes; funções
   direcionais e de sobrecorrente (67, 50/51, 50N/51N, 59N, 32) adicionadas nas faixas maiores.
5. **Anti-ilhamento obrigatório** e **vedação de operação em ilha da rede da distribuidora**;
   desconexão automática rápida (≤ ~2 s) com elemento de interrupção/intertravamento.
6. **Conformidade de equipamentos:** inversores conforme **NBR 16149/16150 e NBR IEC 62116** e
   **certificação/registro INMETRO** (Portaria 140/2022). Dispositivo de **seccionamento visível**.
7. **Medição bidirecional** fornecida pela distribuidora; medição direta ou indireta (com TC) por porte.
8. **Qualidade** referenciada ao **PRODIST Módulo 8**.
9. **MT:** transformador de acoplamento/interface acima de 75 kW; **religador acima de 300 kW**
   (explícito em CPFL); relé digital multifuncional com TCs/TPs.

## DIVERGÊNCIAS (onde variam)
| Tema | Variação observada |
|---|---|
| **Tratamento de SAE/BESS** | **CPFL** = norma **dedicada** (GED-19397). **Neoenergia** = subseção BESS para controle de injeção (SCRPI) + Termo Zero Grid. **Enel** = diagramas de paralelismo permanente bateria/rede (BT e MT). **Cemig/Equatorial** = bateria como atributo do projeto de GD (FV despachável, modulação ≥ 20%). **Energisa/Copel** = não confirmado. |
| **Organização documental** | Estilo "regras básicas em bloco único" (CPFL GED) vs. norma extensa segmentada por tipo de acessante (Cemig ND-5.31: produtor independente vs. MMGD) vs. processo em fluxo (Enel). |
| **Códigos/numeração** | GED-XXXXX (CPFL/RGE), ND-5.XX (Cemig), NT.00020 (Equatorial), DIS-NOR-0XX (Neoenergia), NDU-0XX (Energisa), NTC 905200 (Copel), GRI-EDBR-CNC (Enel). |
| **Separação BT/MT** | Documentos separados (Energisa NDU-013/015; Cemig ND-5.30/5.31; Neoenergia DIS-NOR-031/033) vs. documento único cobrindo BT+MT (CPFL, Equatorial, Enel). |
| **Certificação INMETRO de baterias** | CPFL: **opcional**. Demais: foco em certificação do inversor; bateria conforme IEC quando aplicável. |
| **Controle de injeção** | Zero-grid (CPFL/Neoenergia) vs. limitação de potência injetada parametrizada por orçamento (CPFL híbrido/Equatorial). |
| **Tempos de anti-ilhamento** | CPFL GED-19397/15303: ≤ 2 s (interrupção) e ≤ 0,2 s (cessar injeção ao sair de faixa); intertravamento a ≤ 0,7 p.u. — demais não confirmados numericamente nesta leitura. |

---

# SUGESTÃO DE ESTRUTURA DE SEÇÕES CONSOLIDADA (estado da prática → NRM CERPRO)

Sintetizada a partir das normas verificadas (alinhada também à estrutura prevista no plano da CERPRO):

```
1.  Objetivo
2.  Campo / Âmbito de Aplicação
3.  Referências (ANEEL, PRODIST, ABNT/IEC/IEEE, normas internas)
4.  Definições e Siglas
5.  Responsabilidades (acessante, RT, distribuidora)
6.  Modalidades de SAE
    6.1 SAE sem GD ("junto à carga" / zero-grid)
    6.2 SAE híbrido on-grid (SAE + MMGD)
    6.3 Modos operacionais (on-grid / off-grid / ilha interna)
7.  Requisitos técnicos por porte e tensão (BT / MT; faixas de potência)
8.  Proteção, seccionamento e manobra
    8.1 Tabela de proteção por porte (funções ANSI)
    8.2 Anti-ilhamento e intertravamento (tempos, limiares p.u.)
    8.3 Transformador de acoplamento e religador (limiares de potência)
9.  Controle P/Q e qualidade de energia (PRODIST Mód. 8; FRT; 4 quadrantes)
10. Medição (bidirecional; direta/indireta; PCS/EMS; supervisão remota)
11. Segurança e prevenção/combate a incêndio (monitoramento BMS, DPS, aterramento)
12. Exigências ambientais e descarte (O&M, fim de vida das baterias)
13. Comissionamento, ensaios e O&M
14. Solicitação de acesso — etapas e prazos
    (consulta → orçamento estimado → pedido → orçamento de conexão →
     contrato/acordo operativo → obras → vistoria → energização)
15. Documentação exigida
    (ART/responsabilidade técnica; diagramas unifilares; memorial descritivo;
     formulário de dados do SAE; certificados/registro INMETRO; declaração
     zero-grid/limitação de injeção; placas de advertência)
16. Responsabilidades adicionais / Relacionamento Operacional / Acordo Operativo
17. Disposições transitórias e vigência
18. Anexos
    A. Arranjos/diagramas de referência (BT e MT; paralelismo permanente bateria/rede)
    B. Formulário de solicitação / dados técnicos do SAE
    C. Placas de advertência
    D. Documentação técnica e de segurança (lista de normas de referência)
    E. Matriz de rastreabilidade (requisito → fonte → Obrigatório-ANEEL vs. Critério-distribuidora)
```

**Referências cruzadas de boa prática a adotar:** o **bloco 6/8/15/18** espelha diretamente a
GED-19397 (CPFL); o **fluxo de etapas (14)** espelha Cemig ND-5.31 e Equatorial NT.020; os
**diagramas de paralelismo bateria/rede (Anexo A)** espelham Enel (Anexos C/E); o **Termo Zero
Grid** e o **SCRPI** espelham Neoenergia (Anexo I / item 7.13).

---

# FONTES (URLs)

**[VERIFICADO via fetch]**
- CPFL GED-19397 (SAE) — https://sites.cpfl.com.br/documentos-tecnicos/GED-19397.pdf
- CPFL GED-15303 (MMGD) — http://sites.cpfl.com.br/documentos-tecnicos/GED-15303.pdf
- CPFL — índice de normas técnicas — https://www.cpfl.com.br/normas-tecnicas
- Cemig ND-5.31 (MT) — https://www.cemig.com.br/wp-content/uploads/2025/10/ND_5.31_Conexao-em-MT-.pdf
- Equatorial NT.00020.EQTL Rev.06 — https://ceee.equatorialenergia.com.br/wp-content/uploads/2026/01/NT.00020.EQTL-06-Conexao-de-Micro-e-Minigeracao-Distribuida-ao-Sistema-de-Distribuicao.pdf
- Neoenergia DIS-NOR-031 — https://www.neoenergia.com/documents/d/sp/dis-nor-031-pdf?download=true
- Enel GRI-EDBR-CNC-GRI-0005 — https://www.eneldistribuicao.com.br/rj/documentos/Conexao%20de%20Micro%20e%20Minigera%C3%A7ao%20Distribu%C3%ADda%20ao%20Sistema%20El%C3%A9trico%20da%20Enel%20Grids%20Brasil_3.0.pdf

**[NÃO CONFIRMADO — metadados de busca/portal; baixar manualmente p/ verificação]**
- Energisa NDU-013 (BT) — https://www.energisa.com.br/sites/energisa/files/media/documents/2025-02/NDU%20013%20-%20Crit%C3%A9rios%20para%20a%20Conex%C3%A3o%20em%20Baixa%20Tens%C3%A3o%20de%20Acessantes%20de%20Gera%C3%A7%C3%A3o%20Distribu%C3%ADda%20ao%20Sistema%20de%20Distribui%C3%A7%C3%A3o.pdf
- Energisa NDU-015 (MT) — https://www.energisa.com.br/sites/energisa/files/media/documents/2025-12/NDU%2015%20-%20...pdf
- Copel NTC 905200 — https://www.copel.com/normas
- Cemig ND-5.30 (BT) — base https://www.cemig.com.br (URL de 2024 retornou 404; localizar versão vigente)
- Neoenergia DIS-NOR-033 (Mini/MT) e DIS-NOR-067 (Acesso) — https://www.neoenergia.com/web/bahia/sua-casa/normas-tecnicas

**Contexto federal (não é norma de distribuidora):**
- ANEEL — SAE com centrais geradoras (orientações 10/10/2025) — https://www.gov.br/aneel/pt-br/centrais-de-conteudos/manuais-modelos-e-instrucoes/geracao/registro-autorizacao-e-concessao-de-empreendimentos-de-geracao/sistemas-de-armazenamento-de-energia-eletrica-sae-com-centrais-geradoras

---

# LACUNAS (o que não foi confirmado)
1. **Energisa (NDU-013/015):** bloqueio Akamai 403 — corpo não lido. Confirmar estrutura e se há
   tratamento de SAE/BESS. **Baixar manualmente.**
2. **Copel (NTC 905200):** PDF oficial não lido (só repositórios terceiros). Confirmar índice e SAE.
3. **CPFL GED-15303 vigente:** a cópia lida é a v1.7/2020 (base REN 482). A versão atual (sob REN
   1.000, com "Anexo I – Limitação de Potência Injetada" citado pela GED-19397) **não foi lida**.
4. **Cemig ND-5.30 (BT):** URL de 2024 com 404 — localizar versão vigente; e confirmar a edição
   out/2025 da ND-5.31.
5. **Light, RGE (norma própria), EDP:** não cobertos por leitura direta nesta rodada (RGE está sob
   guarda-chuva CPFL/GED; Light e EDP pendentes).
6. **Detalhes numéricos de anti-ilhamento/qualidade** das normas não-CPFL (tempos, limiares p.u.,
   FRT) não foram tabulados por completo — exigem leitura dirigida dos PDFs já baixados.
7. **REN de SAE da ANEEL:** ainda em tramitação; quando publicada, reclassificar requisitos
   "Critério da distribuidora" que virarem "Obrigatório-ANEEL".
