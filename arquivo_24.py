from math import inf

numbers = []

for z in range(5):
    x = float(input(f"Digite o valor %d:\n" % (z + 1)))
    numbers.append(x)

Maior = -inf

for k in numbers:
    if(k > Maior):
        Maior = k

print(f"O valor maior é: %d\n" % Maior)

