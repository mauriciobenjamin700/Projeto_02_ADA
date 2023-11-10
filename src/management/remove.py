from src.management.search import *

def remove_restaurant(restaurants:list) -> None:
    """
    Função para remover um restaurante da lista.
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """
    # Procurando o restaurante a ser removido
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado, removendo-o da lista
    if id != -1:
        del restaurants[id]
        print("\nRestaurante removido!")
    else:
        print("\nRestaurante não encontrado!")

def remove_item(restaurants: list, id: int) -> None:
    """
    Função para remover um item do menu de um restaurante específico.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        id::int: indice do item que se deseja remover
    
    return:
        None
    
    """
    # Procura o índice do item que será removido
    idx = search_item(restaurants, id)
    
    # Se o item for encontrado, remove-o da lista
    if idx != -1:
        del restaurants[id][-1][idx]
        
    else:
        print("\nRestaurante não encontrado!")
