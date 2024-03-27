'''

    A prefeitura de uma cidade fez uma pesquisa entre seus
habitantes, coletando dados sobre o salário e número de
filhos. A prefeitura deseja saber:

    a. média do salário da população;
    b. média do número de filhos;
    c. maior salário;
    d. percentual de pessoas com salário até R$100,00

'''

qtdPesquisa = int(input("Digite a quantidade de pesquisa a ser realizada: "))

mediaSalario = 0
mediaFilho = 0
maiorSalario = 0
qtdSalarioMenor100 = 0

for cont in range(1, qtdPesquisa + 1 ):
    salario = float(input("Digite o salário: "))
    filho = int(input("Digite o número de filhos: "))
    mediaSalario += salario
    mediaFilho += filho

    if(salario > maiorSalario): 
        maiorSalario = salario
    
    if(salario <= 100):
        qtdSalarioMenor100 += 1

print(f'\t Resultado:  \n\t\t Média de salário: {mediaSalario/qtdPesquisa:.2f}')
print(f'\n\t\t Média de filho: {mediaFilho/qtdPesquisa:.2f} ')
print(f'\n\t\t Maior Salário: {maiorSalario:.2f}')
print(f'\n\t\t Percentual de pessoas com salário até R$ 100,00: {(qtdSalarioMenor100/qtdPesquisa)*100} %')
    