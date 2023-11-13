from src.management.search import *

def remove_restaurant(restaurants:dict, id:str) -> None:
    """
    Função para remover um restaurante da lista.
    Parâmetros:
        restaurants::dict: Restaurantes Cadastrados
    return:
        None
    """

    del restaurants[id]


def remove_item(restaurants: list, key:str, product_name:str) -> None:
    sinal = 0
        
    product_name = product_name.upper()
        
    if product_name in restaurants[key]["menu"]:
        del restaurants[key]["menu"][product_name]
        sinal = 1    
    
    return sinal
