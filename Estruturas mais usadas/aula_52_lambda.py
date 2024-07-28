# lambda == funcao escrita em 1 linha usando a palavra-chave LAMBDA
#           aceita qualquer numero de argumentos, mas somente tem uma expresao
#           (pense nisso como uma abrevicao)
#           (util se necessario de um curto periodo de tempo, temporaria)

# lambda parameters:expression ( essa expressao tem um return 'automatico')

# def double(x):
#     return x * 2

# print(double(5))

double = lambda x : x * 2
multiply = lambda x , y : x * y
add = lambda x , y , z : x + y + z
full_name = lambda first_name , last_name : first_name + ' ' + last_name
age_check = lambda age : True if age >= 18 else False
def math(func,*args):
    return func(*args)

# print(math(double,5))
# print(math(multiply,5,6))
# print(math(add,5,6,7))
# print(full_name('renato','piber'))
print(age_check(18))