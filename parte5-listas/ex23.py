# Exercício 23 - Python
# Usando a mesma lista, encontre e exiba o maior valor.

lista = [5, 12, 8, 20, 3, 15]

maior = lista[0]
for item in lista:
    if item > maior:
        maior = item
print(f"O maior valor é: {maior}")
