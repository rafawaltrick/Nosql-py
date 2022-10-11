from operator import truediv
import Vendedor.cadastrarVendedor

def listaVendedor(meuBanco):

    execucao = True
    while execucao:

        print('''
            Digite "1" para Inserir Vendedor. \n
            Digite "0" para Voltar para o Menu Principal. \n
        ''')

        opcoes = input(str("Escolha a Opção Desejada: "))

        match opcoes:
            case "1":
                Vendedor.cadastrarVendedor.cadastrarVendedor(meuBanco)
            case "0": 
                return