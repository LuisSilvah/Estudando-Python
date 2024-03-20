'''
    Elabore um programa que leia um número e imprima todos os
    números divisíveis por 4 que sejam menores que este número lido
'''

num = int(input("Digite um valor: "))

for cont in range(1, num):
    if(cont % 4 == 0): 
        print(f"Valor divisivel por 4: {cont}")