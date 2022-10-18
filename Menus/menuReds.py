def listaRedis(clienteRedis):
    
    execucao = True
    while execucao:
        
        print('''
              Digite "1" para Adicionar Favoritos ao Redis. \n
              ''')
        
        opcoes = imput(str("Escolha a Opção Desejada: "))
        
        match opcoes:
            case "1":
                break