def ordenamento(meuBanco):
    #Sort
    
    colecao = meuBanco.usuario
    print("\n####SORT####") 
    mydoc = colecao.find().sort("nome")
    for x in mydoc:
        print(x)
        