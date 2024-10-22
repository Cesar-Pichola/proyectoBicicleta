import random
from db_handler import db_handler_users


def list_users():
    """Lista todos los elementos."""
    items = db_handler_users.get_all_items()
    print("***********Usuarios***********")
    if items:
        for item in items:
            print(f"id: {item['id']} Nombre: {item['name']} ")
            print(f"      Apellido:{item['lastName']}")
            print(f"      Telefono:{item['phone']}")
            print(f"      Direccion:{item['address']}")
            print(f"      E-mail:{item['email']} \n")

        
    else:
        print("No hay elementos.")
        
def create_user(name, lastName, email, phone, address):
    new_id = random.randint(1, 10000)
        
    db_handler_users.add_user({
      "id": str(new_id),
      "name": name,
      "lastName": lastName,
      "email": email,
      "phone": phone,
      "address": address

    },)
    print(f"Item creado con éxito.{new_id}")

def update_user(uid,name, lastName, email, phone, address):
    item = db_handler_users.get_user(uid)
    if item != False:
        if name:
            item['name'] = name
        if lastName:
            item['lastName'] = lastName
        if lastName:
            item['email'] = email
        if lastName:
            item['phone'] = phone
        if lastName:
            item['address'] = address
            
            
        if db_handler_users.update_user(uid, item):
            print(f"Item {uid} actualizado.")
        else:
            print(f"Error al actualizar el item {uid}.")
            
def delete_user(uid):
    item = db_handler_users.get_user(uid)
    print(item)
    if item != False:
      db_handler_users.delete_user(uid)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

""" def create_item(item_id, name, description):
    item_data = {
        "name": name,
        "description": description
    }
    db_handler.add_item(item_id, item_data)
    print(f"Item {item_id} creado con éxito.") """

""" def read_item(item_id):
    item = db_handler.get_item(item_id)
    if item:
        print(f"Item {item_id}: {item}")
    else:
        print(f"Item {item_id} no encontrado.") """

""" def update_item(item_id, name=None, description=None):
    item = db_handler.get_item(item_id)
    if item:
        if name:
            item['name'] = name
        if description:
            item['description'] = description
        if db_handler.update_item(item_id, item):
            print(f"Item {item_id} actualizado.")
        else:
            print(f"Error al actualizar el item {item_id}.")
    else:
        print(f"Item {item_id} no encontrado.") """

""" def delete_item(item_id):
    if db_handler.delete_item(item_id):
        print(f"Item {item_id} eliminado.")
    else:
        print(f"Item {item_id} no encontrado.") """

