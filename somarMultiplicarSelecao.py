'''

Construir um programa que faz a leitura de dois valores inteiros A e
B. Se os valores forem iguais deverá somar os dois, caso contrário
multiplique A por B. Ao final de qualquer um dos cálculos deve-se
atribuir o resultado para uma variável C e mostrar seu conteúdo na
tela

'''


numeroA = int(input('Digite o valor do primero número: '))
numeroB = int(input('Digite o valor do segundo número: '))

if(numeroA == numeroB):
    numeroC = numeroA + numeroB
    # print(f'A Soma dos valores é {numeroC}')

else: 
    numeroC = numeroA * numeroB
    # print(f'A Multiplicação dos valores é {numeroC}')

print(f'Resultado da conta: {numeroC}')
