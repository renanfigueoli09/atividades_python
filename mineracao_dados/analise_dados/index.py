import pandas as pd

data = pd.read_csv('sarespv1.csv')

basica = data[data['classification'] == 'Básico'].groupby('SERIE_ANO').size()
print("classificação basica por serie", basica)

diferentes_classificacoes = data.groupby(['SERIE_ANO', 'classification']).size()
print("Alunos com diferentes classificações(por serie): ",diferentes_classificacoes)
#ANTONIO BRASILIO MENEZES DA FONSECA PROFESSOR
escola1 = data[data['NOMESC'] == 'ANTONIO BRASILIO MENEZES DA FONSECA PROFESSOR']
print("Escola Antônio Basílio Menezes da Fonseca: ",escola1)

desempenho_da_escola1 = escola1.groupby(['SERIE_ANO', 'classification'])['medprof'].mean()
print("media de desempenho da esola Antônio Basílio Menezes da Fonseca: ",desempenho_da_escola1 )
