# Faça um programa que, dada uma string, diga se ela e um
# palíndromo ou não. Lembrando que um palíndromo e uma
# palavra que tenha a propriedade de poder ser lida tanto da
# direita para a esquerda como da esquerda para a direita.
# • Exemplo:
# • ovo
# • arara
# • Anotaram a data da maratona


palavra = input("Digite a palavra que deseja verificar palíndromo: ")

if(palavra[::-1] in palavra):
    print(f"A palavra '{palavra}' é um palíndromo")
else: 
    print(f"A palavra '{palavra}' não é um palíndromo")
   