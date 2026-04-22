import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
nome = list(uploaded.keys())[0]

df = pd.read_csv(nome, delimiter=';', encoding='utf-8')

# Tirando espaços extras
df['Location'] = df['Location'].str.strip()
df['Company Name'] = df['Company Name'].str.strip()

# Filtrar EUA e China
eua = df[df['Location'].str.contains('USA')]
china = df[df['Location'].str.contains('China')]

# Empresas únicas
empresas_eua = eua['Company Name'].unique()
empresas_china = china['Company Name'].unique()

# Quantidade
qtd = [len(empresas_eua), len(empresas_china)]
paises = ['USA', 'China']

# Gráfico
plt.bar(paises, qtd)

plt.xlabel('País')
plt.ylabel('Quantidade de empresas')
plt.title('Empresas espaciais - EUA x China')

plt.show()