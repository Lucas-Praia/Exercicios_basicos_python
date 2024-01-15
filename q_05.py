#5.Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
# VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível.
#Calcule e mostre:
#A. O modelo do carro mais econômico;
#B. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
# quilômetros e quanto isto custará, considerando um que a gasolina custe 2,25 o litros


carros = ['Fusca', 'Gol', 'Vectra', 'Celta', 'Kombi']
consumo = [10, 15, 12, 18, 20]


print(f' O modelo mais econômico é: {carros[2]}')

distancia = 1000
preco_gasolina = 2.25

for i in range(len(carros)):
    carro = carros[i]
    consumo_carro = consumo[i]

    litros = distancia / consumo_carro
    custo = litros * preco_gasolina

    print(f" O {carro} consome {litros} litros para percorrer 1000 km, com custo de R${custo}")
