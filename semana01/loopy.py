'''
# Exercício 1 - imprimir números de 1 a 10
for i in range(1, 11):
    print(i)

print("-----")

# Exercício 2 - imprimir apenas números pares
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("-----")

# Exercício 3 - soma de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i

print("Soma:", soma)


# Exercício 4 - Tabuada 

numero = int(input('Digite um número:'))
for c in range(1,11):
    resultado = c * numero
    print(f'{numero} * {c} = {resultado}')

# Exercício 4.1 - Tabuada com While

numero = int(input('Digite um número (0 para sair): '))
while numero != 0:
    for c in range(1,11):
        resultado = c * numero
        print(f'{numero} * {c} = {resultado}')
    numero = int(input('Digite um número (0 para sair): '))        

'''

# Exercício 4.2 - Tabuada 
lista = []
while True:
    numero = int(input('Digite um número para mostrar a tabuada (0 para sair): '))
    if numero == 0:
        break
    lista.append(numero)
    for c in range(1,11):
        resultado = numero * c
        print(f'{numero} * {c} = {resultado}')
    continua = (input('Deseja continuar? (s/n)')).lower()
    if continua != 's':
        break
print(f'Você calculou as tabuadas dos números {lista}')    




