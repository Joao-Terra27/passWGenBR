from time import sleep
from functs import dados

def usuario():
    user = int(input(' \33[1;34m>>>\33[m '))
    sleep(1)
    if user == 1:
        return f'Feito! Sua nova senha é {dados.data[user-1]}'
        
    elif user == 2:
        return f'Feito! Sua nova senha é {dados.data[user-1]}'

    elif user == 3:
        return f'Feito! Sua nova senha é {dados.data[user-1]}'

    elif user == 4:
        return f'Feito! Sua nova senha é {dados.data[user-1]}'

    elif user == 5:
        return f'Feito! Sua nova senha é {dados.data[user-1]}'
        
    else:
        return 'ERRO! O valor inserido é inválido. Por favor escolha um valor entre 1 e 5'  