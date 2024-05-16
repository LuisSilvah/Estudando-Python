# Construa um programa que leia duas strings fornecidas pelo
# usuário e verifique se a segunda string lida está contida no
# final da primeira, imprimindo o resultado da verificação.

string01 = input("Digite a primeira string: ").lower()
string02 = input("Digite a segunda string: ").lower()

if(string02 in string01):
    print("A segunda string contém na primeira string")
else:
    print("As duas string são diferentes")