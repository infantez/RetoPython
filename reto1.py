'''
#RetoPython - Código facilito
Para este primer reto de la semana, tu objetivo será poder crear un programa en Python 
el cual permita registrar a un usuario en el sistema.

Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

Nombre(s)
Apellidos
Número de teléfono
Correo electrónico.
Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida 
al usuario con el siguiente mensaje:

Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + 
seguido del correo electrónico .
'''
# Registro
print("\t REGISTRO DE USUARIO")
print("Por favor, captura la siguiente información")
first_name  = input("Nombre(s): ")
last_name   = input("Apellidos: ")
phone       = input("Número de teléfono: ")
email       = input("Correo electrónico: ")

full_name = first_name + " " + last_name

# Mostrar valores
print("\t BIENVENIDO")
print("¡Hola! " + full_name + ", en breve recibirás un correo a: " + email)
