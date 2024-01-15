#02.Numa eleição existem três candidatos,(candidato01, candidato 02, candidato 03).Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato e o total de votos em branco. Mostre também qual foi o candidato que ganhou a eleição.

cad_01 = 0
cad_02 = 0
cad_03 = 0
brancos = 0
vencedor = 0
maior = 0

eleitor = int(input('Quantos eleitores votaram?'))

for i in range (eleitor):
    voto = int(input(f'{i+1}º eleitor, digite o número do candidato : 1,2,3,0(branco) que você deseja votar:'))

    if voto ==1:
        cad_01+=1

    elif voto ==2:
        cad_02+=1
    
    elif voto ==3:
        cad_03+=1
    
    elif voto ==0:
        brancos+=1
    
    if cad_01 > maior:
        maior = cad_01
        
    if cad_02 > maior:
        maior = cad_02
    if cad_03 > maior:
        maior = cad_03 
    if brancos > maior:
        maior = brancos
    

print(f'O número de votos que o Candidato 1 recebeu foi : {cad_01} ')
print(f'O número de votos que o Candidato 3 recebeu foi : {cad_02} ')
print(f'O número de votos que o Candidato 3 recebeu foi : {cad_03} ')
print(f'O número de votos que o brancos recebeu foi : {brancos} ')
print(f'O vencedor foi: {maior}')
