def buscarNome(meuBanco):
    nome = input(str("Digite o Nome Desejado: "))
    
    colecao = meuBanco.usuario
    print("\n####QUERY####")
    comando = { "nome": nome }
    mydoc = colecao.find_one(comando)
    
    
   
    if mydoc == None:
        print("Usuário Não Encontrado.")
    else:
        print(f'nome:{mydoc["nome"]}')
        print(f'telefone:{mydoc["telefone"]}')
        print(f'email:{mydoc["email"]}')
    return mydoc

def buscarTodos(meuBanco):

    colecao = meuBanco.usuario
    mydoc = colecao.find()
    for x in mydoc:
        print(x) 

    