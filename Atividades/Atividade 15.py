#Atividade 15
#Aluguel de Carros sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input("Digite quantos Km o carro rodou? "))
dias = float(input("Digite quantos que o carro foi alugado? "))

km = km * 0.15
dias = dias * 60

soma = km + dias

print(f"O total do aluguel foi {soma:.2f}")
