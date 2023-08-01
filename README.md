# Actividad_Funciones
Menu con funciones()
def calcular_iva(precio):
    return precio * 0.19
def calcular_descuento(precio, porcentaje_descuento):
    return precio - (precio * porcentaje_descuento / 100)
def calcular_imc(peso, altura):
    return peso / (altura * altura)
while True:
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        try:
            precio = float(input("Ingrese el precio del producto: "))
            iva = calcular_iva(precio)
            print("El IVA es:", iva)
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    elif opcion == "2":
        try:
            precio = float(input("Ingrese el precio del producto: "))
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
            precio_con_descuento = calcular_descuento(precio, porcentaje_descuento)
            print("El precio con descuento es:", precio_con_descuento)
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
    elif opcion == "3":
        try:
            peso = float(input("Ingrese el peso en kg: "))
            altura_cm = float(input("Ingrese la altura en centímetros: "))  # Se ingresa la altura en centímetros
            altura_metros = altura_cm / 100  # Convertir la altura a metros
            imc = calcular_imc(peso, altura_metros)
            print("El IMC es:", imc)
            if imc < 18.5:
                print("Estado: Bajo peso")
            elif 18.5 <= imc < 25:
                print("Estado: Adecuado")
            elif 25 <= imc < 30:
                print("Estado: Sobrepeso")
            elif 30 <= imc < 35:
                print("Estado: Obesidad grado 1")
            elif 35 <= imc < 40:
                print("Estado: Obesidad grado 2")
            else:
                print("Estado: Obesidad grado 3")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
