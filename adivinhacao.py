import random

numero = random.randrange(1,101)
tentativas = 0

print("Escolha o nível de dificuldade:")
print("1 - Fácil, 2 - Médio, 3 - Difícil")
nivel = int(input("Digite o nível: "))

if nivel == 1:
    tentativas = 20
elif nivel == 2:
    tentativas = 10
elif nivel == 3:
    tentativas = 5
    
for rodada in range(1, tentativas + 1):
    print(f"Tentativas {rodada} de {tentativas}")
    valor = input("Digite um número entre 1 a 100: ")
    print("Você digitou ", valor)
    valor=int(valor)
    
    if valor < 1 or valor > 100:
        print("Número inválido!")
        continue
    
    acertou = valor == numero
    maior = valor > numero
    menor = valor < numero
    
    if acertou:
        print("Parabéns, você acertou!")
        break
    else:
        if maior:
            print("Você errou, o número escolhido foi maior")
        elif menor:
            print("Você errou, o número escolhido foi menor")
            
print("Fim de jogo")