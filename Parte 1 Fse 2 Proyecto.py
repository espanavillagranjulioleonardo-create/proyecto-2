
tareas = []                 
puntos_estudiante = 0       
insignias = []             
rol = ""                    
print("Bienvenido al prototipo de organización UVG")
print("Este prototipo permite cambiar de rol para probar la demo.")


while rol != "maestro" and rol != "estudiante":
    rol = input("Ingresa tu rol inicial (maestro/estudiante): ")

opcion = ""  

while opcion != "9":
    print("MENÚ")
    print("Rol actual:", rol)
    if rol == "maestro":
        print("1. Crear tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tablero del estudiante")
        print("0. Cambiar de rol (a estudiante)")
        print("9. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Escribe el nombre de la nueva tarea: ")
            
            existente = False
            i = 0
            while i < len(tareas):
                if tareas[i]["titulo"] == titulo:
                    existente = True
                i = i + 1
            if existente:
                print("Ya existe una tarea con ese título.")
            else:
                tareas.append({"titulo": titulo, "entregada": False})
                print("Tarea creada:", titulo)

        elif opcion == "2":
            if len(tareas) == 0:
                print("No hay tareas.")
            else:
                print("LISTA DE TAREAS")
                i = 0
                while i < len(tareas):
                    if tareas[i]["entregada"]:
                        estado = "✅"
                    else:
                        estado = "⏳"
                    print("-", tareas[i]["titulo"], "-", estado)
                    i = i + 1

        elif opcion == "3":
            print("TABLERO DEL ESTUDIANTE")
            print("Puntos:", puntos_estudiante)
            if len(insignias) == 0:
                print("Insignias: (ninguna)")
            else:
                print("Insignias:", ", ".join(insignias))
            if len(tareas) == 0:
                print("No hay tareas.")
            else:
                i = 0
                while i < len(tareas):
                    if tareas[i]["entregada"]:
                        estado = "✅"
                    else:
                        estado = "⏳"
                    print("-", tareas[i]["titulo"], "-", estado)
                    i = i + 1

        elif opcion == "0":
            rol = "estudiante"
            print("Cambiado a rol: estudiante")

        elif opcion == "9":
            print("Saliendo...")

        else:
            print("Opción no válida.")

    elif rol == "estudiante":
        print("4. Entregar tarea")
        print("5. Ver mis tareas")
        print("6. Ver mi tablero (puntos e insignias)")
        print("0. Cambiar de rol (a maestro)")
        print("9. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "4":
            if len(tareas) == 0:
                print("No hay tareas para entregar.")
            else:
                titulo = input("¿Qué tarea quieres entregar?: ")
                encontrada = False
                i = 0
                while i < len(tareas):
                    if tareas[i]["titulo"] == titulo and tareas[i]["entregada"] == False:
                        tareas[i]["entregada"] = True
                        puntos_estudiante = puntos_estudiante + 10
                        print("¡Tarea entregada! Ganaste 10 puntos.")
                        encontrada = True

                        if puntos_estudiante >= 30:
                            if "Estrella UVG ⭐" not in insignias:
                                insignias.append("Estrella UVG ⭐")
                                print("¡Nueva insignia! -> Estrella UVG ⭐")
                        if puntos_estudiante >= 50:
                            if "Excelencia Académica 🏅" not in insignias:
                                insignias.append("Excelencia Académica 🏅")
                                print("¡Nueva insignia! -> Excelencia Académica 🏅")

                        entregadas = 0
                        j = 0
                        while j < len(tareas):
                            if tareas[j]["entregada"]:
                                entregadas = entregadas + 1
                            j = j + 1
                        if entregadas >= 3:
                            if "Constancia 🎯" not in insignias:
                                insignias.append("Constancia 🎯")
                                print("¡Nueva insignia! -> Constancia 🎯")

                    i = i + 1

                if encontrada == False:
                    print("No encontré esa tarea o ya estaba entregada.")

        elif opcion == "5":
            if len(tareas) == 0:
                print("No hay tareas asignadas aún.")
            else:
                print("MIS TAREAS")
                i = 0
                while i < len(tareas):
                    if tareas[i]["entregada"]:
                        estado = "✅"
                    else:
                        estado = "⏳"
                    print("-", tareas[i]["titulo"], "-", estado)
                    i = i + 1

        elif opcion == "6":
            print("MI TABLERO")
            print("Puntos:", puntos_estudiante)
            if len(insignias) == 0:
                print("Insignias: (ninguna)")
            else:
                print("Insignias:", ", ".join(insignias))
            if len(tareas) == 0:
                print("Tareas: (ninguna)")
            else:
                i = 0
                while i < len(tareas):
                    if tareas[i]["entregada"]:
                        estado = "✅"
                    else:
                        estado = "⏳"
                    print("-", tareas[i]["titulo"], "-", estado)
                    i = i + 1

        elif opcion == "0":
            rol = "maestro"
            print("Cambiado a rol: maestro")

        elif opcion == "9":
            print("Saliendo...")

        else:
            print("Opción no válida.")
