#1.Crie uma tupla com varias palavras(sem acento), voce devera mostrar para cada palavra quais as vogais existente.
vogal = []
tupla = ('eric','matheus','rogerio','raquel')

for palavra in tupla:
    print()
    print(f'Palavra: {palavra}')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f' vogais: {letra}', end='')
