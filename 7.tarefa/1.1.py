import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
nome = list(uploaded.keys())[0]

df = pd.read_csv(nome, delimiter=';', encoding='latin1')

# Fix: Rename the column from 'ï»¿Country' to 'Country' to match expected column name.
df = df.rename(columns={'ï»¿Country': 'Country'})

df['Country'] = df['Country'].str.strip()
df['Region'] = df['Region'].str.strip()

df_na = df[df['Region'] == 'NORTHERN AMERICA']

plt.plot(df_na['Country'], df_na['Deathrate'], 'r-', label='Deathrate')
plt.plot(df_na['Country'], df_na['Birthrate'], 'b--', label='Birthrate')

plt.xlabel('País')
plt.ylabel('Taxas')
plt.title('Taxas de Mortalidade e Natalidade - América do Norte')
plt.legend()

plt.xticks(rotation=45)
plt.show()