# Código base
salario_base = float(input("Digite o salário base: "))
percentual_bonus = float(input("Digite o percentual de bônus: "))

bonus = salario_base * (percentual_bonus / 100)
salario_final = salario_base + bonus

print(f"O salário final é: {salario_final:.2f}")
