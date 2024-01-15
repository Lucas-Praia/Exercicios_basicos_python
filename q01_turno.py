#01. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"ou "Valor Inválido!", conforme o caso.

while True:

    turno = input('Em que turno você estuda?[M]anhã, [V]espertino, [N]oturno: ')

    if turno == 'M':
        print('Bom dia!')
    elif turno == 'V':
        print('Boa tarde!')
    elif turno == 'N':
        print('Boa noite!')