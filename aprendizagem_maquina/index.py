import random
import math

def sigmoid(x):
    return math.tanh(x)

input_size = 2  # Tamanho da entrada
hidden_size = 2  # Número de neurônios na camada oculta
sequence_length = 3  # Comprimento da sequência

W_input = [[random.uniform(-1, 1) for _ in range(input_size)] for _ in range(hidden_size)]
W_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(hidden_size)]

input_sequence = [[random.uniform(-1, 1) for _ in range(input_size)] for _ in range(sequence_length)]

hidden_state = [0.0] * hidden_size

for input_data in input_sequence:
    new_hidden_state = [0.0] * hidden_size
    for j in range(hidden_size):
        new_hidden_state[j] = sum(W_input[j][i] * input_data[i] + W_hidden[j][k] * hidden_state[k] for i in range(input_size) for k in range(hidden_size))
        new_hidden_state[j] = sigmoid(new_hidden_state[j])

    hidden_state = new_hidden_state

output = hidden_state
print("Saída :", output)
