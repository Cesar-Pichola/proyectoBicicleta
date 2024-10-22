from operations import operations_users

def menu_users():
    print("********Menu********")
    print("1. obtener usuarios")
    print("2. agregar usurio")
    print("3. Actualizar actualidar")
    print("4. Eliminar usuario")
    print("5. Salir")
    print("********************")
    
    return input("Selecciona una opción: ")

def main_users():
     while True:
        opcion = menu_users()
        
        if opcion == '1':
           operations_users.list_users()
           
        elif opcion == '2':
           name = input("Ingresa el nombre: ")
           lastName = input("Ingresa el Apellido: ")
           email = input("Ingresa el email: ")
           phone = input("Ingresa numero de telefono: ")
           address = input("Ingresa la direccion: ")
           
           operations_users.create_user(name, lastName, email, phone, address)
        
        elif opcion == '3':

           uid = name = input("Ingresa el id del usuario que quiere actualizar: ")
           name = input("Ingresa el nombre: ")
           lastName = input("Ingresa el Apellido: ")
           email = input("Ingresa el email: ")
           phone = input("Ingresa numero de telefono: ")
           address = input("Ingresa la direccion: ")
           
           operations_users.update_user(uid,name, lastName, email, phone, address)
           
        elif opcion == '4':
            uid  = input("Ingresa el id del usuario que quiere Eliminar: ")
            operations_users.delete_user(uid)
           
        elif opcion == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")