#Média anual escolar

print('Média anual escolar')
print()

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 9 and media <= 10:
    nota = 'A'
elif media >= 8 and media < 9:
    nota = 'B'
elif media >= 7 and media < 8:
    nota = 'C'
elif media >= 6 and media < 7:
    nota = 'D'
elif media >= 5 and media < 6:
    nota = 'E'
else:
    nota = 'F'

print(f'Sua média anual é {media:.1f} e sua nota é {nota}.')