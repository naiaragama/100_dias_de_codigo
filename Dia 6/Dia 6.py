# Faça um programa que calcula o fatorial de um número. (Python)

numero = int(input('Digite o número para realizar o fatorial: '))
if numero == 1 or numero == 0:
    print(f' O fatorial de {numero} é: {1}')
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f' O fatorial de {numero} é: {fatorial}')
