# Desafio: Escreva um programa que verifica se um número é par ou ímpar.

numero = int(input("Digite um número: "))

resultado = numero % 2

if resultado == 0:
    print("O numero digitado é par")
else:
    print("O número digitado é impar")
