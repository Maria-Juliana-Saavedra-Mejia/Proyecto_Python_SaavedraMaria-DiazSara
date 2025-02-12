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

def menu_principal ():
    print("Bienvenido al programa de campuslands")
    print("¿Cómo desea ingresar?")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
    

def menu_camper():
    print("¿Qué desea hacer?")
    print("1. Inscripción")
    print("2. Ingresar al perfil")
    print("3. Salir de campus")
    print("4. Salir del programa")


def menu_trainer():
    print("Bienvenido Trainer")
    print("1. Pedro Gomez")
    print("2. Miguel Rodriguez")
    print("3. Juan Nariño")
    print("4. Santiago Melo")
    print("5. Carlos Rueda")
    print("6. Antonio Vega")

def inscripcion_camper():
    idn = int(input("Ingrese su número de identificación:"))
    nombren = input("Ingrese su(s) nombre(s):")
    apellidon = input("Digite sus apellidos:")
    direccion = input("Ingrese su dirección:")
    acudienten = input("Ingrese el nombre de su acudiente:")
    numcel = int(input("Ingrese su número de celular:"))
    numfijo = int(input("Ingrese su número de teléfono fijo:"))
    curso = ""  # Puedes asignar el curso más tarde si es necesario

    # Verificar si algún campo está vacío
    if not (nombren and apellidon and direccion and acudienten and numcel and numfijo):
        # Si algún campo está vacío, marcar "En proceso" como True y los demás estados como False
        camper = {
            "ID": idn,
            "Nombre": nombren,
            "Apellido": apellidon,
            "Direccion": direccion,
            "Acudiente": acudienten,
            "Numero de celular": numcel,
            "Numero de telefono fijo": numfijo,
            "Estado": {
                "En proceso": True,
                "Inscrito": False,
                "Aprobado": False,
                "Rechazado": False,
                "Cursando": False,
                "Graduado": False,
                "Expulado": False,
                "Retirado": False
            },
            "Riesgo": False,
            "Curso": curso,
            "notas": {
                "modulo1": 0.0,
                "modulo2": 0.0,
                "modulo3": 0.0,
                "modulo4": 0.0,
                "modulo5": 0.0
            }
        }
    else:
        # Si todos los campos están completos, marcar "Inscrito" como True y los demás estados como False
        camper = {
            "ID": idn,
            "Nombre": nombren,
            "Apellido": apellidon,
            "Direccion": direccion,
            "Acudiente": acudienten,
            "Numero de celular": numcel,
            "Numero de telefono fijo": numfijo,
            "Estado": {
                "En proceso": False,
                "Inscrito": True,
                "Aprobado": False,
                "Rechazado": False,
                "Cursando": False,
                "Graduado": False,
                "Expulado": False,
                "Retirado": False
            },
            "Riesgo": False,
            "Curso": curso,
            "notas": {
                "modulo1": 0.0,
                "modulo2": 0.0,
                "modulo3": 0.0,
                "modulo4": 0.0,
                "modulo5": 0.0
            }
        }
    
    # Cargar los campers existentes (asumiendo que ya tienes la lista de campers)
    campers = abrirJSON()  # Asegúrate de tener esta función que abre el archivo JSON
    campers.append(camper)
    
    # Guardar los campers actualizados en el archivo JSON
    guardarJSON(campers) 
    print("Camper inscrito exitosamente!")


def breakpoint ():
     return

def retirar_camper(campers, documento):
    encontrado = False
    for estudiante in campers:
        if estudiante["ID"] == documento:
            # Acceder al diccionario "Estado"
            estados = estudiante["Estado"]
            # Cambiar estado de "En proceso" a False
            estados["En proceso"] = False
            # Cambiar estado de "Retirado" a True
            estados["Retirado"] = True
            encontrado = True
            print(f"El estudiante con ID {documento} ha sido retirado.")
            break  # Salir del ciclo una vez que se encuentra el estudian
        if not encontrado:
            print(f"No se encontró un estudiante con ID {documento}.")
     
        return campers  
     
def trainerAgregarNotasp(camper, documento):
    print ("Estos son los campers de la clase P_1")
    # Mostrar lista de estudiantes en P_1
    est=int(input("Digite el numero del camper al que le quiere ingresar una nota: "))
    #Recorrer el id de los estudiantes en P_1
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota:"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
        
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")



def trainerAgregarNotasp1():
    print ("Estos son los campers de la clase P_2")
    est=int(input("Digite el numero del camper al que le quiere ingresar una nota"))
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
        
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")


def trainerAgregarNotasm():
    print ("Estos son los estudiantes de la clase M_1")
     ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")


def trainerAgregarNotasm1():
    print ("Estos son los estudiantes de la clase M_2")
      ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")

def trainerAgregarNotasJ():
    print ("Estos son los estudiantes de la clase J_1")
            ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")
     

def trainerAgregarNotasJ1():

    print ("Estos son los estudiantes de la clase J_2")
            ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")

def trainerAgregarNotasS():
    print ("Estos son los estudiantes de la clase S_1")
            ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")
def trainerAgregarNotasS1():
    print ("Estos son los estudiantes de la clase S_2")
            ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")

def trainerAgregarNotasC():
    print ("Estos son los estudiantes de la clase C_1")
            ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")
      
def trainerAgregarNotasC1():
    print ("Estos son los estudiantes de la clase C_2")
    ###imprimir la lista de esa clase con notas 
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")
def trainerAgregarNotasA():
    print ("Estos son los estudiantes de la clase A_1")
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")


def trainerAgregarNotasA1():
    print ("Estos son los estudiantes de la clase A_2")
    estm=int(input("Digite el numero del modulo al que quiere ingresar una nota"))
    if estm==1:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    #Poner el promedio en el mudulo del estudiante
    elif estm==2:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==3:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3

    elif estm==4:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
            
    elif estm==5:
        pt=int(input("Digite la nota de la prueba teorica: "))     
        pp=int(input("Digite la nota del proyecto: "))
        otros=int(input("Digite la nota de otros: "))
        promedio=(pt*0.3)(pp*0.6)(otros*0.1)/3
    else:
        print("Codigo incorrecto")

