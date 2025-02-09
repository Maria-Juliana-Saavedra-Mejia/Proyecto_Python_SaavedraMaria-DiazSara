
from deftrainer import trainerAgregarNotasA,trainerAgregarNotasA1,trainerAgregarNotasC, trainerAgregarNotasC1, trainerAgregarNotasp, trainerAgregarNotasp1, breakpoint, trainerAgregarNotasm, trainerAgregarNotasm1,  trainerAgregarNotasS, trainerAgregarNotasS1, trainerAgregarNotasJ, trainerAgregarNotasJ1
import json
def abrirJSON():
    dicFinal = {}
    with open('./camper.json', 'r') as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./camper.json", 'w') as outFile:
        json.dump(dic, outFile)

print("Bienvenido al programa de campuslands")
print("Còmo desea ingresar?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")

opcion = int(input("Digite su opcion: "))

while True:
    if opcion == 1:
        print("¿Qué desea hacer?")
        print("1. Inscripción")
        print("2. Ingresar al perfil")
        print("3. Salir del programa")
        opcioncam = int(input(":"))

        if opcioncam == 1:
            newcamper = abrirJSON()

            idn = int(input("Ingrese su número de identificación:"))
            nombren = input("Ingrese su(s) nombre(s):")
            apellidon = input("Digite sus apellidos:")
            direccion = input("Ingrese su dirección:")
            acudienten = input("Ingrese el nombre de su acudiente:")
            numcel = int(input("Ingrese su número de celular:"))
            numfijo = int(input("Ingrese su número de teléfono:"))

            newcamper["informacion"].append({
                "id": idn,
                "Nombre": nombren,
                "Apellido": apellidon,
                "Direccion": direccion,
                "Acudiente": acudienten,
                "Numero de celular": numcel,
                "Numero de telefono": numfijo
            })

            guardarJSON(newcamper)

        elif opcioncam == 2:
            print("Bienvenido Camper")
            print("Ingrese su número de identificación:")
            for (Id) in ["informacion"]:
                if ["Estado"] == "Aprobado":
                        print("")

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
            breakpoint()  
        else:
            print("Eleccion invalida")

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
            breakpoint()  
        else:
            print("Eleccion invalida")
            
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
            breakpoint()  
        else:
            print("Eleccion invalida")
        

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
            breakpoint()  
        else:
            print("Eleccion invalida")
               
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
            breakpoint()  
        else:
            print("Eleccion invalida")
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
            breakpoint()  
        else:
            print("Eleccion invalida")
    
 
    else:
        print("Codigo incorrecto")
        breakpoint()

