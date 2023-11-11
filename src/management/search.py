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

def search_item(restaurants: list, id: int) -> int:
    """
    Função para pesquisar um item no menu de um restaurante específico.
    
    Parâmetros:
        restaurants::list: Lista de todos os restaurantes.
        id:int: Índice do restaurante em que se deseja buscar o item.
    
    return: 
        idx::int: índice do item encontrado ou -1 se não encontrar.
    """
    cont = 0  # Inicializando um contador.
    idx = -1  # Inicializando o índice de retorno com -1 (item não encontrado).
    
    # Verifica se o ID fornecido é válido
    if id != -1:
        # Solicita ao usuário o nome do produto que deseja buscar
        name = input('\nNome do produto: ').upper()
        
        # Procura o produto no menu do restaurante especificado
        for item in restaurants[id][-1]:
            if item[0] == name:
                idx = cont  # Atribui o valor do contador ao índice de retorno
                return idx
            cont += 1  # Incrementa o contador
         
    return idx
