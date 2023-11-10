from src.utilits.menu import *
from src.management.insert import *
from src.management.search import *
from src.management.remove import *
from src.management.edit import *
from src.utilits.apresentation import *
import json
import os


if os.path.exists("restaurants.json"):

    with open("restaurants.json",'r') as arquivo:
        data = json.load(arquivo)
        
    print(data)
    
else:
    #empty_dict = {}
    with open("restaurants.json",'w') as arquivo:
        json.dump(None, arquivo)

restaurants = []

#restaurants = {"cpnj": [nome, endereço, telefone, tempo medio de entrega]}

#pessoas = {cpf: [nome, endereço, telefone, nascimento, conta bancaria]}

opc = '' 
id = '' 

while opc != '0':
    
    opc = interface()

    if opc == '-1':
        
        print('\nOpção invalida!\n')
    
    
    elif opc == '11':
        add_restaurant(restaurants)
    
    elif opc == '12':
        modify_restaurant(restaurants)

        
    elif opc == '13':
        remove_restaurant(restaurants)
    
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