def inserirProduto(meuBanco):

    colecao = meuBanco.produto
    
    produto = input(str("Digite o Nome do Produto: "))
    preco = input(str("Digite o Preço do Produto: "))
    descricao = input(str("Digite a Descrição: "))
    quantidade = input(str("Digite a Quantidade do Produto: "))

    mydict = { "nome": produto,
                "preco": preco,
                "descricao": descricao,
                "quantidade": quantidade,
                'vendedor': [] 
    }


    x = colecao.insert_one(mydict)   