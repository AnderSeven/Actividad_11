#es lo mismo que el otro solo que con el carnet o codigo y usando diccionarios
a = False
opciones = 0
while a == False:
    print("---Menu---")
    print("1. Registro de estudiantes")
    print("2. Mostrar estudiantes")
    print("3. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
        case 2:
        case 3:
        case _: