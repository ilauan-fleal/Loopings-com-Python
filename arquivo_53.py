cidadeComMaiorIndiceDeAcidentes = 0 

cidadeComMenorIndiceDeAcidentes = 0

NumeroDeVeiculosEmPasseioDaCidadeComMaiorIndice = 0

NumeroDeVeiculosEmPasseioDaCidadeComMenorIndice = 0

TotalDeAcidentesNasCidadesComMenosDeDoisMilVeiculos = 0

MaiorIndiceDeAcidentes = 0

MenorIndiceDeAcidentes = 500

contagem = 0


while(contagem < 5):
    print(f"Digite o nome da cidade %d:(0 para sair)\n" % (contagem + 1))
    cidade = input()
    if(cidade == '0'):
        break
    contagem += 1
    Veiculos = int(input("Digite a quantidade total de veículos em passeio(no ano de 1999):\n"))
    TotalDeAcidentes = int(input("Digite o número total de acidentes de trânsito com vítimas:\n"))
    if Veiculos < 2000:
        TotalDeAcidentesNasCidadesComMenosDeDoisMilVeiculos += TotalDeAcidentes


    if TotalDeAcidentes > MaiorIndiceDeAcidentes:
        MaiorIndiceDeAcidentes = TotalDeAcidentes
        cidadeComMaiorIndiceDeAcidentes = cidade
        NumeroDeVeiculosEmPasseioDaCidadeComMaiorIndice = Veiculos
    if TotalDeAcidentes < MenorIndiceDeAcidentes:
        MenorIndiceDeAcidentes = TotalDeAcidentes
        cidadeComMenorIndiceDeAcidentes = cidade
        NumeroDeVeiculosEmPasseioDaCidadeComMenorIndice = Veiculos

totalDeVeiculos = NumeroDeVeiculosEmPasseioDaCidadeComMaiorIndice + NumeroDeVeiculosEmPasseioDaCidadeComMenorIndice
media = totalDeVeiculos/contagem

Nacidentes = MaiorIndiceDeAcidentes + MenorIndiceDeAcidentes

mediaAcidentes = Nacidentes/contagem

mediaDeAcidentesNasCidadesComMenosDeDoisMilVeiculos = TotalDeAcidentesNasCidadesComMenosDeDoisMilVeiculos/contagem


print(f"O maior índice de acidentes é igual a {MaiorIndiceDeAcidentes} e pertence à cidade {cidadeComMaiorIndiceDeAcidentes}.\n")
print(f"O menor índice de acidentes é igual a {MenorIndiceDeAcidentes} e pertence à cidade {cidadeComMenorIndiceDeAcidentes}.\n")
print(f"A média total de veículos que trafegavam em 1999 nas cinco cidades pesquisadas é igual a %.2f\n" % (media))
print(f"A média total de acidentes nas cidades com menos de 2000 veículos é igual a %.2f\n" % (mediaDeAcidentesNasCidadesComMenosDeDoisMilVeiculos))
