sorteio1 = 7
sorteio2 = 14

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if(num1 == sorteio1):
    print("Você acertou o primeiro!")
    if(num2 == sorteio2):
        print("Parabéns! você acertou os dois números!!")
    else:
        print("Você errou o segundo número!")
else:
    print("Você errou o primeiro número")        