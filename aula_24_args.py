# *args == parametro em forma tupla, useful para uma funcao com varias
#          variaveis

def add(*args): # o nome dps do * é o nome da tupla
    sum = 0
    args = list(args)
    args[0] = 100
    for x in args:
        sum += x
    return sum

print(add(1,2))