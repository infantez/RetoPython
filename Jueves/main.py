# Tuplas - Diccionarios

# Tuplas = Lista inmutable (no se puede incrementar, eliminar o modificar valores)
# Índices       0         1      2        3            4
settings = ("localhost", 3306, "root", "password", "database")
print(settings)
print( type(settings) )
print( len(settings) )
print( settings[0] )
print( settings[-1] )

# SubTupla
sub_settings = settings[2:]
print(sub_settings)
sub_settings2 = settings[::-1]
print(sub_settings2)

for setting in settings:
  print(setting)

host = settings[0]
port = settings[1]
username = settings[2]
password = settings[3]
name = settings[4]

print(host, port, username, password, name)

# Desempaquetado de Tupla
host2, port2, username2, password2, name2 = settings
print(host2, port2, username2, password2, name2)

host3, port3, _, _, _ = settings
print(host3, port3)

host4, port4, *_ = settings
print(host4, port4)

host5, *_, password5, database5 = settings
print(host5, password5, database5)

tuples = (
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9)
)

for _tuple in tuples:
  print(_tuple)

for _tuple in tuples:
  for number in _tuple:
    print(number)

# Desempaquetado de Tupla
for number1, number2, number3 in tuples:
  print(number1, number2, number3)

# DICCIONARIO = Estructura de datos
# No trabajan con Índices, trabajan con pares, llave, valor
# Llave != String - Llaves = Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)
# Métodos = keys, values, items

user = {
  # llave : valor,
  "name"  : "Cody",
  "age"   : 10,
  "email" : "info@codigofacilito.com",
  "active": True,
  10       : 3.14,
  True    : "Verdadero",
  (1, 2, 3): "Tupla"  
}

print(user)
print( type(user) )

print( user["name"] )
print( user["age"] )
print( user["email"] )
print( user["active"] )

print( user[10] )
print( user[True] )
print( user[(1, 2, 3)] )

if "username" in user:
  print( user["username"] )

if "name" in user:
  print( user["name"] )

# None -> Nada
value = user.get("username", "No existe la llave")
print(value)

value2 = user.get("name", "No existe la llave")
print(value2)

print(
  user.keys(), "\n",
  list( user.keys() ), "\n",
  tuple( user.keys() )
)
print(
  user.values(), "\n",
  list( user.values() ), "\n",
  tuple( user.values() )
)
print(
  user.items(), "\n",
  list( user.items() ), "\n",
  tuple( user.items() )
)

for key, value in tuple ( user.items() ):
  print(key, value)
