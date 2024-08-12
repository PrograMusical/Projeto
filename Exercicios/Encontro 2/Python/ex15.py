# Código base
import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)  # atan2 calcula o arco tangente, retornando o ângulo em radianos

print(f"A coordenada polar é: (r={r:.2f}, θ={theta:.2f} rad)")
