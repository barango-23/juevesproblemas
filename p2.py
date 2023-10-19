import random

departamentos = []

def agregar_departamento(nombre, capital):
    departamento = {
        "nombre": nombre,
        "capital": capital
    }
    departamentos.append(departamento)

def mostrar_departamentos():
    if not departamentos:
        print("No hay departamentos registrados.")
    else:
        print("Departamentos Registrados:")
        for departamento in departamentos:
            print(f"{departamento['nombre'].upper()} - Capital: {departamento['capital'].upper()}")
        print()

def jugar():
    if not departamentos:
        print("No hay departamentos registrados para jugar.")
        return

    departamento_aleatorio = random.choice(departamentos)
    nombre_departamento = departamento_aleatorio["nombre"]
    capital_correcta = departamento_aleatorio["capital"]

    print(f"\n¡Adivina la capital de {nombre_departamento}!")

    intentos = 0
    while intentos < 3:
        intentos += 1
        capital_usuario = input("Ingresa la capital: ").upper()

        if capital_usuario == capital_correcta:
            print(f"Correcto la capital de {nombre_departamento} es >>> {capital_correcta}.")
            break
        else:
            print("Incorrecto. ¡Inténtalo de nuevo!")

    if intentos == 3:
        print("Hasta luego, sigue intentando en otra oportunidad.")

while True:
    print("Menu de opciones:")
    print("1. Agregar Departamento")
    print("2. Consultar Departamentos")
    print("3. Jugar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").upper()
    
    if opcion == "1":
        nombre = input("Ingrese el Departamento: ").upper()
        capital = input("Ingrese la Capital del Departamento: ").upper()
        agregar_departamento(nombre, capital)
    
    elif opcion == "2":
        mostrar_departamentos()
    
    elif opcion == "3":
        jugar()
    
    elif opcion == "4" or opcion.upper() == "SALIR":
        print("Gracias por usar el sistema.")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")

