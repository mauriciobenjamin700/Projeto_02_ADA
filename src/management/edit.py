def modify_restaurant(restaurants:list, cnpj:str) -> None:
    """
    Função para modificar informações de um restaurante existente.
    O usuário pode escolher qual campo deseja alterar.
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        cnpj::str: chave do dicionário que será buscado
    return:
        None
    """

    opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - Endereço\n\t3 - Telefone\n\t4 - Tempo médio de entrega\n\nSua escolha: ')
    

    if opc.isnumeric():
        opc = int(opc)
        
        match opc:
            case 1:
                restaurants[cnpj]["name"] = input("\nNovo nome: ")
            
            case 2:
                restaurants[cnpj]["address"] = input("\nNovo Endereço: ")
                
            case 3:
                restaurants[cnpj]["phone"] = input("\nNovo Endereço: ")
                
            case 4:
                restaurants[cnpj]["time"] = input("\nNovo Tempo médio de entrega: ")
                
            case _:
                print("\nChave invalida!")
    
    else:
        print("\nOpção Invalida, insira apenas números!")        



def edit_item(restaurants:dict, key:str, product_name:str, valor:str) -> None:
    """
    Função para modificar informações de um cardapio em um restaurante existente.
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        key::str: chave do dicionário que será buscado
        product_name::str: Nome do produto que tera seus dados alterados.
        valor::str: String representando o valor do produto que será alterado
    return:
        None
    """
    
    sinal = 0
    
    product_name = product_name.upper()
        
    if product_name in restaurants[key]["menu"]:
        restaurants[key]["menu"][product_name] = valor
        sinal = 1    
    
    return sinal
        