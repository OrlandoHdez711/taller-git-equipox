#Equipo Buenas Practicas ¿?

#Trabajar en equipo para crear un proyecto sencillo en Python usando Git y GitHub.
#Aplicar los conceptos básicos de versionamiento, ramas y Pull Requests.

#Definicion de variables
# Definición de variables

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir entre cero.")
        return None

# Definición de operaciones

def ejecutar_operacion(operacion, a, b):
    operaciones = {
        'suma': suma,
        'resta': resta,
        'multiplicacion': multiplicacion,
        'division': division
    }

    funcion = operaciones.get(operacion)
    if funcion:
        return funcion(a, b)
    else:
        print(f"Operación '{operacion}' no válida.")
        return None

# Ingreso de números por parte del usuario

def main():
    print("Calculadora simple (suma, resta, multiplicación y división)")
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor, ingresa solo números válidos.")
        return

    # Escoger una operación
    operacion = input("¿Qué operación deseas realizar? (suma/resta/multiplicacion/division): ").strip().lower()
    resultado = ejecutar_operacion(operacion, num1, num2)

    # Muestra el resultado de la operación escogida
    if resultado is not None:
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()