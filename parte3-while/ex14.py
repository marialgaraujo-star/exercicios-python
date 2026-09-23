# Exercício 14 - Python
# Peça um número e exiba sua tabuada de 1 a 10.

num = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    