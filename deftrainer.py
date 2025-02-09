def trainerAgregarNotas():
    print ("Estos son los campers de la clase P_1")
###imprimir la lista de esa clase con notas 
    est=int(input("Digite el numero del camper al que le quiere ingresar una la nota"))
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


def usertrainer():
    print("Bienvenido trainer Pedro Gomez")
    print("Para agregar notas a clase P_1 ingrese (1)")
    print("Para agregar notas a clase P_2 ingrese (2)")
    print("Para salir digite (3)")
    clase=int("Digite su eleccion: ")


    