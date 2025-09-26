#Equipo Buenas Practicas ¿?

#Trabajar en equipo para crear un proyecto sencillo en Python usando Git y GitHub.
#Aplicar los conceptos básicos de versionamiento, ramas y Pull Requests.

#Definicion de variables
# Definición de variables

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


def ejecutar_operacion(operacion, a, b):
    operaciones = {
        'suma': suma,
    }

    funcion = operaciones.get(operacion)
    if funcion:
        return funcion(a, b)
    else:
        print(f"Operación '{operacion}' no válida.")
        return None


def main():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor, ingresa solo números válidos.")
        return


    resultado = ejecutar_operacion(operacion, num1, num2)


    if resultado is not None:
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()