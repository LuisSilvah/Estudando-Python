'''

Faça um programa que imprima os números inteiros de 100 a
450, que são múltiplos de 7

'''

contador = 100

while(contador <= 450):
    if (contador%7==0):
        print(f"Multiplo de 7 {contador}")
    contador = contador + 1

print("while finalizado...")
