listagem = ('Lápis', 2.75,
            'Borracha', 5,
            'Régua', 7,
            'Caderno', 15.90,
            'Compasso', 10,
            'Mochila', 120.75,
            'Kit de canetas', 5.50,
            'Livro', 200.99,)
print(f'{"LOJA CAPITALISTA OPRESSORA":^40}')
print('Onde sua opressão, é nossa emoção(;')
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

