from random import choice
n1 = input('Nome do aluno(a):')
n2 = input('Nome do aluno(a):')
n3= input('Nome da aluna(o):')
n4= input('Nome do aluno(a):')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O auluno(a) escolhido(a) foi', escolhido)

from random import shuffle
aluno1 = input('Aluno(a):')
aluno2 = input('Aluno(a):')
aluno3 = input('Aluno(a):')
aluno4 = input('Aluno(a):')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem da apresentação será')
print(lista)

