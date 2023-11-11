def modify_restaurant(restaurants:list, cnpj:str) -> None:
    """
    Função para modificar informações de um restaurante existente.
    O usuário pode escolher qual campo deseja alterar.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """

    opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - Endereço\n\t3 - Telefone\n\t4 - Tempo médio de entrega\n\nSua escolha: ')
    
    # Verificando se a opção inserida é um número e está no intervalo correto
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



def edit_item(restaurants: list, id: int, idx:int) -> None:
    """
    Função para editar informações de um item em um restaurante específico.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        id::int: identificação do restaurante, sendo ela a posição que o mesmo se encontra na lista
    
    return:
        None
    """
    
    # Se o item for encontrado
    if idx != -1:
        # Solicita ao usuário qual campo do item deseja alterar
        opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - Preço\n\nSua escolha: ')
        
        # Verifica se a entrada é numérica e se está no intervalo correto
        if opc.isnumeric():
            opc = int(opc)
            if opc > 0  and opc < 3:
                # Solicita ao usuário o novo valor para o campo escolhido
                data = input('\nInfome o novo valor para o respectivo campo: ')
                # Atualiza o valor do campo escolhido no item
                restaurants[id][-1][idx][opc-1] = data
            else:
                print("\nOpção escolhida é invalida")
        else:
            print("\nInforme um valor númerico!")
                
    else:
        print("\nRestaurante não encontrado!")
        