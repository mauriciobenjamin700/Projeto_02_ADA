def add_restaurant(restaurants:dict) -> int:
    """
    Função para adicionar um novo restaurante à lista de restaurantes.
    Recebe um dicionario de restaurantes e adiciona um novo restaurante.
    Retorna 1 em caso de sucesso e 0 em caso de falha
    
    Parâmetros:
        restaurants::dict: lista onde os restaraurantes serão armazenados
    return:
        sinal::int: sinal correspondendo ao resultado da operação
    """
    
    sinal = 1
    try:
        
        print('\nPreencha as informações do restaurante!\n')
        name = input('Nome: ').upper()
        cnpj = input('CNPJ: ')
        address = input('Endereço: ').upper()
        phone = input('Telefone: ')
        time = input('Tempo médio de entrega [Minutos]: ')
        cnpj = ''.join(filter(str.isdigit,cnpj))
        new_dict = {"name": name, "cnpj": cnpj,"address":address,"phone":phone,"time": time, "menu": {}}
        
        #restaurants.append([name, cnpj, address, phone, time, menu])
        
        
        
        restaurants[cnpj] = new_dict

    except:
        sinal = 0
        
    return sinal
    
    
def add_item(restaurants:dict, key:str) -> None:
    """
    Função para adicionar um novo item ao menu de um restaurante.
    Parâmetros:
        restaurants::dict: lista de restaurantes
        key::str: chave do dicionário que será adicionado o novo item
    
    return:
        sinal::int: Sinalização para representar sucesso (1) e falha (0)
    """
    sinal = 1
    try:
        print('\nInforme os dados do item: ')
        name = input('Nome: ').upper()
        valor = input('Preço: ')
        
        restaurants[key]["menu"][name] = valor

    except:
        sinal = 0
        
    return sinal
    
    

