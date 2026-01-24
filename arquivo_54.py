#CALCULADORA DE DÍVIDAS

x = float(input("Digite o valor total de sua dívida?\n"))


Nparcelas = 1

ValorDosJuros = 0

print("\n|Valor da dívida|Valor dos juros|Quantidade total de parcelas|Valor da parcela|\n")

while(1):
    ValorDosJuros = (5/3) * Nparcelas + 5
    if Nparcelas == 1:
        ValorDosJuros = 0
    ValorDosJuros = x * (ValorDosJuros/100)
    ValorTotal = x + ValorDosJuros
    ValorParcela = ValorTotal/Nparcelas
    print(f"Valor total em R$%.2f\n" % ValorTotal)
    print(f"Valor dos juros %.2f\n" % ValorDosJuros)
    print(f"Parcela: %d\n" % Nparcelas)
    print(f"Valor de cada parcela: %.2f\n" % ValorParcela)

    if Nparcelas == 1:
        Nparcelas -= 1
    Nparcelas += 3
    if Nparcelas > 12:
        break

