aluno = {}

aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))

if aluno["media"] >= 50:
    aluno["situacao"] = "AP"
else:
    aluno["situacao"] = "RP"

print("Dados do aluno:", aluno)