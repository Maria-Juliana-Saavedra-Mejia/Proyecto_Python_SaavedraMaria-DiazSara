from modulos import menu_principal, trainerVerHorarioA, trainerVerHorarioC, trainerVerHorarioM, trainerVerHorarioS, trainerVerHorarioJ, menu_trainer, menu_camper,inscripcion_camper, trainerVerHorarioP, trainerAgregarNotasA,trainerAgregarNotasA1,trainerAgregarNotasC, trainerAgregarNotasC1, trainerAgregarNotasp, trainerAgregarNotasp1, trainerAgregarNotasm, trainerAgregarNotasm1,  trainerAgregarNotasS, trainerAgregarNotasS1, trainerAgregarNotasJ, trainerAgregarNotasJ1, abrirJSON, abrirJSO, retirar_camper
from defcoordinador import menu_coordinador, menu_coordinador_opc_1, agregartrainers, agregar_modulo_a_todos_salones
import json

campers = abrirJSON()  
salones=abrirJSO()
menu_principal()
opcion = int(input("Digite su opción: "))

booleanito = True
while booleanito:
    if  opcion == 1:
        menu_camper()
        opcioncam = int(input(": "))
        if opcioncam == 1:
            inscripcion_camper()


        elif opcioncam == 2:
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
                        salones=abrirJSO
                        print(f"El estudiante con ID {documento} está aprobado.")
                        modulo1 = estudiante["notas"]["modulo1"]
                        modulo2 = estudiante["notas"]["modulo2"]
                        modulo3 = estudiante["notas"]["modulo3"]
                        modulo4 = estudiante["notas"]["modulo4"]
                        modulo5 = estudiante["notas"]["modulo5"]
                        print("Sus notas del modulo 1 son: ",{modulo1})
                    
                        if modulo1<60.0:
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

                        if modulo2<60.0:
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

                        if modulo3<60.0:
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

                        if modulo4<60.0:
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

                        if modulo5<60.0:
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
                    
                    break  # Salir del ciclo una vez que se encuentra el estudiante

        elif opcioncam == 3:
            retirar_camper(campers, documento)
                 
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
                trainerVerHorarioP()
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
                trainerVerHorarioM()
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
                trainerVerHorarioJ()
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
                trainerVerHorarioS()
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
                trainerVerHorarioC()
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
                trainerVerHorarioA()
            elif clase==4:
                exit()  
            else:
                print("Eleccion invalida")
                exit()
    
 
        else:
            print("Codigo incorrecto")
            exit()
    elif opcion == 3:
        opcionC = menu_coordinador()
        if opcionC == 1:
            menu_coordinador_opc_1()
        elif opcionC == 2:
            agregartrainers()
        elif opcionC == 3:
            nuevo_modulo = input("Ingrese el nombre del nuevo módulo a agregar a todos los salones: ")
            agregar_modulo_a_todos_salones(nuevo_modulo)
        elif opcionC==4:
            print("")