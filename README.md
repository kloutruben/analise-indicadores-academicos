# Análise de Indicadores Académicos

**Projeto de portfólio de Data Analytics | Excel, Power Query, Power BI e DAX**

> **Aviso:** os dados são inteiramente sintéticos e gerados para aprendizagem. Não representam uma instituição real, nem constituem experiência profissional remunerada.

## Problema de negócio
Uma instituição de ensino fictícia pretende acompanhar taxas de aprovação, desempenho por curso e disciplina, assiduidade e evolução semestral.

## Perguntas de negócio
1. Qual a taxa de aprovação por ano e semestre?
2. Quais cursos e disciplinas apresentam menor desempenho?
3. Como varia o desempenho com a assiduidade?
4. Quais tendências merecem intervenção?

## Dataset
`dados/brutos/avaliacoes_sinteticas.csv` — registo por estudante, disciplina e período; dados sintéticos e reproduzíveis com semente 29. A mesma pessoa pode aparecer em várias disciplinas e períodos. Não somar linhas como se fossem estudantes únicos.

## Regras dos indicadores
- Aprovação: nota_final >= 10 (escala 0–20).
- Taxa de aprovação: avaliações aprovadas / total de avaliações válidas.
- Média das notas: média das notas válidas, sem agregação prévia.
- Estudantes únicos: contagem distinta de `id_estudante`.
- Assiduidade média: média simples da assiduidade por avaliação; não representa presença institucional agregada.

## Como reproduzir
1. Importar o CSV no Excel (Dados > De Texto/CSV) ou Power BI (Obter dados > Texto/CSV).
2. Confirmar tipos: IDs e categorias como texto; ano/semestre inteiros; nota e assiduidade decimais.
3. Remover duplicados apenas se todas as colunas da chave (id_estudante, ano, semestre, disciplina) coincidirem; verificar valores em falta e intervalos.
4. Criar medidas DAX conforme `documentacao/medidas_dax.md`.
5. Criar cartões de KPIs, barras por curso/disciplina, linha por período e dispersão de assiduidade versus nota.
6. Registar decisões, prints do dashboard e conclusões; adicionar o ficheiro `.pbix` após construção.

## Estrutura
- `dados/`: dados brutos e tratados
- `scripts/`: gerador dos dados
- `excel/`: análises em Excel (a desenvolver)
- `powerbi/`: relatório Power BI (a desenvolver)
- `imagens/`: capturas do dashboard (a desenvolver)
- `documentacao/`: dicionário, metodologia, DAX e insights

## Estado
**Em desenvolvimento.** Dados de exemplo e documentação inicial concluídos; dashboard e validação de resultados pendentes.

## Autor
Klout Ruben | Portfólio de Data Analyst
