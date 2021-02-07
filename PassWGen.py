from functs import dados, user
from time import sleep

while True:
    print(dados.senha())
    print()

    print('Qual senha deseja utilizar? [de 1 a 5]')
    print(user.usuario())
    
    resp = ' '
    while resp not in 'SN':
        print('\nDeseja gerar outra senha? [S/N]')
        resp = input('>>> ').strip().upper()[0]
        
    if resp == 'S':
        print(dados.senha())
        print('Escolha outra senha [de 1 a 5]')
        print(user.usuario())
    
    elif resp == 'N':
        print('Ok! Encerrando o programa...')
        sleep(1)
        break