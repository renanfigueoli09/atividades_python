import numpy as np

array_inteiros = np.arange(1, 11)
print("array de inteiros", array_inteiros)

array_random_float = np.random.rand(300, 200, 3)
print("array de números aleatórios:", array_random_float)

notas_alunos = np.random.randint(1, 11, size=(20, 3))
print("Array de notas de alunos:\n", notas_alunos)

array_original = np.arange(1, 13)
matriz = array_original.reshape(3, 4)
matriz_transposta = matriz.T
print("Matriz original:\n", matriz)
print("Matriz transposta:\n", matriz_transposta)

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

soma = array1 + array2
subtracao = array1 - array2
multiplicacao = array1 * array2
divisao = array1 / array2

print("Soma:\n", soma)
print("Subtração:\n", subtracao)
print("Multiplicação:\n", multiplicacao)
print("Divisão:\n", divisao)

array_numeros = np.arange(1, 21)
elementos_pares = array_numeros[1::2]
print("Elementos pares:\n", elementos_pares)

array_random_maiores_que_50 = np.random.randint(1, 101, size=10)
numeros_maiores_que_50 = array_random_maiores_que_50[array_random_maiores_que_50 > 50]
print("Números aleatórios maiores que 50:\n", numeros_maiores_que_50)

array_numeros_aleatorios = np.random.rand(10)
media = np.mean(array_numeros_aleatorios)
mediana = np.median(array_numeros_aleatorios)
desvio_padrao = np.std(array_numeros_aleatorios)

print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
