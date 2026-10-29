# Dicionário de dados
| Campo | Tipo | Significado |
|---|---|---|
| id_estudante | Texto | Identificador fictício de estudante |
| ano | Inteiro | Ano letivo de referência |
| semestre | Inteiro | 1 ou 2 |
| curso | Texto | Curso frequentado |
| disciplina | Texto | Disciplina avaliada |
| nota_final | Decimal | Nota entre 0 e 20 |
| assiduidade_pct | Decimal | Assiduidade de 0 a 100 |
| situacao | Texto | Aprovado (nota >= 10), senão Reprovado |

**Granularidade:** uma linha por estudante × disciplina × ano × semestre. `id_estudante` repete-se legitimamente.
