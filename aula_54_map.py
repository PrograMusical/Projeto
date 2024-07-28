# map() == aplica uma funcao para cada item em uma colecao de itens (iteraveis)
#
# map(function,iterable)

# __-____---exemplo_-____-___-_-______ 
# func = lambda num : num + 1
# num = [1,2,3,4,5,6]

# num2 = map(func,num)

# for i in num2:
#     print(i)
# __-____---_-____-___-_-______

store = [
    ('shirt',20),
    ('pants',25),
    ('jacket',50),
    ('socks',10)
]

to_euros = lambda data : (data[0],data[1]*0.82)
to_dollars = lambda data : (data[0],float('{:.1f}'.format(data[1]/0.82)))

store_dollar = list(map(to_dollars,store))
store_euro = list(map(to_euros,store))

for i in store_euro:
    print(i)

for i in store_dollar:
    print(i)