
from deftrainer import trainerAgregarNotasA,trainerAgregarNotasA1,trainerAgregarNotasC, trainerAgregarNotasC1, trainerAgregarNotasp, trainerAgregarNotasp1, breakpoint, trainerAgregarNotasm, trainerAgregarNotasm1,  trainerAgregarNotasS, trainerAgregarNotasS1, trainerAgregarNotasJ, trainerAgregarNotasJ1
import json

def abrirJSON():
    with open('./camper.json','r',encoding="utf-8") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./camper.json",'w',encoding="utf-8") as outFile:
        json.dump(dic,outFile,indent=4, ensure_ascii=False)

camperNuevo = []

print("Bienvenido al programa de campuslands")
print("¿Cómo desea ingresar?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
opcion = int(input("Digite su opción: "))

booleanito = True
while booleanito:
    if opcion == 1:
        camperNuevo = abrirJSON()  
        print("¿Qué desea hacer?")
        print("1. Inscripción")
        print("2. Ingresar al perfil")
        print("3. Salir del programa")
        opcioncam = int(input(": "))

        if opcioncam == 1:
            idn = int(input("Ingrese su número de identificación:"))
            nombren = input("Ingrese su(s) nombre(s):")
            apellidon = input("Digite sus apellidos:")
            direccion = input("Ingrese su dirección:")
            acudienten = input("Ingrese el nombre de su acudiente:")
            numcel = int(input("Ingrese su número de celular:"))
            numfijo = int(input("Ingrese su número de teléfono fijo:"))
            jornada = input("Ingrese la jornada (Mañana 6-10 am, Mediodía 10-2 pm, Tarde 2-6 pm, Noche 6-10 pm): ").capitalize()
            curso = ""      

            camper = {
                "ID": idn,
                "Nombre": nombren,
                "Apellido": apellidon,
                "Direccion": direccion,
                "Acudiente": acudienten,
                "Numero de celular": numcel,
                "Numero de telefono fijo": numfijo,
                "Estado": [{
                    "En proceso": False,
                    "Inscrito": True,
                    "Aprovado": False,
                    "Rechazado": False,
                    "Cursando": False,
                    "Graduado": False,
                    "Expulado": False,
                    "Retirado": False
                }],
                "Riesgo": "",
                "Curso": curso,
                "Jornada": jornada
                }
            camperNuevo.append(camper)  

            guardarJSON(camperNuevo)  

        elif opcioncam == 2:
            print("Función para ingresar al perfil no implementada aún.")
        
        elif opcioncam == 3:
            print("Gracias por usar el programa.")
            booleanito = False

        else:
            print("Opción no válida.")
            break

          
                        

    elif opcion==2:
     print("Bienvenido Trainer")
     print("1. Pedro Gomez")
     print("2. Miguel Rodriguez")
     print("3. Juan Nariño")
     print("4. Santiago Melo")
     print("5. Carlos Rueda")
     print("6. Antonio Vega")
     
     n1=int(input("Digite su codigo:"))

     if n1==1:
        print("Bienvenido trainer Pedro Gomez")
        print("Para agregar notas a clase P_1 ingrese (1)")
        print("Para agregar notas a clase P_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasp()
        elif clase==2:
            trainerAgregarNotasp1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit() 
        else:
            print("Eleccion invalida")
            exit()

     elif n1==2:
        print("Bienvenido trainer Miguel Rodriguez")
        print("Para agregar notas a clase M_1 ingrese (1)")
        print("Para agregar notas a clase M_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasm()
        elif clase==2:
            trainerAgregarNotasm1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit()  
        else:
            print("Eleccion invalida")
            exit()
            
     elif n1==3:
        print ("Bienvenido trainer Juan Nariño")
        print("Para agregar notas a clase J_1 ingrese (1)")
        print("Para agregar notas a clase J_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasJ()
        elif clase==2:
            trainerAgregarNotasJ1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit()  
        else:
            print("Eleccion invalida")
            exit()
        

     elif n1==4:
        print ("Bienvenido trainer Santiago Melo")
        print("Para agregar notas a clase S_1 ingrese (1)")
        print("Para agregar notas a clase S_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasS()
        elif clase==2:
            trainerAgregarNotasS1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit() 
        else:
            print("Eleccion invalida")
            exit()
               
     elif n1==5:
        print ("Bienvenido trainer Carlos Rueda")
        print("Para agregar notas a clase S_1 ingrese (1)")
        print("Para agregar notas a clase S_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasC()
        elif clase==2:
            trainerAgregarNotasC1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit() 
        else:
            print("Eleccion invalida")
            exit()
     elif n1==6:
        print ("Bienvenida trainer Antonio Vega")
        print("Para agregar notas a clase A_1 ingrese (1)")
        print("Para agregar notas a clase A_2 ingrese (2)")
        print("Para ver su horario digite (3)")
        print ("Para salir digite (4)")
        clase=int(input("Digite su eleccion: "))
        if clase==1:
            trainerAgregarNotasA()
        elif clase==2:
            trainerAgregarNotasA1()
        elif clase==3:
            print("")
            ## imprimir horario y clases
        elif clase==4:
            exit()  
        else:
            print("Eleccion invalida")
            exit()
    
 
     else:
        print("Codigo incorrecto")
        exit()
    

        

        
