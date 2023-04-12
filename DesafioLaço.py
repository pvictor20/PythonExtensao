#Faça um programa que peça verifica se o usuário digitou um número inteiro.
#Caso tenha digitado, mostrar o número na tela.
#Caso não tenha digitado, pedir para o usuário digitar novamente.



while True:
    numero = input("Digite um número inteiro: ")
    if numero.isdigit():
        numero = int(numero) 
        print("Número digitado:", numero) 
        break 
    else:
        print("Número inválido.")


