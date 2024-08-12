# Código base
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Derivada de ax^2 + bx + c é 2ax + b
coef_derivada = [2*a, b]

print(f"Os coeficientes da derivada são: {coef_derivada[0]}x + {coef_derivada[1]}")
