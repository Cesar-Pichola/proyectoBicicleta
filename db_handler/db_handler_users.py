import json
import os

DB_FILE = os.path.join('data', 'users_data.json')


def read_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def write_data(data):
    with open(DB_FILE, 'w') as file:
        json.dump(data, file, indent=4)
        
def get_all_items():
    return read_data()

def add_user(item_data):
    data = read_data()
    data.append(item_data) 
    write_data(data) 

def update_user(item_id, item_data):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(item_id):
            data[index].update(item_data)
            write_data(data)
            return True
        return False
    
def delete_user(item_id):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(item_id):
            del data[index] 
            write_data(data)
            return True
        return False

def get_user(item_id):
    """Obtiene un objeto por su item_id."""
    data = read_data()  

    for item in data:
        if str(item["id"]) == str(item_id):
            return item
    
    print(f"Item con ID {item_id} no encontrado.")
    return False
