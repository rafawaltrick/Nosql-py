def inserir(meuBanco):
    nome = input(str("Digite seu Nome: "))
    cpf = input(str("Digite seu CPF: "))
    email = input(str("Digite seu Email: "))
    telefone = input(str("Digite seu Telefone: "))
    rodando = True
    enderecos = []
    while rodando:
        cadastrarEndereco = input(str("Desja Cadastrar Endereço? (sim/não): "))
        if cadastrarEndereco.lower() == "sim":
            rua = input(str("Digite o Nome da Rua: "))
            numero = input (str("Digite o número: "))
            cidade = input(str("Digite a Cidade: "))
            enderecos.append({
                'rua': rua,
                'numero': numero,
                'cidade': cidade
            })
        else:
            rodando = False
    colecao = meuBanco.usuario
    print("\n #####insert###")
    dicionario = {
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'telefone': telefone,
        'endereco': enderecos,
        'favoritos':[
            ],
        'compras': [
            ]}
    x = colecao.insert_one(dicionario)
    print(x.inserted_id)