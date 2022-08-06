peso = float(input('Qual o seu peso? (kg)'))
altura = float(input('Qual a sua altura? (m)'))
IMC = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= IMC < 25:
    print('Você está no peso ideal!')
elif 25 <= IMC < 30:
    print('Você está em sobrepeso!')
elif 30 <= IMC < 40:
    print('Você está na faixa de obesidade, cuidado!')

print('{:=^40}'.format(' LOJAS HIPER RODRIGUES '))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opção = int(input('Qual a opção escolhida?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2X de {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('Opção inválida de pagamento! Tente novamente')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))








