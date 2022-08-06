n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para se alistar'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))




