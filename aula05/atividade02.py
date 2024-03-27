'''
    Elabore um programa que leia vários números inteiros, até
o usuário digitar um número negativo. Para cada número
lido deverá ser calculado e impresso seu fatorial

    '''

num = int(input("Digite um número inteiro: "))
fatorial = 1

while(num > 0):
    for cont in range(1, num +1):
        fatorial = fatorial * cont
        print(f"Fatorial: {fatorial}")
    fatorial = 1
    num = int(input("Digite um número inteiro: "))
    

print("Número digitado é negativo")    