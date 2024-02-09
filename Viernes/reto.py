# RetoPython #5 - CódigoFacilito
# Autor: Nestor Infante

MESSAGE = "debe tener una longitud mínimo de 5 carácteres y un longitud máxima de 50 \nINTENTA DE VUEVO!\n"
MESSAGE_PHONE = "debe tener una longitud de 10 dígitos \nINTENTA DE VUEVO!\n"
users_list = {}

def main():
  print("\n\t------- BIENVENIDO AL SISTEMA -------\n")
  print("Selecciona una opción:\n")
  print("[1] Registrar nuevos usuarios  \t\t[2] Listar usuarios registrados") 
  print("[3] Ver información de usuario \t\t[4] Modificar usuario")
  print("[5] Eliminar usuario           \t\t[6] Salir")
  task()

def task():
    opc = 0
    try:
        opc = int( input("Opción: ") )
        match opc:
            case 1:
                new_user()
            case 2:
                list_users()
            case 3:
                print("\n\t\t INFORMACIÓN DE USUARIO")
                key = input("Ingresa el ID del usuario a consultar: ")
                show_user(key)
            case 4:
                print("\n\t\t MODIFICAR EL USUARIO")
                key = input("Ingresa el ID del usuario a modificar: ")
                edit_user(key)
            case 5:
                print("\n\t\t ELIMINAR USUARIO")
                key = input("Ingresa el ID del usuario a eliminar: ")
                delete_user(key)
            case 6:
                exit()
            case _:
                print("Lo sentimos, el valor ingresado no es válido (1-6).")
                main()
    except ValueError:
        print("Dato incorrecto.")
        main()


def input_user():
    # Registro de Nombre(s)
    first_name  = input("Nombre(s): ")
    while len(first_name) < 5 or len(first_name) > 50:
        print("El Nombre " + MESSAGE)
        first_name  = input("Nombre(s): ")
            
    # Registro de Apellidos
    last_name   = input("Apellidos: ")
    while len(last_name) < 5 or len(last_name) > 50:
        print("Los Apellidos " + MESSAGE)
        last_name   = input("Apellidos: ")

    # Registro de Teléfono
    phone       = input("Número de teléfono: ")
    while len(phone) != 10:
        print("El número de teléfono " + MESSAGE_PHONE)
        phone       = input("Número de teléfono: ")

    # Registro de Correo electrónico
    email       = input("Correo electrónico: ")
    while len(email) < 5 or len(email) > 50:
        print("El correo electrónico " + MESSAGE)
        email       = input("Correo electrónico: ")

    return first_name, last_name, phone, email


def consult(key):
    print("\nResultado:")
    values = users_list.get(key)
    if values != "" and values != None:
        return values
    else:
        print("No existe la llave ingresada.")


def print_user(key, values):
    if values != "" and values != None:
        print("ID: \t\t\t"              + key)
        print("Nombre(s): \t\t"         + str(values[0]))
        print("Apellidos: \t\t"         + str(values[1]))
        print("Teléfono: \t\t"          + str(values[2]))
        print("Correo electrónico: \t"  + str(values[3]))


def edit_user(key):
    values = consult(key)
    if values != "" and values != None:
        print_user(key, values)    
        print("\n\t\t MODIFICACIÓN")
    
        new_data = input_user()
        users_list[key] = new_data
          
        print("\n¡Actualización completada!")
    
    main()


def show_user(key):
    values = consult(key)
    if values != "" and values != None:
        print_user(key, values) 
    
    main()


def list_users():
    print("\n\t\t LISTADO DE USUARIOS")
    if len(users_list) > 0:
        print("\nUsuarios registrados: ", + len(users_list))
        for key, value in users_list.items():
          print(key, value)
    else:
        print("\nNo hay usuarios registrados!")
    
    main()


def exit():
    print("\n\t\t SALIR DEL SISTEMA")
    print("¡Hasta luego!")


def new_user():
    print("\n\t\t REGISTRO DE USUARIO")
    number_users = 0
    user_id = 1
      
    try:
        number_users = int(input("¿Cuántos nuevos usuarios se pretenden registrar? "))
        if number_users <= 0:
            print("No hay usuarios por registrar")
        else:
            while number_users > 0 and user_id <= number_users:
                val = list(users_list.keys())
                if len(val) > 0:
                    iden = val[-1]
                    id = int(iden)
                    id += 1
                else:
                    id = 1
                # Registro
                print("\n\nPor favor, captura la siguiente información del Usuario #" + str(id))
                
                values = input_user()
                first_name, last_name, phone, email = values

                user_list = {
                "first_name"  : first_name,
                "last_name"   : last_name,
                "phone"       : phone,
                "email"       : email
                }
                
                users_list[str(id)] = list(user_list.values())
                user_id += 1

    except ValueError:
        print("¡LA OPCIÓN QUE INGRESÓ NO ES UN NÚMERO!")
  
    main()
      

def delete_user(key):
    values = consult(key)
    if values != "" and values != None:
        print_user(key, values)
        opc = input("\n¿Seguro que deseas eliminarlo? (s/n): ")
        if opc == "s":
            del users_list[key]      
    
    main()


main()
