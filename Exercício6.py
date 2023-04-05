##Programa que receba 2 valores e devolve o maior entre eles.

num_1 =(input("1° número: "))
num_2 = input("2° número: ")

if (num_1.isdecimal() and num_2.isdecimal()):
    if num_1 > num_2:
        print(f'{num_1} é maior do que o {num_2}')
    elif num_1 == num_2:
        print("São iguais")
    else:
        print(f'{num_2} é maior do que o {num_1}')

else:
    print("Erro")



 
