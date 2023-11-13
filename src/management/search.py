def search_restaurant(restaurants:dict, key:str) -> int:
    """
    Função que busca um restaurante pelo CNPJ.
    Caso encontre retorna 1, caso não retorna 0
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    Retorna:
        result::int:  0 em caso de falha, 1 em caso de sucesso
    """
    # Opções para o usuário escolher como quer buscar o restaurante
    
    id = 0

    # Obtendo a chave de pesquisa (nome ou CNPJ) com base na escolha do usuário
    for valid_keys in restaurants.keys():
        if key == valid_keys:
            id = 1
            
    return id

def search_item(restaurants: list, key:str, name:str) -> int:
    
    sinal = 0
    if name in restaurants[key]["menu"].keys():
        sinal = 1
        
    return sinal
