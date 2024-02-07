# Listas = Estructura de datos.

my_list = [1, 3.4, "String", True, [2, 3.111, "Example", False]]
print(my_list)
print(len(my_list))
print(type(my_list))

numbers = [1, 2, 3, 4, 5]

# Índices     0         1         2       3           4           5       6
#            -7        -6        -5      -4          -3          -2      -1
courses = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Rust", "C#"] # 7 - 1 = último índice
print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[4])

last_index = len(courses) - 1
print(last_index)

index = int( input("Ingresa index: ") )
if index <= last_index:
  print( courses[index] )
else:
  print("Lo sentimos, el índice NO es válido.")

new_list = courses[0:5]
print(new_list)

new_list2 = courses[3:]
print(new_list2)

new_list3 = courses[:3]
print(new_list3)

# Copiar todos los elementos de la lista original
new_list_all = courses[:]
print(new_list_all)

# Saltos en las listas
# new_list_s = courses[start:stop:skips]
new_list_s = courses[::2]
print(new_list_s)

# Invertir la lista
new_list_i = courses[::-1]
print(new_list_i)

# Modificar valores del listado
courses[0] = "CódigoFacilito"
courses[1] = "Django 3.14"
print(courses[0])
print(courses)

# Métodos comúnes de un listado
# append, insert, extend, remove, clear, count, index
# value in list -> True / False

courses.append("JavaScript")
courses.append("TypeScript")
courses.append("Swift")

courses.insert(1, "SQLServer")

new_courses = ["Java9", "Docker", "Unix"]
'''
courses.append( new_courses[0] )
courses.append( new_courses[1] )
courses.append( new_courses[2] )
'''

courses.extend( new_courses )

courses.remove( "CódigoFacilito" )
courses.remove( "Flask" )
courses.remove( "C#" )

print(courses)
print( courses[-1] )

# Conocer cuántas veces se encuentra el elemento en el listado
print( courses.count("Rust") )
print( "Ruby" in courses )
print( "Laravel" in courses )
print( courses.count("Laravel") >= 1 )

print( courses.index("Ruby") )
value = "Laravel"

if value in courses:
  print("El índice es: " + str( courses.index(value) ))
else:
  print("Lo sentimos, el valor NO existe dentro del listado.")

courses.clear()
print(courses)
print( len(courses) )

courses = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Rust", "C#"]
for index, course in enumerate(courses):
  print("El valor para el índice", index, "es", course)

for index, character in enumerate("Hola mundo"):
  print(index, character)

print("Hola mundo"[0])
print("Hola mundo"[-1])

# Listado = mutable (incrementar / decrementar)
# Strings = inmutables (no se pueden modificar su valores originales)

message = "Hola mundo"
new_message = "P" + message[1:]
print( new_message )

