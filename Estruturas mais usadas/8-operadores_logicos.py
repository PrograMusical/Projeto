# sao palavras-chave usadas em testes logicos (declaracoes IF) 
# que permitem testes mais completos e complexos:
#               and : o teste so sera verdadeiro se as DUAS condicoes forem VERDADEIRAS
#               or : o teste so sera verdadeiro se UMA das condicoes for VERDADEIRA
#               not : o teste sera VERDADEIRO se UMA/DUAS condicao(oes) for(em) FALSA(S)

temperatura = int(input("quantos graus? "))

if not (temperatura >= 0 and temperatura <= 30):
    print("a temperatura está mt ruim")

elif not (temperatura < 0 or temperatura > 30):
    print("a temperatura está agradável")

