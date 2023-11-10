from src.management.search import *
def add_restaurant(restaurants:list) -> None:
    """
    Função para adicionar um novo restaurante à lista de restaurantes.
    Recebe a lista de restaurantes e adiciona um novo restaurante.
    
    Parâmetros:
        restaurants::list: lista onde os restaraurantes serão armazenados
    return:
        None
    """
    # Solicitando ao usuário as informações do novo restaurante
    print('\nPreencha as informações do restaurante!\n')
    name = input('Nome: ').upper()
    cnpj = input('CNPJ: ')
    address = input('Endereço: ').upper()
    phone = input('Telefone: ')
    time = input('Tempo médio de entrega [Minutos]: ')
    menu = []
    
    # Adicionando o novo restaurante à lista
    restaurants.append([name, cnpj, address, phone, time, menu])
    print("Restaurante adicionado com sucesso!")
    
    
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
 