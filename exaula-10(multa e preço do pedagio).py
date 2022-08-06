velocidade = float(input('Qual a velocidade atual do seu carro?'))
if velocidade > 80:
    print('Você foi multado pois, excedeu a velociade máxima permitida de 80km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')

n = int(input('Me diga um número:'))
resultado = n % 2
if resultado == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))

d = float(input('Qual a distância da sua viagem(km/h):'))
print('Você fará uma viagem de {}km/h'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preço))





