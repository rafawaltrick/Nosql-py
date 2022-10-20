from Usuario.busca import buscarNome
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

def setaRedis(clienteRedis, meuBanco):
    nome = buscarNome(meuBanco)
    listaObjeto = dumps(nome ['favoritos'])
    clienteRedis.set('usuario: ' + nome['nome'], listaObjeto)
    resultado = clienteRedis.get('usuario: ' + nome['nome'])
    print(resultado)
    
def addFavoritos(clienteRedis, meuBanco):
    colecao = meuBanco.produto
    produtos = colecao.find_one(ObjectId('63060f018c9a180d1186058c'))
    nome = buscarNome(meuBanco)
    novoFavorito = clienteRedis.get('usuario: ' + nome['nome'])
    favoritosDecode = json.loads(novoFavorito.decode())
    favoritosFormatado = {'_id': produtos['_id'], 'nome': produtos['nome']}
    listaNovosFavoritos = [favoritosFormatado, *favoritosDecode]
    clienteRedis.set('usuario: ' + nome['nome'], dumps(listaNovosFavoritos))
    resultado = clienteRedis.get('usuario: ' + nome['nome'])
    print(resultado)
   
    