
nota = 0

contagem = 0
soma = 0

continuar = 1

while(continuar != 0):
    print(f"Digite a nota %d: " % (contagem + 1))
    nota = float(input())
    print("Ok, valor registrado, deseja continuar?(0 para sair ou 1 para continuar)\n")
    contagem += 1
    soma += nota
    continuar = int(input())
    if(continuar != 0 and continuar != 1):
        print("Valor inválido, execute o programa novamente!\n")
        exit(1)
    if(nota > 10):
        print("Escolha valores, na faixa de 1 até 10.\n")
        nota = float(input())
   
    

media = soma/contagem

print(f"A média das notas calculadas é igual a %.2f\n" % media)

