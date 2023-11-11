from src.management.search import *
def add_restaurant(restaurants:dict) -> int:
    """
    Função para adicionar um novo restaurante à lista de restaurantes.
    Recebe um dicionario de restaurantes e adiciona um novo restaurante.
    Retorna 1 em caso de sucesso e 0 em caso de falha
    
    Parâmetros:
        restaurants::list: lista onde os restaraurantes serão armazenados
    return:
        sinal::int: sinal correspondendo ao resultado da operação
    """
    # Solicitando ao usuário as informações do novo restaurante
    sinal = 1
    try:
        
        print('\nPreencha as informações do restaurante!\n')
        name = input('Nome: ').upper()
        cnpj = input('CNPJ: ')
        address = input('Endereço: ').upper()
        phone = input('Telefone: ')
        time = input('Tempo médio de entrega [Minutos]: ')
        new_dict = {"name": name, "cnpj": cnpj,"address":address,"phone":phone,"time": time, "menu": []}
        
        #restaurants.append([name, cnpj, address, phone, time, menu])
        
        restaurants[cnpj] = new_dict

    except:
        sinal = 0
        
    return sinal
    
    
def add_item(restaurants:list) -> None:
    """
    Função para adicionar um novo item ao menu de um restaurante.
    Parâmetros:
        restaurants::list: lista de restaurantes
    
    return:
        None
    """
    # Procurando o restaurante ao qual o item será adicionado
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado
    if id != -1:
        # Solicitando ao usuário as informações do novo item
        print('\nInforme os dados do item: ')
        name = input('Nome: ').upper()
        valor = input('Preço: ')
        
        # Adicionando o novo item ao menu do restaurante
        restaurants[id][-1].append([name, valor])
        print("Item adicionado ao cardápio!")

    else:
        print("\nRestaurante não encontrado!")
 