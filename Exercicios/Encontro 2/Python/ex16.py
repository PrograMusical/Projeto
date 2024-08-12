# Código base
matriz1 = [[float(input(f"Digite o elemento [{i+1},{j+1}] da primeira matriz: ")) for j in range(3)] for i in range(3)]
matriz2 = [[float(input(f"Digite o elemento [{i+1},{j+1}] da segunda matriz: ")) for j in range(3)] for i in range(3)]

matriz_soma = [[matriz1[i][j] + matriz2[i][j] for j in range(3)] for i in range(3)]

print("A matriz soma é:")
for linha in matriz_soma:
    print(linha)
