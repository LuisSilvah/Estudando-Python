# Foram anotadas as idades e alturas de 30 alunos. Faça um
# Programa que determine quantos alunos com mais de 13
# anos possuem altura inferior à média de altura desses
# alunos

alunos = [[17, 2], [15, 2], [13, 1.8]]

mediaAltura = 0
qtdAlunos = 0

alunosAbaixoMedia = 0

for aluno in alunos:
    if(aluno[0] > 13):
        qtdAlunos += 1
        mediaAltura += aluno[1]
        
        if (aluno[1] < mediaAltura/qtdAlunos):
            alunosAbaixoMedia += 1
        
        

print(alunos, mediaAltura/qtdAlunos, alunosAbaixoMedia)