#import sys
#sys.path.append(r"../")
from src.utils.menu import *
from src.management.insert import *
from src.management.search import *
from src.management.remove import *
from src.management.edit import *
from src.utils.presentation import *
import json
import os

FILE_NAME = "restaurants.json"

"""
r para leitura (read)
w para escrita (write)
a para adicionar (append)
"""
#   mode = ['r','w','a']

if os.path.exists(FILE_NAME):

    with open(FILE_NAME,'r') as arquivo:
        restaurants = json.load(arquivo)
        
else: 
    restaurants = {}


"""
estrutura do json
{"cnpf": 1, "name":"IFOOD", "address": "Rua qualquer","phone": "1234512", "time": 30, "menu": {}}
"""

opc = '' 

while opc != '0':
    
    opc = interface()
    
    match opc:
        
        case "-1":
            print('\nOpção invalida!\n')
        
        case '11':
            if (add_restaurant(restaurants)):
                print("\nRestaurante adicionado com sucesso!")  
            else:
                print("\nFalha ao Cadastrar o restaurante.")
    
        case '12':
            key = input('\nCNPJ do restaurante:  ')
            
            if search_restaurant(restaurants, key):
                modify_restaurant(restaurants, key)
                print("\nRestaurante editado com sucesso!") 
            else:
                print("\nRestaurante não encontrado!")

        case '13':  
            key = input('\nCNPJ do restaurante:  ')
            if search_restaurant(restaurants, key):
                remove_restaurant(restaurants, key)
                print("\nRestaurante removido.") 
            else:
                print("\nRestaurante não encontrado!")
    
        case '21':
            
            if len(restaurants) > 0:
                key = input('\nCNPJ do restaurante:  ')
                id = search_restaurant(restaurants,key)
                if(id):
                    if(add_item(restaurants,key)):
                        print("\nCadastrado com sucesso")
                    else: 
                        print("\nFalha ao Cadastrar um novo item.")
            else:
                print("\nAinda não há restaurantes cadastrados na plataforma")
        
        case '22':
            if len(restaurants) > 0:
                key = input('\nCNPJ do restaurante:  ')
                id = search_restaurant(restaurants,key)
                if(id):
                    product_name = input("\nNome do Produto: ")
                    valor = input("\nNovo valor para o produto: ")
                    if(edit_item(restaurants, key, product_name, valor)): 
                        print("\nOperação Realizada com sucesso!")
                    else: print("\nFalha ao editar item")
            else:
                print("\nAinda não há restaurantes cadastrados na plataforma")
                
        case '23':
            if len(restaurants) > 0:
                key = input('\nCNPJ do restaurante:  ')
                id = search_restaurant(restaurants,key)
                if(id):
                    product_name = input("\nNome do Produto: ")
                    if(remove_item(restaurants, key, product_name)): 
                        print("\nOperação Realizada com sucesso!")
                    else: print("\nFalha ao remover item")
            else:
                print("\nAinda não há restaurantes cadastrados na plataforma")     
                
        case '31':
            show_restaurants_list(restaurants)
    
        case '32':
            show_complete_info(restaurants)
    
        case '33':
            key = shortest_delivery_time(restaurants)
            if key != '':
                show_restaurant(restaurants[key])
            else:
                print("\nAinda não há restaurantes cadastrados no sistema")

# Mensagem exibida ao encerrar o sistema.         
print('\nSistema encerrado!')


with open(FILE_NAME, 'w') as arquivo:
    json.dump(restaurants, arquivo, indent=4)