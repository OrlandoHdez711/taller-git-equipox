#Equipo Buenas Practicas ¿?

#Trabajar en equipo para crear un proyecto sencillo en Python usando Git y GitHub.
#Aplicar los conceptos básicos de versionamiento, ramas y Pull Requests.

#Definicion de variables

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def potencia(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        print("Error: No se puede dividir entre 0 en el módulo.")
        return None
    return a % b

# Ejecutar operación

def ejecutar_operacion(operacion, a, b):
    operaciones = {
        'suma': suma,
        'resta': resta,
        'potencia': potencia,
        'modulo': modulo
    }

    funcion = operaciones.get(operacion)
    if funcion:
        return funcion(a, b)
    else:
        print(f"Operación '{operacion}' no válida.")
        return None

# Función principal

def main():
    print("Calculadora simple (suma, resta, potencia y módulo)")
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor, ingresa solo números válidos.")
        return

    operacion = input("¿Qué operación deseas realizar? (suma, resta, potencia, modulo): ").strip().lower()
    resultado = ejecutar_operacion(operacion, num1, num2)

    if resultado is not None:
        print(f"Resultado: {resultado}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()