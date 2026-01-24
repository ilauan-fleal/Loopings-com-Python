CodigoMaisAlto = 0

CodigoMaisBaixo = 0

AlturaMaisAlto = 0

AlturaMaisBaixo = 500


TotalDeAlunos = 0

#LENDO DOIS CONJUNTOS DE 10 VALORES CADA UM

while(TotalDeAlunos <= 10):
    print("Digite o código do aluno(0 para sair):\n")
    codigo = input()
    if(codigo == '0'):
        break
    TotalDeAlunos += 1
    altura = float(input("Digite a altura(em cm):\n"))
    altura = altura/100
    

    if altura > AlturaMaisAlto:
        AlturaMaisAlto = altura
        CodigoMaisAlto = codigo
    if altura < AlturaMaisBaixo:
        AlturaMaisBaixo = altura
        CodigoMaisBaixo = codigo
    



#EXIBINDO INFORMAÇÕES

print(f"O aluno mais alto tem altura  de {AlturaMaisAlto} m   e seu código é {CodigoMaisAlto}.\n")
print(f"O aluno mais baixo tem altura de {AlturaMaisBaixo} m  e seu código é {CodigoMaisBaixo}.\n")


