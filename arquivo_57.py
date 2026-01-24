
#CARDÁPIO DE LANCHONETE
opcao = 1

precoTotal = 0

TotaldeVotosCandidatoA = 0
TotaldeVotosCandidatoB = 0
TotaldeVotosCandidatoC = 0
TotaldeVotosCandidatoD = 0
TotaldeVotosBrancos = 0
TotaldeVotosNulos = 0

while(opcao != 0):
    print("OPÇÕES:\n")
    print("1 -> Voto no candidato A.\n")
    print("2 -> Voto no candidato B.\n")
    print("3 -> Voto no candidato C.\n")
    print("4 -> Voto no candidato D.\n")
    print("5 -> Voto em branco.\n")
    print("6 -> Voto nulo.\n")
    voto= int(input("Informe o voto desejado:\n"))

    if(voto == 1):
        
        print("Ok, o voto selecionado foi no candidato A.\n")
        TotaldeVotosCandidatoA += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break
    elif(voto == 2):
        
        print("Ok, o voto selecionado foi no candidato B.\n")
        TotaldeVotosCandidatoB += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break    
    elif(voto == 3):
        
        print("Ok, o voto selecionado foi no candidato C.\n")
        TotaldeVotosCandidatoC += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break  
    elif(voto == 4):
        
        print("Ok, o voto selecionado foi no candidato D.\n")
        TotaldeVotosCandidatoC += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break  
    elif(voto == 5):
        
        print("Ok, o voto selecionado foi branco.\n")
        TotaldeVotosBrancos += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break 

    elif(voto == 6):
        
        print("Ok, o voto selecionado foi nulo.\n")
        TotaldeVotosNulos += 1
        print("Deseja encerrar a votação ou continuar a votar?:\n")
        print("1 --> Para continuar\n")
        print("0 --> Para encerrar o programa e calcular os votos realizados.\n")
        escolha = int(input())
        if(escolha != 1 and escolha != 0):
            print("Valor inválido, rode o programa novamente!\n")
            exit(1)
        elif(escolha == 1):
            continue
        else:
            
            break 

print(f"O total de votos do candidato A foi igual a %d\n" % (TotaldeVotosCandidatoA))
print(f"O total de votos do candidato B foi igual a %d\n" % (TotaldeVotosCandidatoB))
print(f"O total de votos do candidato C foi igual a %d\n" % (TotaldeVotosCandidatoC))
print(f"O total de votos do candidato D foi igual a %d\n" % (TotaldeVotosCandidatoD))
print(f"O total de votos em branco foi igual a %d\n" % (TotaldeVotosBrancos))
print(f"O total de votos nulos foi igual a %d\n" % (TotaldeVotosNulos))
TotalDeVotos = TotaldeVotosCandidatoA + TotaldeVotosCandidatoB + TotaldeVotosCandidatoC + TotaldeVotosCandidatoD + TotaldeVotosBrancos + TotaldeVotosNulos
print(f"O total de votos foi igual a %d\n" % TotalDeVotos)
print(f"O percentual de votos brancos sobre o total de votos foi de %.2f por cento\n" % ((TotaldeVotosBrancos/TotalDeVotos) * 100))
print(f"O percentual de votos nulos sobre o total de votos foi de %.2f por cento\n" % ((TotaldeVotosNulos/TotalDeVotos) * 100))