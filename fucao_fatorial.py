# Função para calcular o fatorial de um número inteiro!


def fatorial(valor_fatorial):
    fatorial = 1
    contador = valor_fatorial
    while contador > 1: 
        fatorial *= contador 
        contador -= 1 
    return fatorial

print(fatorial(int(input("Digite um número para calcular o fatorial: "))))