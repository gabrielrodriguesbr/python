soma = cont = 0
while True:
    n = int(input('Digite um número[999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont +=1
print(f'A soma dos {cont} valores foi {soma}!')

#Esse mostra a tabuada dos positivos e negativos
while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

#Esse mostra a tabuada só dos positivos
while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('Não sou obrigado a isso, programa encerrado!')