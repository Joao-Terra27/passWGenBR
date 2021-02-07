from time import sleep
import random

def senha():
    global data
    
    low = 'abcdefghijklmnopqrstuvwxyz'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symb = '#@$%&-=+/.'
    numbs = '12345678910'
    data = []
    
    all = low + upp + symb + numbs
    
    print('O computador está gerando 5 senhas para você, por favor aguarde...')
    sleep(2)
    
    for x in range(1, 6):
        length = 16

        password = ''.join(random.sample(all, length))
        
        
        data.append(password[:])
    
    return data