import re
def clear_text(text):
    clear = re.sub(r'[\n\r\t]', ' ', text)
    clear = re.sub(r'[,.!%&]', '', clear)
    return clear

text = """
Eu digo a você hoje, meus amigos, que, embora enfrentemos as dificuldades de hoje e amanhã, eu ainda tenho um sonho. É um sonho profundamente enraizado no sonho americano.

Eu tenho um sonho que um dia esta nação se levantará e viverá o verdadeiro significado de sua crença - nós celebraremos essas verdades e elas serão claras para todos, que os homens são criados iguais.

Eu tenho um sonho que um dia nas colinas vermelhas da Geórgia, os filhos dos antigos escravos e os filhos dos antigos donos de escravos poderão sentar-se juntos à mesa da fraternidade.

Eu tenho um sonho que um dia até mesmo o estado do Mississippi, um estado sufocado pelo calor da injustiça, sufocado pelo calor da opressão, será transformado em um oásis de liberdade e justiça.

"""
print('texto origial', text)
print('novo texto', clear_text(text))
