# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__ - o init ele é o construtor, chama os parametros do
# metodo.
# Esse método é quem define o que acontece quando você cria uma instância da Classe

# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#sempre que quiser mexer no atributo dentro da classe, usa-se o self

#classes
#A classe aceita mais de um parametro. Vamos perguntar da classe TV qual o tamanho da tv do usuario. A resposta vai
# ser o parametro da classe tv.
#O atributo sempre tem o self antes
class TV:

    def __init__(self,size):
        self.cor = 'preta'
        self.ligada = False
        self.size = size
        self.canal = "Netflix"
        self.volume = 10

    #criando o metodo - começa com def - passando o canal, ele recebe o canal do usuario, passa o paramentro no (
    # novo_canal), ai p self.canal irá receber esse novo atributo
    def mudar_canal(self,novo_canal):
        self.canal = novo_canal

#o self é praticamente obrigatório, ele que passa os atributos do a classe específica. Ex: a tv sala só
# tem. E o self é dentro da classe, nao dentro do programa

#programa
# essa cor da tv sala é devido o atributo que ja está na classe tv.
#aqui vou passar o tamanho da tv.
tv_sala = TV(size= 55)
tv_quarto = TV(size= 32)

tv_sala.mudar_canal("globo")

print(tv_sala.canal)
print(tv_quarto.canal)
print(f'O tamanho da tv da sala é: {tv_sala.size}')
print(f'O tamanho da tv do quarto é: {tv_quarto.size}')

