# list comprehension == uma forma de criar a new list com menos sintaxe
#                       pode imitar certas funcoes lambda, facil de ler
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression (if/else) for item in iterable]

# square = []                 # cria uma lista vazia
# for i in range(1,11):       # cria um loop for
#     square.append(i * i)    # define oq cada loop deve fazer
# print(square)

# squares = [i * i for i in range(1,11)]
# print(squares)

students = [100,90,80,70,60,50,40,30,0]

# passed_students = list(filter(lambda x : x >= 60 , students))

# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "failed" for i in students]

print(passed_students)