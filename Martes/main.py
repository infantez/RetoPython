# Estructuras de control
# if, match (switch), foreach, while

# Bool
# True / False
# Operadores relacionales (==, !=, >, >=, <, <=)
# Operadores lógicos (and, or, not)

result = False
print(result)

number1 = 10
number2 = 20

result = number1 == number2
print(result)
result = number1 != number2
print(result)
result = number1 > number2
print(result)
result = number1 >= number2
print(result)
result = number1 < number2
print(result)
result = number1 <= number2
print(result)

#   and = Todas las comparaciones deben ser verdaderas para que el resultado final sea: True
#             True              True         True
result = number1 < number2 and 10 == 10 and 5 == 5 and True and True and True # True
print(result)

#   or = Al menos una de las comparaciones debe ser verdadera para que el resultado final sea: True
#            
result = False or False or True
print(result)

# not = Inverso de la variable boleana
# True -> False, False -> True
print(not not not result)

  #       True        True      True
result = True and (True and (not (False and (True or False))))
print(result)

# if = Se ejecuta siempre cuando la condición es verdadero
# else = Cuando la condición no se cumpla

'''
if <condition (True/False)>:
    pass # Palabra reservada para bloque vacío (estandar de 4 espacios)
'''

if True:
  print("La condicón se cumple")
  print("Este bloque solo se ejecuta cuando la condición sea verdadera")

else:
  print("Este bloque se sejecuta cuando la condición NO se cumpla")

age = int(input("Ingresa tu edad: "))

if age >= 0 and age <= 110:

  if age >= 18:
    print("Tienes la edad para votar.")
  else:
    print("Lo sentimos, no puedes votar.")

else:
  print(">>> La edad no es válida, intenta de nuevo (min:0, max:110).")

# Semáforo
# if (elif)
color = input("Ingresa el color: ")

if color == "green":
  print("Puede continuar")
else:
  if color == "yellow":
    print("Alto parcial")
  else:
    if color == "red":
      print("Alto total")

if color == "green":
  print("Puede continuar")
elif color == "yellow":
  print("Alto parcial")
elif color == "red":
  print("Alto total")
else:
  print("El color no es válido.")

# match (switch)
# switch < 3.10
match color:
  case "red":
    print("Alto total")
  case "yellow":
    print("Alto parcial")
  case "green":
    print("Puedes continuar")
  case _: # else
    print("Lo sentimos, el color no es valido.")

# foreach -> Cuando sepamos cuantas iteraciones se necesitan.
# while -> Cuando NO sepamos cuantas iteraciones se necesitan (Condición).

title = "Estructuras de control"
for caracter in title:
  print(caracter) # Recorre todos los elementos

for number in range(1, 101):
  if not (number % 2 == 0):
    print(number)

# while
'''
while <condition>:
  pass
'''
number = 0

while number < 10:
  print(number)
  number += 1
else:
  print("La condición NO se cumple.")

# Uso correcto del while (se desconoce el número de iteraciones)
# random = 5
# number = 0
# max_attends = 5

attends = 0
random, number, max_attends = 5, 0, 5 # No pasar más de 5 asignaciones de variables de esta forma

while number != random and attends < max_attends:
  number = int(imput("Ingresa un número: "))
  attends += 1
else:
  if number == random:
    print("Felicidades! encontras el número correcto")
  else:
    print("Lo sentimos, NO encontraste el número correcto")