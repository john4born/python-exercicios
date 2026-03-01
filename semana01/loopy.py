'''
#===================================
# Exercício 1 - imprimir números de 1 a 10
#===================================

for i in range(1, 11):
    print(i)
print('Fim da contagem')

#===================================
# Exercício 2 - imprimir apenas números pares
#===================================

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#===================================
# Exercício 3 - Soma simples
#===================================        

soma = 0
for c in range (1, 11):
    soma = soma + c
    print(c)
print(f'A soma total é {soma}')    

#===================================
# Exercício 4 - Loop com parada
#===================================  

while True:
    numero = int(input('Digite um número [0 para sair]: '))
    if numero == 0:
        break
print('Fim do programa...')  

#===================================
# Exercício 5 - Acumulador
#===================================  

total = 0
while True:
    numero = int(input('Digite um número para somar [0 para sair]: '))
    if numero == 0:
        break
    total += numero
print(f'A soma total dos número digitados é {total}')    

#===================================
# Exercício 6 - Contador
#===================================  

contador = 0
while True:
    numero = int(input('Digite um número [0 para sair]: '))
    if numero == 0:
        break
    contador += 1
print(f'A quantidade de números digitados foi de {contador}')    

#===================================
# Exercício 7 - Maior Número 
#=================================== 

maior = 0
while True:
    numero = int(input('Digite um número para validar o maior [0 para sair]: '))
    if numero == 0:
        break
    if numero > maior:
        maior = numero
print(f'O maior número digitado foi {maior}')   
    
'''
#===================================
# Exercício 8 - Menu Simples
#=================================== 

while True:
    print('1 - Tabuada')
    print('2 - Sair')
    opt = int(input('Digite uma opção: '))
    if opt == 2:
        break
    elif opt == 1:
        tabuada = int(input('Digite um número para apresentar a tabuada: '))
        for c in range(1, 11):
            resultado = tabuada * c
            print(f'{tabuada} x {c} = {resultado}')

    else:
        print('Opção inválida, digite novamente')
        
            



