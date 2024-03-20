'''
Escrever um algoritmo que leia uma quantidade desconhecida de
números e conte quantos deles estão nos seguintes intervalos:
[0.25], [26,50], [51,75] e [76,100]. A entrada de dados deve
terminar quando for lido um número negativo.
'''

num = int(input('Digit um valor: '))

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while(num != 0):
    if(num <= 25):
        intervalo1 += 1
        print(f'interalo 1: {num}')
    elif(num >= 26 and num <= 50 ):
        intervalo2 += 1
        print(f"interalo 2: {num}")
    elif(num >= 51 and num <= 75):
        intervalo3 += 1
        print(f"interalo 3: {num}")
    elif(num <= 100): 
        intervalo4 += 1
        print(f"interalo 4: {num}")
    else:
        print("Valor fora dos interalos")

    num = int(input('Digit um valor: '))
else: 
    print("Valores digitado em cada intervalo:")
    print(f"Primeiro intervalo: {intervalo1}")
    print(f"Segundo intervalo: {intervalo2}")
    print(f"Terceiro intervalo: {intervalo3}")
    print(f"Quarto intervalo: {intervalo4}")


