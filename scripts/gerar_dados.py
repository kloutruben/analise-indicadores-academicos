import csv
import os
import random
from datetime import date, timedelta

random.seed(42)
PASTA = "dados"
os.makedirs(PASTA, exist_ok=True)

cursos = [
    (1, "Informática"),
    (2, "Eletrónica e Telecomunicações"),
    (3, "Contabilidade e Gestão"),
]

disciplinas_por_curso = {
    1: ["Programação", "Redes de Computadores", "Bases de Dados", "Matemática"],
    2: ["Eletrónica", "Telecomunicações", "Física", "Matemática"],
    3: ["Contabilidade", "Gestão", "Economia", "Matemática"],
}

disciplinas = []
disc_id = 1
for curso_id, nomes_disc in disciplinas_por_curso.items():
    for nome_disc in nomes_disc:
        disciplinas.append((disc_id, nome_disc, curso_id))
        disc_id += 1

nomes_f = ["Ana", "Maria", "Luísa", "Teresa", "Isabel", "Joana", "Beatriz", "Helena", "Sónia", "Catarina"]
nomes_m = ["João", "Pedro", "Paulo", "Manuel", "Domingos", "António", "Carlos", "Miguel", "Rui", "Tomás"]
apelidos = ["Silva", "Santos", "Fernandes", "Domingos", "Baptista", "Pereira", "Gomes", "Cardoso", "Neto", "Miguel"]

alunos = []
for aluno_id in range(1, 301):
    curso_id = random.choice([c[0] for c in cursos])
    genero = random.choice(["F", "M"])
    primeiro = random.choice(nomes_f if genero == "F" else nomes_m)
    nome = f"{primeiro} {random.choice(apelidos)}"
    nascimento = date(2006, 1, 1) + timedelta(days=random.randint(0, 1460))
    ano_ingresso = random.choice([2023, 2024, 2025])
    turma = random.choice(["A", "B", "C"])

    # Problemas propositados para treinar limpeza de dados
    if random.random() < 0.03:
        genero = genero.lower()
    if random.random() < 0.03:
        nome = f"  {nome}  "

    alunos.append((aluno_id, nome, genero, nascimento.isoformat(), curso_id, ano_ingresso, turma))

avaliacoes = []
av_id = 1
for aluno in alunos:
    aluno_id, _, _, _, curso_id, _, _ = aluno
    aptidao = random.gauss(12, 3)
    for d_id, _, d_curso in disciplinas:
        if d_curso != curso_id:
            continue
        for trimestre in (1, 2, 3):
            nota = round(min(20, max(0, random.gauss(aptidao, 2))), 1)
            aulas = random.randint(30, 40)
            faltas = int(random.gauss(3 + (14 - aptidao) * 0.4, 2))
            faltas = max(0, min(aulas, faltas))

            # Problemas propositados
            r = random.random()
            if r < 0.01:
                nota = ""
            elif r < 0.015:
                nota = random.choice([25, 99, -1])

            avaliacoes.append((av_id, aluno_id, d_id, trimestre, nota, aulas, faltas))
            av_id += 1

# Linhas duplicadas propositadas
avaliacoes.extend(random.sample(avaliacoes, 15))


def gravar(nome_ficheiro, cabecalho, linhas):
    caminho = os.path.join(PASTA, nome_ficheiro)
    with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)
        escritor.writerow(cabecalho)
        escritor.writerows(linhas)
    print(f"{caminho}: {len(linhas)} linhas")


gravar("cursos.csv", ["CursoID", "Curso"], cursos)
gravar("disciplinas.csv", ["DisciplinaID", "Disciplina", "CursoID"], disciplinas)
gravar("alunos.csv", ["AlunoID", "Nome", "Genero", "DataNascimento", "CursoID", "AnoIngresso", "Turma"], alunos)
gravar("avaliacoes.csv", ["AvaliacaoID", "AlunoID", "DisciplinaID", "Trimestre", "Nota", "AulasDadas", "Faltas"], avaliacoes)
