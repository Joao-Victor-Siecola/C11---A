total_idade = 0
contador = 0
mulheres_menos_20 = 0

n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    total_idade += idade
    contador += 1

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / contador

print("Média de idade do grupo:", media_idade)
print("Mulheres com menos de 20 anos:", mulheres_menos_20)