import Compra.inserirCompra
import Compra.buscarCompra

def listaCompra(meuBanco):

    excucao = True
    while excucao:

        print('''
            Digite "1" para Inserir Compra. \n
            Digite "2" para Buscar Compra. \n
            Digite "0" para Voltar para o Menu Principal. \n
        ''')

        opcoes = input(str("Escolha a opção Desejada: "))

        match opcoes:
            case "1":
                Compra.inserirCompra.inserirCompra(meuBanco)
            case "2":
                Compra.buscarCompra.buscarCompra(meuBanco)
            case "0":
                return
