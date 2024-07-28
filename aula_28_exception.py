try:
    numerator = int(input('me de um num '))
    deno = int(input('opa dnv '))
    resu = numerator/deno
    
except ZeroDivisionError as e:
    print(e)
    print('tu tacou um deno 0')
except ValueError as e:
    print(e)
    print('so taca num pls')
except Exception as e:
    print(e)
    print('voce tem algo errado')

else:
    print(resu)
finally:
    print('isto nunca vai para de rodar')