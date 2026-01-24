
idade = 0

contagem = 0  #IRÁ REPRESENTAR O TOTAL DE PESSOAS, NA PESQUISA

soma = 0

continuar = 1

while(continuar != 0):
    print(f"Digite a idade da pessoa(entre 0 e 100 anos) %d: " % (contagem + 1))
    idade = int(input())
    if(idade < 0 or idade > 100):
        print("Erro digite, uma idade que seja entre 0 e 100 anos.\n")
        print("Para isso, execute o programa novamente.\n")
        exit(1)
    print("Ok, valor registrado, deseja continuar?(0 para sair ou 1 para continuar)\n")
    contagem += 1
    soma += idade
    continuar = int(input())
    if(continuar != 0 and continuar != 1):
        print("Valor inválido, execute o programa novamente!\n")
        exit(1)
    
   
    

media = soma/contagem

print(f"A média das idades calculadas é igual a %.2f\n" % media)

if(media > 0 and media < 25):
    print("A turma é jovem.\n")
elif(media > 26 and media < 60):
    print("A turma é adulta.\n")
else:
    print("A turma analisada é idosa.\n")



