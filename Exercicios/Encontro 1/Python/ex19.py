# Código base
n = int(input("Digite o número de termos para a série de Leibniz: "))

pi_aproximado = sum((-1)**k / (2*k + 1) for k in range(n)) * 4

print(f"O valor aproximado de π com {n} termos é: {pi_aproximado:.15f}")
