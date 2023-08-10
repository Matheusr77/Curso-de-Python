#Atividade 10
#Lendo a quantidade de dinheiro que uma pessoa tem na carteira e ver quantos dólares ela pode comprar

print("Neste programa vamos ver quantos dólares você pode comprar\n")
print("Lembrando que vamos usar a cotação de U$1,00 = R$4,87\n")

valor = float(input("Digite a quantos reais você tem: "))

dolar = valor / 4.87

print(f"\nVocê pode comprar {dolar:.2f} dólares")

