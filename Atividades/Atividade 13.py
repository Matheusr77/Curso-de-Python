#Atividade 13
# Algoritmo que vai ler o salário de um funcionário e vai retornar com um aumento de 15%

print('Com este algoritmo irei mostrar seu salário com um aumento de 15%. \n')
n1 = int(input('Digite aqui seu salário atual:'))

ai = (n1 * 15) / 100
a = n1 + ai

print(f'O seu novo salário é de R${a:.2f}.')

