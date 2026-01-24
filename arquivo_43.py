#IMPLEMENTANDO CAIXA MAIS RUDIMENTAR!
#MONTANDO TABELA DE PREÇOS


continuar = 1





contagem = 0

contagem2 = 0

while(continuar != 0):
    
    total = int(input("Digite a quantidade total de itens, que irá comprar:\n"))
    if(total <= 0):
        print("Erro há que escolher no mínimo 1 item, execute o programa novamente.\n")
        exit(1)
    while(contagem < total):
        contagem += 1
        print(f"Insira o preço do item: %d" % contagem)
        preco = float(input())
    while(contagem2 < total):
        contagem2 += 1
        print(f"%d - %.2f" % (contagem2, preco * contagem2))
    print("Tabela exibida:\n")
    print("Deseja continuar, ou é possível encerrar o programa?\n")
    print("1 -> Continuar.\n")
    print("0 -> Encerrar o programa.\n")
    continuar = int(input())
    if(continuar != 1 and continuar != 0):
        print("Dado inválido, programa encerrado.\n")
        exit(1)
    elif(continuar == 0):
        print("Programa encerrado!\n")
        exit(1)
    







