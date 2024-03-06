'''

2. (DESAFIO) Construir um programa que faz a leitura de três
número inteiros e imprime o maior

'''

numero01 = int(input('Digite o valor do primero número: '))
numero02 = int(input('Digite o valor do segundo número: '))
numero03 = int(input('Digite o valor do terceiro número: '))

if(numero01 > numero02 and numero01 > numero03):
    print(f"Maior número é {numero01}")

else: 
    if(numero02 > numero01 and numero02 > numero03):  
       print(f"Maior número é {numero02}")  

    else:
        print(f"Maior número é {numero03}")