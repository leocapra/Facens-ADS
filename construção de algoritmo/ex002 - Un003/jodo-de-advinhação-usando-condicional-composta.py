import random
print("Digite 1 para jogar fácil")
print("Digite 2 para jogar dificil")

opcao = input("Qual o nível desejado? :  ")

if(opcao == "1"):
    sorteio = random.randint(1,5)
    print("Você escolheu o modo de jogo, fácil! Boa sorte!")
    print("Advinhe um numero de 1 a 5.")
elif(opcao == "2"):
    sorteio = random.randint(1,20)
    print("Você escolheu o modo de jogo, dificil! Boa sorte!")
    print("Advinhe um numero de 1 a 20.")
else:
    print("A opção", opcao, "não existe!")

num = int(input("Digite um número: "))
if(num == sorteio):
    print("Parabéns, você acertou!")
else:
    print("Você errou! O número era", sorteio)