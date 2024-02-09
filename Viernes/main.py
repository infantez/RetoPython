# Funciones
# def = definition   
# Argumentos = Datos de entrada para una función
# Parámetros = Variables

def print_numbers():
    for number in range(1, 11):
        print(number)

print_numbers()

# Separar cada función por dos espacios en blanco PEP8
# Tratar de que las funciones realicen una sola tarea

def suma(number1, number2):
    # Puede retornar más de un valor en una tupla (inmutable)
    return number1 + number2


def resta(number1, number2):
    return number1 - number2


def multiplicacion(number1, number2):
    return number1 * number2


result = suma(50, 67)
print(result)

scores = []

for option in range(0, 5):
    score = int( input("Ingresa una calificación: ") )
    scores.append(score)

print(scores)

suma = 0
for score in scores:
    suma += score

average = suma /  len(scores)
print(average)

# Función sum de Python
average2 = sum(scores) / len(scores)
print(average2)

match average2:
    case 10:
        print("Muchas felicidades aprobaste la materia.")
    case 9 | 8:
        print("Aprobaste la materia.")
    case 7:
        print("Aprobaste la materia pero necesitas practicar más.")
    case _:
        print("Lo sentimos, no aprobaste la materia.")


def set_scores():
    scores = []

    for option in range(0, 5):
        score = int( input("Ingresa una calificación: ") )
        scores.append(score)
    
    return scores


def average(numbers):
    return sum(numbers) / len(numbers)


def show_message(average):

    match average:
        case 10:
            print("Muchas felicidades aprobaste la materia.")
        case 9 | 8:
            print("Aprobaste la materia.")
        case 7:
            print("Aprobaste la materia pero necesitas practicar más.")
        case _:
            print("Lo sentimos, no aprobaste la materia.")

    print(average)
'''
scores = set_scores()
avg = average(scores)
show_message(avg)
'''

show_message ( average( set_scores() ) )
