from main import*
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
    print("3. Salir del programa")


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
                curso = ""      
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
                        "Aprovado": False,
                        "Rechazado": False,
                        "Cursando": False,
                        "Graduado": False,
                        "Expulado": False,
                        "Retirado": False
                    },
                    "Riesgo": "",
                    "Curso": "",
                    "Nota teorica": "",
                    "Nota Practica": ""
                } 
                campers.append(camper)
                guardarJSON(campers)  
                print("Camper inscrito exitosamente!")

def breakpoint ():
     return

def menu_p():
    print("Bienvenido trainer Pedro Gomez")
    print("Para agregar notas a clase P_1 ingrese (1)")
    print("Para agregar notas a clase P_2 ingrese (2)")
    print("Para ver su horario digite (3)")
    print ("Para salir digite (4)") 
    
def trainerAgregarNotasp():
            print("Bienvenido trainer Pedro Gomez")
            print("Para agregar notas a clase P_1 ingrese (1)")
            print("Para agregar notas a clase P_2 ingrese (2)")
            print("Para ver su horario digite (3)")
            print ("Para salir digite (4)")
            clase=int(input("Digite su eleccion: "))
            print ("Estos son los campers de la clase P_1")
            est=int(input("Digite el numero del camper al que le quiere ingresar una nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))

            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))

            elif nota==3:
                otros=int(input("Digite la nota: "))

            else:
                print("Codigo incorrecto")
def trainerAgregarNotasp1():
            print ("Estos son los campers de la clase P_2")
       
            est=int(input("Digite el numero del camper al que le quiere ingresar una  nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
   
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
       
            elif nota==3:
                otros=int(input("Digite la nota: "))
     
            else:
                print("Codigo incorrecto")

def trainerAgregarNotasm():
        print ("Estos son los estudiantes de la clase M_1")
        ###imprimir la lista de esa clase con notas 
        est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
        print ("1. para trabajos")
        print ("2. para proyectos")
        print ("3. para otros")
        nota=int(input("Ingrese que nota quiere agregar: "))

        if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
         
        elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
         
        elif nota==3:
                otros=int(input("Digite la nota: "))
         
        else:
             print("Codigo incorrecto")


def trainerAgregarNotasm1():
      print ("Estos son los estudiantes de la clase M_2")
      ###imprimir la lista de esa clase con notas 
      est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
      print ("1. para trabajos")
      print ("2. para proyectos")
      print ("3. para otros")
      nota=int(input("Ingrese que nota quiere agregar: "))
      if nota==1:
          trabajos=int(input("Digite la nota del trabajo: "))
   
      elif nota==2:
          proyectos=int(input("Digite la nota del proyecto: "))
   
      elif nota==3:
          otros=int(input("Digite la nota: "))
   
      else:
       print("Codigo incorrecto")

def trainerAgregarNotasJ():
            print ("Estos son los estudiantes de la clase J_1")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
          
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
         
            elif nota==3:
                 otros=int(input("Digite la nota: "))
         
            else:
                    print("Codigo incorrecto")
     

def trainerAgregarNotasJ1():

            print ("Estos son los estudiantes de la clase J_2")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
         
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
         
            elif nota==3:
                otros=int(input("Digite la nota: "))
         
            else:
                    print("Codigo incorrecto")

def trainerAgregarNotasS():
            print ("Estos son los estudiantes de la clase S_1")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
         
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
         
            elif nota==3:
                otros=int(input("Digite la nota: "))
         
            else:
                print("Codigo incorrecto")
def trainerAgregarNotasS1():
    print ("Estos son los estudiantes de la clase S_2")
            ###imprimir la lista de esa clase con notas 
    est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
    print ("1. para trabajos")
    print ("2. para proyectos")
    print ("3. para otros")
    nota=int(input("Ingrese que nota quiere agregar: "))
    if nota==1:
        trabajos=int(input("Digite la nota del trabajo: "))
  
    elif nota==2:
        proyectos=int(input("Digite la nota del proyecto: "))
  
    elif nota==3:
        otros=int(input("Digite la nota: "))
  
    else:
        print("Codigo incorrecto")

def trainerAgregarNotasC():
            print ("Estos son los estudiantes de la clase C_1")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
         
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
         
            elif nota==3:
                otros=int(input("Digite la nota: "))
         
            else:
                print("Codigo incorrecto")
      
def trainerAgregarNotasC1():
    print ("Estos son los estudiantes de la clase C_2")
    ###imprimir la lista de esa clase con notas 
    est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
    print ("1. para trabajos")
    print ("2. para proyectos")
    print ("3. para otros")
    nota=int(input("Ingrese que nota quiere agregar: "))
    if nota==1:
        trabajos=int(input("Digite la nota del trabajo: "))
 
    elif nota==2:
        proyectos=int(input("Digite la nota del proyecto: "))
 
    elif nota==3:
        otros=int(input("Digite la nota: "))
 
    else:
        print("Codigo incorrecto")

def trainerAgregarNotasA():
    print ("Estos son los estudiantes de la clase A_1")

    est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
    print ("1. para trabajos")
    print ("2. para proyectos")
    print ("3. para otros")
    nota=int(input("Ingrese que nota quiere agregar: "))
    if nota==1:
         trabajos=int(input("Digite la nota del trabajo: "))
 
    elif nota==2:
         proyectos=int(input("Digite la nota del proyecto: "))

    elif nota==3:
         otros=int(input("Digite la nota: "))

    else:
         print("Codigo incorrecto")
def trainerAgregarNotasA1():
    print ("Estos son los estudiantes de la clase A_2")

    est=int(input("Digite el numero del estudiante al que le quiere ingresar una nota"))
    print ("1. para trabajos")
    print ("2. para proyectos")
    print ("3. para otros")
    nota=int(input("Ingrese que nota quiere agregar: "))
    if nota==1:
         trabajos=int(input("Digite la nota del trabajo: "))
 
    elif nota==2:
         proyectos=int(input("Digite la nota del proyecto: "))

    elif nota==3:
         otros=int(input("Digite la nota: "))

    else:
         print("Codigo incorrecto")




def menu_coordinador():
    print("Bienvenido coordinador")
    print("Que quieres hacer:")
    print("1.Agregar trainers")
    print("2.Eliminar campers")
    print("3.Revisar inscripcion")
    print("4.Mostrar campers")
    print("5.Crear nueva ruta")
    print("6.Modulo matriculas")
    print("7.Modulo reportes")
    opciontra=int(input(":"))

 