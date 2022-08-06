from rich import print
import os

# rodar sempre, mostrar candidatos, escolha do usuário e loop(reiniciar)
#pass para branco ou nulo, os.system('cls') pra limpar automático

VOTOS_BOLSONARO = 0
VOTOS_LULA = 0
while True:
    print('-'*20)
    print(f'[on blue]Total Bolsonaro:[/]{VOTOS_BOLSONARO}{os.linesep}[on red]Total Lua:[/]{VOTOS_LULA}')
    print('-'*20)
    try:
        voto= int(input(f'Escolha seu voto:{os.linesep}1- BOLSONARO{os.linesep}2- LULA{os.linesep} Sua escolha: '))
        if voto==1:
            VOTOS_BOLSONARO +=1
        elif voto==2:
            VOTOS_LULA +=1
        else:
            pass
    except:
        print('Digite APENAS 1 ou 2!')
    os.system('cls')