def inserirCompra(meuBanco):
    cadastrando = True
    nome = []
    while cadastrando:
        cadastrarCompra = input(str("Deseja cadastra Produto? (sim/não): "))
        if cadastrarCompra.lower() == "sim":
            nome = input(str("Digite o Nome do Produto: "))
            nome.append({
                'nome': nome
            })
        else:
            cadastrando = False
    colecao = meuBanco.compra
    lista = {
        'nome': nome 
            }
    x = colecao.insert_one(lista)
    print(x.inserted_id)