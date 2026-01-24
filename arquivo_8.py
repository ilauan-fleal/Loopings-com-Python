#Validando entrada de dados!

nota = float(input("Insira uma nota entre 0 e 10:\n"))

while(nota < 0 or nota > 10):
    print("Insira um valor válido!\n")
    nota = float(input())