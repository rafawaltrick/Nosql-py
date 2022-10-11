def atualizaravendedor(meuBanco):
    colecao = meuBanco.vendedor
    nomeVendedor = input(str("Digite o Nome do Vendedor a ser Atualizado: "))
    meusDados = { "nome": nomeVendedor  }
    
    atualizarVendedor = input(str("Deseja Atualizar o Nome ou CPF: "))
    print(atualizarVendedor)
    if(atualizarVendedor.lower() == "nome"):
        nomeVendedorAtualizado = input(str("Digite o Novo Nome: "))
        novoDado = { "$set": { "nome": nomeVendedorAtualizado } }
        colecao.update_one(meusDados, novoDado)
        
    if(atualizarVendedor.lower() == "cpf"):
        cpfAtualizado = input(str("Digite o novo CPF: "))
        novoCpf = {"$set": {"documento": cpfAtualizado }} 
        colecao.update_one(meusDados, novoCpf)
    
    
#print "customers" after the update:
    for x in colecao.find():
        print(x)