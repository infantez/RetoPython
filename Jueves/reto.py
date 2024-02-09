# RetoPython #4 - CódigoFacilito
# Autor: Nestor Infante

MESSAGE = "debe tener una longitud mínimo de 5 carácteres y un longitud máxima de 50 \nINTENTA DE VUEVO!\n"
MESSAGE_PHONE = "debe tener una longitud de 10 dígitos \nINTENTA DE VUEVO!\n"
users_list = {}

def menu():
  print("\n\t------- BIENVENIDO AL SISTEMA -------\n")
  print("Selecciona una opción:\n")
  print("[1] Registrar nuevos usuarios \t\t[2] Listar usuarios registrados \n[3] Ver información de usuario \t\t[4] Modificar usuario \n[5] Salir")
  opc = 0
  try:
    opc = int(input("Opción: "))
    task(opc)
  except ValueError:
    print("Dato incorrecto.")
    menu()

def task(opc):
  match opc:
    case 1:
      print("\n\t\t REGISTRO DE USUARIO")
      number_users = 0
      user_id = 1
      
      try:
        number_users = int(input("¿Cuántos nuevos usuarios se pretenden registrar? "))
      except ValueError:
        print("¡LA OPCIÓN QUE INGRESÓ NO ES UN NÚMERO!")

      while number_users > 0 and user_id <= number_users:
        # Registro
        print("\n\nPor favor, captura la siguiente información del Usuario #" + str(len(users_list)+1))
          
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

        user_list = {
          "first_name"  : first_name,
          "last_name"   : last_name,
          "phone"       : phone,
          "email"       : email
        }
          
        users_list[str(len(users_list)+1)] = list(user_list.values())
        user_id += 1

      else:
        if number_users <= 0:
          print("No hay usuarios por registrar")
        
      menu()
    case 2:
      print("\n\t\t LISTADO DE USUARIOS")
      if len(users_list) > 0:
        print("\nUsuarios registrados: ", + len(users_list))
        for key, value in users_list.items():
          print(key, value)
      else:
        print("\nNo hay usuarios registrados!")
      menu()
    case 3:
      print("\n\t\t INFORMACIÓN DE USUARIO")
      try:
        key = input("Ingresa el ID del usuario a consultar: ")
        print("\nResultado:")
        values = users_list.get(key, "No existe la llave ingresada.")
        if values != "No existe la llave ingresada." and values != "":
          print("ID: \t\t\t"              + key)
          print("Nombre(s): \t\t"         + str(values[0]))
          print("Apellidos: \t\t"         + str(values[1]))
          print("Teléfono: \t\t"          + str(values[2]))
          print("Correo electrónico: \t"  + str(values[3]))
        else:
          print("No existe la llave ingresada.")
      except ValueError:
        print("Dato incorrecto.")
        menu()
      menu()
    case 4:
      print("\n\t\t MODIFICAR EL USUARIO")
      try:
        key = input("Ingresa el ID del usuario a modificar: ")
        print("\nResultado:")
        values = users_list.get(key, "No existe la llave ingresada.")
        if values != "No existe la llave ingresada." and values != "":
          print("ID: \t\t\t"              + key)
          print("Nombre(s): \t\t"         + str(values[0]))
          print("Apellidos: \t\t"         + str(values[1]))
          print("Teléfono: \t\t"          + str(values[2]))
          print("Correo electrónico: \t"  + str(values[3]))

          print("\n\t\t MODIFICACIÓN")
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

          new_data = [first_name, last_name, phone, email]
          users_list[key] = new_data
          
          print("\n¡Actualización completada!")
        else:
          print("No existe la llave ingresada.")
      except ValueError:
        print("Dato incorrecto.")
        menu()
      menu()
    case 5:
      print("\n\t\t SALIR DEL SISTEMA")
      print("¡Hasta luego!")
    case _:
      print("Lo sentimos, el valor ingresado no es válido (1-5).")
      menu()

menu()
    