import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
nome = list(uploaded.keys())[0]

df = pd.read_csv(nome, delimiter=';', encoding='utf-8')

roscosmos = df[df['Company Name'] == 'Roscosmos']

sucesso = len(roscosmos[roscosmos['Status Mission'] == 'Success'])
falha = len(roscosmos[roscosmos['Status Mission'] != 'Success'])

valores = [sucesso, falha]
labels = ['Sucesso', 'Falha']

plt.pie(valores, labels=labels, autopct='%1.1f%%')

plt.title('Missões da Roscosmos')

plt.show()