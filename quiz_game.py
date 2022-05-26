print("Seja bem-vindo ao jogo de quiz!") 

jogar = input("Você gostaria de jogar? ").lower() 

if jogar != "sim":
    quit()

print("Ok, Vamos jogar!!")
pontos = 0

resposta = int(input("Quantas vezes o Brasil foi campeão mundial de futebol? "))
if resposta == 5:
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = int(input("Em que ano foi proclamada a independência do Brasil? "))
if resposta == 1822:
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = input("Quem foi o inventor do avião? ").lower()
if resposta == "santos dumont":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

resposta = input("Qual livro brasileiro mais traduzido no mundo? ").lower()
if resposta == "o alquimista":
    print("Correto!")
    pontos += 1
else:
    print("Incorreto!")

print(f"Você acertou {pontos} de 4 questões, obrigado por jogar.")