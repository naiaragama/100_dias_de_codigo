# Desafio: Crie uma calculadora simples que realiza operações de adição, subtração, divisão e multiplicação.

operacao = input('Qual operação deseja realizar? Digite adição, subtração, divisão ou multiplicação: ').lower()
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o primeiro número: '))

if operacao == 'adição':
    calculo = numero1 + numero2
elif operacao == 'subtração':
    calculo = numero1 - numero2
elif operacao == 'divisão':
    calculo = numero1 / numero2 
else:
    calculo = numero1 * numero2

print(f'O resultado da operação é: {calculo}')
