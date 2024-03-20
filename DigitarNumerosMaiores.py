'''
    Escreva um que solicita 10 números ao usuário, e ao final mostre
    os dois maiores números digitados pelo usuário. 
'''

maior01 = 0
maior02 = 0

for cont in range(1, 11):
    num = int(input("Digite um Número: "))
    if(num > maior01):
        maior02 = maior01
        maior01 = num
    elif(num > maior02):
        maior02 = num
   
print(f"Os dois maiores números são: {maior01} - {maior02}")        