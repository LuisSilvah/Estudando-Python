'''

    Faça um programa que receba a idade, altura e peso de 25
pessoas. Calcule e mostre:
    a. A quantidade de pessoas com idade superior a 50
    anos
    b. A média das alturas das pessoas com a idade entre 10
    e 20 anos
    c. O percentual de pessoas com peso inferior a 50 quilos.

'''

qtdPessoas = 0
qtdPessoasAltura = 0
qtdPessoasPeso = 0
qtdPessoasMaior50Anos = 0
mediaAltura = 0


for cont in range(1, 6):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = int(input("Digite a peso: "))
    
    qtdPessoas += 1

    if(idade >= 50): 
        qtdPessoasMaior50Anos += 1
    elif(idade >= 10 and idade <= 20):
        qtdPessoasAltura += 1
        mediaAltura += altura

    if(peso < 50):
        qtdPessoasPeso += 1
    
    print(f'\t Resultado:  \n\t\t Quantidade de pessoas maior que 50 anos: {qtdPessoasMaior50Anos:.1f}')
    print(f'\n\t\t Média das alturas das pessoas com a idade entre 10 e 20 anos: {mediaAltura/qtdPessoasAltura:.2f} ')
    print(f'\n\t\t O percentual de pessoas com peso inferior a 50 quilos: {(qtdPessoasPeso / qtdPessoas)*100} %')
    

