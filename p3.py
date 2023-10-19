carros = []

agregar_carro = lambda marca, modelo, año, placa: carros.append({
    "marca": marca,
    "modelo": modelo,
    "año": año,
    "placa": placa
})

mostrar_carros = lambda: [print(f"{key}: {value}") for carro in carros for key, value in carro.items()]

actualizar_informacion = lambda opcion: {
    "1": lambda: input("Ingrese la nueva marca: "),
    "2": lambda: input("Ingrese el nuevo modelo: "),
    "3": lambda: int(input("Ingrese el nuevo año: ")),
    "4": lambda: input("Ingrese la nueva placa: ")
}[opcion]()

con_carros = 0

while True:
    print("=" * 20)
    print("Menu:")
    print("1. Agregar Carro")
    print("2. Consultar Carros")
    print("3. Actualizar Información de Carro")
    print("0. Salir")
    print("=" * 20)
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca del carro: ")
        modelo = input("Ingrese el modelo del carro: ")
        año = int(input("Ingrese el año del carro: "))
        placa = input("Ingrese la placa del carro: ")
        
        agregar_carro(marca, modelo, año, placa)
        
        print("-" * 30)
        mostrar_carros()
        
    elif opcion == "2":
        if carros:
            print("Lista de Carros:")
            mostrar_carros()
        else:
            print("No hay carros registrados.")
            
    elif opcion == "3":
        if carros:
            mostrar_carros()
            indice = int(input("Ingrese el número de carro que desea actualizar: "))
            if 0 < indice <= len(carros):
                nuevo_valor = actualizar_informacion(opcion)
                campo_actualizado = list(carros[indice - 1].keys())[int(opcion) - 1]
                carros[indice - 1][campo_actualizado] = nuevo_valor
                print(f"Información actualizada exitosamente para el campo '{campo_actualizado}'.")
            else:
                print("Número de carro inválido.")
        else:
            print("No hay carros registrados.")

    elif opcion == "0":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        
    con_carros += 1

print("Número de carros registrados:", con_carros)
