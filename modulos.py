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
    
def perfilCamper():
    campers = abrirJSON() 
    documento = int(input("Digite su numero de identidad -> "))
    encontrado = False  # Bandera para verificar si se encontró el estudiante
    for estudiante in campers:
        if estudiante["ID"] == documento:
            # Acceder al diccionario "Estado"
            estados = estudiante["Estado"]
            encontrado = True
            if not encontrado:
                print("Estudiante con ese ID no encontrado.")

            # Revisar si "Aprobado" es True
            if estados["Aprobado"]:  # Solo si Aprobado es True
                salones=abrirJSO()
                print(f"El estudiante con ID {documento} está aprobado.")
                grupo = estudiante["grupo"]
                print("Su grupo es: ",grupo)
                modulo1 = estudiante["notas"]["modulo1"]
                modulo2 = estudiante["notas"]["modulo2"]
                modulo3 = estudiante["notas"]["modulo3"]
                modulo4 = estudiante["notas"]["modulo4"]
                modulo5 = estudiante["notas"]["modulo5"]
                
                for pacos in salones: 
                   
                    if pacos["grupo"] == estudiante["grupo"]: 
                        profesor = pacos["Profesor"]
                        salon_nombre = pacos["Salon"]
                        fecha_inicio = pacos["Fecha de inicio"]
                        fecha_fin = pacos["Fecha de finalizacion"]
                        horario = pacos["Horario"]                            
                        modulos = pacos["Modulos"]
                        ruta = pacos["Ruta"]                                 
                            # Imprimir la información del salón y del estudiante
                        print("Su profesor es:", profesor)
                        print("Su salón es:", salon_nombre)
                        print("Su fecha de inicio es:", fecha_inicio)
                        print("Su fecha de finalización es:", fecha_fin)
                        print("Su horario es:", horario)
                        print("Su ruta es:", ruta)
                        print("Sus módulos son:", modulos)

                
                print("Sus notas del modulo 1 son: ",{modulo1})
                if modulo1<60.0 and modulo1>0:
                    riesgo = estudiante["riesgo"]=True
                    print("Su riesgo es alto en el primer modulo")
                elif modulo1>=60.0 and modulo1<80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es medio en el primer modulo")
                elif modulo1>=80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es bajo en el primer modulo")
                elif modulo1 == 0.0:
                    print("Modulo no terminado")

                print("Sus notas del modulo 2 son: ",{modulo2})

                if modulo2<60.0 and modulo2>0:
                    riesgo = estudiante["riesgo"]=True
                    print("Su riesgo es alto en el segundo modulo")
                elif modulo2>=60.0 and modulo2<80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es medio en el segundo modulo")
                elif modulo2>=80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es bajo en el segundo modulo")
                elif modulo2 == 0.0:
                    print("Modulo no terminado")

                print("Sus notas del modulo 3 son: ",{modulo3})

                if modulo3<60.0 and modulo3>0:
                    riesgo = estudiante["riesgo"]=True
                    print("Su riesgo es alto en el tercer modulo")
                elif modulo3>=60.0 and modulo3<80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es medio en el tercer modulo")
                elif modulo3>=80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es bajo en el tercer modulo")
                elif modulo3 == 0.0:
                    print("Modulo no terminado")

                print("Sus notas del modulo 4 son: ",{modulo4})

                if modulo4<60.0 and modulo4>0:
                    riesgo = estudiante["riesgo"]=True
                    print("Su riesgo es alto en el cuarto modulo")
                elif modulo4>=60.0 and modulo4<80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es medio en el cuarto modulo")
                elif modulo4>=80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es bajo en el cuarto modulo")
                elif modulo4 == 0.0:
                    print("Modulo no terminado")
                    
                print("Sus notas del modulo 5 son: ",{modulo5})

                if modulo5<60.0 and modulo5>0:
                    riesgo = estudiante["riesgo"]=True
                    print("Su riesgo es alto en el quinto modulo")
                elif modulo5>=60.0 and modulo5<80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es medio en el quinto modulo")
                elif modulo5>=80.0:
                    riesgo = estudiante["riesgo"]=False
                    print("Su riesgo es bajo en el quinto modulo")
                elif modulo5 == 0.0:
                    print("Modulo no terminado")

            else:
                print(f"El estado de aprobación del estudiante con ID {documento} es False.")
            
            break  # Salir del ciclo una vez que se encuentra el estudiantes
     

def trainerVerHorarioP():
    grupop = ("P_1", "P_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")
def trainerVerHorarioM():
    grupop = ("M_1", "M_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")
def trainerVerHorarioJ():
    grupop = ("J_1", "J_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")
def trainerVerHorarioS():
    grupop = ("C_1", "C_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")

def trainerVerHorarioC():
    grupop = ("C_1", "C_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")
def trainerVerHorarioA():
    grupop = ("A_1", "A_2")  
    for salon in salones["salones"]:
        if salon["grupo"] in grupop: 
            print(f"Grupo: {salon['grupo']}")
            print(f"Profesor: {salon['Profesor']}")
            for horario in salon["Horario"]:
                print(f"- {horario}")






def trainerAgregarNotasp(campers):
    campers = abrirJSON() 
    print("Estos son los campers de la clase P_1")
    curso_especifico = "P_1"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")




def trainerAgregarNotasp1(campers):
    campers = abrirJSON() 
    print ("Estos son los campers de la clase P_2")
    curso_especifico = "P_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")

    




def trainerAgregarNotasm(campers):
    campers = abrirJSON() 
    print ("Estos son los estudiantes de la clase M_1")
    curso_especifico = "M_1"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


def trainerAgregarNotasm1(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase M_2")
    curso_especifico = "M_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


def trainerAgregarNotasJ(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase J_1")
    curso_especifico = "J_1"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")

     

def trainerAgregarNotasJ1(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase J_2")
    curso_especifico = "J_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


def trainerAgregarNotasS(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase S_1")
    curso_especifico = "S_1"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")



def trainerAgregarNotasS1(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase S_2")
    curso_especifico = "S_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")



def trainerAgregarNotasC(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase C_1")
    curso_especifico = "C_1"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


      
def trainerAgregarNotasC1(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase C_2")
    curso_especifico = "C_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")  
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


def trainerAgregarNotasA(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase A_1")
    curso_especifico = "A_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
    # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


def trainerAgregarNotasA1(campers):
    campers = abrirJSON()
    print ("Estos son los estudiantes de la clase A_2")
    curso_especifico = "A_2"
    filtro = list(filter(lambda camper: camper["grupo"] == curso_especifico, campers))
    for camper in filtro:
        print(f"{camper['Nombre']} {camper['Apellido']} - Grupo: {camper['grupo']} - ID: {camper['ID']}")
    est = int(input("Digite el número del camper al que le quiere ingresar una nota: "))
    estm = int(input("Digite el número del módulo al que quiere ingresar una nota: "))
    if estm in range(1, 6):  
        pt = int(input("Digite la nota de la prueba teórica: "))     
        pp = int(input("Digite la nota del proyecto: "))
        otros = int(input("Digite la nota de otros: "))
        promedio = (pt * 0.3 + pp * 0.6 + otros * 0.1)/3
        print(f"El promedio del módulo {estm} es: {promedio}")
        # Actualizar la nota del camper
        for camper in campers:
            if camper["ID"] == est:
                camper["notas"][f"modulo{estm}"] = promedio
                print(f"Nota registrada para {camper['Nombre']} {camper['Apellido']}.")
                break
        else:
            print("No se encontró un camper con ese ID.")
            
        guardarJSON(campers)
    else:
        print("Código incorrecto de módulo.")


