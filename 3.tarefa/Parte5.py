import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 51, (4,4))

print("Matriz:")
print(mtz)


media_linhas = mtz.mean(axis=1)
media_colunas = mtz.mean(axis=0)

print("Média linhas:", media_linhas)
print("Média colunas:", media_colunas)


print("Maior média linhas:", media_linhas.max())
print("Maior média colunas:", media_colunas.max())

valores, contagem = np.unique(mtz, return_counts=True)

print("Valores:", valores)
print("Contagem:", contagem)

print("Aparecem 2 vezes:")
print(valores[contagem == 2])
