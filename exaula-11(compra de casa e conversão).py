casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')

num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')