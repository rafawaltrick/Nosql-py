import Compra.inserirCompra

def listaCompra(meuBanco):

    excucao = True
    while excucao:

        print('''
            Digite "1" para Inserir Compra. \n
            Digite "0" para Voltar para o Menu Principal. \n
        ''')

        opcoes = input(str("Escolha a opção Desejada: "))

        match opcoes:
            case "1":
                Compra.inserirCompra.inserirCompra
            case "0":
                return
