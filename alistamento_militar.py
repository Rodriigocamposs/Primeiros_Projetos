nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - nascimento

if idade == 17:
    print('Esta na hora do alistamento militar')
elif idade < 17:
    print(f'Faltam {17 - idade} anos para se alistar')
elif idade > 17:
    print(f'Ja passou {idade - 17} anos do alistamento, procure o serviço militar mais proximo')