# Seja a seguinte definição de uma estrutura de dados
# representando um livro:
# • código do livro: número inteiro
# • título: string
# • número de autores: número inteiro
# de acordo com o número de autores – nomes dos
# autores: string
# • preço: número reais

# Você irá trabalhar com dicionários e listas
# Crie um dicionário de livros, onde o código do livro é a chave e
# este dicionário, para cada chave é constituído de uma lista com
# as outras informações (Veja os exemplos acima)
# Na construção do programa use o tratamento de exceções
# Após a leitura dos dados, realizara as seguintes tarefas
# • Buscar um livro pelo título, imprimir todas as suas informações
# se ele existir
# • Buscar um livro pelo código, imprimir todas as suas
# informações se ele existir
# • imprimir os dados dos livros com preço superior a R$50.00.
# Apresente os dados no formato de uma tabela

biblioteca = [
    {'codigo': 1, 'titulo': 'livro01', 'qtdAutores': 2, 'autores': ['Luis', 'Gustavo'], 'preco': 29.00},
    {'codigo': 2, 'titulo': 'livro02', 'qtdAutores': 1, 'autores': ['Luis Silvah'], 'preco': 20.00}
]

opcao = int(input("Digite uma opção do menu: "))

print("""
      1. Buscar 
      """)

for livro in biblioteca:
    # if(livro['codigo'] == 1):
    #     print(livro)
    
    if(livro['titulo'] == 'livro02'):
        print(livro)

