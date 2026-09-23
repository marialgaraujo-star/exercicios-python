# Exercício 15 - Python
# Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos foram digitados.

count = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    if num > 0:
        count += 1
print(f"Quantidade de números positivos digitados: {count}")