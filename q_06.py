#6.Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar cerca de 200 mouses
# que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
# número indeterminado de entradas, cada uma contendo: um número de identificação do mouse e o tipo de defeito:
#1. Necessita de esfera;
#2. Necessita de limpeza;
#3. Necessita troca do cabo ou conector;
#4. Quebrado ou inutilizado
#5. Uma identificação fora dessa faixa deve retornar uma mensagem de erro.

print(f"{'-'*20} BEM VINDO AO CONTROLE DE QUALIDADE DAS SUCATAS {'-'*20}")

dic = {

}

while True:
    id = int(input('Insira o id: \n'))


    defeito = int(input('\nQual o serviço a ser realizado? [1]Necessita de esfera; [2]Necessita de limpeza; ['
                        '3]Necessita troca do cabo ou conector; [4] Quebrado ou inutilizado\n'))

    if defeito == 1:

        dic[id] = 'Necessade de esferas.'

    elif defeito == 2:
        dic[id] = 'Necessade de limpeza.'
    elif defeito == 3:
        dic[id] = 'Necessade troca do cabo ou conector.'
    elif defeito == 4:
         dic[id] = 'Quebrado ou inutilizado.'
    else:
        print('Erro. Índice Inválido')
        print('O dicionário com o ID e seus respectivos valores é: \n')
        print(dic)







