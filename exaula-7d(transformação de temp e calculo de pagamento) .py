salário = float(input('Quanto o funcionário ganha? R$'))
novo = salário + (salário * 15 / 100)
print('Com o aumento de 15%,o funcionário passará a ganhar R$', novo)
print('Um funcionário que ganhava R${:.2f},com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))

c = float(input('Informe a temperatura em °C:'))
f = ((9 * c) / 5) + 32
print('A temperatura de', c,'°C, corresponde a', f,'°F')

dias = int(input('Por quantos dias o carro foi alugado?'))
KM = float(input('Quantos kilômetros rodados?'))
pago = (dias * 60) + (KM * 0.15)
print('O total a pagar é R$', pago)
print('O total a pagar é R${:.2f}'.format(pago))








