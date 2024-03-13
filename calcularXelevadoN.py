'''
Escreva um programa que calcule x elevado a n. Considere que n é um
valor inteiro não negativo. PROIBIDO USAR QUALQUER FUNÇÃO
MATEMATICA EXISTENTE no PYTHON

'''

baseNumero = int(input("Digite a base do numero: "))
elevadoNumero = int(input("Digite o valor da potencia: "))

resultadoPotencia = 1
contador = 1

while(contador <= elevadoNumero):
    print(f"Elevar o numero {elevadoNumero} === {baseNumero} * {baseNumero}")
    resultadoPotencia = resultadoPotencia * baseNumero
    contador = contador + 1

print(f"WHILE finalizado {resultadoPotencia}")    


