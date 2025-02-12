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
                "Introducción a la Programación",
                "Python",
                "HTML/CSS",
                "Scrum",
                "Git",
                "JavaScript",
                "Intro Back",
                "Intro BBDD",
                "MySQL",
                "Java",
                "PostgreSQL",
                "SpringBoot" 
                ] 
    elif rutan=="NodeJS":
                newtrainer["Trainers"][salonn]={
                "Modulos": [
                "Introducción a la Programación",
                "Python",
                "HTML/CSS",
                "Scrum",
                "Git",
                "JavaScript",
                "Intro Back",
                "Intro BBDD",
                "MongoDB",
                "MySQL",
                "Express"
            ]}
    elif rutan==".NET":
                newtrainer["Trainers"][salonn]={
                "Modulos": [
                "Introducción a la Programación",
                "Python",
                "HTML/CSS",
                "Scrum",
                "Git",
                "JavaScript",
                "Intro Back",
                "Intro BBDD",
                "MongoDB",
                "MySQL",
                "Express"
            ]}

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


def modulo_matricular():
     
