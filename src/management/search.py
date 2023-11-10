def search_restaurant(restaurants:list) -> int:
    """
    Função que busca um restaurante pelo nome ou CNPJ.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    Retorna:
        id: int (o índice do restaurante na lista ou -1 se não for encontrado.)
    """
    # Opções para o usuário escolher como quer buscar o restaurante
    opc = input('\nDeseja acessar por:\n\t1 - Nome do Restaurante\n\t2 - CNPJ do restaurante\n\nSua escolha: ')
    key = ''
    cont = 0
    id = -1

    # Obtendo a chave de pesquisa (nome ou CNPJ) com base na escolha do usuário
    if opc == '1':
        key = input('Nome do restaurante: ').upper()
    elif opc == '2':
        key = input('CNPJ do restaurante: ')
    
    # Continuando a busca do restaurante, a função retorna o índice do restaurante
    # ou -1 se não encontrá-lo na lista
    for restaurant in restaurants:
        if restaurant[int(opc)-1] == key:
            id = cont
            return id
        cont += 1
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
