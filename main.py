from modulos import menu_principal, perfilCamper, trainerVerHorarioA, trainerVerHorarioC, trainerVerHorarioM, trainerVerHorarioS, trainerVerHorarioJ, menu_trainer, menu_camper,inscripcion_camper, trainerVerHorarioP, trainerAgregarNotasA,trainerAgregarNotasA1,trainerAgregarNotasC, trainerAgregarNotasC1, trainerAgregarNotasp, trainerAgregarNotasp1, trainerAgregarNotasm, trainerAgregarNotasm1,  trainerAgregarNotasS, trainerAgregarNotasS1, trainerAgregarNotasJ, trainerAgregarNotasJ1, abrirJSON, abrirJSO, retirar_camper
from defcoordinador import menu_coordinador, menu_coordinador_opc_1, agregartrainers, agregar_modulo_a_todos_salones, reportes, eliminar_modulos, eliminarTrainers, mostrar_datos, asignar_grupo_estudiante
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
            perfilCamper()

        elif opcioncam == 3:

           # retirar_camper(campers, documento)
            print("")
        elif opcioncam == 4:
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
                trainerAgregarNotasp(campers)
            elif clase==2:
                trainerAgregarNotasp1(campers)
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
                trainerAgregarNotasm(campers)
            elif clase==2:
                trainerAgregarNotasm1(campers)
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
                trainerAgregarNotasJ(campers)
            elif clase==2:
                trainerAgregarNotasJ1(campers)
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
                trainerAgregarNotasS(campers)
            elif clase==2:
                trainerAgregarNotasS1(campers)
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
                trainerAgregarNotasC(campers)
            elif clase==2:
                trainerAgregarNotasC1(campers)
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
                trainerAgregarNotasA(campers)
            elif clase==2:
                trainerAgregarNotasA1(campers)
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
            asignar_grupo_estudiante()
        elif opcionC==5:
            mostrar_datos()
        elif opcionC==6:
            eliminarTrainers()
        elif opcionC==7:
            eliminar_modulos()
            
    elif opcion ==4:
        break