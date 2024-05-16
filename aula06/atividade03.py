# Elabore um programa que leia nome, sexo e idade de um
# usuário. Se sexo for feminino e idade menor que 25,
# imprime o nome da pessoa e a palavra “ACEITA”, caso
# contrário imprimir “NÃO ACEITA”.

nomeUsuario = input("Digite o nome do usuário: ")
sexo = input("Qual o sexo do usuário (Feminino / Masculino): ").lower()
idade = int(input("Digite a idade do usuário: "))

if (sexo == "feminino" and idade < 25):
    print(f"{nomeUsuario} ACEITA")
else:
    print("NÃo ACEITA")