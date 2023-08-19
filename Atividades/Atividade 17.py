#Atividade 17
#Calculando a Hipotenusa

import math

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hip = pow(co, 2) + pow(ca, 2)
hip = math.sqrt(hip)

print(f"A hipotenusa é: {hip:.2f}")
