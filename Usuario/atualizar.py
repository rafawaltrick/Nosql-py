def atualizar(meuBanco):
    #update
    nome = input(str("Digite o Nome a ser Atualizado: "))
    novoNome = input(str("Digite o Novo Nome: "))

    colecao = meuBanco.usuario

    filtro = { "nome": nome }
    novoNome = { "$set": { "nome": novoNome } }

    colecao.update_one(filtro, novoNome)

    #print "customers" after the update:
    for x in colecao.find():
        print(x)