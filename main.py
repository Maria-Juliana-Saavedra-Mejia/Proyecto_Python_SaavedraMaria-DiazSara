from modulos import menu_principal, menu_trainer, menu_camper,inscripcion_camper, trainerAgregarNotasA,trainerAgregarNotasA1,trainerAgregarNotasC, trainerAgregarNotasC1, trainerAgregarNotasp, trainerAgregarNotasp1, breakpoint, trainerAgregarNotasm, trainerAgregarNotasm1,  trainerAgregarNotasS, trainerAgregarNotasS1, trainerAgregarNotasJ, trainerAgregarNotasJ1
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
menu_principal()
opcion = int(input("Digite su opción: "))

booleanito = True
while booleanito:
    if opcion == 1:
       menu_camper()
       opcioncam = int(input(": "))
       if opcioncam == 1:
            inscripcion_camper()
       elif opcioncam == 2:
            documento=int(input("Digite su numero de identidad"))
            
            for i in range(len(campers)):
                if documento==campers[i]["ID"]:
                    if campers[i]["Estado"]["Aprobado"]==True:
                        print(campers[i]["Nombre"])
                        x=campers[i]["Curso"]
                        print(x)
                        for i in range(salones["salones"]):
                            if x==salones["salones"][i]["grupo"]:
                                print("EL grupo es: ",salones["salones"]["grupo"])
                                print("EL grupo es: ",salones["salones"]["Profesor"])
                                print("EL grupo es: ",salones["salones"]["Salon"])
                                print("EL grupo es: ",salones["salones"]["Fecha de inicio"])
                                print("EL grupo es: ",salones["salones"]["Fecha de finalizacion"])
                                print("EL grupo es: ",salones["salones"]["Ruta"])
                                print("EL grupo es: ",salones["salones"]["Modulos"])
                                campers["Modulos"]
                                guardarJSON(campers)
                    else:
                        print("No se le ha asignado un grupo")
                else:
                    print("Documento no registrado")

       elif opcioncam == 3:
                print("Gracias por usar el programa.")
                booleanito = False

       else:
                print("Opción no válida.")
                break

          
                        
    elif opcion==2:
        menu_trainer()
        n1=int(input(": "))
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
    


            

        
