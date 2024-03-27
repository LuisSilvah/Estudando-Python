'''
    Implemente um programa que determine se um inteiro e
positivo dado pelo usuário, é primo

'''

num = int(input("Digite um número inteiro: "))

while(num > 0):
    if(num%2 == 0 or num%3 == 0 or num%5 == 0):
        print(f"Número não é primo: {num}")
    else: 
        print(f"Número é primo: {num}")
    num = int(input("Digite um número inteiro: "))

print("Número digitado é negativo")       