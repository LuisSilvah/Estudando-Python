# Escreva um programa que leia a idade e o primeiro nome de
# várias pessoas. Seu programa deve terminar quando uma
# idade negativa for digitada. Ao terminar, seu programa deve
# escrever o nome e a idade da pessoa mais jovem e mais
# velha.

nomeUsuario = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))

nomeJovem = nomeUsuario
idadeJovem = idade

nomeVelho = ""
idadeVelho = 0

while idade >= 0:
    
    if(idade > idadeVelho):
        idadeVelho = idade
        nomeVelho = nomeUsuario
        
    elif (idade < idadeJovem):
        idadeJovem = idade
        nomeJovem = nomeUsuario 
        
    nomeUsuario = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    

print("\n Teminou codigo")
print(f"\n Nome Velho {nomeVelho} \n Idade Velho {idadeVelho}")
print(f"\n Nome Jovem {nomeJovem} \n Idade Jovem {idadeJovem}")