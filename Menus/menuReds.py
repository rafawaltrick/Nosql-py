

import Redis.manipulacao as funcao


def listaRedis(clienteRedis, meuBanco):
    
    execucao = True
    while execucao:
        
        print('''
        
        Digite "1" para Adicionar Favoritos ao Redis. \n
        Digite "2" para Adicionar Um Item a Lista dos Favoritos. \n
        
        
            ''')
        
        opcoes = input(str("Escolha a Opção Desejada: "))
        
        match opcoes:
            case "1": 
                funcao.setaRedis(clienteRedis,meuBanco)
            case "2":
                funcao.addFavoritos(clienteRedis, meuBanco)    
                