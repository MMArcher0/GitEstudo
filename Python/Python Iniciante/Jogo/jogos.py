import forca
import adivinhacao

print("------------------")
print("Escolha o seu jogo")
print("------------------")

print("1 Forca")
print("2 Adivinhação")

jogo = input("Qual Jogo?")

try:
    val = int(jogo)

except ValueError:
    print("Digite uma opção valida")

if(int(jogo) == 1 ):
    forca.jogar_forca()
elif(int(jogo ==2 )):
    adivinhacao.jogar_adivinhacao()
else:
    print("Digite uma opção valida")