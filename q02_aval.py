#Ler a idade de 10 alunos e exibir quantos alunos tem idade maior que 20. Calcule e apresente a média de idade destes alunos.




idades_alunos = []
mais_de_20 = 0
soma = 0

# Lendo as idades dos 10 alunos
for i in range(1, 11):
    idade = int(input(f"Informe a idade do aluno {i}: "))
    
    # Armazenando a idade na lista
    idades_alunos.append(idade)

    # Verificando se o aluno tem mais de 20 anos
    if idade > 20:
        mais_de_20 += 1
        soma += idade

# Calculando a média de idade dos alunos com mais de 20 anos
if mais_de_20 > 0:
    media = soma / mais_de_20


print(f'A lista de idade dos alunos é: {idades_alunos}')
print(f'\nQuantidade de alunos com mais de 20 anos: {mais_de_20}')
print(f"Média de idade dos alunos com mais de 20 anos: {media:.2f}")
