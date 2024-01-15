#03.Você é desenvolvedor back-end da escola ETECH, e lhe foi dada a missão de desenvolver uma aplicação que tem por nome “JOGO DA ADIVINHAÇÃO”.
#O jogo deve solicitar ao usuário o seu nome para que ele seja tratado de forma particular, toda mensagem deste ponto em diante deve dirigir-se a ele pelo nome.
#Solicite ao usuário o nível de jogo que ele deseja jogar.(5pt)
#Nível 1 - número de 0 a 30, com 5 chances para acertar.
#Nível 2 - número de 0 a 100 com 3 chances para acertar.
#Se o jogador acertar o numero secreto o programa deverá parar.

import random
total_tentativas = 0

print('*********************************')
print('bem vindo ao jogo de adivinhação!')
print('*********************************')

nome = input('Digite o seu nome?\n')

while total_tentativas == 0:
    print(f'{nome}, qual o nível do jogo?\n')
    print("Nível [1] ou Nível [2]\n")
    nivel = int(input(f'{nome}, defina um nível: \n'))
    #nível_um
    if(nivel == 1):
        numero_secreto = random.randint(0,30)
        for i in range (1,6):
            total_tentativas = 5
            chute = int(input(f'{nome}, essa é a sua {i}ª tentativa. Chute um número de 0 a 30: \n'))
            if (chute ==numero_secreto):
                print(f'Parabéns!! Você acertou!. O número secreto era: {numero_secreto}\n')
                break
            elif (chute !=numero_secreto):
                print(f'Você errou!. Você tem {total_tentativas - i} tentativas.\n')
        else:
                print('You Lose. Tentativas esgotadas!!\n')
            
              
    elif(nivel == 2):
        numero_secreto = random.randint(0,100)
        total_tentativas = 3
        print(f'O número secreto é: {numero_secreto}')
        for j in range(1,4):
            chute = int(input(f'{nome}, essa é a sua {j}ª tentativa. Chute um númeo de 0 a 100: '))
            if (chute == numero_secreto):
                print(f'Parabéns!!. Você acertou. O número secreto era {numero_secreto}')
                break
            elif(chute!=numero_secreto):
                print(f'Você errou!. Você tem {total_tentativas - j} tentativas. \n')
        else:
            print('You Lose. Tentativas esgotadas!!\n')
    
    else:
        print("escolha um nível entre 1 e 2!")
        total_tentativas = 0