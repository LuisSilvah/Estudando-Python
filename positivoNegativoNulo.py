# Verificar se o valor é Positivo, Negativo ou Nulo

numero = int(input('Digite algum número: '))

if(numero >= 0):
    if(numero > 0):
        print(f'Número: {numero} é positivo')
    
    else: 
        print(f'Número: {numero} é nulo')

else: 
    print(f'Número: {numero} é negativo')    