import sys
sys.path.append(r"../")

from src.utilits.menu import *
from src.management.insert import *
from src.management.search import *
from src.management.remove import *
from src.management.edit import *
from src.utilits.apresentation import *
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
{"cnpf": 1, "name":"IFOOD", "address": "Rua qualquer","phone": "1234512", "time": 30, "menu": []}
"""

opc = '' 
id = '' 
aux = ''

while opc != '0':
    
    opc = interface()

    if opc == '-1':
        
        print('\nOpção invalida!\n')
        
    elif opc == '11':
        if (add_restaurant(restaurants)):
            print("Restaurante adicionado com sucesso!")
            
        else:
            print("Falha ao Cadastrar o restaurante")
    
    elif opc == '12':
        key = input('\nCNPJ do restaurante:  ')
        
        if search_restaurant(restaurants, key):
            modify_restaurant(restaurants, key)
        else:
            print("\nRestaurante não encontrado!")

        
    elif opc == '13':
        key = input('\nCNPJ do restaurante:  ')
        if search_restaurant(restaurants, key):
            remove_restaurant(restaurants, key)
        else:
            print("\nRestaurante não encontrado!")
    
    elif opc == '21':
        if len(restaurants) > 0:
            add_item(restaurants)
        else:
            print("\nAinda não há restaurantes cadastrados na plataforma")
    
        
    elif opc == '22':
        
        if len(restaurants) > 0:
            id = search_restaurant(restaurants)
            edit_item(restaurants, id)
        else:
            print("\nAinda não há restaurantes cadastrados na plataforma")
            
    
    elif opc == '23':
        
        if len(restaurants) > 0:
            id = search_restaurant(restaurants)

            remove_item(restaurants, id)
        else:
            print("\nAinda não há restaurantes cadastrados na plataforma")
    
    elif opc == '31':
        show_list_restaurants(restaurants)
    
    elif opc == '32':
        show_describ_all_restaurants(restaurants)
    
    elif opc == '33':
        id = low_time(restaurants)
        if id >= 0:
            show_restaurant(restaurants[id])
        else:
            print("\nAinda não há restaurantes cadastrados no sistema")

# Mensagem exibida ao encerrar o sistema.         
print('\nSistema encerrado!')


with open(FILE_NAME, 'w') as arquivo:
    json.dump(restaurants, arquivo, indent=4)