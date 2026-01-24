
#CALCULANDO MÉDIA DOS ALUNOS DE UMA DETERMINADA TURMA


alunos = int(input("Qual é a quantidade total de alunos da turma?\n"))

mat = int(input("Qual é o total de matérias que eles estudam?\n"))

mediaTurma = 0

for x in range(alunos):
    print("Aluno número -> " , alunos)

    mediaAluno = 0
    for y in range(mat):
        print("Nota da matéria ->", y + 1, end='\n')
        nota = float(input())
        mediaAluno += nota

    mediaAluno = mediaAluno / mat
    print("Média desse aluno:", mediaAluno, "\n")
    mediaTurma += mediaAluno

mediaTurma = mediaTurma/alunos
print("Média turma:\n", mediaTurma)


