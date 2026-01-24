#EXIBINDO A SOMA DE TODOS OS NÚMEROS MÚLTIPLOS DE 3 DE 1 ATÉ 1000000

total = 0

for contagem in range(1000000):
    contagem = contagem + 1
    if(contagem % 3 == 0):
        continue
    total = total + contagem
print(total)



