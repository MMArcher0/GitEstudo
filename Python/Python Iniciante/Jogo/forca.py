
def jogar_forca():
    print("--------------------------")
    print("Bem vindo ao jogo de forca")
    print("--------------------------")

    palavra_secreta = "melancia"

    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input("Qual letra quer tentar?").strip().lower() #Recebe o input da letra e retira espaços e deixa em lower case
        index = 1

        for letra in palavra_secreta:

            if(chute == letra):
                print("Seu chute {} esta na palavra, na posição {}".format(chute, index))

            index = index + 1


if(__name__ == "__main__"):
    jogar_forca()