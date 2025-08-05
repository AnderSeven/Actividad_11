#es lo mismo que el otro solo que con el carnet o codigo y usando diccionarios
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

a = False
opciones = 0
estudiantes = {}

while a == False:
    print("---Menu---")
    print("1. Registro de estudiantes")
    print("2. Mostrar estudiantes")
    print("3. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            cantidad = int(input("Cuantos nombres quiere ingresar: "))
            for i in range(cantidad):
                s = False
                while s == False:
                    codigo = int(input("Ingrese un ID: "))
                    if codigo in estudiantes:
                        print("El Id ya existe, ingrese otro")
                    else:
                        s = True
                nombre = input("Ingrese el nombre: ")
                estudiantes[codigo] = nombre
        case 2:
            if len(estudiantes) > 0:
                ids_ordenados = quick_sort(list(estudiantes.keys()))
                print("Lista ordenada por ID: ")
                for codigo in ids_ordenados:
                    print(f"Codigo: {codigo}, Nombre: {estudiantes[codigo]}")
            else:
                print("No hay ningun estudiante registrado")
        case 3:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")