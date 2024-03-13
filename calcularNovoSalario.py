'''
 Ler o salário do funcionario e perguntar qual nivel ele e enquadra (plano) 
 e calcular novo salario


    PLANO   |   SALARIO
    1           10%
    2           15%
    3           20%

'''


novoSalario = 0

salarioAtual = int(input('Digite o salário do funcionário: '))
cargoPlano = int(input('Digite o plano do funcionário: '))


if (cargoPlano == 3 ):
        novoSalario = salarioAtual*1.3
elif(cargoPlano == 2 ):
        novoSalario = salarioAtual*1.2
else: 
        novoSalario = salarioAtual*1.1

print(f"Novo salário {novoSalario:.2f}")        

