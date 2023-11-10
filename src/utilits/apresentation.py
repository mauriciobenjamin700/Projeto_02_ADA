
def show_restaurant(restaurant:list) -> None:
    """
    Exibe os dados de um restaurante.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    
    """

    print(f'\n\tNome: {restaurant[0]}\n\tCNPJ: {restaurant[1]}\n\tEndereço: {restaurant[2]}\n\tTelefone: {restaurant[3]}\n\tTempo médio para um entrega: {restaurant[4]}')


def show_list_restaurants(restaurants:list):
    """
    Exibe uma lista de restaurantes cadastrados.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    
    """
    if len(restaurants) > 0:
        # Imprime o cabeçalho para a lista de restaurantes cadastrados.
        print('\nRestaurantes Cadastrados: ')
        
        # Percorre cada restaurante na lista fornecida.
        for restaurant in restaurants:
            # Imprime os detalhes do restaurante de forma formatada.
            show_restaurant(restaurant)
    
    else:
        print("\nNão há restaurantes cadastrados no sistema")
        
def show_describ_all_restaurants(restaurants: list) -> None:
    """
    Exibe uma descrição detalhada de cada restaurante cadastrado, incluindo os itens do menu.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    """
    if len(restaurants) > 0:
        # Imprime o cabeçalho para a lista de restaurantes cadastrados.
        print('\nRestaurantes Cadastrados: ')
        
        # Percorre cada restaurante na lista fornecida.
        for restaurant in restaurants:
            # Imprime os detalhes do restaurante de forma formatada.
            show_restaurant(restaurant)
            
            # Verifica se o restaurante possui itens no menu.
            if len(restaurant[-1])>0:
                # Imprime o cabeçalho para a lista de produtos disponíveis do restaurante.
                print('Produtos Disponiveis: ')
                
                # Percorre cada item no menu do restaurante.
                for item in restaurant[-1]:
                    # Imprime os detalhes do item de forma formatada.
                    print(f'\n\t| {item[0]} | R${item[1]},00 |')
            else:
                print("\nNão há itens disponiveis no cardapio ainda!")
    else:
        print("\nNão há restaurantes cadastrados no sistema")

def low_time(restaurants:list) -> int:
    """
    Função responsavel por análisar todos os restaurantes disponiveis na plataforma e
    retornar o restaurante com o menor tempo de entrega.
    função retorna -1 caso não encontre.
    
    Parâmetros:
        restaurants::list: Lista contendo todos os restaurantes cadastrados na plataforma.
        
    Retorna:
        id::int: identificação da posição que o restaurante adequada se encontra caso existir
    """
    
    id = -1
    
    if len(restaurants) == 0:
        print("\nNão há restaurantes cadastrados na plataforma")
        
    elif len(restaurants) == 1:
        id+=1
    
    else:
        
        maior = int(restaurants[0][4])
    
        for restaurant in restaurants:
            id+=1
        
            if int(restaurant[4]) > maior:
                maior = int(restaurant[4])
        
    return id