import numpy as np
import pandas as pd
dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Ex_01
Q1 = np.percentile(dados, 25)
Q2 = np.percentile(dados, 50)
Q3 = np.percentile(dados, 75)

print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)

#Ex_02
percentile_25 = np.percentile(dados, 25)
print("Percentil 25:", percentile_25)

#Ex_03
percentile_50 = np.percentile(dados, 50)
print("Percentil 50 (Mediana):", percentile_50)

#Ex_04
percentile_75 = np.percentile(dados, 75)
print("Percentil 75:", percentile_75)

#Calculo da mediana e moda arquivo<tinanic.csv>
df = pd.read_csv('titanic.csv')

mediana = df['Survived'].median()
moda = df['Survived'].mode().values[0]

mediana_pclass = df['Pclass'].median()
moda_pclass = df['Pclass'].mode().values[0]

mediana_idade = df['Age'].median()
moda_idade = df['Age'].mode().values[0]

mediana_sibsp = df['SibSp'].median()
moda_sibsp = df['SibSp'].mode().values[0]

print("Mediana de Sobreviventes:", mediana)
print("Moda de Sobreviventes:", moda)

print("Mediana por classes", mediana_pclass)
print("Moda por classes", moda_pclass)

print("Mediana por idade", mediana_idade)
print("Moda por idade", moda_idade)

print("Mediana de SibSp:", mediana_sibsp)
print("Moda de SibSp:", moda_sibsp)

media_idade = df['Age'].mean()
print("Média por idade", media_idade)
