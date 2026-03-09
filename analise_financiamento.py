#Programa para saber se você pode ou não financiar uma casa!

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Digite a quantidade de anos para pagar: '))

parcela = valor_casa / (anos * 12)

if parcela > salario * 30 / 100:
    print(f'Empréstimo negado. A parcela mensal é de: R$ {parcela:.2f}, que é maior que 30% do salário.')
elif parcela == salario * 30 / 100:
    print(f'Foi aprovado, mas a parcela mensal é de: R$ {parcela:.2f}, que é exatamente 30% do salário. Cuidado com o orçamento!')
else:
    print(f'Empréstimo aprovado. A parcela mensal é de: R$ {parcela:.2f}')
    print('Obrigado por financiar conosco!')
    