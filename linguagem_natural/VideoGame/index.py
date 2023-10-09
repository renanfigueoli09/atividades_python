import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')
df['Proporção_NA'] = df['NA_Sales'] / df['Global_Sales']
df['Proporção_EU'] = df['EU_Sales'] / df['Global_Sales']
df['Proporção_JP'] = df['JP_Sales'] / df['Global_Sales']
df['Proporção_Outros'] = df['Other_Sales'] / df['Global_Sales']

top_10_japao = df.nlargest(10, 'Proporção_JP')
print("10 maiores vendas do Japão:")
print(top_10_japao[['Name', 'Proporção_JP']])

# plt.figure(figsize=(10, 6))
# plt.bar(df['Name'][:10], df['EU_Sales'][:10], label='Vendas Europa', alpha=0.7)
# plt.bar(df['Name'][:10], df['Global_Sales'][:10], label='Vendas Globais', alpha=0.7)
# plt.xlabel('games')
# plt.ylabel('Vendas (em milhões)')
# plt.title('Vendas na Europa X Vendas Globais (10)')
# plt.xticks(rotation=90)
# plt.legend()
# plt.show()
