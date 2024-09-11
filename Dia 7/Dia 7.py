# Escreva um programa que calcula a tabuada de um número. (Python)

# numero = int(input('Digite o número que deseja calcular a tabuada: '))
numero = int(input('Digite o número que deseja calcular a tabuada, digite um numero de 1 a 10: '))

print(f"\nTabuada do número {numero}:")

for i in range(1, 11):
    calculo = numero * i
    print(f"{numero} X {i}= {calculo}")
