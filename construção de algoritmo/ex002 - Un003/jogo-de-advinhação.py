import random

sorteio = random.randint(1, 10)

num = int(input("Digite um numero de 0 a 10:  "))

if(sorteio == num):
    print("Parabéns! você acertou!")
else: 
    print("Que pena!, você errou!")