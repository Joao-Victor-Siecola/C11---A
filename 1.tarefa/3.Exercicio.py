sexo = input("Digite seu sexo (M/F): ").upper()

while sexo != "M" and sexo != "F":
    print("Entrada inválida.")
    sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == "M":
    print("Você é homem.")
else:
    print("Você é mulher.")
