import Usuario
import Usuario.cadastro
import Usuario.ordenar 
import Usuario.busca
import Usuario.atualizar
import Usuario.excluir


def listaUsuario(meuBanco):

    execucao = True
    while execucao:

        print ('''
            Digite "1" para Buscar Usuário. \n
            Digite "2" para Iserir um Usuário. \n
            Digite "3" para Ordenar os Usuários. \n
            Digite "4" para Buscar Usuário. \n
            Digite "5" para Buscar Produto. \n
            Digite "6" para Atualizar o Nome. \n
            Digite "7" para Excluir o Nome. \n
            Digite "0" para Voltar para o Menu Principal. \n
        
        ''')
        opcoes = input(str("Escolha a Opção Desejada: "))

        match opcoes:
            case "1":
                Usuario.busca.buscarNome(meuBanco)
            case "2":
                Usuario.cadastro.inserir(meuBanco)
            case "3":    
                Usuario.ordenar.ordenamento(meuBanco)
            case "4":
                Usuario.busca.buscarTodos(meuBanco)   
            case "5":
                Usuario.busca.buscarProdutos(meuBanco)   
            case "6":
                Usuario.atualizar.atualizar(meuBanco)  
            case "7":
                Usuario.excluir.excluirNome(meuBanco)
            case "0":
                return    
       