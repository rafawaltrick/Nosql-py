from operator import truediv
import Vendedor.cadastrarVendedor
import Vendedor.buscarVendedor
import Vendedor.atualizarVendedor
import Vendedor.excluirVendedor

def listaVendedor(meuBanco):

    execucao = True
    while execucao:

        print('''
            Digite "1" para Inserir Vendedor. \n
            Digite "2" para Buscar Vendedor. \n
            Digite "3" para Atualizar os Dados do Vendedor. \n
            Digete "4" para Excluir Um Vendedor. \n
            Digite "0" para Voltar para o Menu Principal. \n
        ''')

        opcoes = input(str("Escolha a Opção Desejada: "))

        match opcoes:
            case "1":
                Vendedor.cadastrarVendedor.cadastrarVendedor(meuBanco)
            case "2":
                Vendedor.buscarVendedor.buscarVendedor(meuBanco)
            case "3":
                Vendedor.atualizarVendedor.atualizaravendedor(meuBanco)
            case "4":
                Vendedor.excluirVendedor.excluirVendedor(meuBanco)
            case "0": 
                return