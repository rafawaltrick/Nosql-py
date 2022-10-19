from Usuario.busca import buscarNome


def setaRedis(clienteRedis, meuBanco):
    nome = buscarNome(meuBanco)
    print(nome)
    clienteRedis.hset('usuario: ' + nome['nome'], nome['favoritos'])
    resultado = clienteRedis.hget('usuario: ' + nome['nome'], nome['favoritos'])
    print(resultado)