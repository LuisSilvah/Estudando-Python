'''
(DESAFIO) Construir um programa que faz a leitura de duas
notas de um aluno, N1 e N2, e os respectivos pesos, P1 e P2. O
programa deve calcular a média ponderada alcançada por aluno
e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou
igual a sete;
• A mensagem "Reprovado", se a média for menor do que
sete;
• A mensagem "Aprovado com Distinção", se a média for igual
a dez.

'''

nota01 = int(input('Digite a primeira nota: '))
peso01 = int(input('Digite o peso da nota: '))

nota02 = int(input('Digite a segunda nota: '))
peso02 = int(input('Digite o peso da nota: '))

media = (nota01 + nota02) / (peso01 + peso02)

if(media >= 7 ):
    if(media == 10):
        print(f"Aluno foi Aprovado com Distinção media {media:.2f}")

    else:
        print(f"Aluno foi Aprovado media {media:.2f}")

else: 
    print(f"Aluno foi Reprovado media {media:.2f}")