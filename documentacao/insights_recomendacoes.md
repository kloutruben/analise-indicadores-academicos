# Insights e Recomendações — Indicadores Académicos

## 1. Objetivo da análise

Analisar o desempenho académico de três cursos de uma instituição de ensino fictícia, identificando padrões de aprovação e reprovação, com o objetivo de apoiar decisões de gestão académica.

## 2. Fonte e características dos dados

- **Tipo de dados:** Sintéticos (fictícios)
- **Período:** 2024–2026
- **Total de registos:** 3.240 avaliações
- **Ferramenta utilizada:** Microsoft Excel
- **Técnicas:** Fórmulas, Tabelas Dinâmicas e análise de indicadores (KPIs)

## 3. Indicadores gerais

| Indicador | Resultado |
|---|---|
| Total de avaliações | 3.240 |
| Avaliações aprovadas | 1.924 |
| Avaliações reprovadas | 1.316 |
| Taxa de aprovação | 59,38% |
| Nota média | 10,9/20 |
| Assiduidade média | 72,5% |
| Registos sem nota | 0 |
| Registos com situação inconsistente | 0 |

**Nota metodológica:** A taxa de aprovação representa a percentagem de avaliações aprovadas, não a percentagem de estudantes aprovados.

## 4. Insight 01 — Desempenho académico por curso

### Resultados

| Curso | Aprovados | Reprovados | Taxa de aprovação |
|---|---:|---:|---:|
| Engenharia de Telecomunicações | 640 | 440 | 59,26% |
| Gestão | 646 | 434 | 59,81% |
| Informática | 638 | 442 | 59,07% |

### Interpretação

O curso de Gestão apresentou a maior taxa de aprovação, com 59,81%, enquanto Informática registou a menor, com 59,07%.

A diferença entre ambos foi de aproximadamente 0,74 pontos percentuais.

Os resultados indicam um desempenho relativamente semelhante entre os três cursos, sem diferenças expressivas nas taxas de aprovação observadas.

### Recomendações

1. Analisar os resultados por disciplina para identificar áreas com maior incidência de reprovação.
2. Comparar as taxas de aprovação entre semestres e anos letivos.
3. Investigar a associação entre assiduidade e desempenho académico.
4. Acompanhar os indicadores periodicamente através de dashboards.

## 5. Limitações

Os dados utilizados são sintéticos e não representam estudantes reais.

Os resultados têm finalidade educativa e demonstram competências de análise de dados. Não devem ser interpretados como conclusões sobre uma instituição real.

## 6. Conclusão

A análise inicial demonstrou que os três cursos apresentam taxas de aprovação próximas de 59%.

Embora Gestão tenha obtido o melhor resultado, são necessárias análises adicionais por disciplina, semestre e assiduidade para identificar padrões mais específicos.

**Próxima análise:** Relação entre assiduidade e desempenho académico.

## Insight 02 — Relação entre Assiduidade e Desempenho Académico

### Objetivo

Investigar a associação entre os níveis de assiduidade e o desempenho académico, utilizando as notas finais de 3.240 registos de avaliações de uma instituição fictícia.

### Metodologia

As avaliações foram classificadas em três categorias:

- **Baixa assiduidade:** inferior a 50%.
- **Média assiduidade:** de 50% a menos de 75%.
- **Alta assiduidade:** igual ou superior a 75%.

Foi utilizada uma Tabela Dinâmica no Microsoft Excel para calcular a nota média e a quantidade de avaliações em cada categoria.

### Resultados

| Assiduidade | Nota média | Avaliações |
|---|---:|---:|
| Alta | 12,60 | 1.476 |
| Média | 9,68 | 1.455 |
| Baixa | 8,29 | 309 |
| **Total** | **10,88** | **3.240** |

### Principais descobertas

1. A categoria de alta assiduidade apresentou a maior nota média, com 12,60 valores.
2. A categoria de baixa assiduidade registou a menor nota média, com 8,29 valores.
3. A diferença entre as categorias Alta e Baixa foi de aproximadamente 4,30 valores.
4. Os resultados revelam uma associação positiva entre assiduidade e desempenho académico nas categorias analisadas.

### Interpretação

Os dados sugerem que avaliações associadas a níveis mais elevados de assiduidade tendem a apresentar melhores resultados académicos.

No entanto, esta análise é descritiva e não permite estabelecer uma relação causal. Outros fatores, como dificuldade das disciplinas, métodos de avaliação e características dos estudantes, poderão influenciar os resultados.

### Recomendações

1. Monitorizar os níveis de assiduidade ao longo de cada semestre.
2. Investigar as disciplinas com maior incidência de baixa assiduidade.
3. Analisar separadamente os resultados por curso e disciplina.
4. Avaliar a associação entre assiduidade e desempenho utilizando técnicas estatísticas adicionais.

### Limitações

O dataset é sintético e os resultados têm finalidade demonstrativa. As observações representam avaliações, não necessariamente estudantes únicos.

A análise por categorias não substitui uma análise de correlação entre as variáveis numéricas originais.

### Ferramentas utilizadas

Microsoft Excel, fórmulas condicionais, Tabelas Dinâmicas, estatística descritiva e visualização de dados.
