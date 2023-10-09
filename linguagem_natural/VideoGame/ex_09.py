import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('vgsales.csv')
print(dados.head())

dados['Proporcao_NA'] = dados['NA_Sales'] / dados['Global_Sales']
dados['Proporcao_EU'] = dados['EU_Sales'] / dados['Global_Sales']
dados['Proporcao_JP'] = dados['JP_Sales'] / dados['Global_Sales']
dados['Proporcao_Outros'] = dados['Other_Sales'] / dados['Global_Sales']

top_10_japan = dados.sort_values(by='Proporcao_JP', ascending=False).head(10)
print("\nTop 10 vendas proporcionais do Japão:")
print(top_10_japan[['Name', 'Proporcao_JP']])

plt.figure(figsize=(12, 6))
plt.plot(dados['Year'], dados['EU_Sales'], label='Vendas na Europa', marker='o', linestyle='-', color='blue')
plt.plot(dados['Year'], dados['Global_Sales'], label='Vendas Globais', marker='o', linestyle='-', color='green')
plt.xlabel('Ano')
plt.ylabel('Vendas (em milhões)')
plt.title('Europa vs. Global')
plt.legend()
plt.grid(True)
plt.show()
