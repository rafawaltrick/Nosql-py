def buscarCompra(meuBanco):
    nome = input(str("Digite o Nome do Produto Comprado: "))
    
    colecao = meuBanco.compra
    compra = colecao.find()
    for x in colecao.find({}, {"produto": 1}):
        print(x)
        
        


