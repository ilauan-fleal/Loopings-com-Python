#CRIANDO UM PROGRAMA , QUE RECEBE DOIS NÚMEROS INTEIROS E RETORNA OS NÚMEROS
#QUE ESTÃO NO INTERVALO COMPREENDIDOS ENTRE ELES

x = int(input("Digite o primeiro inteiro:\n"))

y = int(input("Digite o segundo inteiro:\n"))

while(x > y):
    print("Erro, o primeiro valor deve ser menor do que o segundo!\n")
    x = int(input("Digite o primeiro inteiro:\n"))
    y = int(input("Digite o segundo inteiro:\n")) 

soma = 0

for z in range(x + 1, y):
    print(f'-%d-' % z, end='')
    soma += z

print(f"\nA soma de todos os valores é igual a %d\n" % soma)
