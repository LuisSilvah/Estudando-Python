# Elabore um programa que leia uma lista de no máximo 10
# elementos reais, o programa deverá imprimir o maior e
# segundo maior elemento e suas respectivas posições na
# lista

lista = []
maior = 0
menor = 99999999999999999

for i in range(1, 11):
    num = int(input(f"Digite o {i}° valor: "))
    
    lista.append(num)
    
for num in lista:

    if(num < menor):
        menor = num

    elif(num > maior):
        maior = num

for i in range(len(lista)):
    if(lista[i] == maior):
        print(f"{i} - {maior}")
    
    if(lista[i] == menor):
        print(f"{i} - {menor}")
        

print(lista)