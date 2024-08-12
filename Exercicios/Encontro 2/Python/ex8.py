# Código base
import math

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"A hipotenusa do triângulo é: {hipotenusa:.2f}")
