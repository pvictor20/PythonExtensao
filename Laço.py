

#print("Digite -1 a qualquer momento para sair")
#ligado = True

#while ligado:
#    idade = int(input("Digite uma idade"))
#    if idade == -1:
#        ligado = False
#   else:
#        print(Idade = {}.format(idade))

        # i = 6

#while i <=6:
#    print(i)
#   i += 1 



#while True:
#    print("Ajuda, estou preso... i = {}".format(i))

#    if i == 6:
#        break

soma_das_idades = 0
contar_as_idades = 0
print("Digite -1 a qualquer momento para sair.")

while True:
    idade = int(input("Digite uma idade: "))
    if idade == -1:
        break
    soma_das_idades += idade
    contar_as_idades += 1
    print(f"Soma = {soma_das_idades}")
    print((f"Contador = {contar_as_idades}"))

    if contar_as_idades == 0:
        print("Não tem média")
    else:
        print(f"Média {soma_das_idades/contar_as_idades}")