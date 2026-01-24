#CALCULANDO O CUSTO MÉDIO POR CD - RW

continuar = 1
contagem = 0
somaCusto = 0
while(continuar != 0):
    print("Olá, digite a quantidade total de CD's RW's comprados:\n")
    TotalDeCds = int(input())
    while(contagem < TotalDeCds):
        print(f"Digite o custo do CD %d:" % (contagem + 1))
        custoCd = float(input())
        somaCusto += custoCd
        contagem += 1
    mediaCusto = somaCusto/contagem
    print(f"O custo total de CD's é igual a R$%.2f\n" % somaCusto)
    print(f"A média de preço por CD é igual a R$%.2f\n" % mediaCusto)
    print("Deseja continuar, ou é possível encerrá-lo?\n")
    print("1 -> Sim.\n")
    print("0 -> Não.\n")
    continuar = int(input())
    if(continuar != 1 and continuar != 0):
        print("Valor inválido, programa encerrado.\n")
        exit(1)

    elif(continuar == 0):
        print("Ok, programa encerrado, até breve.\n")
        exit(1)

