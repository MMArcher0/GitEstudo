import random

# Jogo da forca
def jogar_forca():
    # Apresentação inicial do jogo
    print("--------------------------")
    print("Bem vindo ao jogo de forca")
    print("--------------------------")

    # Declara variaveis necessarias para o jogo
    chutes_acertados = []
    chutes_errados = []
    gabarito = []
    lista_frutas = []
    enforcou = False
    acertou = False
    erros = 0

    # Abre o arquivo com as frutas
    frutas = open("frutas.txt", "r")

    # Le o arquivo linha por linha, e adiciona numa lista.
    for fruta in frutas:
        lista_frutas.append(fruta.strip().lower())

    # Seleciona um valor pseudo random entre 0 e o total de palavras e define como a palavra_secreta
    palavra_secreta = random.randrange(0, len(lista_frutas))
    palavra_secreta = lista_frutas[palavra_secreta]

    # Gera o gabarito da palavra_secreta e lista para armezenar chutes acertados
    for letra in palavra_secreta:
        chutes_acertados.append("_")
        gabarito.append(letra)

    # Executa o jogo
    while not enforcou and not acertou:

        # Mostra ao jogador quantas letras tem na palavra_secreta
        print("A palavra secreta tem: {} letras".format(len(palavra_secreta)))

        # Mostra ao jogador quantas e quais letras não estão na palavra_secreta
        letras_erradas = " "
        for letra in chutes_errados:
            letras_erradas += letra
        print("Letras chutadas que não estão na palavra: \n{}".format(letras_erradas.strip().upper()))

        # Gera uma demonstração visual do numero de letras, com as letras já acertadas
        acertos = " "
        print("Letras já acertadas da palavra: ")
        for letra in chutes_acertados:
            acertos += letra
        print(acertos.strip().upper())

        # Solicita ao jogador um chute para a palavra secreta
        chute = input(
            "Qual letra quer tentar?").strip().lower()  # Recebe o input da letra e retira espaços e deixa em lower case

        # Gera um index para armazenar as letras acertadas na lista de chutes_acertados
        # Verifica se a letra chutada esta na palavra_secreta se não adiciona um erro
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    chutes_acertados[index] = chute

                index += 1

        else:
            erros += 1
            chutes_errados.append(chute)

        # Verifica se o usuario já acertou a palavra_secreta
        # Verifica se o usuario já se enforcou
        enforcou = erros == 6
        acertou = gabarito == chutes_acertados

        # Mensagens caso usuario tenha ganho ou perdido
        if enforcou:
            print("Fim de jogo, Você perdeu")

        elif acertou:
            print("Fim de jogo, Você ganhou")
            print("A palavra secreta era: {}".format(palavra_secreta))


if __name__ == "__main__":
    jogar_forca()
