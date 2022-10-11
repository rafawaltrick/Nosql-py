import Produto.inserirProd
import Produto.atualizarProduto
import Produto.buscarProduto
import Produto.excluirProduto

def listaProduto(meuBanco):
    execucao = True
    while execucao:
        print('''
        Digite "1" Para Inserir um Produto.
        Digite "2" Para Atualizar um Produto.
        Digite "3" Para Buscar um Produto.
        Digite "4" Para Exclir um Produto.
        Digite "0" Para Retonar ao Menu Principal.
            ''')
            
        opcao = input(str("Escolha a Opção desejada: "))

        match opcao:
            case "1":
                Produto.inserirProd.inserirProduto(meuBanco)
            case "2":
                Produto.atualizarProduto.atualizarProduto(meuBanco)
            case "3":
                Produto.buscarProduto.buscarProduto(meuBanco)
            case "4":
                Produto.excluirProduto.excluirProduto(meuBanco)
            case "0":
                return
