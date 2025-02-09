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
            nombren = input("Digite su nombre:")
            apellidon = input("Digite su apellido:")
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
                

    elif opcion == 2:
        # Lógica para Trainer
        print("Bienvenido Trainer")
        # Lógica para agregar notas a los campers...

    elif opcion == 3:
        # Lógica para Coordinador
        pass

    else:
        print("Opción incorrecta. Intente nuevamente.")
        break