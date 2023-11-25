def interface() -> str:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.
    A mesma aciona outros submenus para mostrar opções para o usuário
    
    Parâmetros:
        None
    Retorna:
        opc::str: identificação da operação que será realizada
    """  
    # Exibe as opções da tela inicial
    print(('''
                            INICIO
    |-------------------------------------------------------|
    | 1 - Gestão de restaurantes                            |
    | 2 - Gestão de cardápio                                |
    | 3 - Visualizar informações (Restaurantes e cardápios) |
    | 0 - Encerrar programa                                 |
    |------------------------------------------------------ |
    '''))


    opc = input('\nOpção desejada: ')

    match opc:
        case '1':
            opc = restaurants_list_management() 

        case '2':
            opc = restaurants_menu_management()
        
        case '3':
            opc = show_information()
        case '0':
            opc = '0'
        case _:
            opc = '-1'
        
    return opc


def restaurants_list_management() -> str:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::str: identificação da operação que será realizada
    """  
    print(('''
                    GESTAO DE RESTAURANTES
    |-------------------------------------------------------|
    | 1 - Adicionar restaurante                             |
    | 2 - Editar restaurante                                |
    | 3 - Remover restaurante                               |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
     
    opc = input('\nOpção desejada: ')


    if opc == '1':
        opc =  '11'
    elif opc == '2':
        opc =  '12'
    elif opc == '3':
        opc = '13'
    elif opc == '4':
        opc = '4'
    else:
        opc = '-1'
        
    return opc
    
# Função que exibe o menu de gerenciamento do cardápio
def restaurants_menu_management() -> str:   
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::str: identificação da operação que será realizada
    """ 
    print(('''
                        GESTAO DE CARDAPIO
    |-------------------------------------------------------|
    | 1 - Adicionar item ao cardápio                        |
    | 2 - Editar item do cardápio                           |
    | 3 - Remover item do cardápio                          |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
    
    
    opc = input('\nOpção desejada: ')

    # Redireciona o usuário com base na sua escolha
    if opc == '1':
        opc = '21'
    elif opc == '2':
        opc = '22'
    elif opc == '3':
        opc = '23'
    elif opc == '4':
        opc = '4'
    else:
        opc = '-1'
        
    return opc


def show_information() -> str:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::str: identificação da operação que será realizada
    """
    print(('''
                    VISUALIZAR INFORMACOES
    |-------------------------------------------------------|
    | 1 - Exibir lista de restaurantes                      |
    | 2 - Exibir detalhadamente cada restaurante            |
    | 3 - Exibir restaurante com o menor tempo de entrega   |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
    
    opc = input('\nOpção desejada: ')


    if opc == '1':
        opc = '31'
    elif opc == '2':
        opc = '32'
    elif opc == '3':
        opc = '33'
    elif opc == '4':
        opc = '4'
            
    return opc

