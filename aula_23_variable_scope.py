# scope == a regiao onde a variavel é reconhecida
#          L == local
#          E == Enclosing
#          G == Global
#          B == Built-in

name = 'code' # variavel global

def nome():
    name='bro' # variavel local
    print(name)

nome() # a funcao primeiro utiliza da variavel local
print(name)