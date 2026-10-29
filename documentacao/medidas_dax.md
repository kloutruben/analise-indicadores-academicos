# Medidas DAX
Renomear a tabela importada para `Avaliacoes`.

```dax
Total Avaliacoes = COUNTROWS(Avaliacoes)

Avaliacoes Aprovadas =
CALCULATE(COUNTROWS(Avaliacoes), Avaliacoes[nota_final] >= 10)

Taxa Aprovacao =
DIVIDE([Avaliacoes Aprovadas], [Total Avaliacoes])

Nota Media = AVERAGE(Avaliacoes[nota_final])

Estudantes Unicos = DISTINCTCOUNT(Avaliacoes[id_estudante])

Assiduidade Media = AVERAGE(Avaliacoes[assiduidade_pct])
```

Formatar `Taxa Aprovacao` como percentagem. `Assiduidade Media` já está em escala 0–100, por isso apresentar como número com sufixo %, não como percentagem nativa.
