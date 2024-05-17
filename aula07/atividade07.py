# Construa um programa que leia dois números inteiros: a e b
# e uma lista com N valores inteiros (N fornecido pelo usuário).
# O programa deverá imprimir quantos elementos da Lista
# pertencem ao intervalo [a;b]

num01 = int(input("Digite o primeiro valor inteiro: "))
num02 = int(input("Digite o segundo valor inteiro: "))

lista = []
# contador = 0

num = int(input("Digite o valor da lista: "))

while num > 0:
    lista.append(num)
    
    num = int(input("Digite o valor da lista: "))

# for i in lista[num01:num02]:
#     contador += 1

print(f"\n No intervalo de '{lista[num01:num02]}' tem '{len(lista[num01:num02])}' elementos")


    