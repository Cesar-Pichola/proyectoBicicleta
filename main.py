import users
import bicycles

def main_menu():
    print("********Menu********")
    print("1. Mantenimiento Usuarios")
    print("2. Mantenimiento bicicletas y/o solicitar bicicleta ")
    print("6. Salir")
    print("********************")
    
    return input("Selecciona una opción: ")

def main():
    while True:
        opcion = main_menu()
        
        if opcion == '1':
           users.main_users()
        
        if opcion == '2':
           bicycles.main_bicicles()
           
           
        elif opcion == '6':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()