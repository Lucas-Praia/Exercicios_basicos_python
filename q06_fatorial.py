#06.criar um programa para solicitar 10 valores inteiros do usuário, calcular o fatorial destes valores e exibir o
# resultado de cada fatorial.
import random
import math

num = random.randint(0,10)
fatorial = math.factorial(num)
print(f'O fatorial de {num} é {fatorial}')
