import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print("DataFrame:")
print(df)

media_x_menor_30 = df['X'][df['X'] < 30].mean()
print("\nMédia dos elementos da coluna X menores que 30:", media_x_menor_30)

media_linha_D = df.loc['D'].mean()
soma_linha_E = df.iloc[4].sum()

print("\nMédia da linha D:", media_linha_D)
print("Soma da linha E:", soma_linha_E)

slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print("\nSlicing:")
print(slicing)

print("\nSoma de cada linha:")
print(slicing.sum(axis=1))

print("\nSoma de cada coluna:")
print(slicing.sum(axis=0))
