# a funcao INPUT() permite armazenarmos dados informados pelo usuario

nome = input("qual é o seu nome? ") 
# sempre que algo for adicionado no input,
# seu datatype será STR

# para armazenar numeros, é necessario que utilizemos o typecast:
idade = int(input("qual a sua idade? "))
idade += 1

altura = float(input("qual a sua altura? "))

print("ola" + nome )
print("voce tem " + str(idade) + " anos de idade")
print("sua altura é: " + str(altura))
