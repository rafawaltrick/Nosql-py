def atualizarProduto(meuBanco):
    nomeProduto = input(str("Digite o Nome do Produto a ser Atualizado: "))
    nomeAtualizado = input(str("Digite o Novo Nome: "))

    colecao = meuBanco.produto

    filtro = {"nome": nomeProduto}
    nomeAtualizado = {"$set": {"nome": nomeAtualizado}}

    colecao.update_one(filtro, nomeAtualizado)

    for x in colecao.find():
        print(x)