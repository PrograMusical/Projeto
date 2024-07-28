from earsketch import *

setTempo(120)

# variaveis
x = 0
y = 1
drum = PROGRAMUSICAL_WE_WILL_ROCK_YOU_DRUM

for i in range(1, 10):
    # numero 1
    if i == 1:
        fitMedia(drum, 1, i, i+1.5) # aqui termina no 2.5
        
    # numeros pares
    elif (i % 2) == 0:   
        start = i + x + 0.5
        end = start + 1.5
        fitMedia(drum, 1, start, end)
        x += 1
     
    # numeros impares
    else: 
        start = i + y
        end = start + 1.5
        fitMedia(drum, 1, start, end)
        y += 1
    
    # print("i:"+ str(i), "x:"+str(x),"y:"+str(y))
        

    
    

