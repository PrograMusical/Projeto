# if statements == são condicoes que permitem q novos blocos de codigo sejam
#                   executados, alterando assim o fluxo do programa

idade = int(input("qual a sua idade? "))

if idade >= 18:
    print("voce já é um adulto")

elif idade < 0:
    print("você ainda não nasceu")

else:
    print("voce é uma criança")
