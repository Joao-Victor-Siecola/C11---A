import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
nome = list(uploaded.keys())[0]

df = pd.read_csv(nome, delimiter=';', encoding='utf-8')

df['Location'] = df['Location'].str.strip()

eua = df[df['Location'].str.contains('USA')]
china = df[df['Location'].str.contains('China')]

empresas_eua = eua['Company Name'].unique()
empresas_china = china['Company Name'].unique()

qtd = [len(empresas_eua), len(empresas_china)]
paises = ['USA', 'China']

plt.bar(paises, qtd)

plt.title('Quantidade de Empresas Espaciais')
plt.ylabel('Quantidade')
plt.xlabel('País')

plt.show()