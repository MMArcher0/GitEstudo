
def jogar_forca():
    print("--------------------------")
    print("Bem vindo ao jogo de forca")
    print("--------------------------")

    palavra_secreta = "maça"

    chutes_acertados = ["_","_","_","_"]

    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input("Qual letra quer tentar?").strip().lower() #Recebe o input da letra e retira espaços e deixa em lower case
        index = 0

        for letra in palavra_secreta:

            if(chute == letra):
                chutes_acertados[index] = chute

            index = index + 1

        print(chutes_acertados)

if(__name__ == "__main__"):
    jogar_forca()