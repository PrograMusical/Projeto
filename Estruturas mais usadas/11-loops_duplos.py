# loops duplos ou nested loops == são conjuntos de dois ou mais tipos de loops
#                                 executados dentro de outros loops
#                                 onde por exemplo: uma repeticao do loop principal sera 
#                                 uma iteracao completa do loop secundario
#                                 (a funcao do loop principal é repetir o loop secundario)

# formar um retangulo com loops internos for
linhas = int(input("quantas linhas voce quer? "))
colunas = int(input("quantas colunas voce quer? "))
simbolo = input("qual simbolo voce quer? ")

for i in range(linhas):
    for j in range(colunas):
        print(simbolo , end="")
    print()
