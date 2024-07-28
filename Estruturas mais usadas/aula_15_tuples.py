# tuplas == colecao de dados ordenados e imutavel
#           usada para agrupar dados relacionados

student = ('bro' , 21 , 'male') # para criar uma tupla usamdos ()

print(student.count('bro'))
print(student.index('male'))

for x in student:
    print(x)

if 'bro' in student:
    print('bro esta aqui')

