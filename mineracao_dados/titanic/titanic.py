import pandas as pd
titanic = pd.read_csv('titanic.csv')
titanic.head()
type(titanic)
titanic.head(10)
titanic.Sex.head()
titanic.Sex.head(10)
col_id_sex = ["PassengerId","Sex"]
titanic[col_id_sex].head(10)
titanic["PassengerId"].head()
titanic.PassengerId.head()
type(titanic[col_id_sex])
titanic.shape
titanic.columns
titanic.dtypes
col_id_survived = ["PassengerId", "Survived"]
titanic[col_id_survived].head(10)
homens = titanic[titanic['Sex'] == 'male']['Sex'].count()
mulheres = titanic[titanic['Sex'] == 'female']['Sex'].count()
idade_homens = titanic[titanic['Sex'] == 'male']['Age'].mean()
idade_mulheres = titanic[titanic['Sex'] == 'female']['Age'].mean()
Survived = titanic['Survived'].sum()
mortos = titanic['Survived'].count() - Survived
Pclass_1 = titanic[titanic['Pclass'] == 1]['Pclass'].count()
Pclass_2 = titanic[titanic['Pclass'] == 2]['Pclass'].count()
Pclass_3 = titanic[titanic['Pclass'] == 3]['Pclass'].count()
homens_Pclass_1 = titanic[(titanic['Pclass'] == 1) & (titanic['Sex'] == 'male')]['Sex'].count()
mulheres_Pclass_1 = titanic[(titanic['Pclass'] == 1) & (titanic['Sex'] == 'female')]['Sex'].count()
homens_Pclass_2 = titanic[(titanic['Pclass'] == 2) & (titanic['Sex'] == 'male')]['Sex'].count()
mulheres_Pclass_2 = titanic[(titanic['Pclass'] == 2) & (titanic['Sex'] == 'female')]['Sex'].count()
homens_Pclass_3 = titanic[(titanic['Pclass'] == 3) & (titanic['Sex'] == 'male')]['Sex'].count()
mulheres_Pclass_3 = titanic[(titanic['Pclass'] == 3) & (titanic['Sex'] == 'female')]['Sex'].count()
media_idade_homens_Pclass_1 = titanic[(titanic['Pclass'] == 1) & (titanic['Sex'] == 'male')]['Age'].mean()
media_idade_mulheres_Pclasse_1 = titanic[(titanic['Pclass'] == 1) & (titanic['Sex'] == 'female')]['Age'].mean()
media_idade_homens_Pclasse_2 = titanic[(titanic['Pclass'] == 2) & (titanic['Sex'] == 'male')]['Age'].mean()
media_idade_mulheres_Pclasse_2 = titanic[(titanic['Pclass'] == 2) & (titanic['Sex'] == 'female')]['Age'].mean()
media_idade_homens_Pclasse_3 = titanic[(titanic['Pclass'] == 3) & (titanic['Sex'] == 'male')]['Age'].mean()
media_idade_mulheres_Pclasse_3 = titanic[(titanic['Pclass'] == 3) & (titanic['Sex'] == 'female')]['Age'].mean()
dependencias = titanic[(titanic['SibSp'] > 0) | (titanic['Parch'] > 0)]['PassengerId'].count()
irmaos_conjugues = titanic[titanic['SibSp'] > 0]['PassengerId'].count()
media = titanic['Fare'].mean()
media_homens = titanic[titanic['Sex'] == 'male']['Fare'].mean()
media_mulheres = titanic[titanic['Sex'] == 'female']['Fare'].mean()

print("Quantidade de homens:", homens)
print("Quantidade de mulheres:", mulheres)
print("Média de idade de homens:", idade_homens)
print("Média de idade de mulheres:", idade_mulheres)
print("Número de sobreviventes:", Survived)
print("Número de mortos:", mortos)
print("Número de pessoas na Pclasse 1:", Pclass_1)
print("Número de pessoas na Pclasse 2:", Pclass_2)
print("Número de pessoas na Pclasse 3:", Pclass_3)
print("Homens na Pclasse 1:", homens_Pclass_1)
print("Mulheres na Pclasse 1:", mulheres_Pclass_1)
print("Homens na Pclasse 2:", homens_Pclass_2)
print("Mulheres na Pclasse 2:", mulheres_Pclass_2)
print("Homens na Pclasse 3:", homens_Pclass_3)
print("Mulheres na Pclasse 3:", mulheres_Pclass_3)
print("Média de idade de homens na Pclasse 1:", media_idade_homens_Pclass_1)
print("Média de idade de mulheres na Pclasse 1:", media_idade_mulheres_Pclasse_1)
print("Média de idade de homens na Pclasse 2:", media_idade_homens_Pclasse_2)
print("Média de idade de mulheres na Pclasse 2:", media_idade_mulheres_Pclasse_2)
print("Média de idade de homens na Pclasse 3:", media_idade_homens_Pclasse_3)
print("Média de idade de mulheres na Pclasse 3:", media_idade_mulheres_Pclasse_3)
print("Número de passageiros com dependentes:", dependencias)
print("Número de passageiros com irmãos ou conjugues:", irmaos_conjugues)
print("Média de preço da passagem:", media)
print("Média de preço da passagem para homens:", media_homens)
print("Média de preço da passagem para mulheres:", media_mulheres)