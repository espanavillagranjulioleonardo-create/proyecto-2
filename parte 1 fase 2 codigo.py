
rol = ""            
tarea1 = ""           
tarea1_entregada = "no"
puntos = 0
insignia = "ninguna"

print("Bienvenido al prototipo de organización UVG")


while rol != "maestro" and rol != "estudiante":
    rol = input("Escribe tu rol (maestro/estudiante): ")

opcion = ""

while opcion != "5":
    print(" MENÚ ")
    if rol == "maestro":
        print("1. Crear tarea")
        print("2. Ver tablero del estudiante")
        print("3. Cambiar a estudiante")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            if tarea1 == "":
                tarea1 = input("Escribe el nombre de la tarea: ")
                print("Tarea creada:", tarea1)
            else:
                print("Ya existe una tarea:", tarea1)

        elif opcion == "2":
            print(" TABLERO DEL ESTUDIANTE ")
            print("Puntos:", puntos)
            print("Insignia:", insignia)
            if tarea1 == "":
                print("No hay tareas aún.")
            else:
                print("Tarea:", tarea1, "-", tarea1_entregada)

        elif opcion == "3":
            rol = "estudiante"
            print("Has cambiado a estudiante.")

        elif opcion == "5":
            print("Adiós.")

        else:
            print("Opción no válida.")

    elif rol == "estudiante":
        print("1. Entregar tarea")
        print("2. Ver mis tareas")
        print("3. Ver mi tablero")
        print("4. Cambiar a maestro")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            if tarea1 != "" and tarea1_entregada == "no":
                tarea1_entregada = "sí"
                puntos = puntos + 10
                print("¡Entregaste la tarea y ganaste 10 puntos!")
                if puntos >= 30:
                    insignia = "Estrella UVG"
            else:
                print("No hay tareas pendientes o ya la entregaste.")

        elif opcion == "2":
            if tarea1 == "":
                print("No tienes tareas.")
            else:
                print("Tarea:", tarea1, "-", tarea1_entregada)

        elif opcion == "3":
            print(" MI TABLERO ")
            print("Puntos:", puntos)
            print("Insignia:", insignia)

        elif opcion == "4":
            rol = "maestro"
            print("Has cambiado a maestro.")

        elif opcion == "5":
            print("Adiós.")

        else:
            print("Opción no válida.")
