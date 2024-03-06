# Verfique se o numero digitado é multiplo por 5

numero = int(input('Digite algum número: '))

if(numero % 5 == 0):
    print(f'Número {numero} é multiplo de 5')

else: 
    print(f'Número {numero} não é multiplo de 5')