def excluirVendedor(meuBanco):
    nome = input(str("Digite o Nome a Ser Excluido: "))

    colecao = meuBanco.vendedor
    filtro = { "nome": nome }

    colecao.delete_one(filtro)
    print(nome)