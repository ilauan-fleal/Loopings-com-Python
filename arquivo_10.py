#VALIDANDO NOVAS INFORMAÇÕES!

nome = input("Insira o seu nome (maior do que 3 caracteres):\n")

while(len(nome) <= 3):
    print("Dado inválido!\n")
    nome = input("Insira o seu nome (maior do que 3 caracteres):\n")
idade = int(input("Insira a sua idade(entre 0 e 120):\n"))

while(idade < 0 or idade > 150):
    print("Dado inválido!\n")
    idade = int(input("Insira a sua idade(entre 0 e 150):\n"))


salario = float(input("Agora insira seu salário:\n"))

while(salario < 0):
    print("Valor inválido!\n")
    salario = float(input("Agora insira seu salário:\n"))



sexo = input("Escolha uma opção (m) -> masculino ou (f) -> feminino.\n")

while(sexo.upper() != 'M' and sexo.upper() != 'F'):
    print("Dado inválido!\n")
    sexo = input("Escolha uma opção (m) -> masculino ou (f) -> feminino.\n")


estadoCivil = input("Escolha uma opção (s) -> solteiro, (c) -> casado , (v) -> viúvo , (d) -> divorciado.\n")
while(estadoCivil.upper() != 'S' and estadoCivil.upper() != 'C' and estadoCivil.upper() != 'V' and estadoCivil.upper() != 'D'):
    print("Dado inválido!\n")
    estadoCivil = input("Escolha uma opção (s) -> solteiro, (c) -> casado , (v) -> viúvo , (d) -> divorciado.\n")


    