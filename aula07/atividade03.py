# Elabore um programa que leia uma lista de no máximo 20
# elementos inteiros. Em seguida o programa deverá imprimir
# a quantidade de valores múltiplos de 3.


lista = []
multiplos = []

for i in range(1,4):
    num = int(input(f"Digite o valor do {i}° número: "))
    lista.append(num)
    
for num in lista: 
    if (num % 3 == 0):
        multiplos.append(num)
       
    
print(f"Existem '{len(multiplos)}' Números multiplos de 3")   
print(f"\n {multiplos}")