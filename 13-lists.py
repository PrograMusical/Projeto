# indices: 0          1            2            3     --> indicam a "posicao" daquele valor dentro da lista
food = ["pizza" , "cookie" , "hamburguer" , "hotdog"] 
# print(food[0]) # acessando o item de indice 0

# food[0] = "sushi" # subsituindo o valor da posicao 0
# print(food[0])

# iterando os itens de uma lista
# for i in food:
#     print(i)


# algumas funcoes
# adiciona um novo item
food.append("ice cream")
print(food)

# remove um item da lista
food.remove("ice cream")
print(food)

# remove o ultimo item da lista
food.pop()
print(food)

# adiciona um novo item com um indice especifico
food.insert(0 , "coco")
print(food) 

# organiza a lista 
food.sort()
print(food)

# deleta todos os itens
food.clear()

print(food)
