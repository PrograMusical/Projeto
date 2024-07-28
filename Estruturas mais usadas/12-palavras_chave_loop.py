# BREAK --> encerra a iteração
# while True:
#     nome = input("qual é o seu nome? ")
#     if not name == "":
#         break

# CONTINUE --> indica para o loop que ele dece apenas continuar e partir para o proximo item da repeticao
# fone = "1234-1234"

# for i in fone:
#     if i == "-":
#         continue
#     print(i , end="")

#  PASS --> tem valor semantico... nao possui funcao especifica, indica para o programador que algo deve ser feito ali mais tarde
for i in range(1 , 20):
    if i == 13:
        pass
    else:
        print(i)
