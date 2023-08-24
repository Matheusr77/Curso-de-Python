#Atividade 22
#Analisador de Textos

nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome com todas as letras maiúsculas é: {nome.upper()}")
print(f"Seu nome com todas as letras minúsculas é: {nome.lower()}")
print(f"O seu nome tem {(len(nome) - nome.count(' '))} letras")
print(f"O seu primeiro nome tem {nome.find(' ')} letras")
