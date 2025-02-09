import json
from deftrainer import usertrainer,trainerAgregarNotasp, trainerAgregarNotasp1, breakpoint, trainerAgregarNotasm, trainerAgregarNotasm1, trainerAgregarNotasJ, trainerAgregarNotasJ1
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
     n1=int(input("Digite su codigo"))
     if n1==1:
        usertrainer()
        while True:
            if clase==1:
                trainerAgregarNotasp()
            elif clase==2:
                trainerAgregarNotasp1()

            elif clase==3:
                breakpoint()


    elif n1==2:
        usertrainer()
        if clase==1:
            trainerAgregarNotasm()

        elif clase==2:
                trainerAgregarNotasm1()

          

    
    elif n1==3:
        usertrainer()
        usertrainer=n1
        if clase==1:
            trainerAgregarNotasJ()
    elif n1==4:
        if clase==1:
            trainerAgregarNotasJ1()
        

    elif n1==4:
        usertrainer()
        if clase==1:
            print ("Estos son los estudiantes de la clase C_1")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una la nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
                ##Agregar nota a diccionario
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
                ##Agregar nota a diccionario
            elif nota==3:
                otros=int(input("Digite la nota: "))
                ##Agregar nota a diccionario
            else:
                print("Codigo incorrecto")
    elif n1==6:
        print ("Bienvenida trainer Antonio Vega")
        print("Para agregar notas a clase A_1 ingrese (1)")
        print("Para agregar notas a clase A_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase A_1")
            ###imprimir la lista de esa clase con notas 
            est=int(input("Digite el numero del estudiante al que le quiere ingresar una la nota"))
            print ("1. para trabajos")
            print ("2. para proyectos")
            print ("3. para otros")
            nota=int(input("Ingrese que nota quiere agregar: "))
            if nota==1:
                trabajos=int(input("Digite la nota del trabajo: "))
                ##Agregar nota a diccionario
            elif nota==2:
                proyectos=int(input("Digite la nota del proyecto: "))
                ##Agregar nota a diccionario
            elif nota==3:
                otros=int(input("Digite la nota: "))
                ##Agregar nota a diccionario
            else:
                print("Codigo incorrecto")
    else:
        print("Codigo incorrecto")

