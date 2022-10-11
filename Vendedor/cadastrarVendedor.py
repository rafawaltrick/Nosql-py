def cadastrarVendedor(meuBanco):

    colecao = meuBanco.vendedor

    nome = input(str("Digite o Nome do Vendedor: "))
    documento = input(str("Digite o CPF/CNPJ do Vendedor: "))
    #produto = input(str("Digite o(s) Produtos: "))

    mydict = {
        "nome": nome,
        "documento": documento,
        "produtos": []
    }

    x = colecao.insert_one(mydict)
    
