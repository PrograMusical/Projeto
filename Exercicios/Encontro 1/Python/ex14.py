# Código base
vetor1 = [float(input(f"Digite o elemento {i+1} do primeiro vetor: ")) for i in range(3)]
vetor2 = [float(input(f"Digite o elemento {i+1} do segundo vetor: ")) for i in range(3)]

produto_escalar = sum(vetor1[i] * vetor2[i] for i in range(3))

print(f"O produto escalar dos vetores é: {produto_escalar}")
