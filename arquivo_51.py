
CodigoMaisGordo = 0

CodigoMaisMagro = 0

CodigoMaisAlto = 0

CodigoMaisBaixo = 0

PesoMaisGordo = 0

PesoMaisMagro = 1000

AlturaMaisAlto = 0


AlturaMaisBaixo = 500

SomaDosPesos = 0

SomaDasAlturas = 0

TotalDeClientes = 0

while(1):
    print("Digite o código do cliente(0 para sair):\n")
    codigo = input()
    if(codigo == '0'):
        break
    TotalDeClientes += 1
    altura = float(input("Digite a altura(em cm):\n"))
    altura = altura/100
    peso = float(input("Digite o peso(em kg):\n"))

    SomaDosPesos += peso
    SomaDasAlturas += altura
    if altura > AlturaMaisAlto:
        AlturaMaisAlto = altura
        CodigoMaisAlto = codigo
    if altura < AlturaMaisBaixo:
        AlturaMaisBaixo = altura
        CodigoMaisBaixo = codigo
    if peso > PesoMaisGordo:
        PesoMaisGordo = peso
        CodigoMaisGordo = codigo
    if peso < PesoMaisMagro:
        PesoMaisMagro = peso
        CodigoMaisMagro = codigo
MediaDasAlturas = SomaDasAlturas/TotalDeClientes
MediaDosPesos = SomaDosPesos/TotalDeClientes


#EXIBINDO INFORMAÇÕES

print(f"O cliente mais alto tem altura  de {AlturaMaisAlto} m   e seu código é {CodigoMaisAlto}.\n")
print(f"O cliente mais baixo tem altura de {AlturaMaisBaixo} m  e seu código é {CodigoMaisBaixo}.\n")
print(f"O cliente mais gordo tem peso igual a {PesoMaisGordo} kg e seu código é {CodigoMaisGordo}.\n")
print(f"O cliente mais magro tem peso igual a {PesoMaisMagro} kg e seu código é {CodigoMaisMagro}.\n")
print(f"A média calculada das alturas é igual a {MediaDasAlturas} m.\n")
print(f"A média calculada dos pesos é igual a {MediaDosPesos} kg.\n")
