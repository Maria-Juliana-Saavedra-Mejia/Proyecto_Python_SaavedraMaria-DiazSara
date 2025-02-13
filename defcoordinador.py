import json

def abrirJSON():
    with open('./json/camper.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./json/camper.json",'w') as outFile:
        json.dump(dic,outFile,indent=4, ensure_ascii=False)

def abrirJSO():
    with open('./json/salones.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSO(dic):
    with open("./json/salones.json",'w') as outFile:
        json.dump(dic,outFile,indent=4, ensure_ascii=False)

campers = abrirJSON()  
salones=abrirJSO()

def menu_coordinador ():
      print("Agregar notas prueba de inscripcion (1)")
      print("Agregar trainers (2)")
      print("Agregar modulos (3)")
      print("Modulo matriculas (4)")
      print("Modulo reportes(5)")
      print("Eliminar trainers (6)")
      print("Eliminar modulos (7)")
      op=int(input("Digite su eleccion: "))
      return op

# Función para mostrar el menú y asignar notas
def menu_coordinador_opc_1():
    # Cargar la lista de campers
    campers = abrirJSON()  # Asegúrate de tener esta función para abrir el archivo JSON
    # Recorrer todos los estudiantes
    for estudiante in campers:
        estados = estudiante["Estado"]
        # Solo procesar estudiantes que están inscritos
        if estados["Inscrito"] == True:
            print(f"Estudiante: {estudiante['Nombre']} {estudiante['Apellido']} (ID: {estudiante['ID']})")
            nota1 = float(input("Ingrese la nota teorica: "))
            nota2 = float(input("Ingrese la nota practica: "))
            # Calcular el promedio de las notas
            promedio = (nota1 + nota2) / 2
            # Verificar si el estudiante aprueba o rechaza
            if promedio >= 60:
                # Si aprueba, cambiar estado a Aprobado
                estudiante["Estado"]["Aprobado"] = True
                estudiante["Estado"]["Rechazado"] = False
                print(f"El estudiante con ID {estudiante['ID']} ha aprobado.")
            else:
                # Si no aprueba, cambiar estado a Rechazado
                estudiante["Estado"]["Aprobado"] = False
                estudiante["Estado"]["Rechazado"] = True
                print(f"El estudiante con ID {estudiante['ID']} ha sido rechazado.")
    # Guardar los cambios en el JSON
    guardarJSON(campers)


def agregartrainers ():       
    newtrainer = abrirJSON()
    nomtn = input("Ingrese el nombre del nuevo trainer:")
    salonn = input("Ingrese el salon del nuevo trainer :")
    fechain = input("Digite la fecha de inicio:")
    fechafn = input("Digite la fecha de finalizacion:")
    horarion = input("Ingrese el horario:")
    rutan =input("Ingrese la ruta a seguir:")
    newtrainer["Trainers"][salonn]={
                    "Profesor": nomtn,
                    "Salon": salonn,
                    "Fecha de inicio": fechain,
                    "Fecha de finalizacion": fechafn,
                    "Horario": horarion,
                    "Ruta": rutan}
    if rutan=="Java":
                newtrainer["Trainers"][salonn]["Modulos"]=[
                "Fundamentos de programación",
                "Programacion Web",
                "Programacion Formal",
                "Base de datos",
                "Backend" 
                ] 
    elif rutan=="NodeJS":
                newtrainer["Trainers"][salonn]["Modulos"]=[
                "Fundamentos de programación",
                "Programacion Web",
                "Programacion Formal",
                "Base de datos",
                "Backend"
            ]
    elif rutan==".NET":
                newtrainer["Trainers"][salonn]["Modulos"]=[
                "Fundamentos de programación",
                "Programacion Web",
                "Programacion Formal",
                "Base de datos",
                "Backend"
            ]

    guardarJSON(newtrainer)


# Función para agregar un módulo a todos los salones
def agregar_modulo_a_todos_salones(nuevo_modulo):
    # Abrir y cargar los datos de los salones
    with open('./json/salones.json', 'r') as f:
        data = json.load(f)
    salones = data["salones"]  # Acceder a la lista de salones
    # Recorrer todos los salones y agregar el nuevo módulo
    for salon in salones:
        salon["Modulos"].append(nuevo_modulo)
        print(f"Se ha agregado el módulo '{nuevo_modulo}' al grupo {salon['grupo']} ({salon['Salon']})")
    # Guardar los cambios
    guardarJSO(data)



def eliminar_modulos():
    salones = abrirJSO()  
    
    print("Los grupos disponibles son:")
    

    for salon in salones:
        print(f"Grupo: {salon['grupo']} - Salon: {salon['Salon']} - Módulos: {', '.join(salon.get('Modulos', ['No asignado']))}")


    grupo_a_modificar = input("Ingrese el grupo (ej. J_1, P_1, etc.) del cual desea eliminar los módulos: ").strip()

    grupo_encontrado = False
    for salon in salones:
        if salon["grupo"] == grupo_a_modificar:
            grupo_encontrado = True
            if "Modulos" in salon and salon["Modulos"]:
                salon["Modulos"] = []  
                print(f"Los módulos del grupo {grupo_a_modificar} han sido removidos (ahora es una lista vacía []).")
            else:
                print(f"El grupo {grupo_a_modificar} ya tenía el campo 'Modulos' vacío o no estaba asignado.")
            break

    if not grupo_encontrado:
        print(f"No se encontró un grupo con el nombre {grupo_a_modificar}.")
    else:
        guardarJSO(salones)
        print("Cambios guardados correctamente.")







def mostrar_datos():
    campers = abrirJSON()  
    salones = abrirJSO()   
    
    print("\nOpciones de filtro:")
    print("1. Inscritos")
    print("2. Aprobados")
    print("3. En riesgo")
    print("4. Trainers")
    
    opcion = input("Seleccione una opción (1-4): ").strip()
    nombres = set()  

    if opcion == "1":
        for camper in campers:
            if camper["Estado"].get("Inscrito", False):
                nombres.add(camper["Nombre"])
        print("\nCampers Inscritos:")
    elif opcion == "2":
        for camper in campers:
            if camper["Estado"].get("Aprobado", False):
                nombres.add(camper["Nombre"])
        print("\nCampers Aprobados:")
    elif opcion == "3":
        for camper in campers:
            if camper.get("Riesgo", False):
                nombres.add(camper["Nombre"])
        print("\nCampers en Riesgo:")
    elif opcion == "4":
        for salon in salones:
            if "Profesor" in salon:
                nombres.add(salon["Profesor"])
        print("\nLista de Trainers:")
    else:
        print("Opción no válida.")
        return

    if nombres:
        for nombre in nombres:
            print(f"- {nombre}")
    else:
        print("No hay registros que coincidan con el filtro seleccionado.")






def asignar_grupo_estudiante():
    estudiantes = abrirJSON()
    salones = abrirJSO()
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    nuevo_grupo = input("Ingrese el grupo a asignar: ")
    grupos_disponibles = [salon["grupo"] for salon in salones]
    
    if nuevo_grupo not in grupos_disponibles:
        print("Error: El grupo ingresado no está disponible.")
        return
    
    for estudiante in estudiantes:
        if estudiante["ID"] == id_estudiante:
            estudiante["grupo"] = nuevo_grupo
            print(f"Grupo asignado correctamente a {estudiante['Nombre']} {estudiante['Apellido']}.")
            guardarJSON(estudiantes)
            return
    
    print("Error: No se encontró un estudiante con ese ID.")




















def reportes():
    campers=abrirJSON

    for i in range (campers+1):
        print

def eliminarTrainers():
    salones = abrirJSO()  # Cargar datos desde salones.json
    
    print("Los grupos disponibles son:")
    
    # Mostrar todos los grupos disponibles
    for salon in salones:
        print(f"Grupo: {salon['grupo']} - Salon: {salon['Salon']} - Profesor: {salon.get('Profesor', 'No asignado')}")

    # Pedir al usuario el grupo que desea modificar
    grupo_a_modificar = input("Ingrese el grupo (ej. J_1, P_1, etc.) del cual desea eliminar el profesor: ").strip()

    # Buscar el grupo y actualizar el profesor a ""
    grupo_encontrado = False
    for salon in salones:
        if salon["grupo"] == grupo_a_modificar:
            grupo_encontrado = True
            if "Profesor" in salon and salon["Profesor"]:
                salon["Profesor"] = ""  # Asignar valor vacío en lugar de eliminar el campo
                print(f"El profesor del grupo {grupo_a_modificar} ha sido removido (ahora es '').")
            else:
                print(f"El grupo {grupo_a_modificar} ya tenía el campo 'Profesor' vacío o no estaba asignado.")
            break

    # Si no se encuentra el grupo
    if not grupo_encontrado:
        print(f"No se encontró un grupo con el nombre {grupo_a_modificar}.")
    else:
        # Guardamos los cambios en el archivo
        guardarJSO(salones)
        print("Cambios guardados correctamente.")


