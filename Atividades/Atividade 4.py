#Atividade 4

# Todas as variáveis
n1 = input('Digite alguma coisa e retornarei o seu tipo primitivo e demais informações:')

# Variáveis para definir o seu tipo
num = n1.isnumeric()
alpha = n1.isalpha()
alnum = n1.isalnum()
mai = n1.isupper()
min = n1.islower()
esp = n1.isspace()

# Print para retornar se é verdadeiro ou falso o seu tipo
print('O seu tipo primitivo é:', type(n1))
print(f'É um número? {num}') 
print(f'É alfabético? {alpha}')
print(f'É alfanúmerico? {alnum}')
print(f'Está em maiúsculas? {mai}')
print(f'Está em minúsculas? {min}')
print(f'Só tem espaços? {esp}')
# Ou print('Só tem espaços? ' ,a.isspace())