def inserirCompra(meuBanco):
    cadastrando = True
    produto = []
    while cadastrando:
        cadastrarProduto = input(str("Deseja cadastra Produto? (sim/não): "))
        if cadastrarProduto.lower() == "sim":
            nome = input(str("Digite o Nome do Produto: "))
            valor = input(str("Digite o valor do produto: "))
            produto.append({
                '_id': {},
                'nome': nome,
                'valor': valor
            })
        else:
            cadastrando = False
    data_compra = input(str("Digita a Data da Compra: "))
    colecao = meuBanco.compra
    lista = {
        'produto': produto,
        'usuario': ({'_id': {}, 'nome': {}}),
        'vendedor': ({'_id': {}, 'nome': {}}),
        'data_compra': data_compra
            }
    x = colecao.insert_one(lista)
    print(x.inserted_id)