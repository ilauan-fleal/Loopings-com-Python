
ListaDeAtletas = []

while(1):
    Nome = input("Nome do atleta (ou 0 para encerrar.)\n")
    if Nome == "0":
        break
    #DICIONÁRIO CRIADO
    atleta = {
        "Nome": Nome,
        "Saltos": [],
        "Média": 0,
        "Melhor_salto": 0,
        "Pior_salto":0,

    }
    for i in range(5):
        atleta.get("Saltos").append(float(input(f"Distância do salto {i + 1}:\n")))
    atleta.get("Saltos").sort()
    atleta["Pior_salto"] = atleta.get("Saltos").pop(0)
    atleta["Melhor_salto"] = atleta.get("Saltos").pop()
    atleta["Média"] = sum(atleta.get("Saltos")) / 3
    print(f"\nMelhor salto: {atleta.get("Melhor_salto"):.1f} m\n")
    print(f"\nPior salto: {atleta.get("Pior_salto"):.1f} m\n")
    print(f"\nMédia dos demais saltos: {atleta.get("Média"):.1f} m\n")
    ListaDeAtletas.append(atleta)
print("\nResultado final:\n")
for atleta in ListaDeAtletas:
    print(f"{atleta.get("Nome")}:{atleta.get("Média"):.1f}m\n")
