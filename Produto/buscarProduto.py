def buscarProduto(meuBanco):
    nome = input(str("Digite o Nome do Produto Desejado: "))

    colecao = meuBanco.produto
    comando = {"nome": nome}
    mudoc =colecao.find_one(comando)

    if mydoc == None:
        print("Produto Não encontrado.")
    else:
        print(f'nome:{mydoc}')