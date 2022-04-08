import random

# Menu Inicial
def jogar_adivinhacao():
    print("----------------------------------")
    print("|Bem-vindo ao jogo de advinhação!|")
    print("----------------------------------")
    print("|     Selecione a dificuldade    |")
    print("| 1 Facil                        |")
    print("| 2 Medio                        |")
    print("| 3 Dificil                      |")
    print("| 4 Impossivel                   |")
    print("----------------------------------")

    # Seleção de dificuldade

    dificuldade_selecionada = bool(1)
    while(dificuldade_selecionada):

        dificuldade = input("Digite o numero:")

        try:
            val = int(dificuldade)

        except ValueError:
            print("Ta de sanagem né mano 凸ಠ益ಠ)凸")
            continue

        if(int(dificuldade) <= 4 and int(dificuldade) >=1):
            dificuldade_selecionada = bool(0)

        else:
            print("Digita um input certo ai, pelamor ddeus 凸-_-凸")

    # Inicia os parametros de jogo

    maximo_rodadas = 0
    rodada = 0
    adivinhou = bool(0)
    min_random = 0
    max_random = 0
    pontuacao = 1000

    # Seta os parametros de acordo com a dificuldade

    if(int(dificuldade) == 1):
        maximo_rodadas = 10
        rodada = 1
        min_random = 1
        max_random = 51

    elif(int(dificuldade) == 2):
        maximo_rodadas = 6
        rodada = 1
        min_random = 1
        max_random = 51

    elif(int(dificuldade) == 3):
        maximo_rodadas = 5
        rodada = 1
        min_random = 1
        max_random = 101

    elif(int(dificuldade) == 4):
        maximo_rodadas = 5
        rodada = 1
        min_random = 1
        max_random = 10001

    else:
        print("NA programador, nem sabe fazer as parada")


    # Gera o numero secreto

    num_secreto = round(random.randrange(min_random, max_random))

    # Inicia o jogo

    while(maximo_rodadas >= rodada):

        print("------------------------------------")
        print("Rodada {} de {}".format(rodada, maximo_rodadas))
        print("Pontuação atual {:.0f}".format(pontuacao))
        chute = input("Digite o numero entre {} e {}: ".format(min_random,max_random - 1))
        print("Você digitou", chute)

        #Verifica o input
        try:
            val = int(chute)

        except ValueError:
            print("Ta de sanagem né")
            continue
        if(int(chute) < min_random or int(chute) > max_random):
            print("Você tem que digitar um numero dentro dos especificados")
            continue

        #Verifica se acertou

        acertou = num_secreto == int(chute)
        maior = num_secreto < int(chute)
        menor = num_secreto > int(chute)

        if(acertou):
            print("Você acertou")
            adivinhou = bool(1)
            break
        elif(maior):
            print("Você errou, Seu numero esta acima do numero secreto")
            rodada = rodada + 1
            pontuacao = pontuacao * 0.9
        elif(menor):
            print("Você errou, Seu numero esta abaixo do numero secreto")
            rodada = rodada + 1
            pontuacao = pontuacao * 0.9
        else:
            print("Você errou")
            rodada = rodada + 1
            pontuacao = pontuacao * 0.9

    #Mensagem de final de partida

    if(adivinhou):
        print("Você é o bixão mesmo em")
        print("Pontuação Final {:.0f}".format(pontuacao))
    else:
        print("Você é muito ruim abandone essa carreira")
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar_adivinhacao()