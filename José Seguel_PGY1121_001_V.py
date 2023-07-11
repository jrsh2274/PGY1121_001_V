import re
rut = -1

#funcion que valida que se ingresen datos cnumericos para las coordenas del arreglo
def validar_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            entero = int(entrada)
            return entero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

#funcion que muestra lalos lotes disponibles
def mostrar_disponibilidad_deptos(deptos):
    print("Departamentos Disponibles:")
    for fila in deptos:
        for lote in fila:
            if lote == 'X':
                print("[X]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

#funcion para desplegar el detalle del depto seleccionado
def mostrar_detalles_deptos(deptos_seleccionados, depto_idx, detalles_deptos):
    depto = deptos_seleccionados[depto_idx]
    numero_depto = depto_idx + 1

    # Obtener los detalles del lote desde la lista de detalles_deptos
    detalles = detalles_deptos[depto_idx]
    tamaño_terreno = detalles['Tipo']
    precio = detalles['precio']

    print("Detalles del Departamento Seleccionado:")
    print("Número de Departamento:", numero_depto)
    print("Tipo:", 'Tipo')
    print("Precio:","$", precio)

# Detalle de deptos disponibles desde una lista
detalles_deptos = [
    {'Tipo': 'A', 'precio': '3.800 UF'},
    {'Tipo': 'B', 'precio': '3.000 UF'},
    {'Tipo': 'C', 'precio': '2.800 UF'},
    {'Tipo': 'D', 'precio': '3.500 UF'}]

deptos_seleccionados = [1, 2, 3, 4]


#funcion para desplegar informacion de los clientes 
def mostrar_clientes(clientes):
    print("Clientes que han comprado un depratamentos:")
    for cliente in clientes:
        print("RUT:", cliente)
  
#funcion para ingresar y validar datos del cliente que selecciono un lote para comprar
def seleccionar_depto(deptos, deptos_seleccionados, clientes, detalles_deptos):
    rut = input("Ingrese su RUT: ")
    while not rut.isdigit() or len(rut) != 8:
        print("RUT inválido. Debe ser un número de 8 dígitos.")
        rut = input("Ingrese su RUT nuevamente: ")


    mostrar_disponibilidad_deptos(deptos)    

    fila = validar_entero("Ingrese el piso del departamento: ")
    columna = validar_entero("Ingrese tipo de departamento: ")

    if fila < 0 or fila >= len(deptos) or columna < 0 or columna >= len(deptos[0]):
        print("Coordenadas inválidas. Intente nuevamente.")
        return
#valida si el lote ya fue seleccionado del arreglo
    if deptos[fila][columna] == 'X':
        print("El departmanto seleccionado no está disponible. Por favor, elija otro.")
        return
#despliega datos del lote seleccionado
    deptos[fila][columna] = 'X'
    lote_seleccionado = (fila, columna)
    deptos_seleccionados.append(lote_seleccionado)
    clientes.append((rut))

    print("¡Departamento seleccionado con éxito!")

    depto_idx = len(deptos_seleccionados) - 1
    mostrar_detalles_deptos(deptos_seleccionados, depto_idx,detalles_deptos)
#funcion pasa salir del codigo
def salir():
    print("¡Gracias por confiar en Inmobiliaria Feliz!")
    print("José Seguel Horta")
    print("14.255.183-7")
    print("10-Julio-2023")
    exit()

#funcion para desplegar menu principal
def main():
    deptos = [[' ' for _ in range(5)] for _ in range(10)]
    deptos_seleccionados = []
    clientes = []
    

    while True:
        print("\n--- Inmobiliaria Casa Feliz ---")
        print("*****************************")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = input("Ingrese la opción deseada: ")
        print("*************************") 

        if opcion == '1':
            seleccionar_depto(deptos, deptos_seleccionados, clientes,detalles_deptos)
        elif opcion == '2':
            mostrar_disponibilidad_deptos(deptos)
            seleccionar_depto(deptos, deptos_seleccionados, clientes,detalles_deptos)
        elif opcion == '3':
            if len(deptos_seleccionados) == 0:
                print("No ha seleccionado ningún lote.")
            else:
                depto_idx = validar_entero("Ingrese el tipo de depto seleccionado: ") - 1
                if depto_idx < 0 or depto_idx >= len(deptos_seleccionados):
                    print("Número de depto inválido.")
                else:
                    mostrar_clientes(clientes)
                    mostrar_detalles_deptos(deptos_seleccionados,depto_idx,detalles_deptos)
        elif opcion == '4':
            mostrar_clientes(rut)
        elif opcion == '5':
            salir()
        print("Opción inválida. Intente nuevamente.")

# verifica si el archivo actual está siendo ejecutado directamente como un programa independiente 
 
if __name__ == '__main__':
    main()