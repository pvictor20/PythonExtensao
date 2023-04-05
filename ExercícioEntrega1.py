altura = float(input("informe sua altura: "))
peso = float(input("Informe seu peso: "))
sexo = input('M - Masculino e F - Feminino: ').casefold()

if (sexo == "m"):
    peso_ideal = 72.7 * altura - 50
elif(sexo == 'f'):
    peso_ideal = 62.1 * altura - 44.7
else:
    print("Deu erro, digite novamente.")

diferença = peso - peso_ideal

if diferença > 0:
    print("Você está acima do peso ideal. Bora de acad!")
elif diferença < 0:
    print("Tá indo para acad, boa.")
else:
    print('Parabéns, você conseguiu, está certinho!')