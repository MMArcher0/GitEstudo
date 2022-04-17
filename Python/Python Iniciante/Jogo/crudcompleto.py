
cadastros = []

def casdastrar():
    while True:
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        sexo = input("Digite o sexo: ")
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")

        print("Confirme se todas as informações estão corretas")
        print("Digite 1 se estiver correto")
        print("Digite 2 se estiver incorreto")

        opcao_selecionada = input()


#def consultar():

#def exibir_todos():

#def alterar():

#def excluir():

while True:
    print("---------------------------------")
    print("1 - Cadastrar ")
    print("2 - Consultar ")
    print("3 - Exibir todos os cadastros")
    print("4 - Alterar um cadastro")
    print("5 - Excluir um cadastro")
    print("6 - Encerrar a aplicação")
    print("---------------------------------")

    opcao_selecionada = input("Digite o numero da opção desejada: ")

    try:
        opcao_selecionada = int(opcao_selecionada)

    except:
        input("Por favor digite uma opção valida")
        continue

    if(opcao_selecionada == 1):
        casdastrar()

    #elif(opcao_selecionada == 2):
        #consultar()

    #elif(opcao_selecionada == 3):
        #exibir_todos()

    #elif(opcao_selecionada == 4):
        #alterar()

    #elif(opcao_selecionada == 5):
        #excluir()

    elif(opcao_selecionada == 6):
        break