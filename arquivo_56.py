#CARDÁPIO DE LANCHONETE
pedido = 1

precoTotal = 0

TotaldeCachorrosQuentes = 0
TotalDeBaurusSimples = 0
TotalDeBaurusComOvos = 0
TotalDeHamburgueres = 0
TotalDeCheeseBurguers = 0
TotalDeRefrigerantes = 0

while(pedido != 0):
    print("MENU DA LANCHONETE:\n")
    print("1 -> Cachorro Quente cód: 100 preço: R$ 1,20.\n")
    print("2 -> Bauru simples cód: 101 preço: R$ 1,30.\n")
    print("3 -> Bauru com ovo cód: 102 preço: R$ 1,50.\n")
    print("4 -> Hambúrguer cód: 103 preço: R$ 1,20.\n")
    print("5 -> Cheeseburguer cód: 104 preço: R$ 1,30.\n")
    print("6 -> Refrigerante cód: 105 preço: R$ 1,00.\n")
    pedido = int(input("Informe o pedido desejado:\n"))

    if(pedido == 1):
        
        print("Ok, o pedido selecionado foi cachorro quente com o valor de R$1,20 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotaldeCachorrosQuentes += n
        print(f"OK,o pedido foi de %d unidade(s) de Cachorro-Quente.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.20
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.20,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    elif(pedido == 2):
        
        print("Ok, o pedido selecionado foi bauru simples com o valor de R$1,30 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotalDeBaurusSimples += n
        print(f"OK,o pedido foi de %d unidade(s) de Bauru Simples.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.30
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.30,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    elif(pedido == 3):
        
        print("Ok, o pedido selecionado foi bauru com o ovo com o valor de R$1,50 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotalDeBaurusComOvos += n
        print(f"OK,o pedido foi de %d unidade(s) de Bauru com ovo.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.50
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.50,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    elif(pedido == 4):
        
        print("Ok, o pedido selecionado foi Hambúrguer com o valor de R$1,20 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotalDeHamburgueres += n
        print(f"OK,o pedido foi de %d unidade(s) de Hambúrguer.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.20
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.20,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    elif(pedido == 5):
        
        print("Ok, o pedido selecionado foi CheeseBurguer com o valor de R$1,30 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotalDeCheeseBurguers += n
        print(f"OK,o pedido foi de %d unidade(s) de CheeseBurguer.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.30
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.30,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    elif(pedido == 6):
        
        print("Ok, o pedido selecionado foi refrigerante com o valor de R$1,00 por unidade\n")
        n = int(input("Selecione a quantidade desejada:\n"))
        TotalDeRefrigerantes += n
        print(f"OK,o pedido foi de %d unidade(s) de refrigerante.\n" % (n))
        if(n < 0):
            print("Valor inválido, execute o programa de novo inválido!\n")
            exit(1)
        preco = n * 1.00
        precoTotal += preco
        print(f"O preço pago por este pedido é de R$%.2f\n" % preco)
        print(f"%.2f * %d = %.2f\n" % (1.00,n,preco))
        print("Deseja fazer um novo pedido ou encerrar a conta:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e emitir a nota de pagamento.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            print("Ok, nota fiscal gerada:\n")
            break
    else:
        print("Opção não encontrada, tente novamente!\n")
        continue

 
if(TotaldeCachorrosQuentes > 1):
    print(f"Cachorros quentes: %.2f * %d = %.2f\n" % (1.20, TotaldeCachorrosQuentes, 1.20 * TotaldeCachorrosQuentes))
if(TotalDeBaurusSimples > 1):
    print(f"Baurus simples: %.2f * %d = %.2f\n" % (1.30, TotalDeBaurusSimples, 1.30 * TotalDeBaurusSimples))
if(TotalDeBaurusComOvos > 1):
    print(f"Baurus com ovos: %.2f * %d = %.2f\n" % (1.50, TotalDeBaurusComOvos, 1.50 * TotalDeBaurusComOvos))
if(TotalDeHamburgueres > 1):
    print(f"Hambúrguers: %.2f * %d = %.2f\n" % (1.20, TotalDeHamburgueres, 1.20 * TotalDeHamburgueres))
if(TotalDeCheeseBurguers > 1):
    print(f"Cheesebúrguers: %.2f * %d = %.2f\n" % (1.30, TotalDeCheeseBurguers, 1.30 * TotalDeCheeseBurguers))
if(TotalDeRefrigerantes > 1):
    print(f"Refrigerantes: %.2f * %d = %.2f\n" % (1.00, TotalDeRefrigerantes, 1.00 * TotalDeRefrigerantes))
                        
print(f"Preço total R$ %.2f\n" % precoTotal)



