# Exercício 03 - Python
# Peça o raio de um círculo e calcule a área. Use 3,14159 como valor de pi.

import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo é: {area:.2f}")
