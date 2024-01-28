#FUNCIONES
#Para definir una funcion:
#En Python, una función es un bloque de código que realiza una tarea específica cuando es llamada. Sirve para encapsular una pieza de lógica o tarea repetitiva, permitiendo reutilizar ese código en diferentes partes de un programa.

def my_function ():
    print("Esto es una función")
my_function()
my_function()
my_function()


def sum_two_values (first_number, second_number):
    print(first_number + second_number)
sum_two_values(5, 7)

def sum_two_values_with_return (first_number, second_number):
    return first_number, second_number
my_result = sum_two_values(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name}, {surname}")
print_name(surname = "Vintila", name = "Bogdan")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Bogdan", "Vintila")
print_name_with_default("Bogdan", "Vintila", "Boxan")
print_name_with_default("name", "surname",)


def print_texts (*text):
    print(type(text))
    print(text)
print_texts("Hola", "Bogdan", "George")



