#2. Crie uma tupla preenchida com uma contagem por extenso de zero a vinte,seu programa devera ler um numero
# entre 0 a 20 e mostra-lo por extenso.

contagem = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
            'quatroze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numero = int(input('Digite um número: '))
for i in range(20):
    if numero == i:
        i = contagem[i]
        print(i)