#4. Crie 5 dicionario para guardar dados de um filme como :Titulo, Autor e ano de nascimento.Apos criados os cinco
# dicionario coloque esses dicionario dentro de uma lista que se chama Locadora.
#4.1 Mostre a primeira posicao da lista exbindo somente o nome do filme e o autor.

locadora = []
filme_1 = {
    'Titulo': 'Esqueceram do Thiago', 'Autor': 'Eric Douglas', 'Ano de nascimento':'1998'
}
filme_2 = {
    'Titulo': 'Raquel - O pesadelo dos alunos', 'Autor': 'Lucas Praia', 'Ano de nascimento':'1994'
}
filme_3 = {
    'Titulo': 'Quem é você?', 'Autor': 'Matheus Faneco', 'Ano de nascimento':'2000'
}
filme_4 = {
    'Titulo': 'Choram as rosas', 'Autor': 'Paulo Senna', 'Ano de nascimento':'1990'
}
filme_5 = {
    'Titulo': 'Thiago - The vocal', 'Autor': 'Thiago Nascimento', 'Ano de nascimento':'1990'
}
locadora.append(filme_1)
locadora.append(filme_2)
locadora.append(filme_3)
locadora.append(filme_4)
locadora.append(filme_5)

print(f"\nNome do filme: {locadora[0]['Titulo']}")
print(f"Autor: {locadora[0]['Autor']}")
print(('-' * 20))