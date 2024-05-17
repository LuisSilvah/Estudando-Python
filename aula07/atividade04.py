# Elabore um programa que leia um conjunto de vários valores
# inteiros e os coloque em 2 listas conforme forem pares ou
# ímpares (uma lista para números pares e outra lista para
# números ímpares). A leitura dos números é finalizada
# quando um número negativo é lido.

num = int(input("Digite um valor inteiro: "))

listaPares = []
listaImpares = []

while num > 0:
    if(num % 2 == 0):
        listaPares.append(num)
    else:
        listaImpares.append(num)
    
    num = int(input("Digite um valor inteiro: "))

else:
    print("Todos os números pares \n")
    
    for par in listaPares:
        print(f"{par}", end=' ')
        
        
    print("\n Todos os números ímpares \n")
    
    for impar in listaImpares:
        print(f"{impar}", end=' ')