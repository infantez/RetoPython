# Variables
# Tipos de datos

# Nombre_de_la_variable = Valor

first_name = "Nestor Eduardo" # String - "" o ''
last_name = "Infante Zenteno"

print(first_name)
print(last_name)

full_name = first_name + " " + last_name
print(full_name)

# int, float, string, bool

age     = 30
score   = 8.4
active  = True

print(age)
print(score)
print(active)

print(type(full_name))
print(type(age))
print(type(score))
print(type(active))


VERSION = 3.12 # En Python no existen constantes
print(VERSION)

result = input("Ingresa tu nombre: ") # String
print("Se ingresó por teclado: " + result)
print(type(result))

# int - float - str
name    = input("Ingresa tu nombre: ")
age     = int(input("Ingresa tu edad: "))
score   = float(input("Ingresa tu calificación: "))

# Operadores relacionales ( ==, !=, >, >=, <, <= )
active  = input("¿El usuario se encuentra activo? (si/no) ") == "si"

print(name, age, score, active)
print(type(name), type(age), type(score), type(active))

# print - input - int - float - str
print(str(10))
print(type(str(10)))
