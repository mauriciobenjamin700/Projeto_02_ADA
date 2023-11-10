from search import *

def modify_restaurant(restaurants:list) -> None:
    """
    Função para modificar informações de um restaurante existente.
    O usuário pode escolher qual campo deseja alterar.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """
    # Procurando o restaurante a ser modificado
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado
    if id != -1:
        # Solicitando ao usuário qual campo deseja modificar
        opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - CNPJ\n\t3 - Endereço\n\t4 - Telefone\n\t5 - Tempo médio de entrega\n\nSua escolha: ')
        
        # Verificando se a opção inserida é um número e está no intervalo correto
        if opc.isnumeric():
            opc = int(opc)
            
            if opc > 0 and opc < 6:
                # Solicitando ao usuário o novo valor para o campo escolhido
                data = input('\nInfome o novo valor para o respectivo campo: ')
                restaurants[id][opc-1] = data
                print("\nValor atualizado com sucesso!")
            else:
                print("\nOpção escolhida é invalida!")
        
        else:
            print("\nOpção Invalida, insira apenas números!")        
    else:
        print("\nRestaurante não encontrado!")


def edit_item(restaurants: list, id: int) -> None:
    """
    Função para editar informações de um item em um restaurante específico.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        id::int: identificação do restaurante, sendo ela a posição que o mesmo se encontra na lista
    
    return:
        None
    """
    # Procura o índice do item que será editado
    idx = search_item(restaurants, id)
    
    # Se o item for encontrado
    if idx != -1:
        # Solicita ao usuário qual campo do item deseja alterar
        opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - Preço\n\nSua escolha: ')
        
        # Verifica se a entrada é numérica e se está no intervalo correto
        if opc.isnumeric():
            opc = int(opc)
            if opc > 0  and opc < 3:
                # Solicita ao usuário o novo valor para o campo escolhido
                data = input('\nInfome o novo valor para o respectivo campo: ')
                # Atualiza o valor do campo escolhido no item
                restaurants[id][-1][idx][opc-1] = data
            else:
                print("\nOpção escolhida é invalida")
        else:
            print("\nInforme um valor númerico!")
                
    else:
        print("\nRestaurante não encontrado!")
        