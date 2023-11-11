import json
import os
if os.path.exists("restaurants.json"):

    with open("restaurants.json",'r') as arquivo:
        data = json.load(arquivo)
        
    print(data)
    
else:
    
    with open("restaurants.json",'w') as arquivo:
        json.dump({},arquivo)