from math import inf

num = []
soma = 0
print("Escolha qual é o total de temperaturas que deseja digitar:\n")

qtde = int(input())


for a in range(qtde):
    n = float(input(f"Digite a temperatura(em Celsius) %d:\n" % (a + 1)))
    

    soma += n
    num.append(n)

Maior = -inf

for h in num:
    if(h > Maior):
        Maior = h



Menor = inf

for d in num:
    if(d < Menor):
        Menor = d

media = soma/qtde

print(f"A menor temperatura é igual a %d\n" % Menor)
print(f"A maior temperatura é igual a %d\n" % Maior)
print(f"A média das temperaturas obtidas é igual a %.2f\n" % media)
