# Normas CERPRO

Repositório colaborativo do squad de **elaboração de normas** da CERPRO. Centraliza a redação, revisão, aprovação e publicação de normas, procedimentos e padrões internos.

## Objetivo

Manter um processo organizado e rastreável para criar e manter normas, com versionamento, histórico de mudanças e revisão por pares — substituindo documentos soltos por uma fonte única de verdade.

## Estrutura do repositório

```
normas-cerpro/
├── normas/             # Normas publicadas (vigentes)
│   └── NRM-0000-modelo/
├── rascunhos/          # Normas em elaboração (drafts)
├── templates/          # Modelos para novas normas e documentos
├── docs/               # Processo, papéis do squad e guias
│   ├── processo.md
│   ├── papeis.md
│   └── glossario.md
└── CONTRIBUTING.md     # Como contribuir
```

## Como funciona (resumo)

1. Uma nova norma nasce como **rascunho** em `rascunhos/`, a partir do template.
2. O squad elabora e revisa o conteúdo via **Pull Requests**.
3. Após aprovação, a norma é movida para `normas/` e marcada como **vigente**.
4. Alterações futuras seguem o mesmo fluxo, mantendo o histórico.

Detalhes completos em [`docs/processo.md`](docs/processo.md).

## Papéis do squad

O time é descrito em [`docs/papeis.md`](docs/papeis.md): coordenação, redação técnica, especialistas de conteúdo, revisão e aprovação.

## Primeiros passos para o time

1. Leia o [CONTRIBUTING.md](CONTRIBUTING.md).
2. Conheça o [processo](docs/processo.md) e os [papéis](docs/papeis.md).
3. Para criar uma norma, copie [`templates/norma.md`](templates/norma.md) para `rascunhos/`.
