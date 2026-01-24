total = 0

for x1 in range(60):
    for x2 in range(x1 + 1, 60):
        for x3 in range(x2 + 1, 60):
            for x4 in range(x3 + 1, 60):
                for x5 in range(x4 + 1, 60):
                    for x6 in range(x5 + 1, 60):
                        total = total + 1
#IMPRIMINDO TOTAL DE POSSIBILIDADES
print(total)



