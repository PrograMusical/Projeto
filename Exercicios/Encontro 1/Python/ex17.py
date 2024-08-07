# Código base
matriz1 = [[float(input(f"Digite o elemento [{i+1},{j+1}] da primeira matriz: ")) for j in range(2)] for i in range(2)]
matriz2 = [[float(input(f"Digite o elemento [{i+1},{j+1}] da segunda matriz: ")) for j in range(2)] for i in range(2)]

matriz_produto = [
    [matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0], matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]],
    [matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0], matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]]
]

print("A matriz produto é:")
for linha in matriz_produto:
    print(linha)
