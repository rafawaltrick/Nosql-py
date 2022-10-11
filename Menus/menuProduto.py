import Produto.inserirProd
import Produto.atualizarProduto

def listaProduto(meuBanco):
    execucao = True
    while execucao:
        print('''
        Digite "1" Para Inserir um Produto.
        Digite "2" Para Atualizar um Produto.
        Digite "0" Para Retonar ao Menu Principal.
            ''')
            
        opcao = input(str("Escolha a Opção desejada: "))

        match opcao:
            case "1":
                Produto.inserirProd.inserirProduto(meuBanco)
            case "2":
                Produto.atualizarProduto.atualizarProduto(meuBanco)
            case "0":
                return
