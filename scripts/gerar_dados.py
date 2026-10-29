import csv,random,pathlib,zipfile
p=pathlib.Path(__file__).resolve().parents[1];random.seed(29)
courses={'Engenharia de Telecomunicacoes':['Redes','Matematica','Sinais'],'Gestao':['Contabilidade','Estatistica','Marketing'],'Informatica':['Programacao','Bases de Dados','Redes']}
rows=[]
for year in [2024,2025,2026]:
 for semester in [1,2]:
  for course,subjects in courses.items():
   for student in range(1,61):
    for subject in subjects:
     attendance=round(random.uniform(45,100),1); grade=round(max(0,min(20,random.gauss(10.5+(attendance-70)*.11,3.1))),1)
     rows.append([f'E{year}{list(courses).index(course)+1:02d}{student:03d}',year,semester,course,subject,grade,attendance,'Aprovado' if grade>=10 else 'Reprovado'])
with open(p/'dados/brutos/avaliacoes_sinteticas.csv','w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['id_estudante','ano','semestre','curso','disciplina','nota_final','assiduidade_pct','situacao']);w.writerows(rows)
print(f'{len(rows)} linhas geradas')
