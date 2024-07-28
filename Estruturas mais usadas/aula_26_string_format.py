# srt.format == da mais controle ao mostrar coisas no output

# animal = 'cow'
# item = 'moon'

# string = 'the {a} jumped {i}'

# # print('the ' + animal + ' jumped ' + item)
# print('the {} jumped {}'.format(animal,item)) # oq sera printada eguria nessa ordem dos args
# print('the {1} jumped {1}'.format(animal,item)) # positional argument
# print(string.format(a=animal,i=item)) # kwargs

name = 'bro'

print('hello my name is {}'.format(name))
print('hello my name is {:10} opa'.format(name))
print('hello my name is {n:>10} opa'.format(n=name))

import math
number = 1000 #math.pi

print('o numero de pi é {:.2f}'.format(number))
print('o numero de pi é {:,}'.format(number))
print('o numero de pi é {:b}'.format(number))
print('o numero de pi é {:o}'.format(number))
print('o numero de pi é {:X}'.format(number))
print('o numero de pi é {:E}'.format(number))