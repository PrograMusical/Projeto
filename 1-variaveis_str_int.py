# COMO MOSTRAR NUM E STR JUNTOS???
# print('ola' + 1) # -----> isso nao funcionaria pois estamos usando
# uma concatenacao de strings em numeros, alem de que os tipos de dados sao diferentes

# # há dois modos:
# # 1) Converter o numero para str:
frase = 'ola ' + str(1)
print(frase)

# # 2) Colocar uma virgula (','):
palavra = 'ola'
numero = 1
print(frase , numero)
