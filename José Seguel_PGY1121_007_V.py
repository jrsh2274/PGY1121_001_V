# Programación de Algoritmos
# Profesor Giovanni Valdivia
# Examen final
# Autores: José Seguel : 14.255.183-7 

# rescata fecha calendario al salir
import datetime

# Precios de los departamentos
precios = {
    "A": 3800,
    "B": 3000,
    "C": 2800,
    "D": 3500
}

# Estado de los departamentos
departamentos = [["-" for _ in range(4)] for _ in range(10)]

# Compradores
compradores = []

def mostrar_menu():
    print("---- Bienvenido a Inmobiliaria Mundo Feliz")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprar_departamento():
    print("Departamentos disponibles:")
    print("Piso\tTipo\tA\tB\tC\tD")
    for piso, deptos in reversed(list(enumerate(departamentos, start=1))):
        print(piso, end='\t')
        for tipo in deptos:
            print(tipo, end='\t')
        print()
    
    while True:
        piso_input = input("Ingrese el número de piso: ")
        if piso_input.isdigit():
            piso = int(piso_input)
            if 1 <= piso <= 10:
                break
            else:
                print("El número de piso debe estar entre 1 y 10.")
        else:
            print("Ingrese un número válido para el piso.")
    
    while True:
        tipo = input("Ingrese el tipo de departamento (A, B, C o D): ").upper()
        if tipo in ["A", "B", "C", "D"]:
            break
        else:
            print("Tipo de departamento inválido. Intente nuevamente.")
    
    depto = departamentos[10 - piso][ord(tipo) - ord("A")]
    if depto == "-":
        run_input = input("Ingrese el RUN del comprador (solo 8 dígitos): ")
        if len(run_input) == 8 and run_input.isdigit():
            run = run_input
            compradores.append((run, tipo))
            departamentos[10 - piso][ord(tipo) - ord("A")] = "X"
            print("Operación realizada correctamente.")
        else:
            print("El RUN ingresado no es válido. Debe contener exactamente 8 dígitos.")
    else:
        print("El departamento seleccionado no está disponible.")

def mostrar_departamentos_disponibles():
    print("Departamentos disponibles:")
    print("Piso\tTipo\tA\tB\tC\tD")
    for piso, deptos in reversed(list(enumerate(departamentos, start=1))):
        print(piso, end='\t')
        for tipo in deptos:
            print(tipo, end='\t')
        print()

def ver_listado_compradores():
    print("Listado de compradores:")
    for run, tipo in sorted(compradores):
        print(f"RUN: {run} - Departamento: Tipo {tipo}")

def mostrar_ventas_totales():
    totales = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for _, tipo in compradores:
        totales[tipo] += 1
    
    total_ventas = 0
    
    print("Ventas totales:")
    print("Tipo de Departamento Cantidad Total")
    for tipo, cantidad in totales.items():
        precio = precios[tipo]
        total = precio * cantidad
        total_ventas += total
        print(f"Tipo {tipo} {' '*(8-len(tipo))}{precio} UF {cantidad} {' '*(6-len(str(cantidad)))}{total} UF")
    print(f"TOTAL {' '*8}{sum(totales.values())} {' '*4}{total_ventas} UF")

# Función para obtener la fecha actual formateada
def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    return fecha_actual.strftime("%d/%m/%Y")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            comprar_departamento()
        elif opcion == "2":
            mostrar_departamentos_disponibles()
        elif opcion == "3":
            ver_listado_compradores()
        elif opcion == "4":
            mostrar_ventas_totales()
        elif opcion == "5":
            nombre = "José"  
            apellido = "Seguel"
            fecha_actual = obtener_fecha_actual()
            print(f"¡Hasta pronto Inmobiliaria Mundo Feliz, {nombre} {apellido}! Salida del sistema: {fecha_actual}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar la función principal
main()
