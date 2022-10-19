

import Redis.manipulacao as funcao


def listaRedis(clienteRedis, meuBanco):
    
    execucao = True
    while execucao:
        
        print('''
        
        Digite "1" para Adicionar Favoritos ao Redis. \n
        
        
            ''')
        
        opcoes = input(str("Escolha a Opção Desejada: "))
        
        match opcoes:
            case "1": 
                funcao.setaRedis(clienteRedis,meuBanco)
                