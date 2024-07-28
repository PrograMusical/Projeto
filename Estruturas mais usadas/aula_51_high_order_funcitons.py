# high order functions === uma funcao que tambem
#                      1. aceita a funcao como um argumento
#                                       or 
#                      2. retorna uma funcao
#                      (em python, funcao tb sao tratados como objetos)
#                       
#                       obs == é praticamente o ato da gente utilizar funcoes
#                       dentro de outras funcoes
#                       
#                       funcoes de alta ordem sao funcoes que aceitam outras funcoes

# part i
# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func('hello')
#     print(text)

# hello(loud)    
# hello(quiet)

#part ii
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

