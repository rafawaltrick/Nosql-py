import pymongo
import redis
import Menus.menuUsuario
import Menus.menuProduto
import Menus.menuVendedor
import Menus.menuCompra
import Menus.menuReds
from pymongo.server_api import ServerApi


clienteRedis = redis.Redis(host='redis-12427.c273.us-east-1-2.ec2.cloud.redislabs.com',
                port=12427,
                password='12345678')


conexao = pymongo.MongoClient ("mongodb+srv://rafawaltrick:392913rw@naorelacional.dxfl9ll.mongodb.net/?retryWrites=true&w=majority")

meuBanco = conexao.mercadoLivre

execucao = True
while execucao:

    print ('''
        Digite "1" para Menu Usuário. \n
        Digite "2" para Menu Produto. \n
        Digite "3" para Menu Vendedor. \n
        Digite "4" para Menu Compra. \n
        Digite "5" para menu Redis. \n
        Digite "0" para Sair.\n
    ''')
    opcoes = input(str("Escolha a Opção Desejada: "))
    match opcoes:
        case "1":
            Menus.menuUsuario.listaUsuario(meuBanco)
        case "2":
            Menus.menuProduto.listaProduto(meuBanco)
        case "3":
            Menus.menuVendedor.listaVendedor(meuBanco)
        case "4":
            Menus.menuCompra.listaCompra(meuBanco)  
        case "5":
            Menus.menuReds.listaRedis(clienteRedis, meuBanco)
        case "0":
            break
            


