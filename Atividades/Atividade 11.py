#Atividade 11
# Programa que vai ler a altura e largura em metros e logo depois calcular a quantidade de tinta necessária para pintá-la
# OBS: Cada litro de tinta pinta 2m²

print("Vamos definir quantos litros de tinta será necessário para pintar uma parede\n")

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = alt * larg

litros = area / 2

print(f"\nSerá necessário {litros:.2f} litros de tinta para pintar uma parede")