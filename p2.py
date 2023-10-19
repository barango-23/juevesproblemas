import random
import os

departamentos = []

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def agregar_departamento(nombre, capital):
    departamento = {
        "nombre": nombre,
        "capital": capital
    }
    departamentos.append(departamento)
    limpiar_terminal()

def mostrar_departamentos():
    if not departamentos:
        print("No hay departamentos registrados.")
    else:
        print("\nDepartamentos Registrados:")
        for departamento in departamentos:
            print(f"{departamento['nombre'].upper()} - Capital: {departamento['capital'].upper()}")
        print()

def jugar():
    if not departamentos:
        print("No hay departamentos registrados para jugar.")
        return

    while True:
        departamento_aleatorio = random.choice(departamentos)
        nombre_departamento = departamento_aleatorio["nombre"]
        capital_correcta = departamento_aleatorio["capital"]

        print(f"\n¡ Adivina la capital de {nombre_departamento} !")

        intentos = 0
        while intentos < 3:
            intentos += 1
            capital_usuario = input("Ingresa la capital: ").upper()

            if capital_usuario == capital_correcta:
                print(f"\n¡ Correcto ! La capital de {nombre_departamento} es >>> {capital_correcta} :)")
                break
            else:
                print("\nintentalo de nuevo >:c")

        if intentos == 3:
            print(f"\nLo siento, has agotado tus intentos. La capital correcta era {capital_correcta} , Hasta luego..")

        jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (S/N): ").upper()
        if jugar_nuevamente != 'S':
            break

    limpiar_terminal()

while True:
    print("="*50)
    print("{:^50}".format(">>>>>Menu de opciones<<<<<"))
    print("="*50)
    print("{:<50}".format("1. Agrega un Departamento 🌇"))
    print("{:<50}".format("2. Consultar los Departamentos 📑"))
    print("{:<50}".format("3. jugar el juego de las adivinanzas 👀"))
    print("{:<50}".format("4. Salir"))
    
    print("="*50)

    opcion = input("\nSeleccione una opción: ").upper()
    print("↧"*20)
    if opcion == "1":
        nombre = input("\nIngrese el Departamento: ").upper()
        capital = input("Ingrese la Capital del Departamento: ").upper()
        agregar_departamento(nombre, capital)
    
    elif opcion == "2":
        mostrar_departamentos()
    
    elif opcion == "3":
        jugar()
    
    elif opcion == "4":
        salir = input("\n¿Desea salir? (S/N): ").upper()
        if salir == 'S':
            break
    
    else:
        print("\nOpción inválida. Por favor, seleccione una opción válida.\n")
