#MONTANDO TABUADA EM VALORES PRÉ-DEFINIDOS

v = int(input("Escreva o valor, cuja tabuada, você gostaria de exibir:\n"))

x = int(input("Escreva um número inteiro, que irá iniciar a tabuada.\n"))

y = int(input("Escreva o inteiro, no qual a tabuada, deverá terminar.\n"))

for z in range(x, y + 1):
    print(f"%d * %d = %d" % (v , z, v * z))



