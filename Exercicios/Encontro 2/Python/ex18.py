# Código base
x0 = float(input("Digite o valor de x0: "))
y0 = float(input("Digite o valor de y0: "))
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x = float(input("Digite o valor de x para interpolação: "))

y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)

print(f"O valor interpolado de y para x={x} é: {y:.2f}")
