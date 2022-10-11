def excluirProduto(meuBanco):
    nome = input(str("Digite o Produto a Ser Excluido: "))

    colecao = meuBanco.produto
    filtro = { "nome": nome }

    colecao.delete_one(filtro)
    print(nome)