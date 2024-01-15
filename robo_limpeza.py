#Algoritmo de um robô de limpeza.
#Ele vai percorrer uma área de vai coletar 10 itens de sujeira, após isso ele retorna para a base.

import random


sala = [0] * 16

for i in range(16):
    indice_aleatorio = random.randint(0, 15)
    sala[indice_aleatorio] = 1

print(f'A sala com sujeira: {sala}')

coletor = 0

for i in range(16):
    if sala[i] == 1:
        sala[i] = 0
        coletor += 1
        if coletor == 10:
            break

print(f'A sala limpa: {sala}')
