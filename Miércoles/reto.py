# RetoPython #3 - Código facilito
# Autor: Nestor Infante

print("\t REGISTRO DE USUARIO")
MESSAGE = "debe tener una longitud mínimo de 5 carácteres y un longitud máxima de 50 \nINTENTA DE VUEVO!\n"
MESSAGE_PHONE = "debe tener una longitud de 10 dígitos \nINTENTA DE VUEVO!\n"
number_users = 0

user_id = 1
users_list = []

try:
  number_users = int(input("¿Cuántos nuevos usuarios se pretenden registrar? "))
except ValueError:
  print("¡LA OPCIÓN QUE INGRESÓ NO ES UN NÚMERO!")

while number_users > 0 and user_id <= number_users:
  # Registro
  print("\n\nPor favor, captura la siguiente información del Usuario #" + str(user_id))
  
  # Registro de Nombre(s)
  first_name  = input("Nombre(s): ")
  while len(first_name) < 5 or len(first_name) > 50:
    print("El Nombre " + MESSAGE)
    first_name  = input("Nombre(s): ")
  
  user_list = []
  user_list.append(user_id)
  user_list.append(first_name)

  # Registro de Apellidos
  last_name   = input("Apellidos: ")
  while len(last_name) < 5 or len(last_name) > 50:
    print("Los Apellidos " + MESSAGE)
    last_name   = input("Apellidos: ")
  
  user_list.append(last_name)

  # Registro de Teléfono
  phone       = input("Número de teléfono: ")
  while len(phone) != 10:
    print("El número de teléfono " + MESSAGE_PHONE)
    phone       = input("Número de teléfono: ")

  user_list.append(phone)

  # Registro de Correo electrónico
  email       = input("Correo electrónico: ")
  while len(email) < 5 or len(email) > 50:
    print("El correo electrónico " + MESSAGE)
    email       = input("Correo electrónico: ")

  user_list.append(email)
  users_list.append( user_list )
  user_id += 1

else:
  if number_users <= 0:
    print("No hay usuarios por registrar")

# Mostrar valores
if len(users_list) > 0:
  print("\n\n\t BIENVENIDOS")
  print("Usuarios registrados: ", + user_id-1)
  print("\n")
  for user in users_list:
    print("ID: " + str(user[0]))
    print("Nombre(s): " + str(user[1]))
    print("Apellidos: " + str(user[2]))
    print("Teléfono: " + str(user[3]))
    print("Correo electrónico: " + str(user[4]))
    print("\n")
