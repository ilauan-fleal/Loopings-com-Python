#PROGRAMA DE PROVA ESCOLAR

from os import system

AlunoComMaiorAcerto = ""
AlunoComMenorAcerto = ""

MaiorAcerto = 0
MediaTurma = 0
TotalDeAlunos = 0

#CRIANDO DICIONÁRIOS VAZIOS!

gabarito = {}
alunos = {}

Nquestoes = int(input("Digite o número total de questões:\n"))
MenorAcerto = Nquestoes

for x in range(1, Nquestoes + 1):
    resposta = input(f"Digite a resposta correta da questão {x}:\n").upper()
    gabarito["questão" + str(x)] = resposta
    system("cls")
while(1):
    #LIMPANDO A TELA == SCREEN CLEANER
    system("cls")
    aluno = input("Digite o nome do aluno ou 0 para sair:\n")
    if(aluno== "0"):
        print("Encerrando...\n")
        break
    TotalDeAlunos += 1
    alunos[aluno] = {"acertos":0}
    for k in range(1 , Nquestoes + 1):
        resposta = input(f"Digite a resposta que o aluno {aluno} deu para questão {k}:\n").upper()
        alunos[aluno]["questão" + str(k)] = resposta
    for aluno, respostas in alunos.items():
        for questao, resposta in respostas.items():
            if questao == "acertos":
                continue
            if resposta == gabarito[questao]:
                alunos[aluno]["acertos"] += 1
        acertos = alunos[aluno]["acertos"]
        nota = 10 * (acertos / Nquestoes)
        print(f"O aluno {aluno} obteve {acertos} dentre {Nquestoes}.\n")
        print(f"O aluno ficou com a nota {nota:.2f}.\n")
        if acertos > MaiorAcerto:
            MaiorAcerto = acertos
            AlunoComMaiorAcerto = aluno
        if acertos < MenorAcerto:
            MenorAcerto = acertos
            AlunoComMenorAcerto = aluno
        MediaTurma += nota
        MediaTurma = MediaTurma/TotalDeAlunos


print(f"O aluno com maior quantidade de acertos é {AlunoComMaiorAcerto} com {MaiorAcerto}.\n")
print(f"O aluno com menor quantidade de acertos é {AlunoComMenorAcerto} com {MenorAcerto}.\n")
print(f"A média da turma calculada é igual a %.2f\n" % MediaTurma)