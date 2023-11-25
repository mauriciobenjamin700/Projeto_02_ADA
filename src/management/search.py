def search_restaurant(restaurants:dict, key:str) -> int:
    """
    Função que busca um restaurante pelo CNPJ.
    Caso encontre retorna 1, caso não retorna 0
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        key::str: chave do dicionário que será buscado
    Retorna:
        result::int:  0 em caso de falha, 1 em caso de sucesso
    """
    
    id = 0

    for valid_keys in restaurants.keys():
        if key == valid_keys:
            id = 1
            
    return id

def search_item(restaurants: list, key:str, name:str) -> int:
    """
    Função que busca em restaurante pelo CNPJ um item no menu e retorna 1 para sucesso e 0 para falha
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        key::str: chave do dicionário que será buscado
        name::str: nome do item do menu que está sendo buscado.
    Retorna:
        result::int:  0 em caso de falha, 1 em caso de sucesso
    """
        
    sinal = 0
    if name in restaurants[key]["menu"].keys():
        sinal = 1
        
    return sinal
