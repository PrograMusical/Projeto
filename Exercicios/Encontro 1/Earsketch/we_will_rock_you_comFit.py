from earsketch import *

setTempo(120)
# adicionando os sons nas variaveis
parte1 = PROGRAMUSICAL_WE_WILL_ROCK_YOU_PARTE1
parte2 = PROGRAMUSICAL_WE_WILL_ROCK_YOU_PARTE2
parte3 = PROGRAMUSICAL_WE_WILL_ROCK_YOU_PARTE3
parte4 = PROGRAMUSICAL_WE_WILL_ROCK_YOU_PARTE4
parte5 = PROGRAMUSICAL_WE_WILL_ROCK_YOU_PARTE5

# inserindo cada parte no daw 
fitMedia(parte1, 1, 1, 15)
fitMedia(parte2, 1, 15, 30)
fitMedia(parte3, 1, 30, 45)
fitMedia(parte4, 1, 45, 60)
fitMedia(parte5, 1, 60, 65)

