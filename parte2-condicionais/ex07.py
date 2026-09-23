# Exercício 07 - Python
# Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior.")
elif num2 > num1:
    print(f"O número {num2} é maior.")
else:
    print("Os números são iguais.")