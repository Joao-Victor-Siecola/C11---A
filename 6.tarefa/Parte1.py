import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print("Series Ano 1:")
print(seriesAno1)
print("\nSeries Ano 2:")
print(seriesAno2)

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print("\nTotal no Ano 1:", round(totalAno1, 2), "%")
print("Total no Ano 2:", round(totalAno2, 2), "%")

variacao = seriesAno2 - seriesAno1

print("\nCrescimento/declínio:")
print(variacao)

crescimento = variacao[variacao > 0]

print("\nLinguagens que cresceram:")
print(crescimento)

ano3 = seriesAno2 + variacao
ano4 = ano3 + variacao

print("\nValores projetados para o 4º ano:")
print(ano4)
print("\nLinguagem mais popular:")
print(ano4.nlargest(1))