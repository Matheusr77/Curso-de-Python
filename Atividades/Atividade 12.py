#Atividade 12
#Algoritmo que vai ler o preço de um produto e aplicar um desconto de 5%

print('Com este algoritmo irei aplicar um desconto de 5% em qualquer produto.\n')
n1 = float(input('Digite aqui o preço do produto:'))

di = (n1 * 5) / 100
d = n1 - di

print(f'O desconto do produto é de R${di:.2f}.')
print(f'Já o preço final com o desconto aplicado é R${d:.2f}.')
