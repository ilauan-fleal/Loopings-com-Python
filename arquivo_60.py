
#CRIANDO PROGRAMA SIMILAR AO ANTERIOR

ListaDeAtletas = []

while(1):
    Nome = input("Insira o nome do atleta de ginástica(ou 0 para sair):\n")
    if Nome == "0":
        break

    atleta = {
        "Nome": Nome,
        "Notas":[],
        "Média": 0,
        "Melhor_nota":0,
        "Pior_nota": 0,
    }
    for z in range(7):
        atleta.get("Notas").append(float(input("Nota: ")))
    atleta.get("Notas").sort()
    atleta["Melhor_nota"] = atleta.get("Notas").pop()
    atleta["Pior_nota"] = atleta.get("Notas").pop(0)
    media = sum(atleta.get("Notas"))
    media = media / (7-2)
    atleta["Média"] = media
    ListaDeAtletas.append(atleta)

print("\nResultado final:\n")
for atleta in ListaDeAtletas:
    print(f"Atleta: {atleta.get("Nome")}\n")
    print(f"Melhor nota: {atleta.get("Melhor_nota")}\n")
    print(f"Pior nota: {atleta.get("Pior_nota")}\n")
    print(f"Média: {atleta.get("Média"):.2f} ")
    



    