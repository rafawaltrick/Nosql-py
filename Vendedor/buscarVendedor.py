def buscarVendedor(meuBanco):
    colecao = meuBanco.vendedor

    vendedor = colecao.find()
    for x in vendedor:
        print(x)