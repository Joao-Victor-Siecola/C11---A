pessoas = []

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    pessoas.append({"nome": nome, "peso": peso})

mais_pesada = max(pessoas, key=lambda x: x["peso"])
mais_leve = min(pessoas, key=lambda x: x["peso"])

print("Pessoa mais pesada:", mais_pesada["nome"])
print("Pessoa mais leve:", mais_leve["nome"])