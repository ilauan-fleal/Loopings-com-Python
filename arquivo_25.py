
numbers = []
total = 0
soma = 0
media = 0


for n in range(5):
    print(f"Digite o valor -> %d.\n" % (n + 1))
    x = float(input())
    numbers.append(x)
    total += 1



for r in numbers:
    soma += r
    media += r/total

print(f"A soma dos números é de %d\n" % soma)
print(f"A média dos números é de %.2f\n" % media)
