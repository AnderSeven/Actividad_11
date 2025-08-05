def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

opciones = 0
a = False
nombres = []

while a == False:
    print("---Menu---")
    print("1. Ingrese los nombres")
    print("2. Mostrar la lista")
    print("3. Salir")
    opciones = int(input("Elija una opcion: "))

    match opciones:
        case 1:
            cantidad = int(input("Cuantos nombres quiere ingresar: "))
            for i in range(cantidad):
                n = input("Ingrese el nombre: ")
                nombres.append(n)
        case 2:
            if len(nombres) > 0:
                resultado = quick_sort(nombres)
                print("Lista ordenada:")
                for nombre in resultado:
                    print(nombre)
            else:
                print("No hay ningun estudiante registrado")
        case 3:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")
