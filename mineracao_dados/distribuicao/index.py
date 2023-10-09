import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

jogadas = np.random.randint(1, 7, size=50)
dados = pd.DataFrame({'Jogadas': jogadas})
print(dados.head(10))

plt.hist(jogadas, bins=6, alpha=0.7, edgecolor='k')
plt.xlabel('Resultado do Dado')
plt.ylabel('Frequência')
plt.title('Distribuição das Jogadas de Dado')
plt.show()

pares = len(dados[dados['Jogadas'] % 2 == 0])
coroas = len(dados[dados['Jogadas'] == 6])

print(f'valores pares: {pares}')
print(f'coroas (valor 6): {coroas}')
