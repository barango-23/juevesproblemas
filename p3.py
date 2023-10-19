# Calculadora con funciones lambda
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: División por cero"

while True:
    print("=" * 30)
    print("Calculadora Matemática")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=" * 30)

    opcion = input("Seleccione una opción (1-5): ")

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", division(num1, num2))
    elif opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
