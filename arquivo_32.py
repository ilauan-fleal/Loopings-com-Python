from math import inf

num = []
soma = 0
print("Escolha qual é o total de números que deseja digitar:\n")

qtde = int(input())


for a in range(qtde):
    n = float(input(f"Digite o valor %d:\n" % (a + 1)))
    if(n < 0 or n > 1000):
        print("O valor digitado está fora do intervalo:\n")
        exit(1)

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


print(f"A soma de todos os números digitados é igual a %d\n" % soma)
print(f"O menor valor é igual a %d\n" % Menor)
print(f"O maior valor é igual a %d\n" % Maior)