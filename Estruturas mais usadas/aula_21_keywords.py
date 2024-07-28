# keywords == argumentos precedidos por um identificador, dessa forma a 
#             ordem dos argumentos nao importa, diferentemente dos
#             argumentos posicionais. Nesse caso o python sabe o nome dos
#             argumentos que a funcao recebe

def hello(first,mid,last):
    print(first+mid+last)

hello(mid='dude',last='code',first='bro')