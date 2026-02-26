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