import pandas as pd
import missingno as msno
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('../mineracao_dados/titanic/titanic.csv', index_col=False, sep=",", header=0)
dataset.head()
print(dataset.shape)
missing_data = dataset.isnull().sum().to_frame()
missing_data = missing_data.rename(columns={0:'Empty Cells'})
print(missing_data)

msno.matrix(dataset, figsize=(10,5), fontsize=11)
unknown_age = dataset[dataset["Age"].isnull()]
unknown_age[["PassengerId","Name", "Survived", "Age"]][:20]
missing_age = dataset["Age"].isnull()
missing_cabin = dataset["Cabin"].isnull()
unknown_age_and_cabin = dataset[missing_age & missing_cabin]
print("Number of passengers missing age and cabin information:", len(unknown_age_and_cabin))
um_mulheres = dataset[dataset['Sex'] == 'female']['PassengerId'].count()
num_homens = dataset[dataset['Sex'] == 'male']['PassengerId'].count()
m_idade = dataset['Age'].mean()
m_idade_mulheres = dataset[dataset['Sex'] == 'female']['Age'].mean()
m_idade_homens = dataset[dataset['Sex'] == 'male']['Age'].mean()
homens_45_mais = dataset[(dataset['Sex'] == 'male') & (dataset['Age'] > 45)]['PassengerId'].count()
mulheres_25_menos = dataset[(dataset['Sex'] == 'female') & (dataset['Age'] < 25)]['PassengerId'].count()
homens_primeira_classe = dataset[(dataset['Sex'] == 'male') & (dataset['Pclass'] == 1)]['PassengerId'].count()
homens_segunda_classe = dataset[(dataset['Sex'] == 'male') & (dataset['Pclass'] == 2)]['PassengerId'].count()
homens_terceira_classe = dataset[(dataset['Sex'] == 'male') & (dataset['Pclass'] == 3)]['PassengerId'].count()
mulheres_primeira_classe = dataset[(dataset['Sex'] == 'female') & (dataset['Pclass'] == 1)]['PassengerId'].count()
mulheres_segunda_classe = dataset[(dataset['Sex'] == 'female') & (dataset['Pclass'] == 2)]['PassengerId'].count()
mulheres_terceira_classe = dataset[(dataset['Sex'] == 'female') & (dataset['Pclass'] == 3)]['PassengerId'].count()

plt.figure(figsize=(12, 6))
plt.hist(dataset[dataset['Pclass'] == 1]['Age'], bins=20, color='blue', alpha=0.5, label='1ª Classe')
plt.hist(dataset[dataset['Pclass'] == 2]['Age'], bins=20, color='green', alpha=0.5, label='2ª Classe')
plt.hist(dataset[dataset['Pclass'] == 3]['Age'], bins=20, color='red', alpha=0.5, label='3ª Classe')
plt.xlabel('Idade')
plt.ylabel('Número de Passageiros')
plt.legend()
plt.title('Histograma de Idades por Classe')
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(dataset[(dataset['Pclass'] == 1) & (dataset['Sex'] == 'male')]['Age'], bins=20, color='blue', alpha=0.5, label='Homens')
plt.hist(dataset[(dataset['Pclass'] == 1) & (dataset['Sex'] == 'female')]['Age'], bins=20, color='pink', alpha=0.5, label='Mulheres')
plt.xlabel('Idade')
plt.ylabel('Número de Passageiros')
plt.legend()
plt.title('Histograma de Idades de Homens e Mulheres da Primeira Classe')
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(dataset[(dataset['Pclass'] == 2) & (dataset['Sex'] == 'male')]['Age'], bins=20, color='blue', alpha=0.5, label='Homens')
plt.hist(dataset[(dataset['Pclass'] == 2) & (dataset['Sex'] == 'female')]['Age'], bins=20, color='pink', alpha=0.5, label='Mulheres')
plt.xlabel('Idade')
plt.ylabel('Número de Passageiros')
plt.legend()
plt.title('Histograma de Idades de Homens e Mulheres da Segunda Classe')
plt.show()
plt.figure(figsize=(12, 6))
plt.hist(dataset[(dataset['Pclass'] == 3) & (dataset['Sex'] == 'male')]['Age'], bins=20, color='blue', alpha=0.5, label='Homens')
plt.hist(dataset[(dataset['Pclass'] == 3) & (dataset['Sex'] == 'female')]['Age'], bins=20, color='pink', alpha=0.5, label='Mulheres')
plt.xlabel('Idade')
plt.ylabel('Número de Passageiros')
plt.legend()
plt.title('Histograma de Idades de Homens e Mulheres da Terceira Classe')
plt.show()
mean_age = np.mean(dataset.Age)
print("A idade média do navia era ", mean_age, "anos")

dataset['Age_2'] = dataset['Age'].fillna(0)
mean_age = np.mean(dataset.Age_2)
print("A idade média sobre o navio era ", mean_age, "anos")

clean_dataset = dataset.dropna(subset=["Embarked"])
clean_dataset = clean_dataset.reindex()
print("A forma do conjunto de dados limpo é", clean_dataset.shape)

mean_age = clean_dataset["Age"].mean()
print("A idade media e", mean_age)

clean_dataset["Age"].fillna(mean_age, inplace=True)
print(clean_dataset.isnull().sum().to_frame().rename(columns={0:'Empty Cells'}))

clean_dataset["Cabin"].fillna("Unknown", inplace=True)
print(clean_dataset.isnull().sum().to_frame().rename(columns={0:'Empty Cells'}))
def get_rows(sex, port):

    '''Retorna linhas que correspondem em termos de sexo e porto de embarque'''

    return dataset[(dataset.Embarked == port) & (dataset.Sex == sex)]


def proportion_survived(sex, port):

    '''Retorna a proporção de pessoas que atendem aos critérios e que sobreviveram'''

    survived = get_rows(sex, port).Survived

    return np.mean(survived)


sexes = ["male", "male", "male", "female","female", "female"]
ports = ["C", "Q", "S" ] * 2
passenger_count = [len(get_rows(sex, port)) for sex,port in zip(sexes, ports)]
passenger_survival = [proportion_survived(sex, port) for sex,port in zip(sexes, ports)]
table = pd.DataFrame(dict(

    sex=sexes,

    port=ports,

    passenger_count=passenger_count,

    passenger_survival_rate=passenger_survival

))