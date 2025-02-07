from modulocamper import* 
print("Bienvenido al programa de campuslands")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
opcion=int(input("Digite su opcion: "))
camper={}
if opcion ==1:
    print("¿Que desea hacer?")
    print("1. Inscripcion")
    print("2. Ingresar al perfil")
    opcioncam=int(input(":"))
    if opcioncam==1:
        newcamper={}
        idn=int(input("Ingrese su nùmero de identificaciòn:"))
        newcamper["id"]=idn
        nombren=input("Digite su nombre completo:")
        newcamper["Nombre completo"]=nombren
        direccion=input("Ingrese su direcciòn:")
        newcamper["Direccion"]=direccion
        numcel=int(input("Ingrese su numero de celular:"))
                newcamper["Numero de celular "]
        
             
elif opcion==2:
    print("Bienvenido Trainer")
    n1=int(input("Digite su codigo"))
    if n1==1:
        print("Bienvenido trainer Pedro Gomez")
        print("Para agregar notas a clase P_1 ingrese (1)")
        print("Para agregar notas a clase P_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
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
    elif n1==2:
        print("Bienvenido trainer Miguel Sarmiento")
        print("Para agregar notas a clase M_1 ingrese (1)")
        print("Para agregar notas a clase M_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase M_1")
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

    
    elif n1==3:
        print ("Bienvenido trainer Juan Nariño")
        print("Para agregar notas a clase J_1 ingrese (1)")
        print("Para agregar notas a clase J_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase J_1")
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
    elif n1==4:
        print ("Bienvenido trainer Johan Mejia")
        print("Para agregar notas a clase JO_1 ingrese (1)")
        print("Para agregar notas a clase JO_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase JO_1")
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

    elif n1==5:
        print ("Bienvenido trainer Julian Ojeda")
        print("Para agregar notas a clase JU_1 ingrese (1)")
        print("Para agregar notas a clase JU_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase P_1")
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
        print ("Bienvenida trainer Sue Cardenas")
        print("Para agregar notas a clase S_1 ingrese (1)")
        print("Para agregar notas a clase S_2 ingrese (2)")
        print("Para salir digite (3)")
        clase=int("Digite su eleccion: ")
        if clase==1:
            print ("Estos son los estudiantes de la clase P_1")
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

