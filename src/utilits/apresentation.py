
def show_restaurant(restaurant:dict) -> None:
    """
    Exibe os dados de um restaurante.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    
    """

    print(f"""-----------------
|Nome    : {restaurant["name"]}
|CNFJ    : {restaurant["cnpj"]}
|Endereço: {restaurant["address"]}
|Telefone: {restaurant["phone"]}
|Entrega : {restaurant["time"]}

""")
    


def show_list_restaurants(restaurants:dict):
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
        for key in restaurants.keys():
            # Imprime os detalhes do restaurante de forma formatada.
            show_restaurant(restaurants[key])
    
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

        print('\nRestaurantes Cadastrados: ')
        
 
        for key in restaurants.keys():

            show_restaurant(restaurants[key])
            
            # Verifica se o restaurante possui itens no menu.
            if len(restaurants[key]["menu"])>0:
                # Imprime o cabeçalho para a lista de produtos disponíveis do restaurante.
                print('Produtos Disponiveis: ')
                
                # Percorre cada item no menu do restaurante.
                for chave in restaurants[key]["menu"]:
                    # Imprime os detalhes do item de forma formatada.
                    print(f'\n\t| {chave} | R${restaurants[key]["menu"][chave]},00 |')
            else:
                print("\nNão há itens disponiveis no cardapio ainda!")
    else:
        print("\nNão há restaurantes cadastrados no sistema")

def low_time(restaurants:dict) -> int:
    """
    Função responsavel por análisar todos os restaurantes disponiveis na plataforma e
    retornar o restaurante com o menor tempo de entrega.
    função retorna -1 caso não encontre.
    
    Parâmetros:
        restaurants::list: Lista contendo todos os restaurantes cadastrados na plataforma.
        
    Retorna:
        id::int: identificação da posição que o restaurante adequada se encontra caso existir
    """
    
    id = ''
    menor = 999999
    
    
    if len(restaurants) == 1:
        id = restaurants.keys()
    elif len(restaurants) > 1:
        for key in restaurants.keys():

            if int(restaurants[key]["time"]) < menor:
                menor = int(restaurants[key]["time"])
                id = key
        
    return id