# matriz ou lista 2D == é uma variável de variáveis, possuindo a mesma logica de uma lista comum

# listas comuns
bebidas = ["cafe" , "refri", "cha"]
lanche = ["pizza" , "hamburguer" , "cachorro-quente"]
sobremesa = ["bolo" , "sorvete"]

# matriz
#          0        1        2
comida = [bebidas, lanche, sobremesa]
# de forma extensa:
# comida = [
#      0          1      2
# 0 ["cafe" , "refri", "cha"],
#      0            1                  2
# 1 ["pizza" , "hamburguer" , "cachorro-quente"],
#      0          1
# 2 ["bolo" , "sorvete"]
#]


print(comida[0][0]) # saida => cafe
print(comida[2][0]) # saida => bolo
