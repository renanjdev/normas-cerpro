# NTC-D-XX — Conexão de Sistemas BESS (v01/2026, R0) — minuta da Engenharia CERPRO

> Extração fiel (texto) do documento enviado pela CERPRO. Fonte primária — não editar; usar como referência.

CERPRO
Cooperativa de Eletrificação Rural da Região de Promissão
NTC-D-XX
NORMA TÉCNICA E PADRONIZAÇÃO
REQUISITOS E PROCEDIMENTOS PARA CONEXÃO DE
SISTEMAS BESS
(Battery Energy Storage Systems)
AO SISTEMA DE DISTRIBUIÇÃO DA CERPRO
Versão 01/2026 — Revisão R0
Elaborado por Engenharia CERPRO
Aprovado pelo Grupo Técnico de Padronização
CONTROLE DE REVISÕES
SUMÁRIO
CONTROLE DE REVISÕES	2
SUMÁRIO	3
1. APRESENTAÇÃO	4
2. CAMPO DE APLICAÇÃO	6
2.1 Aplicação	6
2.2 Não aplicação	6
3. OBJETIVO	8
4. REFERÊNCIAS NORMATIVAS E DOCUMENTAIS	9
4.1 Resoluções, Procedimentos e Portarias	9
4.3 Normas ABNT	9
4.4 Normas IEC	11
4.5 Normas IEEE	12
4.6 Normas internacionais de segurança contra incêndio (NFPA / UL)	12
4.7 Normas Regulamentadoras do Ministério do Trabalho	13
5. RESPONSABILIDADES	14
6. TERMOS E DEFINIÇÕES	15
7. CRITÉRIOS BÁSICOS DE CONEXÃO	18
7.1 BESS sem Geração Distribuída	18
7.2 BESS cem Geração Distribuída (Sistemas Hibridos)	21
7.3 Requisitos Ambientais	22
7.4 Requisitos de Segurança	22
7.4 Requisitos de Qualidade de Energia	22
7.4 Requisitos de Operação, Manutenção e Descarte	23
7.4 Responsabilidades Adicionais	24
7.4 Forma de protocolo	25
8. ETAPAS E DOCUMENTOS PARA VIABILIZAÇÃO DO ACESSO	26
8.1 Fluxo processual	26
1. APRESENTAÇÃO
A CERPRO — Cooperativa de Eletrificação Rural da Região de Promissão, permissionária do serviço público de distribuição regulada pela Agência Nacional de Energia Elétrica (ANEEL), consolida neste documento as diretrizes técnicas, procedimentais, ambientais e de segurança para a conexão de Sistemas BESS (Battery Energy Storage Systems) ao seu sistema de distribuição.
1.1 ESS e BESS
É essencial distinguir, desde o início, os conceitos de ESS e BESS, que possuem relação hierárquica — não são sinônimos.
ESS (Energy Storage System) e seu equivalente em português SAE (Sistema de Armazenamento de Energia) designam a FAMÍLIA GERAL de todos os sistemas capazes de armazenar energia para uso posterior, independentemente da forma física de armazenamento. A família ESS/SAE inclui, entre outras tecnologias:
PHES (Pumped Hydro Energy Storage) — bombeamento hidrelétrico reversível (atualmente a modalidade com maior capacidade instalada em escala global);
CAES (Compressed Air Energy Storage) — armazenamento por ar comprimido em cavernas subterrâneas;
Flywheels — volantes de inércia que armazenam energia cinética em discos giratórios de alta velocidade;
TES (Thermal Energy Storage) — armazenamento térmico (p.ex. sal fundido em usinas termossolares);
Hidrogênio — produção via eletrólise, estocagem e reconversão eletroquímica (P2G/P2P);
Capacitores e supercapacitores — armazenamento eletrostático;
SMES (Superconducting Magnetic Energy Storage) — armazenamento eletromagnético;
BESS (Battery Energy Storage System) — armazenamento eletroquímico em baterias.
BESS é, portanto, um SUBCONJUNTO ESPECÍFICO da família ESS/SAE — corresponde apenas aos sistemas cuja tecnologia de armazenamento se baseia em baterias eletroquímicas.
Esta NTC-D-XX disciplina EXCLUSIVAMENTE os sistemas BESS, por serem o tipo predominante em aplicações behind-the-meter e em sistemas de distribuição da CERPRO.
Demais tecnologias da família ESS/SAE estão fora do escopo desta norma e, quando forem objeto de pedido de acesso, serão tratadas caso a caso pela CERPRO, em regulamentação específica.
Assim, ao longo deste documento:
"BESS" é o termo técnico principal e refere-se ao sistema de armazenamento por baterias objeto desta norma;
"ESS" e "SAE" são empregados apenas quando a referência doutrinária, normativa ou legal trata da família geral.
1.2 Modalidades contempladas
As modalidades de BESS contempladas por esta norma são:
BESS junto à carga (behind-the-meter), sem microgeração ou minigeração distribuída associada;
BESS híbrido, em conjunto com microgeração ou minigeração distribuída (MMGD);
2. CAMPO DE APLICAÇÃO
2.1 Aplicação
Esta norma aplica-se a todas as unidades consumidoras conectadas (ou com pedido de conexão protocolado) ao sistema de distribuição da CERPRO, em baixa tensão (BT, tensão nominal < 2,3 kV) ou média tensão (MT, 2,3 kV ≤ tensão nominal < 69 kV), que desejem instalar, ampliar, substituir ou operar Sistemas BESS, com ou sem geração distribuída associada.
Aplica-se também a empreendimentos que utilizem BESS para:
backup / UPS;
integração de fontes renováveis (peak-shifting, smoothing, firming);
compensação reativa / correção de fator de potência local;
arbitragem tarifária (load shifting, peak shaving);
operação ilhada intencional de microrredes e sistemas críticos.
2.2 Não aplicação
Não são objeto desta norma:
2.2.1 Outras tecnologias da família ESS/BESS
Considerando que esta NTC tem por objetivo disciplinar especificamente o armazenamento eletroquímico em baterias (BESS), ficam fora de seu escopo as seguintes tecnologias de armazenamento de energia (ESS), ainda que conectadas ao sistema da CERPRO:
PHES (Pumped Hydro Energy Storage) — armazenamento por bombeamento hidrelétrico;
CAES (Compressed Air Energy Storage) — armazenamento por ar comprimido;
Flywheels — volantes de inércia (armazenamento cinético);
TES (Thermal Energy Storage) — armazenamento térmico (ex.: sal fundido, gelo, materiais de mudança de fase);
Hidrogênio e célula a combustível — armazenamento químico por eletrólise e reconversão (Power-to-Gas / Power-to-Power);
Capacitores e supercapacitores — armazenamento eletrostático;
SMES (Superconducting Magnetic Energy Storage) — armazenamento eletromagnético.
Eventuais solicitações de acesso que envolvam tais tecnologias poderão ser analisadas pela CERPRO caso a caso, mediante regulamentação específica, observadas as diretrizes legais aplicáveis, bem como a regulamentação superveniente da ANEEL.
2.2.2 Outras situações excluídas do escopo
sistemas fotovoltaicos sem BESS (ver NTC-D-09);
baterias automotivas e veiculares não-estacionárias (EV, V2G, V2H e V2X móveis);
sistemas BESS off-grid permanentes, sem qualquer interface com a rede da CERPRO;
conexões em alta tensão (≥ 69 kV), que serão objeto de regulamentação específica em conjunto com o ONS.
3. OBJETIVO
Estabelecer critérios técnicos, procedimentos, documentação mínima, requisitos de segurança, requisitos ambientais e obrigações das partes baseando sempre nos órgãos regulatórios e normativos brasileiros quando existentes, ou passa a prevalecer essa norma caso não exista regulação ou normas especificas dos orgãos, para que o acessante possa projetar, protocolar, instalar, comissionar, operar e descomissionar Sistemas BESS (Battery Energy Storage Systems) conectados ao sistema de distribuição da CERPRO, de forma a preservar a segurança das pessoas, das instalações e do meio ambiente, bem como a qualidade e a continuidade do serviço de distribuição.
4. REFERÊNCIAS NORMATIVAS E DOCUMENTAIS
Este capítulo apresenta, com breves comentários explicativos, todas as bases legais, regulatórias, normativas e documentais que fundamentam a NTC-D-XX. As referências são citadas nos demais capítulos e anexos desta norma e devem ser observadas pelo acessante em toda a vigência do BESS.
4.1 Resoluções, Procedimentos e Portarias
REN ANEEL nº 956/2021 — que estabelece os Procedimentos de Distribuição de Energia Elétrica no Sistema Elétrico Nacional, e suas atualizações
REN ANEEL nº 1.000/2021 — que estabelece as Regras de Prestação do Serviço Público de Distribuição de Energia Elétrica, e suas atualizações.
PRODIST Módulo 3 — Conexão ao Sistema de Distribuição de Energia Elétrica
PRODIST Módulo 8 — Qualidade da Energia Elétrica
Portaria INMETRO nº 140/2022 — RTQ/RAC/ENCE para equipamentos de geração, condicionamento e armazenamento fotovoltaico. Estabelece o registro INMETRO OBRIGATÓRIO para baterias (inclusive de lítio), inversores e inversores híbridos on-grid com bateria até 75 kW. Exige BMS em baterias de lítio, sódio e similares, e cita explicitamente as normas IEC 62619 e ABNT NBR 16976.
Portaria INMETRO nº 515/2023 — Requisitos para Conversores FV conectados à rede. Base técnica dos ajustes de proteção da Tabela do item 9.1.1 desta NTC.
Portaria INMETRO nº 17/2016 — Portaria antecessora que dispõe sobre critérios gerais de avaliação da conformidade — invocada para casos de transição.
Resolução ANEEL nº 616/2014 — Define limites de exposição humana a campos elétricos, magnéticos e eletromagnéticos em frequências até 300 GHz. Aplicável ao entorno do BESS (Cap. 12.3).
Resolução CONAMA nº 237/1997 — Critérios e procedimentos de licenciamento ambiental. Fundamento para exigência, pelos órgãos estaduais (IAT/PR, CETESB/SP etc.), de licença para BESS de maior porte em ambiente externo.
Resolução CONAMA nº 401/2008 — Regula a coleta, reutilização, reciclagem, tratamento e disposição final ambientalmente adequada de pilhas e baterias que contenham chumbo, cádmio, mercúrio e seus compostos. Complementa a Lei 12.305/2010 no regime de logística reversa.
4.3 Normas ABNT
ABNT NBR 17.153:2023 — Sistemas de Armazenamento de Energia (BESS) — ESPINHA DORSAL desta NTC-D-XX. O título da norma usa o termo amplo "BESS" (família ESS), mas seu conteúdo técnico é fortemente orientado a BESS (sistemas eletroquímicos por baterias), que é o subconjunto aplicável a esta NTC. Estabelece requisitos de projeto, integração, BMS, PCS, EMS, segurança, ensaios e comissionamento. Aderência integral exigida no Memorial Descritivo (Anexo B). Quando a NBR 17.153 tratar de tecnologias não-BESS (p.ex. referências a CAES, flywheel), tais seções não se aplicam a esta NTC.
ABNT NBR 5410:2004 — Instalações elétricas de baixa tensão até 1 kV CA ou 1,5 kV CC. Base para o projeto do lado carga do BESS, incluindo condutores, proteções, aterramento e DPS.
ABNT NBR 14039 — Instalações elétricas de média tensão (1,0 kV a 36,2 kV). Aplicável ao transformador de acoplamento, cabine primária, disjuntor de MT e chaveamento do BESS acima de 75 kW.
ABNT NBR 5419:2015 — Proteção contra descargas atmosféricas. Exige DPS adequados e SPDA para gabinetes externos, estruturas de suporte do BESS e equipamentos associados.
ABNT NBR 14519:2011 — Medidores eletrônicos de energia ativa. Referência metrológica para os medidores de faturamento utilizados no ponto de conexão do BESS.
ABNT NBR 15479 / 15688 / 15751 — Conjunto de normas de aterramento: medição de resistência, sistemas aéreos de MT e aterramento de subestações. Aplicável ao projeto de aterramento do BESS (Cap. 9.2.9).
ABNT NBR 16149:2013 e ABNT NBR 16150:2013 — Características da interface de conexão com a rede elétrica e procedimentos de ensaio de conformidade. Definem os ajustes padrão de proteção de PCS/inversores em BT (Tabela do item 9.1.1).
ABNT NBR IEC 62116:2012 — Procedimento de ensaio de anti-ilhamento para inversores interativos. Ensaio OBRIGATÓRIO no comissionamento do BESS (Cap. 14.1.2).
ABNT NBR 16690 — Instalações elétricas de arranjos fotovoltaicos — requisitos de projeto. Aplicável ao lado FV de BESS híbridos DC-coupled.
ABNT NBR 16767:2019 — Baterias chumbo-ácido estacionárias para sistemas fotovoltaicos. Aplicável a BESS com química de chumbo-ácido, inclusive para backup/UPS.
ABNT NBR 16975:2021 e ABNT NBR 16976:2021 — Baterias de lítio-íon estacionárias — requisitos de segurança e desempenho. Normas brasileiras de referência para células/módulos de lítio, exigidas pela Portaria INMETRO 140/2022.
ABNT NBR 10151 — Acústica — Avaliação do ruído em áreas habitadas. Referência para o compromisso de ruído do conjunto PCS + HVAC + transformador do BESS (Cap. 12.2).
ABNT NBR 17240 — Sistemas de detecção e alarme de incêndio para projeto, instalação, comissionamento e manutenção. Complementa a NFPA 72 no contexto brasileiro (Cap. 13.4).
4.4 Normas IEC
IEC 60364 — Série internacional de instalações elétricas em BT. Análoga à ABNT NBR 5410, útil como referência cruzada em projetos de BESS importados ou multinacionais.
IEC 60896 — Baterias estacionárias chumbo-ácido — requisitos gerais e métodos de ensaio. Exigida para BESS chumbo-ácido (Portaria INMETRO 140/2022, Seção 5.3).
IEC 61140 — Protection against electric shock — princípios fundamentais. Base técnica da classificação de equipamentos e sistemas de proteção do BESS.
IEC 61439-1 e 61439-2 — Conjuntos de manobra e comando de baixa tensão — requisitos gerais e conjuntos industriais. Aplicável a quadros, CCMs e gabinetes CA do BESS.
IEC 61850 — Comunicação em subestações de energia elétrica — protocolo moderno para automação. OBRIGATÓRIA para BESS > 500 kW ou integrados a subestações da CERPRO (Cap. 10.2.1).
IEC 62040-1/-2/-3 — Uninterruptible Power Supplies (UPS) — requisitos gerais, EMC e desempenho. Aplicável a BESS cuja finalidade seja UPS.
IEC 62109-2 — Safety of power converters for use in photovoltaic power systems — inversores. Exigência da Portaria INMETRO 140/2022 para inversores híbridos e on-grid com bateria.
IEC 62116 — Utility-interconnected photovoltaic inverters — Test procedure of islanding prevention measures. Ensaio laboratorial de anti-ilhamento.
IEC 62133 — Secondary cells and batteries containing alkaline or other non-acid electrolytes. Aplicável a baterias portáteis/industriais — citada pela Portaria INMETRO 140/2022.
IEC 62619 — Safety requirements for secondary lithium cells and batteries for use in industrial applications. NORMA-CHAVE para BESS de lítio; obrigatória para células/módulos conforme Portaria INMETRO 140/2022 Seção 5.3.9.
IEC 62620 — Secondary lithium cells and batteries containing alkaline or other non-acid electrolytes — industrial applications. Performance e testes.
IEC 62933-2-1 — Electrical Energy Storage (EES) systems — Part 2-1: Unit parameters and testing methods. Escopo: família EES/ESS em geral. Base para declaração padronizada de parâmetros (kWh, kW, RTE, ciclos) no Anexo A — aplicável ao BESS como subconjunto do EES.
IEC 62933-5-1 — EES — Safety considerations for grid-integrated EES systems. Escopo: família EES/ESS em geral, mas com seções específicas para baterias eletroquímicas, que são as efetivamente aplicáveis a esta NTC. COMPLEMENTO INTERNACIONAL da NFPA 855 para integração de BESS à rede (Cap. 13).
IEC 62933-5-2 — EES — Safety requirements for grid-integrated EES systems — electrochemical-based systems. Parte da série 62933 dedicada EXCLUSIVAMENTE a sistemas eletroquímicos (BESS). Norma diretamente aplicável.
IEC 62443 — Industrial communication networks — IT security for industrial automation and control systems. Exigida para EMS e SCADA do BESS > 500 kW (Cap. 10.2.3).
4.5 Normas IEEE
IEEE Std 242-2001 (Buff Book) — Recommended Practice for Protection and Coordination of Industrial and Commercial Power Systems. Referência para estudos de coordenação e seletividade (Anexo K).
IEEE Std 519-2014 — Recommended Practice and Requirements for Harmonic Control in Electric Power Systems. Complementa o PRODIST Módulo 8 nos limites de harmônicos gerados pelo PCS.
IEEE Std 1547-2018 e 1547.1-2005 — Standard for Interconnection and Interoperability of Distributed Energy Resources. Principal referência internacional para interconexão de DER (inclusive BESS) com sistemas de distribuição.
IEEE Std 1547.4-2011 — Guide for Design, Operation, and Integration of Distributed Resource Island Systems with Electric Power Systems. Aplicável a BESS em microrredes e ilhamento intencional.
IEEE Std 2030.3-2016 — Standard Test Procedures for Electric Energy Storage Equipment and Systems for Electric Power Systems Applications. Escopo: família ESS (inclui BESS, flywheels, CAES etc.). Para fins desta NTC, aplicam-se os procedimentos de ensaio específicos para BESS.
4.6 Normas internacionais de segurança contra incêndio (NFPA / UL)
NFPA 855:2023 — Standard for the Installation of Stationary Energy Storage Systems — NORMA INTERNACIONAL PRIMÁRIA adotada por esta NTC para toda a matéria de segurança (Cap. 13). O título refere-se a "ESS estacionários" (família), mas a norma é majoritariamente dedicada a sistemas ELETROQUÍMICOS (BESS) — Capítulo 9 da NFPA 855 trata especificamente de baterias. Os capítulos para flywheels e CAES existem, mas não se aplicam a esta NTC. Define capacidades máximas por grupo (Tabela 7), distâncias mínimas (Tabela 8), compartimentação 2 h, ventilação, detecção, supressão, controle de deflagração e planos de emergência.
NFPA 68 — Standard on Explosion Protection by Deflagration Venting. Base para o venteio explosivo no teto exigido no item 13.6 desta NTC.
NFPA 69 — Standard on Explosion Prevention Systems. Alternativa ao venteio, por ventilação ou inertização, para o controle de deflagração.
NFPA 70 (NEC) — National Electrical Code — código elétrico estadunidense. Referência técnica adicional para projeto e aterramento de BESS, com aplicação subsidiária.
NFPA 72 — National Fire Alarm and Signaling Code. Referência conjuntamente com a ABNT NBR 17240 para a detecção e sinalização de incêndio do BESS.
UL 9540 — Energy Storage Systems and Equipment. O título é amplo (família ESS), mas na prática a certificação aplica-se majoritariamente a BESS — é a certificação do SISTEMA BESS INTEGRADO. Exigida ou aceita nesta NTC como alternativa ao UL 1973 isolado (Cap. 8.2.4).
UL 9540A — Test Method for Evaluating Thermal Runaway Fire Propagation in BATTERY Energy Storage Systems. Diferentemente da UL 9540, este método de ensaio é EXCLUSIVAMENTE BESS-específico (só faz sentido para sistemas eletroquímicos, onde ocorre thermal runaway). Ensaio CRÍTICO — seu relatório é obrigatório em BESS indoor, químicas NMC/NCA/LCO e permite flexibilizar distâncias mínimas da NFPA 855.
UL 1973 — Standard for Batteries for Use in Stationary, Vehicle Auxiliary Power and Light Electric Rail Applications. Aceita para certificação de baterias estacionárias.
UL 1974 — Standard for Evaluation for Repurposing Batteries. Aplicável quando o projeto utilizar baterias de segunda vida (Cap. 12.7.3).
4.7 Normas Regulamentadoras do Ministério do Trabalho
NR-10 — Segurança em Instalações e Serviços em Eletricidade — Obrigatória para todo trabalhador que opere ou mantenha o BESS. Define qualificação, habilitação, EPI, procedimentos de segurança e documentação técnica (Prontuário de Instalações Elétricas).
NR-10 SEP (Anexo I) — Aplica-se a trabalhos no Sistema Elétrico de Potência (SEP). OBRIGATÓRIA para responsáveis técnicos e equipes em BESS conectado em MT.
NR-33 — Segurança e Saúde nos Trabalhos em Espaços Confinados — Aplicável a containers e gabinetes metálicos de BESS quando caracterizados como espaço confinado; exige PET, supervisor, ventilação, monitoramento de gases e resgate.
NR-35 — Trabalho em Altura — Aplicável à montagem, manutenção e inspeção em racks altos e estruturas elevadas do BESS.
5. RESPONSABILIDADES
Compete aos órgãos de mercado, planejamento, operação, automação, proteção,
atendimento e ligação, a responsabilidade de cumprir as disposições desta norma.
6. TERMOS E DEFINIÇÕES
Para fins desta norma, além das definições da NTC-D-09 e do PRODIST Módulo 1, aplicam-se os termos a seguir. Observar especialmente a hierarquia conceitual ESS/BESS (família) → BESS (subconjunto eletroquímico por baterias) descrita no item 1.1.
6.1 Acessada — A CERPRO.
6.2 Acessante — Pessoa física ou jurídica que solicita ou possui conexão de BESS.
6.3 Acumulador — Dispositivo ou módulo que armazena energia (em qualquer forma: química, eletroquímica, mecânica, térmica, eletrostática ou eletromagnética).
6.4 ATS — Automatic Transfer Switch (chave de transferência automática).
6.5 BESS — Battery Energy Storage System. Subconjunto específico da família ESS/BESS, em que o armazenamento de energia é ELETROQUÍMICO, realizado por BATERIAS. Sistema completo composto por módulos de bateria, BMS, PCS, EMS, HVAC, proteções e gabinete. Sinônimo em português (pouco utilizado): BESS-B ou BESSB. É o OBJETO EXCLUSIVO desta NTC-D-XX.
6.6 BMS — Battery Management System; responsável por monitorar e proteger a bateria (tensão, corrente, temperatura, SOC, SOH; atua em sobrecarga, sobredescarga, sobrecorrente, sobretemperatura, curto-circuito e desbalanceamento; prevenção ativa de thermal runaway).
6.7 Bateria de fluxo — Tecnologia de estado líquido (vanádio, zinco-bromo).
6.8 Behind-the-meter (BTM) — Sistema atrás do medidor de faturamento.
6.9 Benefit stacking — Agregação de múltiplas receitas/serviços de um mesmo BESS.
6.10 Black start — Restabelecimento da rede sem energia externa.
6.11 BOL/EOL — Begin/End of Life; condição da bateria no início e fim de vida útil.
6.12 C-rate — Razão corrente de carga/descarga pela capacidade nominal.
6.13 DoD — Depth of Discharge (profundidade de descarga).
6.14 DSV — Dispositivo de Seccionamento Visível.
6.15 Elemento de Desconexão — Dispositivo de seccionamento visível e travável.
6.16 Elemento de Interrupção — Dispositivo que desconecta automaticamente o BESS da rede em caso de falha.
6.17 EMS — Energy Management System; coordena carga/descarga, despacho, P/Q, SCRPI e SCADA.
6.18 FRT/LVRT/HVRT — Fault/Low-Voltage/High-Voltage Ride-Through.
6.19 Hard Limit — Limite rígido de injeção, em hardware independente do software.
6.20 HVAC — Sistema de climatização (ar forçado ou líquido).
6.21 Ilhamento intencional — Operação isolada deliberada com abertura física certificada.
6.22 Ilhamento não intencional — Energização da rede desenergizada pelo BESS. PROIBIDO.
6.23 LEL — Lower Explosive Limit.
6.24 LFP (LiFePO₄) — Lítio-ferro-fosfato; química RECOMENDADA como padrão.
6.25 Li-ion NMC — Lítio-níquel-manganês-cobalto; maior energia, MAIOR RISCO de thermal runaway.
6.26 LPI — Limitação de Potência Injetada.
6.27 MMGD — Micro e Minigeração Distribuída.
6.28 Modo Fail Safe — Em falha, SCRPI reduz potência ao menor valor em até 15 s.
6.29 Off-gassing / Venting — Liberação de gases inflamáveis/tóxicos em falha incipiente (pré-combustão).
6.30 On-Grid / Off-Grid / Zero-Grid — Operação conectada, isolada, ou conectada com injeção nula.
6.31 PCS — Power Conversion System (inversor bidirecional).
6.32 Peak shaving — Redução de demanda via descarga no pico.
6.33 PIP — Pre-Incident Plan (plano de resposta pré-incidente, NFPA 855).
6.34 RTE — Round-Trip Efficiency (eficiência de ciclo completo).
6.35 ESS (Energy Storage System) — FAMÍLIA GERAL de sistemas capazes de armazenar energia elétrica, térmica, cinética, química ou eletromagnética para uso posterior. Abrange, entre outras, PHES, CAES, flywheels, TES, hidrogênio/célula a combustível, capacitores, SMES e BESS. O termo equivalente em português, consagrado pela ABNT NBR 17.153:2023 e pela Lei 15.269/2025, é BESS. Esta NTC utiliza "ESS" e "BESS" indistintamente quando se refere à família geral, e "BESS" quando trata do subconjunto eletroquímico.
6.35-A BESS — Sistema de Armazenamento de Energia. Equivalente em português de ESS (ver item 6.35). Não confundir com BESS: o BESS é a família geral; o BESS é um subconjunto dela (o eletroquímico por baterias).
6.35-B PHES — Pumped Hydro Energy Storage. Armazenamento por bombeamento hidrelétrico; é ESS, NÃO é BESS. Fora do escopo desta norma.
6.35-C CAES — Compressed Air Energy Storage. Armazenamento por ar comprimido; é ESS, NÃO é BESS. Fora do escopo desta norma.
6.35-D Flywheel — Volante de inércia. Armazenamento cinético; é ESS, NÃO é BESS. Fora do escopo desta norma.
6.35-E TES — Thermal Energy Storage. Armazenamento térmico (sal fundido, gelo, PCM); é ESS, NÃO é BESS. Fora do escopo desta norma.
6.36 SCEE — Sistema de Compensação de Energia Elétrica.
6.37 SCRPI — Sistema de Controle de Redução da Potência Injetável.
6.38 SMF — Sistema de Medição para Faturamento.
6.39 SoC / SoH — State of Charge / State of Health.
6.40 STS — Static Transfer Switch.
6.41 Swiss Cheese Model — Defesa em Profundidade, estratégia de camadas redundantes de segurança.
6.42 Thermal runaway — Reação exotérmica auto-sustentada de célula ou módulo.
6.43 UC — Unidade Consumidora.
6.44 UPS — Uninterruptible Power Supply.
7. CRITÉRIOS BÁSICOS DE CONEXÃO
7.1 BESS sem Geração Distribuída
7.1.1 Considerações Iniciais
A aplicação de sistemas de armazenamento de energia (BESS) junto às cargas, na ausência de geração distribuída, permite a execução de diversas funções operacionais relevantes.
Entretanto, esses arranjos não devem permitir a injeção de potência ativa na rede da distribuidora. Em outras palavras, o sistema deve operar exclusivamente para atendimento da carga local, mantendo a funcionalidade de “zero-grid” no que se refere à exportação de energia.
Nesse contexto, destacam-se as seguintes funcionalidades:
Backup / UPS
Garantia de continuidade do fornecimento de energia em caso de falhas ou interrupções da rede.
Compensação de Reativos Local
Melhoria do fator de potência e suporte à qualidade de energia da instalação.
Arbitragem / Peak Shaving
Otimização do consumo energético por meio do armazenamento em horários de menor custo e utilização em períodos de maior demanda ou tarifa.
7.1.2 Requisitos de Conexão
Será permitida a operação do sistema de armazenamento de energia (BESS) em paralelo com a rede de distribuição da CERPRO, desde que sejam atendidos todos os requisitos estabelecidos ao longo deste documento, com destaque para a condição obrigatória de não injeção de potência ativa no sistema de distribuição.
A conexão física do BESS à rede da CERPRO, seja em baixa tensão (BT) ou em média tensão (MT), deverá atender aos seguintes requisitos normativos:
Para conexão em BT: atendimento à Norma Técnica CERPRO NTC D04;
Para conexão em MT: atendimento ao conjunto de documentos da Norma Técnica CERPRO NTC D03.
Destaca-se que sistemas BESS com potência superior a 75 kW deverão:
Ser conectados por meio de transformador de acoplamento, adequado aos níveis de tensão do ponto de conexão;
Possuir proteção por disjuntor atuante em média tensão;
Contar com relé de proteção, com, no mínimo, as funções especificadas neste documento.
Adicionalmente, para sistemas com potência instalada superior a 300 kW, mesmo na ausência de exportação de energia, será obrigatória a instalação de:
Religador no ponto de conexão do circuito alimentador onde ocorre o paralelismo com a rede da distribuidora;
Equipamento com recursos de supervisão remota, podendo ter as funções de proteção habilitadas ou não, conforme critério da CERPRO.
Esse equipamento deverá:
Participar do cálculo de proporcionalidade do sistema;
Atender às necessidades de supervisão e controle em tempo real;
Permitir a realização de seccionamento e proteção remota e automática, a partir do Centro de Operação da distribuidora.
O objetivo dessas exigências é garantir a segurança operacional e a qualidade do fornecimento de energia elétrica para todos os consumidores do sistema de distribuição.
7.1.3 Modos de Operação do BESS
Para a conexão de sistemas de armazenamento de energia (BESS) ao sistema elétrico da CERPRO, o consumidor deverá garantir a implementação dos seguintes modos operacionais:
• Operação On-Grid¹
Neste modo, o sistema opera em paralelo com a rede da distribuidora, devendo atender às seguintes condições:
Não injeção de potência ativa (W) na rede elétrica da distribuidora;
Permissão para operação do banco de baterias na prestação de serviços ancilares, tais como:
compensação de potência reativa;
mitigação de distúrbios de qualidade da energia elétrica;
Permissão para arbitragem energética, especialmente para consumidores com tarifas binômias, possibilitando:
carregamento das baterias em períodos de menor tarifa;
utilização da energia armazenada em horários de maior custo.
Nota (1): No momento da conexão, o consumidor deverá indicar, no formulário correspondente, quais funcionalidades estarão habilitadas no sistema de armazenamento de energia.
• Operação Off-Grid²
Neste modo, o sistema opera de forma isolada (ilhada), tipicamente como backup de energia na ausência de fornecimento da CERPRO.
Devem ser garantidas as seguintes condições:
Implementação de ilhamento seguro, evitando qualquer possibilidade de injeção de energia na rede da distribuidora;
Desacoplamento automático da instalação elétrica em caso de ausência da rede.
Nota (2): O arranjo deve prever uma chave de intertravamento, garantindo o desacoplamento imediato da instalação elétrica da rede no momento em que o sistema de armazenamento entrar em operação.
7.1.4 Requisitos Técnicos
Os consumidores que desejam formalizar a solicitação de conexão à rede elétrica da CERPRO, quando da utilização de Sistemas BESS conectadas à rede, deverão apresentar as seguintes informações e documentos:
Documento de identificação do titular (CPF ou CNPJ)
Comprovante de endereço (quando aplicável)
Ato constitutivo / contrato social (PJ);
Procuração com poderes específicos (quando aplicável).
ART
Certidão de Registro e Quitação CREA/CFT do RT, atualizada;
Documento de identificação do Responsável Técnico
Memorial descritivo, contendo:
Dados do empreendimento: identificação do acessante, localização, classe de tensão, demanda/geração associada;
Especificação do sistema de armazenamento (baterias): tecnologia, capacidade nominal, tensão, corrente, configuração e características operacionais;
Especificação do PCS (Power Conversion System): potência nominal, faixas de operação, controle de potência ativa e reativa, modos de operação;
Especificação do BMS (Battery Management System): funcionalidades de monitoramento, proteção, balanceamento e gestão das baterias;
Especificação do EMS (Energy Management System): estratégia de operação, lógica de controle, integração com geração, carga e rede;
Sistema de climatização (HVAC): requisitos e características do controle térmico do ambiente e/ou das baterias;
Memória de cálculo: dimensionamento do sistema, critérios adotados e premissas técnicas;
Plano de Segurança: medidas de prevenção, proteção e mitigação de riscos;
Plano de Emergência: procedimentos para situações de contingência;
Plano de Descomissionamento: diretrizes para desativação e destinação final dos equipamentos.
Diagrama unifilar do projeto elétrico.
Planta Baixa do Sistema (BESS/SAE)
Deverá apresentar, de forma clara e em escala adequada, os seguintes elementos:
Implantação dos equipamentos: localização do gabinete do BESS, PCS, quadros elétricos e sistema de climatização (HVAC);
Acessos operacionais: entradas para operação, manutenção e emergência;
Rotas de fuga: devidamente sinalizadas e desobstruídas, conforme normas de segurança;
FDC (Fire Department Connection): ponto de conexão para combate a incêndio, quando aplicável;
Distâncias mínimas: afastamentos entre equipamentos, limites da edificação e áreas adjacentes, conforme requisitos normativos e do fabricante;
Áreas de segurança: delimitação de zonas de risco e circulação;
Elementos complementares: ventilação, barreiras físicas, sinalização de segurança e eventuais sistemas de proteção contra incêndio.
Estudo de Proteção e Aterramento.
Sistema de Intertravamento e Proteção com as características da chave de intertravamento, sendo aceitas chaves estáticas e chaves eletromecânicas;
Datasheet
Manuais Técnicos
Certificações (ex.: normas IEC), conforme Anexo D, que comprovem o correto funcionamento do sistema.
Certificação INMETRO de durabilidade e de desempenho das baterias conectadas
Certificado INMETRO dos inversores
Datasheet do BESS;
Datasheet dos Inversores
Manuais técnicos/usuário do equipamento
Cronograma físico-financeiro
Apresentação de ensaios ou declaração do fornecedor que comprovem a atuação do sistema de forma a não injetar potência ativa na rede elétrica da distribuidora (Zero Grid).
Anexo B, devendo ser informada, a finalidade do sistema de armazenamento, tais como: back-up de energia, compensação reativa e/ou arbitragem no ponto de conexão.
Ressalta-se que, no referido anexo, também deverão constar as informações operacionais do sistema, incluindo:
Parâmetros de operação, como o fator de potência a ser mantido/corrigido no ponto de conexão;
Programação dos horários de carga e descarga do banco de baterias, quando aplicável à estratégia de arbitragem tarifária.
É obrigatória a fixação de placa de advertência³ na tampa da caixa do medidor, de forma a garantir sua plena visibilidade. Adicionalmente, devem ser previstas placas de advertência nas seguintes situações e locais:
Ponto de entrega aérea: Instalar a placa no postinho, na parede ou na cabine com buchas de passagem, sempre voltada para o lado da via pública, junto à conexão do ramal de ligação (ou ramal de serviço).
Unidade consumidora em edificações com múltiplas unidades:
Nos casos de edifícios de uso coletivo ou com medição agrupada, as placas devem ser instaladas:
No ponto de entrega do edifício (poste);
Na caixa de distribuição, quando existente.
Ponto de entrega subterrânea: Instalar a placa na fachada da edificação, próxima ao número do imóvel/empreendimento, ou na parte mais alta do duto de entrada localizado no poste da distribuidora (CERPRO).
Nota (3): Os requisitos e especificações das placas de advertência para sistemas de armazenamento estão disponíveis no ANEXO C.
7.2 BESS cem Geração Distribuída (Sistemas Hibridos)
7.2.1 Considerações Iniciais
Os sistemas on-grid com armazenamento em baterias, usualmente denominados sistemas híbridos, têm se consolidado como uma solução eficiente para a integração de Micro e Minigeração Distribuída (MMGD), especialmente no atendimento às exigências estabelecidas no artigo 73 da REN nº 1.000/2021.
Além de sua função principal na integração da geração distribuída, esses sistemas oferecem maior flexibilidade operacional, podendo ser utilizados em situações de contingência da rede da distribuidora, contribuindo para a continuidade do fornecimento de energia.
Adicionalmente, embora menos convencional, destaca-se a aplicação desses sistemas na arbitragem tarifária. Nessa estratégia, a energia é armazenada em períodos de menor custo e utilizada em horários de tarifas mais elevadas, o que se mostra particularmente vantajoso para consumidores enquadrados na tarifa branca (Grupo B) e nas modalidades horo-sazonais verde e azul (Grupo A).
7.2.2 Requisitos de Conexão
Será permitida a operação em paralelo do BESS com a rede de distribuição da CERPRO, desde que atendidos todos os requisitos estabelecidos neste documento, especialmente a condição de não injeção de potência ativa no sistema de distribuição.
Conforme a Norma Técnica NTC D09, a CERPRO poderá suspender o paralelismo com o sistema de micro e minigeração distribuída nas seguintes situações:
Durante desligamentos programados;
Em condições de emergência no sistema elétrico;
Quando inspeções identificarem condições inseguras, falhas de manutenção ou deficiências operacionais e de proteção;
Quando a operação da unidade consumidora comprometer o desempenho do sistema elétrico ou não atender aos requisitos de qualidade de energia.
A conexão física do BESS à rede de distribuição, em baixa tensão (rede secundária) ou média tensão (rede primária), deve atender aos requisitos das normas técnicas aplicáveis da CERPRO, conforme o nível de tensão e as características da conexão.
Para centrais de minigeração distribuída, com potência instalada superior a 75 kW, é obrigatória a conexão por meio de transformador de acoplamento, compatível com os níveis de tensão do ponto de conexão, e a instalação de sistema de proteção com disjuntor em média tensão. O sistema de proteção deve contemplar, no mínimo, as funções exigidas na Norma Técnica NTC D09.
Nos casos em que houver necessidade de operação remota do sistema, deverá ser prevista a instalação de religador com telecomando, permitindo a supervisão e controle à distância.
Adicionalmente, sempre que a implantação do sistema implicar em adequações ou reforma do padrão de entrada da unidade consumidora, será obrigatória a instalação de Dispositivo de Proteção contra Surtos (DPS), conforme requisitos normativos aplicáveis.
O arranjo físico da conexão deverá seguir as diretrizes estabelecidas nas normas técnicas da CERPRO, podendo variar em função da distribuidora específica, potência instalada, configuração dos sistemas de medição e proteção existentes, bem como das adequações necessárias para atendimento integral aos requisitos técnicos vigentes.
7.2.3 Modos de Operação do BESS
O consumidor deve assegurar que o BESS atenda aos seguintes modos operacionais:
a) Operação On-Grid (conectado à rede)
Na operação em paralelo com a rede de distribuição, devem ser observados os seguintes requisitos:
O sistema deve respeitar, em todos os regimes de operação, a potência máxima aprovada no Orçamento de Conexão, sob pena de aplicação das sanções cabíveis em caso de descumprimento;
É permitida a utilização do banco de baterias para a prestação de serviços ancilares, tais como compensação de potência reativa e mitigação de distúrbios de qualidade da energia;
É permitida a arbitragem tarifária para consumidores com tarifas binômias, possibilitando o carregamento das baterias em períodos de menor custo e sua utilização em horários de maior tarifa.
Nota: No momento da solicitação de acesso, o consumidor deve indicar, no formulário específico, quais funcionalidades operacionais serão habilitadas no BESS.
b) Operação Off-Grid (modo ilhado)
Na operação isolada da rede de distribuição, devem ser observados os seguintes requisitos:
O sistema deve garantir o ilhamento interno seguro, restrito às instalações da unidade consumidora, de forma a impedir qualquer injeção indevida de energia na rede da concessionária;
O BESS deve assegurar condições adequadas de fornecimento às cargas internas durante a ausência de energia da rede.
Nota: Sistemas com inversores certificados pelo INMETRO, conforme a Portaria nº 140/2022, podem operar sem a necessidade de chave de intertravamento. Para arranjos distintos, é obrigatória a utilização de dispositivos de desconexão/intertravamento.
Os diferentes arranjos de conexão aplicáveis ao sistema de armazenamento estão descritos no Anexo A – Arranjos Permitidos.
7.2.3 Requisitos Técnicos
Os consumidores que desejarem formalizar a solicitação de conexão à rede de distribuição da CERPRO para Sistemas Híbridos (on-grid com armazenamento) deverão encaminhar, em conjunto com a documentação exigida para MMGD, conforme estabelecido na NTC D09, as seguintes informações e documentos complementares:
Documento de identificação do titular (CPF ou CNPJ)
Comprovante de endereço (quando aplicável)
Ato constitutivo / contrato social (PJ);
Procuração com poderes específicos (quando aplicável).
ART
Certidão de Registro e Quitação CREA/CFT do RT, atualizada;
Documento de identificação do Responsável Técnico
Memorial descritivo, contendo:
Dados do empreendimento: identificação do acessante, localização, classe de tensão, demanda/geração associada;
Especificação do sistema de armazenamento (baterias): tecnologia, capacidade nominal, tensão, corrente, configuração e características operacionais;
Especificação do PCS (Power Conversion System): potência nominal, faixas de operação, controle de potência ativa e reativa, modos de operação;
Especificação do BMS (Battery Management System): funcionalidades de monitoramento, proteção, balanceamento e gestão das baterias;
Especificação do EMS (Energy Management System): estratégia de operação, lógica de controle, integração com geração, carga e rede;
Sistema de climatização (HVAC): requisitos e características do controle térmico do ambiente e/ou das baterias;
Memória de cálculo: dimensionamento do sistema, critérios adotados e premissas técnicas;
Plano de Segurança: medidas de prevenção, proteção e mitigação de riscos;
Plano de Emergência: procedimentos para situações de contingência;
Plano de Descomissionamento: diretrizes para desativação e destinação final dos equipamentos.
Diagrama unifilar do projeto elétrico.
Planta Baixa do Sistema (BESS/SAE)
Deverá apresentar, de forma clara e em escala adequada, os seguintes elementos:
Implantação dos equipamentos: localização do gabinete do BESS, PCS, quadros elétricos e sistema de climatização (HVAC);
Acessos operacionais: entradas para operação, manutenção e emergência;
Rotas de fuga: devidamente sinalizadas e desobstruídas, conforme normas de segurança;
FDC (Fire Department Connection): ponto de conexão para combate a incêndio, quando aplicável;
Distâncias mínimas: afastamentos entre equipamentos, limites da edificação e áreas adjacentes, conforme requisitos normativos e do fabricante;
Áreas de segurança: delimitação de zonas de risco e circulação;
Elementos complementares: ventilação, barreiras físicas, sinalização de segurança e eventuais sistemas de proteção contra incêndio.
	Para operação on-grid, é necessário apresentar os ensaios ou declaração do fornecedor que comprovam a atuação do sistema caso opere de modo a Limitar a Potência Injetada
Estudo de Proteção e Aterramento.
Sistema de Intertravamento e Proteção com as características da chave de intertravamento, sendo aceitas chaves estáticas e chaves eletromecânicas;
Datasheet
Manuais Técnicos
Certificações (ex.: normas IEC), conforme Anexo D, que comprovem o correto funcionamento do sistema.
Certificação INMETRO de durabilidade e de desempenho das baterias conectadas
Certificado INMETRO dos inversores
Datasheet do BESS;
Datasheet dos Inversores
Manuais técnicos/usuário do equipamento
Cronograma físico-financeiro
Apresentação de ensaios ou declaração do fornecedor que comprovem a atuação do sistema de forma a não injetar potência ativa na rede elétrica da distribuidora (Zero Grid).
Anexo B, devendo ser informada, a finalidade do sistema de armazenamento, tais como: back-up de energia, compensação reativa e/ou arbitragem no ponto de conexão.
Ressalta-se que, no referido anexo, também deverão constar as informações operacionais do sistema, incluindo:
Parâmetros de operação, como o fator de potência a ser mantido/corrigido no ponto de conexão;
Programação dos horários de carga e descarga do banco de baterias, quando aplicável à estratégia de arbitragem tarifária.
É obrigatória a fixação de placa de advertência6 na tampa da caixa do medidor, de forma a garantir sua plena visibilidade. Adicionalmente, devem ser previstas placas de advertência nas seguintes situações e locais:
Ponto de entrega aérea: Instalar a placa no postinho, na parede ou na cabine com buchas de passagem, sempre voltada para o lado da via pública, junto à conexão do ramal de ligação (ou ramal de serviço).
Unidade consumidora em edificações com múltiplas unidades:
Nos casos de edifícios de uso coletivo ou com medição agrupada, as placas devem ser instaladas:
No ponto de entrega do edifício (poste);
Na caixa de distribuição, quando existente.
Ponto de entrega subterrânea: Instalar a placa na fachada da edificação, próxima ao número do imóvel/empreendimento, ou na parte mais alta do duto de entrada localizado no poste da distribuidora (CERPRO).
Nota (6): Os requisitos e especificações das placas de advertência para sistemas de armazenamento estão disponíveis no ANEXO C.
7.3 Requisitos Ambientais
O sistema de armazenamento de energia em baterias (BESS) deve ser implantado e operado em local compatível com as condições ambientais do sítio de instalação. (IEC 62933-4-3:2025; IEC 62933-5-1:2024)
O BESS deve dispor de proteção contra descargas atmosféricas, sismos, inundação, chuva, umidade, corrosão, poeira, ingresso de fauna e flora e demais agentes externos capazes de comprometer sua segurança, desempenho ou vida útil. (IEC 62933-4-3:2025)
O invólucro, os sistemas auxiliares e os componentes do BESS devem ser compatíveis com a faixa de temperatura, umidade, altitude e agressividade ambiental previstas para o local de instalação. (IEC 62933-4-3:2025; UL 9540)
O BESS deve dispor de sistema de drenagem, contenção e gestão de efluentes e resíduos, quando aplicável. (IEC 62933-4-2:2025; IEC 62933-5-2:2025)
Devem ser avaliados e documentados os impactos ambientais decorrentes da falha de célula, módulo, bateria ou subsistema eletroquímico do BESS. (IEC 62933-4-2:2025)
O empreendimento deve prever procedimentos de desativação, coleta, logística reversa, destinação final ambientalmente adequada e descomissionamento, em conformidade com a legislação e regulamentação aplicáveis.
(IEC 62933-5-2:2025; Lei nº 12.305/2010; Resolução CONAMA nº 401/2008; Instrução Normativa Ibama nº 8/2012)
7.4 Requisitos de Segurança
O BESS deve atender às normas técnicas, códigos, regulamentos e requisitos da autoridade competente aplicáveis ao sistema, aos seus componentes e à instalação. (IEC 62933-5-1:2024; IEC 62933-5-2:2025; NFPA 855; NFPA 70; NFPA 1)
O BESS deve ser fornecido com certificação, listagem ou comprovação de conformidade do sistema e dos componentes críticos, conforme norma aplicável. (UL 9540; UL 1973; UL 1741)
O sistema deve dispor, no mínimo, de funções de proteção, monitoramento e supervisão por meio de BMS e, quando aplicável, EMS, incluindo monitoramento contínuo de tensão, corrente, temperatura, alarmes e eventos anormais. (IEC 62933-5-2:2025; UL 9540)
O BESS deve possuir recursos de desligamento seguro, intertravamentos, sinalização de segurança, aterramento, proteção contra curto-circuito, controle de acesso e meios de resposta a emergências. (IEC 62933-5-2:2025; NFPA 70; NFPA 855; UL 9540)
O BESS deve dispor de ventilação e, quando aplicável, climatização, detecção e mitigação de gases inflamáveis, tóxicos ou asfixiantes, bem como detecção, controle e supressão de incêndio compatíveis com a tecnologia empregada e com o local de instalação. (IEC 62933-5-2:2025; NFPA 855; NFPA 1; UL 9540A)
A proteção contra thermal runaway e propagação de falha deve ser definida com base na configuração real do sistema e nos ensaios aplicáveis. (UL 9540A; NFPA 855; IEC 62933-5-2:2025)
Devem ser estabelecidos procedimentos documentados de operação, inspeção, manutenção, resposta a emergências e treinamento das equipes envolvidas. (IEC 62933-5-2:2025; NFPA 855)
As fichas de dados de segurança, quando aplicáveis aos produtos químicos e materiais envolvidos, devem estar disponíveis e acessíveis às equipes de operação e manutenção. (ABNT NBR 14725; IEC 62933-5-2:2025)
Distanciamentos
Os afastamentos entre o BESS, edificações, divisas, vias públicas, materiais combustíveis, materiais perigosos e demais exposições devem ser definidos conforme a configuração efetiva da instalação, os relatórios de ensaio aplicáveis, as instruções do fabricante e os requisitos da autoridade competente. (NFPA 855; UL 9540A; UL 9540)
Salvo disposição específica mais restritiva, os sistemas de armazenamento de energia em baterias (BESS) instalados ao tempo devem observar afastamento mínimo em relação a edificações e demais exposições relevantes, adotando-se sempre o critério mais restritivo entre:
as normas técnicas aplicáveis, em especial a NFPA 855;
as especificações e recomendações do fabricante do sistema; e
as exigências estabelecidas pelo Corpo de Bombeiros e pelos órgãos licenciadores competentes.
Nessas condições, o valor de 3,0 m previsto na norma deve ser entendido como referência mínima, podendo ser ampliado conforme as características do sistema, os resultados de ensaios de propagação térmica e os requisitos de segurança aplicáveis.
A redução do afastamento mínimo somente é permitida quando houver comprovação técnica por ensaio aplicável, barreira de proteção ao fogo, parede adjacente incombustível sem aberturas, invólucro com resistência ao fogo compatível, ou outra medida equivalente aceita pela autoridade competente. (NFPA 855; UL 9540A)
As saídas de exaustão do BESS devem ser posicionadas de modo a não descarregar sobre rotas de fuga, passagens de pedestres ou tomadas de ar de edificações. (NFPA 855; IEC 62933-5-2:2025)
As distâncias entre o BESS e portas, janelas, aberturas operáveis e tomadas de ar devem atender às instruções do fabricante, aos relatórios de ensaio e aos requisitos da autoridade competente. (NFPA 855; UL 9540A; UL 9540)
7.5 Requisitos de Qualidade de Energia
A qualidade da energia elétrica no ponto de conexão deverá atender integralmente aos critérios estabelecidos no PRODIST Módulo 8, conforme regulamentação vigente da ANEEL.
O empreendimento deverá garantir que sua operação não provoque degradação dos parâmetros de qualidade da energia, incluindo, mas não se limitando a:
níveis de tensão em regime permanente;
fator de potência;
distorções harmônicas;
desequilíbrio de tensão;
flutuação de tensão (flicker);
variações de frequência do sistema;
variações de tensão de curta duração (VTCD);
Caso sejam identificadas não conformidades, o acessante deverá adotar as medidas corretivas necessárias para atendimento aos limites estabelecidos no PRODIST.
7.6 Requisitos de Operação, Manutenção e Descarte
7.6.1 Condições Gerais de Conexão
A conexão de unidades consumidoras com BESS, com ou sem geração distribuída associada, somente será autorizada desde que não implique riscos técnicos ou de segurança ao sistema elétrico, a outros consumidores ou às equipes de operação e manutenção da CERPRO.
Em nenhuma hipótese poderá haver prejuízo à qualidade e continuidade do fornecimento de energia elétrica.
7.6.2 Responsabilidades do Consumidor
O consumidor é integralmente responsável pelo cumprimento dos requisitos estabelecidos nesta Norma Técnica, respondendo civil e criminalmente por eventuais danos pessoais e materiais decorrentes de manobras, operações ou interligações indevidas.
Também é responsável pela proteção de seus equipamentos contra distúrbios provenientes da rede elétrica, tais como faltas, surtos atmosféricos, desequilíbrios de corrente, variações de tensão e frequência, não cabendo à CERPRO qualquer responsabilidade por danos ocorridos em suas instalações.
Adicionalmente, compete ao consumidor realizar a manutenção preventiva e corretiva de todos os equipamentos e instalações sob sua responsabilidade. A CERPRO não se responsabiliza por danos decorrentes de falhas internas, uso inadequado ou conservação inadequada das instalações, ainda que tenha realizado inspeções.
7.6.3 Suspensão do Fornecimento
A CERPRO poderá suspender o fornecimento de energia elétrica, de forma imediata e sem aviso prévio, caso sejam identificadas irregularidades ou deficiências técnicas e/ou de segurança que representem risco iminente a pessoas, bens ou ao adequado funcionamento do sistema elétrico.
Nessas situações, o titular da unidade consumidora será posteriormente notificado quanto aos motivos da desconexão, devendo apresentar, às suas expensas, as medidas corretivas e respectivos prazos para regularização, como condição para a reconexão ao sistema.
7.6.4 Operação Segura do BESS
É expressamente proibido que o Sistema de Armazenamento de Energia (BESS) energize a rede da CERPRO quando esta estiver desenergizada. A ocorrência dessa condição pode resultar em riscos graves, incluindo acidentes fatais, danos ao sistema elétrico e prejuízos a terceiros, sendo o consumidor integralmente responsabilizado.
Nesse contexto, é indispensável o cumprimento rigoroso dos procedimentos de segurança estabelecidos pelas Normas Regulamentadoras (NRs), aplicáveis às atividades com eletricidade e às operações de instalação, manutenção e intervenção em sistemas elétricos.
7.6.5 Sinalização de Segurança
Devem ser instaladas, no mínimo, duas placas de advertência permanentes, confeccionadas em material resistente (metálico ou não metálico), com resistência a intempéries e radiação ultravioleta, afixadas na caixa de medição ou cabine primária e no ponto de entrega da unidade consumidora, conforme Anexo C. As placas devem conter, de forma indelével, os seguintes dizeres:
“CUIDADO – RISCO DE CHOQUE ELÉTRICO – BATERIAS” (para BESS sem geração distribuída);
“CUIDADO – RISCO DE CHOQUE ELÉTRICO – SISTEMA HÍBRIDO” (para BESS com geração distribuída).
7.6.6 Descarte de Baterias
O consumidor é responsável pelo descarte ambientalmente adequado das baterias, devendo atender à Resolução CONAMA nº 401 e à Política Nacional de Resíduos Sólidos (PNRS), que estabelecem diretrizes para coleta, reutilização, reciclagem e destinação final, bem como a obrigatoriedade da logística reversa, envolvendo fabricantes, importadores, distribuidores e comerciantes.
7.7 Responsabilidades Adicionais
7.7.1. Atendimento aos Requisitos

O acessante deve cumprir integralmente os requisitos aplicáveis, conforme as características da conexão pretendida, assegurando a correta instalação, integração e operação do BESS com ou sem Micro e Minigeração Distribuída (MMGD), nas redes de distribuição.
7.7.2. Estudos de Impacto

A CERPRO poderá solicitar a realização de estudos específicos para avaliação dos impactos decorrentes da conexão do sistema. Nesses casos, o acessante, por meio de seu responsável técnico, deverá fornecer todas as informações necessárias à análise, conforme exigido formalmente.
7.7.3. Regularidade da Injeção de Energia

Conforme a regulamentação vigente, a injeção de energia elétrica na rede de distribuição sem prévia anuência da CERPRO, seja por ligação nova ou ampliação de geração, caracteriza irregularidade grave.
Tal prática pode resultar em sanções, incluindo:
Suspensão ou desligamento da unidade consumidora;
Perda do direito de enquadramento na GD I no sistema de compensação de energia;
Desconsideração da energia injetada no período irregular;
Aplicação de demais penalidades previstas na regulamentação.
Portanto, toda instalação de BESS, com ou sem geração distribuída associada, deve ser previamente submetida à análise e aprovação da CERPRO, por meio de solicitação formal nos canais oficiais de projetos particulares, observando integralmente as normas técnicas vigentes.
7.8 Forma de protocolo
Para protocolar o projeto, a documentação deverá ser encaminhada por meio do e-mail cerpro@cerpro.com.br ou entregue presencialmente na sede da CERPRO.
Após o recebimento, será emitido o respectivo protocolo, momento a partir do qual se iniciará a contagem dos prazos aplicáveis ao processo.
8. ETAPAS E DOCUMENTOS PARA VIABILIZAÇÃO DO ACESSO
8.1 Fluxo processual
O fluxo abaixo descreve as etapas ordenadas, com os respectivos prazos:
Etapa 1 — (Facultativa) Consulta de Acesso / Orçamento Estimado;
Etapa 2 — Solicitação de Orçamento de Conexão (formulário Anexo A + documentos do item 8.2);
Etapa 3 — Análise documental pela CERPRO (até 5 dias úteis);
Etapa 4 — Estudos técnicos e Emissão do Orçamento de Conexão (quando aprovado): 15 dias (com ou sem micro e sem reforço), 30 dias (com ou sem micro e com reforço), 45 dias (demais)
Etapa 6 — Aceite e assinatura do OC e do Relacionamento Operacional
Etapa 7 — Execução das obras (Prazo: Art. 88);
Etapa 8 — Comissionamento prévio + Relatório;
Etapa 9 — Solicitação de Vistoria;
Etapa 10 — Vistoria técnica CERPRO: 5 dias úteis (BT), 10 dias (MT); laudo em 3 dias úteis;
Etapa 11 — Primeiro paralelismo PRESENCIAL com vistoriador CERPRO;
Etapa 12 — Energização e início de operação comercial;
Etapa 13 — Cadastro ANEEL (quando aplicável), em até 5 dias úteis.
9. FORMA DE CONEXÃO E SISTEMA DE PROTEÇÃO
9.1 Requisitos em Baixa Tensão (BT) — P ≤ 75 kW
Tabela 3 — Elementos mínimos na interface de conexão em BT
9.1.1 Ajustes mínimos de proteção em BT
Conforme Portaria INMETRO 515/2023 e ABNT NBR 16149:
9.1.2 DSV e Elemento de Interrupção
DSV visível, travável em LOTO, com placa "DSV BESS — CERPRO" (Anexo H);
Elemento de interrupção atuante com U ≤ 0,7 p.u. de Un, atraso ≤ 2,0 s.
9.2 Requisitos em Média Tensão (MT) — P > 75 kW
9.2.1 Transformador de acoplamento
Obrigatório, isolação galvânica, ligação triângulo-estrela aterrada (Dyn11 ou Dyn1);
13,8 kV e 34,5 kV — enrolamento dedicado para função 59N;
Impedância e TAPs conforme estudo apresentado.
9.2.2 Chave seccionadora
Tripolar, manual e motorizada (telecomando para P > 300 kW);
Intertravamento mecânico tipo Kirk; indicação OPEN/CLOSED; abertura visível.
9.2.3 Disjuntor geral de MT
Tripolar, isolamento a vácuo ou SF6 (óleo mineral VEDADO);
Acionamento por molas com carregamento motorizado;
Bobina de abertura com dupla alimentação (CC + CA auxiliar);
Indicação mecânica e elétrica de posição; bloqueio Kirk;
Cores: I — vermelho (fechado); O — verde (aberto);
Capacidade de interrupção compatível com Icc (informado no OC).
9.2.4 Relé digital multifuncional
Tabela 4 — Funções ANSI mínimas obrigatórias
9.2.5 Ride-through (FRT)
Tabela 5 — Suportabilidade a afundamentos de tensão (LVRT) em MT
Tabela 6 — Suportabilidade a desvios de frequência
9.2.6 Anti-ilhamento em MT
Abertura em ≤ 2,0 s após detecção;
Limiar U ≤ 0,7 p.u.;
Função 78 (salto de vetor) como método primário; df/dt como redundância em P > 500 kW;
PROIBIDO ajuste de subfrequência ≥ 58,5 Hz para anti-ilhamento.
9.2.7 Proteção auxiliar e alimentação
Fonte auxiliar com autonomia mínima de 2 h (no-break + banco de baterias + retificador);
Capacidade mínima do no-break: 1000 VA;
Iluminação de emergência na sala de proteção.
9.2.8 Religador telecomandado
Obrigatório para P > 300 kW;
Integração ao COS CERPRO via DNP3 ou IEC 61850.
9.2.9 Aterramento
ABNT NBR 5410, 14039, 15751, 15479;
Resistência de aterramento ≤ 10 Ω (em regra);
Revisão do projeto existente em função do BESS;
Equipotencialização de gabinetes, racks e estruturas;
DPS conforme ABNT NBR 5419 (incluindo DPS CC).

---

## Tabelas (extração bruta)

### Tabela bruta 1
| Revisão | Data | Responsáveis | Descrição |
| R0 | __/__/2026 | Grupo Técnico de Padronização | Emissão inicial. |

### Tabela bruta 2
| Elemento | PCS com INMETRO | PCS sem INMETRO |
| DSV (desconexão) | Sim | Sim |
| Elemento de interrupção | Não (embarcado) | Sim (externo) |
| 27 / 59 (sub/sobretensão) | Sim | Sim |
| 81U / 81O (sub/sobrefrequência) | Sim | Sim |
| 78 / IEC 62116 (anti-ilhamento) | Sim | Sim |
| 25 (sincronismo) | Sim | Sim |
| 62 (reconexão temporizada) | Sim | Sim |
| DPS Classe II mínimo | Sim | Sim |

### Tabela bruta 3
| Função | Ajuste | Tempo de atuação |
| 27 — Subtensão | 0,80 p.u. (176 V em 220 V) | 2,0 s |
| 59 — Sobretensão | 1,12 p.u. (246 V em 220 V) | 1,0 s |
| 81U — Subfrequência 1 | 57,5 Hz | 0,2 s |
| 81U — Subfrequência 2 | 56,5 Hz | Instantâneo |
| 81O — Sobrefrequência | 62,5 Hz | 0,2 s |
| 78 — Anti-ilhamento | Ativo | ≤ 2,0 s |
| 25 — Reconexão | ΔV ≤ 10%, Δf ≤ 0,3 Hz | Janela 180 s |

### Tabela bruta 4
| ANSI | Descrição | Obrigatória |
| 25 | Verificação de sincronismo | Sim |
| 27 | Subtensão | Sim |
| 32 | Potência direcional reversa | Sim |
| 46 | Desequilíbrio de corrente | Sim |
| 47 | Sequência/desbalanço de tensão | Sim |
| 50/50N | Sobrecorrente instantânea fase/neutro | Sim |
| 50BF | Falha do disjuntor | Sim (> 500 kW) |
| 51/51N | Sobrecorrente temporizada | Sim |
| 51V | Sobrecorrente restrição de tensão | Sim (> 500 kW) |
| 59 | Sobretensão | Sim |
| 59N | Sobretensão residual | Sim |
| 62 | Temporização de reconexão | Sim |
| 67/67N | Sobrecorrente direcional | Sim |
| 78 | Salto de vetor / anti-ilhamento | Sim |
| 81U/81O | Sub/sobrefrequência | Sim |
| 81 df/dt | ROCOF | Sim (> 500 kW) |

### Tabela bruta 5
| Tensão no PAC (p.u.) | Tempo mínimo conectado |
| V ≤ 0,20 | Não exigida |
| 0,20 < V ≤ 0,50 | 0,5 s |
| 0,50 < V ≤ 0,80 | 2,5 s |
| 0,80 < V ≤ 1,10 | Tempo ilimitado |
| 1,10 < V ≤ 1,18 | 1,0 s |
| V > 1,18 | Não exigida |

### Tabela bruta 6
| Frequência (Hz) | Tempo mínimo |
| f ≤ 57,0 | Não exigida |
| 57,0 < f ≤ 57,5 | 5 s |
| 57,5 < f ≤ 58,5 | 20 s |
| 58,5 ≤ f ≤ 62,5 | Tempo ilimitado |
| 62,5 < f ≤ 63,0 | 10 s |
| f > 63,0 | Não exigida |
