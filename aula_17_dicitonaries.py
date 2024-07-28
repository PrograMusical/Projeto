# dicionario == colecao de dados mutavel, sem ordem, com uma chave unica
#               

capitals = {
    'usa' : 'whashington',
    'india' : 'new dhli',
}
capitals.update({'germany' : 'berlin'})
capitals.update({'usa' : 'brasilia'})
capitals.pop('usa')
capitals.clear()
# print(capitals['usa'])
# print(capitals.get('ger')) # uma forma de ver se essa chave existe
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for x,y in capitals.items():
    print(x , y)