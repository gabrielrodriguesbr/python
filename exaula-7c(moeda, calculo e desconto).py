real = float(input('Quantos reais você tem na carteira? R$'))
dólar = real / 5.26
euro = real / 5.95
print('Com R${:.2f} você pode comprar US${:.2f} e £{:.2f}'.format(real, dólar, euro))

larg = float(input('Largura da parede:'))
alt = float(input("Altura da parede:"))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você precisará de {}L de tinta'.format(tinta))

preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$', preço, 'na promoção custará R$', novo)






