tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas de 18 anos ou mais é {tot18}.')
print(f'Ao todo temos {totH} homem(ns) cadastrado(s).')
print(f'E temos {totM20} mulher(es) com menos de 20 anos de idade.')
