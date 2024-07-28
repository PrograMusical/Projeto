# set == colecao de dados sem ordem, portanto sem index, e sem valores repetidos

utensiles = {'fork' , 'spoon' , 'knife' , 'knife','a'} 

dishes = {'a' , 'b' , 'c'}

# utensiles.add('napkin')
# utensiles.remove('fork')
# utensiles.clear()
# utensiles.update(dishes)
# dinner_table = utensiles.union(dishes)

# for x in dinner_table:
#     print(x)

# print(dishes.difference(utensiles))

print(utensiles.intersection(dishes))