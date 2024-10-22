from operations import operations_bicycles

def menu_users():
    print("********Menu********")
    print("1. obtener bicicletas disponibles")
    print("2. obtener bicicletas ocupadas")
    print("3. agregar bicicleta")
    print("4. Actualizar bicicleta")
    print("5. Eliminar usuario")
    print("6. Solicitar bicicleta")
    print("7. devolver bicicleta")
    print("8. Solicitud de mantenimientos")
    print("9. Agregar mantenimiento")
    print("10. Salir")
    print("********************")
    
    return input("Selecciona una opción: ")

def main_bicicles():
     while True:
        opcion = menu_users()
        
        if opcion == '1':
           operations_bicycles.list_enabled_bicycles()
        
        elif opcion == '2':
           operations_bicycles.list_disabled_bicycles()
           
        elif opcion == '3':
           brand = input("Ingresa la marca: ")
           model = input("Ingresa el model: ")
           type_ = input("Ingresa el tipo: ")
           color = input("Ingresa el color: ")
           
           operations_bicycles.create_bicycle(brand, model, type_, color)
        
        elif opcion == '4':

           id = name = input("Ingresa el id de la bicicleta que quiere actualizar: ")
           brand = input("Ingresa la marca: ")
           model = input("Ingresa el model: ")
           type_ = input("Ingresa el tipo: ")
           color = input("Ingresa el color: ")
           
           operations_bicycles.update_bicycle(id,brand, model, type_, color)
           
        elif opcion == '5':
            id  = input("Ingresa el id de la bicicleta que quiere Eliminar: ")
            operations_bicycles.delete_bicycle(id)
            
        elif opcion == '6':
            idUser  = input("Ingresa el id del usuario: ")
            idBicycle  = input("Ingresa el id de la bicicleta: ")
            operations_bicycles.request_bicycle(idUser, idBicycle)
        
        elif opcion == '7':
            id  = input("Ingresa el id de la bicicleta ")
           
            operations_bicycles.return_bicycle(id)
            
        elif opcion == '8':
           
            operations_bicycles.get_bicycle_maintenance()
        
        elif opcion == '9':
            type_  = input("Ingresa el tipo de mantenimiento: ")
            description  = input("Ingresa la descripcion: ")
            operations_bicycles.add_maintenance(type_, description)
            
        elif opcion == '10':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")