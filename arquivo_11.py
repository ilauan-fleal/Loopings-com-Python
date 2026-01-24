
PaisA = int(input("Insira a população do país A:\n"))

PaisB = int(input("Insira a população do país B:\n"))

TaxaA = float(input("Informe a taxa de crescimento do país A:\n"))

TaxaB = float(input("Informe a taxa de cescimento do país B:\n"))

TaxaA = TaxaA/100

TaxaB = TaxaB/100

contagem = 0

while(PaisA <= PaisB):
    PaisA = PaisA * TaxaA
    PaisB = PaisB * TaxaB
    contagem += 1

print(f"A população de A ultrapassará ou se igualará a população de B em %d anos.\n" % contagem)