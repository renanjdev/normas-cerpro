# Processo de elaboração de normas

Este documento descreve o ciclo de vida de uma norma na CERPRO, da ideia à publicação e manutenção.

## Visão geral do fluxo

```
  Demanda  →  Rascunho  →  Elaboração  →  Revisão  →  Aprovação  →  Vigente  →  Manutenção/Revogação
```

## 1. Demanda

- Uma necessidade de norma é identificada (lacuna, exigência legal, melhoria de processo).
- Registre a demanda como uma **issue**, descrevendo o problema e o objetivo esperado.
- A coordenação prioriza e atribui um responsável (redator) e os especialistas envolvidos.

## 2. Rascunho

- O redator cria uma branch `norma/NRM-XXXX-titulo-curto`.
- Copia `templates/norma.md` para `rascunhos/NRM-XXXX-titulo-curto.md`.
- Reserva o próximo número sequencial `NRM-XXXX`.

## 3. Elaboração

- Redação do conteúdo em conjunto com os especialistas de conteúdo.
- Commits pequenos e frequentes; discussões registradas na issue ou no PR.

## 4. Revisão

- Abertura do **Pull Request** marcando os revisores.
- Revisão técnica (conteúdo correto e completo) e revisão editorial (clareza e padronização).
- Ajustes feitos via novos commits no mesmo PR.

## 5. Aprovação

- A aprovação final segue os [papéis definidos](papeis.md).
- Ao aprovar: atualizar cabeçalho (versão, estado **Vigente**, aprovador, data de vigência).
- Mover o arquivo de `rascunhos/` para `normas/NRM-XXXX-titulo-curto/`.

## 6. Manutenção

- Mudanças seguem o mesmo fluxo (branch → PR → revisão → aprovação).
- Cada alteração incrementa a versão e registra no **Histórico de revisões**.

## 7. Revogação

- Quando uma norma deixa de valer, marque o estado como **Revogada** no cabeçalho.
- Indique a norma substituta, se houver, e a data de revogação.
- A norma revogada permanece no repositório para fins de histórico.

## Versionamento

- Use versionamento simples: `0.x` para rascunhos, `1.0` na primeira publicação, incrementos a cada revisão aprovada.
