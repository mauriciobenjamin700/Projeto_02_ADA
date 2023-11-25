
def show_restaurant(restaurant:dict) -> None:
    """
    Exibe os dados de um restaurante.
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
    
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
    


def show_restaurants_list(restaurants:dict):
    """
    Exibe uma lista de restaurantes cadastrados.
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        
    return:
        None
    
    """
    if len(restaurants) > 0:
        
        print('\nRestaurantes Cadastrados: ')
        
       
        for key in restaurants.keys():
            
            show_restaurant(restaurants[key])
    
    else:
        print("\nNão há restaurantes cadastrados no sistema")
        
def show_complete_info(restaurants: list) -> None:
    """
    Exibe uma descrição detalhada de cada restaurante cadastrado, incluindo os itens do menu.
    
    Parâmetros:
        restaurants::dict: lista de restaurantes
        
    return:
        None
    """
    if len(restaurants) > 0:

        print('\nRestaurantes Cadastrados: ')
        
 
        for key in restaurants.keys():

            show_restaurant(restaurants[key])
            
            
            if len(restaurants[key]["menu"])>0:
                
                print('Produtos Disponiveis: ')
                
                
                for chave in restaurants[key]["menu"]:
                   
                    print(f'\n\t| {chave} | R${restaurants[key]["menu"][chave]},00 |')
            else:
                print("\nNão há itens disponiveis no cardapio ainda!")
    else:
        print("\nNão há restaurantes cadastrados no sistema")

def shortest_delivery_time(restaurants:dict) -> int:
    """
    Função responsavel por análisar todos os restaurantes disponiveis na plataforma e
    retornar o restaurante com o menor tempo de entrega.
    função retorna -1 caso não encontre.
    
    Parâmetros:
        restaurants::dict: Lista contendo todos os restaurantes cadastrados na plataforma.
        
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