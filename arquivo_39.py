#ESSE PROGRAMA, EM PYTHON, DEVERÁ CALCULAR A QUANTIDADE MÉDIA DE ALUNOS POR TURMA.

continuar = 1

TotalTurmas = 0

contagem = 0

soma = 0

while(continuar != 0):
    print("Digite a quantidade total de turmas:\n")
    TotalTurmas = int(input())
    while(contagem < TotalTurmas):
        contagem += 1
        print(f"Digite o total de alunos(no máx. 40) da turma %d:\n" % (contagem))
        totalDeAlunos = int(input())
        if(totalDeAlunos > 40):
            print("Erro, são no máximo 40 alunos por turma.\n")
        soma += totalDeAlunos
    AlunosPorTurma = soma/TotalTurmas
    print(f"O total de alunos por turma é igual a %d" % AlunosPorTurma)
    print("Deseja continuar e fazer outro cálculo?\n")
    continuar = int(input())
    if(continuar == 0):
        exit(1)
   

    
