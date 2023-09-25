import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    'tamanho_coleira': ['Pequeno', 'Médio', 'Grande', 'Médio', 'Grande', 'Pequeno'],
    'tamanho_botas_correto': [1, 0, 1, 0, 1, 1] 
})

data = pd.get_dummies(data, columns=['tamanho_coleira'], drop_first=True)

X = data.drop('tamanho_botas_correto', axis=1)
y = data['tamanho_botas_correto']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Acurácia do Modelo: {accuracy}')
print(f'Relatório de Classificação:\n{report}')

def prever_tamanho_botas(tamanho_coleira):
    input_data = pd.get_dummies(pd.Series(tamanho_coleira), drop_first=True)

    predicao = model.predict(input_data)

    if predicao[0] == 1:
        return "Tamanho correto"
    else:
        return "Tamanho incorreto"

tamanho_coleira_cliente = 'Pequeno'  
resultado_previsao = prever_tamanho_botas(tamanho_coleira_cliente)
print(f"Previsão para o cliente: {resultado_previsao}")

