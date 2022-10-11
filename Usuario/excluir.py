def excluirNome(meuBanco):
#delete
    nome = input(str("Digite o Nome a Ser Excluido: "))

    colecao = meuBanco.usuario
    filtro = { "nome": nome }

    colecao.delete_one(filtro)
    print(nome)