from Usuario.busca import buscarNome


def listaReds(clienteRedis, meuBanco):
    nome = buscarNome(meuBanco)
    clienteRedis.SADD('usuario: ' + nome['nome'], nome['favoritos'])
    resultado = clienteRedis.hget('usuario: ' + nome['nome'], nome['favoritos'])
    print(resultado)