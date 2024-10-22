import json
import os

DB_FILE = os.path.join('data', 'bicycles_data.json')
DB_FILE_maintenance = os.path.join('data', 'bicycles_maintenance.json')
DB_FILE_ALERT = os.path.join('data', 'alerts_data.json')


""" bicicleta """
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

""" mantenimiento """
def read_data_maintenance():
    if not os.path.exists(DB_FILE_maintenance):
        return {}
    with open(DB_FILE_maintenance, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}
        
def write_data_maintenance(data):
    with open(DB_FILE_maintenance, 'w') as file:
        json.dump(data, file, indent=4)

""" alertas """

def read_data_alert():
    if not os.path.exists(DB_FILE_ALERT):
        return {}
    with open(DB_FILE_ALERT, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}
        
def write_data_alert(data):
    with open(DB_FILE_ALERT, 'w') as file:
        json.dump(data, file, indent=4)

"""****** Prodecures********** """

def get_alerts():
    return read_data_alert()

def get_bicycle_maintenance():
    return read_data_maintenance()
  
def get_enabled_bicycles():
    data = read_data()   
    filtered_bicycles = []  
    
    for bike in data:
        if bike['busyIdUser'] is None:
            filtered_bicycles.append(bike) 
    
    return filtered_bicycles

def get_disabled_bicycles():
    data = read_data()   
    filtered_bicycles = []  
    
    for bike in data:
        if bike['busyIdUser'] is not None:
            filtered_bicycles.append(bike) 
    
    return filtered_bicycles

def add_bicycle(item_data):
    data = read_data()
    data.append(item_data) 
    write_data(data) 

def update_bicycle(item_id, item_data):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(item_id):
            data[index].update(item_data)
            write_data(data)
            return True
        return False
    
def delete_bicycle(item_id):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(item_id):
            del data[index] 
            write_data(data)
            return True
        return False

def get_bicycle(item_id):
    """Obtiene un objeto por su item_id."""
    data = read_data()  

    for item in data:
        if str(item["id"]) == str(item_id):
            return item
    
    print(f"Item con ID {item_id} no encontrado.")
    return False

def request_bicycle(idUser, idBicycle):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(idBicycle):
            item["busyIdUser"] = idUser
            data[index].update(item)
            write_data(data)
            return True
        return False
    
def return_bicycle(idBicycle):
    data = read_data()
    for index, item in enumerate(data):
         
        if str(item["id"]) == str(idBicycle):
            item["busyIdUser"] = None
            data[index].update(item)
            write_data(data)
            return True
        return False

def add_maintenance(item_data):
    data = read_data_maintenance()
    data.append(item_data) 
    write_data_maintenance(data)
    
def add_alert(item_data):
    data = read_data_alert()
    data.append(item_data) 
    write_data_alert(data) 