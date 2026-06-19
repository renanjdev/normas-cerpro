# Como contribuir

Este guia explica como o squad colabora na elaboração de normas.

## Fluxo de trabalho (Git)

1. **Crie uma branch** a partir da principal:
   ```bash
   git checkout -b norma/NRM-0001-nome-curto
   ```
2. **Crie ou edite** o documento em `rascunhos/` usando o template.
3. **Faça commits** pequenos e descritivos (veja convenção abaixo).
4. **Abra um Pull Request** quando o rascunho estiver pronto para revisão.
5. **Revisão por pares**: ao menos um revisor e a aprovação final conforme [papéis](docs/papeis.md).
6. Após aprovado, o PR é **mesclado** e a norma promovida para `normas/`.

## Convenção de nomes

- Identificador da norma: `NRM-XXXX` (numeração sequencial de 4 dígitos).
- Pasta/arquivo: `NRM-0001-titulo-curto`.
- Branch: `norma/NRM-0001-titulo-curto`.

## Convenção de commits

Use prefixos para facilitar o histórico:

- `norma:` nova norma ou mudança de conteúdo normativo
- `revisao:` ajustes vindos de revisão
- `docs:` documentação do processo/repositório
- `template:` mudanças em modelos

Exemplo: `norma: adiciona NRM-0001 sobre controle de documentos`

## Estados de uma norma

| Estado        | Local            | Significado                          |
|---------------|------------------|--------------------------------------|
| Rascunho      | `rascunhos/`     | Em elaboração, sujeita a mudanças    |
| Em revisão    | PR aberto        | Aguardando revisão do squad          |
| Vigente       | `normas/`        | Aprovada e em vigor                  |
| Revogada      | `normas/` (marcada) | Substituída ou descontinuada      |

## Dúvidas

Abra uma _issue_ ou fale com a coordenação do squad.
