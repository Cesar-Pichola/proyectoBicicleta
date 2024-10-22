import random
from db_handler import db_handler_bicycles
from db_handler import db_handler_users



def list_enabled_bicycles():
    items = db_handler_bicycles.get_enabled_bicycles()
    print("***********Bicicletas habilitadas***********")
    if items:
        for item in items:
            print(f"id: {item['id']} Marca: {item['brand']} ")
            print(f"      Modelo:{item['model']}")
            print(f"      tipo:{item['type']}")
            print(f"      color:{item['color']} \n")

        
    else:
        print("No hay elementos.")
        
def list_disabled_bicycles():
    items = db_handler_bicycles.get_disabled_bicycles()
    print("***********Bicicletas ocupadas***********")
    if items:
        for item in items:
            print(f"id: {item['id']} Marca: {item['brand']} ")
            print(f"      Modelo:{item['model']}")
            print(f"      tipo:{item['type']}")
            print(f"      color:{item['color']} \n")

        
    else:
        print("No hay elementos.")
        
def create_bicycle(brand, model, type_, color):
    new_id = random.randint(1, 10000)
        
    db_handler_bicycles.add_bicycle({
        "id": new_id,
        "brand":brand ,
        "model": model,
        "type": type_,
        "color": color,
        "busyIdUser": None
    },)
    print(f"Item creado con éxito.{new_id}")

def update_bicycle(id,brand, model, type_, color):
    item = db_handler_bicycles.get_bicycle(id)
    if item != False:
        if brand:
            item['brand'] = brand
        if model:
            item['model'] = model
        if type_:
            item['type'] = type_
        if color:
            item['color'] = color
            
            
        if db_handler_bicycles.update_bicycle(id, item):
            print(f"Item {id} actualizado.")
        else:
            print(f"Error al actualizar el item {id}.")
            
def delete_bicycle(id):
    item = db_handler_bicycles.get_bicycle(id)
    if item != False:
      db_handler_bicycles.delete_bicycle(id)
      
def request_bicycle(idUser, idBicycle):

    itemUser = db_handler_users.get_user(idUser)  
    itemBicycle = db_handler_bicycles.get_bicycle(idBicycle) 
    
    if itemUser != False and itemBicycle != False: 
        db_handler_bicycles.request_bicycle(idUser,idBicycle )
        
        """ Save Alert """
        db_handler_bicycles.add_alert( {
        "idBicycle": idBicycle,
        "description": "La bicicleta fue entregada"  
    },)
    else:
        print("******************Error***********************")
        print("*Usuario y/o bicicleta no existe, verifique..*") 
        print("**********************************************")
        
def return_bicycle(idBicycle):
    item = db_handler_bicycles.get_bicycle(idBicycle)
    if item != False:
      db_handler_bicycles.return_bicycle(idBicycle)
      db_handler_bicycles.add_alert( {
        "idBicycle": idBicycle,
        "description": "La bicicleta fue devuelta."  
    },)
      
def get_bicycle_maintenance():
    items = db_handler_bicycles.get_bicycle_maintenance()
    
    if items:
        for item in items:
            print(f"id: {item['idBicycle']}")
            print(f"      Typo:{item['Type']}")
            print(f"      Description:{item['description']} \n")

        
    else:
        print("No hay elementos.")
        

def add_maintenance(type_, description):
    new_id = random.randint(1, 10000)
        
    db_handler_bicycles.add_maintenance({
        "idBicycle": new_id,
        "Type": type_,
        "description": description
    },)
    print(f"Item creado con éxito.{new_id}")

