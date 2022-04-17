lista = []


def adicionar(nome):
    lista.append(nome)
    print("Nome adicionado com sucesso")


def buscar_todos():
    print("Seguem todos os nomes na lista")
    for indice in lista:
        print(indice)


def excluir(nome):
    lista.remove(nome)
    print("Nome removido com sucesso")


def alterar(nome_antigo, nome_novo):
    lista[lista.index(nome_antigo)] = nome_novo
    print("Nome alterado com sucesso")


def busca_especifica(nome):
    try:
        lista[lista.index(nome)]
        print("Nome especificado esta na lista")
    except:
        print("Nome especificado não esta na lista")


while True:
    print("------------------------------------")
    print("* 1 para adicionar a lista         *")
    print("* 2 para verificar todos na lista  *")
    print("* 3 para excluir nome da lista     *")
    print("* 4 para alterar um nome na lista  *")
    print("* 5 para buscar nome especifico    *")
    print("* 6 para finalizar aplicação       *")
    print("------------------------------------")

    opcao_selecionada = input("Digite aqui a opção desejada: ")

    try:
        opcao_selecionada = int(opcao_selecionada)

    except:
        print("Digite uma opção valida >:(")
        input("Digite qualquer coisa para continuar")
        continue

    if (opcao_selecionada == 1):
        adicionar(input("Digite o nome que deseja adicionar a lista: "))

    elif (opcao_selecionada == 2):
        buscar_todos()

    elif (opcao_selecionada == 3):
        excluir(input("Digite o nome que deseja excluir da lista: "))

    elif (opcao_selecionada == 4):
        nome_antigo = input("Digite o nome que deseja alterar na lista: ")
        nome_novo = input("Digite o nome com a alteração desejada: ")
        alterar(nome_antigo, nome_novo)

    elif (opcao_selecionada == 5):
        busca_especifica(input("Digite o nome que deseja verificar se esta na lista: "))

    elif (opcao_selecionada == 6):
        break

    else:
        print("Digite uma opção valida >:(")

    input("Digite qualquer coisa para continuar")