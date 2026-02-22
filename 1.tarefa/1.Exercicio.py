nome_completo = input("Digite seu nome: ")
print("Nome em maiúsculo: ", nome_completo.upper())
print("Nome em minúsculo: ", nome_completo.lower())

print("Número de caracteres: ", len(nome_completo))

partes = nome_completo.split()
ultimo_nome = partes[1]
novo_nome = nome_completo.replace(ultimo_nome, "do inatel", 1)
print("Novo nome: ", novo)