#Ejercios en clases

def varios_valores(*args):
  for arg in args:
    print(arg)

varios_valores(4.5,"Buen dia",[1,2,3,4,5])

def mostrar_valores():
  return("buen dia", 15, [10,20,30])

mostrar_valores()

def resta(a,b):
  return a-b

resta(30,10)

def resta(a,b):
  return a-b

resta(b=30,a=10)

def funcion():
  return "Bienvenidos a Python"
frase=funcion()
print(frase)

def resta(a=None, b=None):
  if a==None or b==None:
    print("Error, faltan parametros a la funcion")
    return
  return a-b
resta()

def resta(a=None, b=None):
  if a is None or b is None:
    print("Error, faltan parametros a la funcion")
    return
  return a - b
while True:
  try:
   a = int(input("Ingrese el valor de 'a': "))
   b = int(input("Ingrese el valor de 'b': "))
   resultado = resta(a,b)
   print("El resultado de la resta es: ", resultado)
   break

  except ValueError:
    print("Error, ingrese valores numericos validos en 'a' y 'b'")

#Calcular_Iva
def calcular_iva(precio):
  return (precio * 1.19 / 100)
resultado_iva = calcular_iva(1000)
print("El IVA al 19% es:", resultado_iva)

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