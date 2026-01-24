
#PROGRAMA DE PESQUISA ELEITORAL

VotosCandidatoA = 0

VotosCandidatoB = 0

VotosCandidatoC = 0

print("Bem-vindo ao simulador de eleições:\n")

print("Existem três opções para votar:\n")

continuar = 1
escolha = 0

while(continuar != 0):
    
    print("Candidato A --> Tecla 1\n")
    print("Candidato B --> Tecla 2\n")
    print("Candidato C --> Tecla 3\n")

    
    escolha = int(input())
    if(escolha == 1):
        VotosCandidatoA += 1
        print(f"Dado registrado, candidato A tem %d votos.\n" % VotosCandidatoA)
        print("Deseja continuar a votação(1 para sim e 0 para não)?\n")
        continuar = int(input())
  
    elif(escolha == 2):
        VotosCandidatoB += 1
        print(f"Dado registrado, candidato B tem %d votos.\n" % VotosCandidatoB)
        print("Deseja continuar a votação(1 para sim e 0 para não)?\n")
        continuar = int(input())
    elif(escolha == 3):
        VotosCandidatoC += 1
        print(f"Dado registrado, candidato C tem %d votos.\n" % VotosCandidatoC)
        print("Deseja continuar a votação(1 para sim e 0 para não)?\n")
        continuar = int(input())
    else:
        print("Candidato não encontrado!\n")
        print("Deseja continuar a votação(1 para sim e 0 para não)?\n")
        continuar = int(input())


print(f"Total de votos: Candidato A %d votos\n" % VotosCandidatoA)
print(f"Total de votos: Candidato B %d votos\n" % VotosCandidatoB)
print(f"Total de votos: Candidato C %d votos\n" % VotosCandidatoC)
