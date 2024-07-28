# **kwargs == parametro q agrupa todos os argumentos em um dicionario
#             util para funcoes que usam varias variables
# kwargs == keywords arguments

def hello(**nome):
    # print(f'hello {nome['first']} {nome['last']}')
    print('hello' , end=' ')
    for key,value in nome.items():
        print(value , end=' ')

hello(title = 'mr.' , first='bro' , last='code' , mid='dude')