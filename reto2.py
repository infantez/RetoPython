# RetoPython #2 - Código facilito
# Autor: Nestor Infante

print("\t REGISTRO DE USUARIO")
MESSAGE = "debe tener una longitud mínimo de 5 carácteres y un longitud máxima de 50 \nINTENTA DE VUEVO!\n"
MESSAGE_PHONE = "debe tener una longitud de 10 dígitos \nINTENTA DE VUEVO!\n"
number_users = 0
cont = 1
users_name, users_email = "", ""

try:
  number_users = int(input("¿Cuántos nuevos usuarios se pretenden registrar? "))
except ValueError:
  print("¡LA OPCIÓN QUE INGRESÓ NO ES UN NÚMERO!")

while number_users > 0 and cont <= number_users:
  # Registro
  print("\n\nPor favor, captura la siguiente información del Usuario #" + str(cont))
  
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

  # Almacenamiento de Nombre(s) + Apellidos y Correo electrónico
  users_name += first_name + " " + last_name + "\n"
  users_email += email + "\n"
  cont += 1

else:
  if number_users <= 0:
    print("No hay usuarios por registrar")

# Mostrar valores
if number_users >= 1:   
  print("\n\n\t BIENVENIDOS")
  print("¡Hola!\n" + users_name)
  print("En breve recibirán un correo a:\n" + users_email)

