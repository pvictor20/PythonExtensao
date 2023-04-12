#for c in range (1, 10,1 ):
#    print(c)
#

fatorial = 1
try:
    num = int(input("Digite um número: "))

    for contador in range(num, 1, -1):
        fatorial *= contador
    print(f'{num}! = {fatorial}')

except:
    print("Entrada inválida")


lista = [1, 2, 3, 4]

print(lista[0])