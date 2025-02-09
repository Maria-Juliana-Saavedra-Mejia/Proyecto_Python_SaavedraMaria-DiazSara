def agregartrainers ():
 newtrainer = abrirJSON()

idn = int(input("Ingrese su número de identificación:"))
nombren = (input("Ingrese su(s) nombre(s):"))
apellidon =( input("Digite sus apellidos:"))
direccion = input("Ingrese su dirección:")
acudienten = input("Ingrese el nombre de su acudiente:")
numcel = int(input("Ingrese su número de celular:"))
numfijo = int(input("Ingrese su número de teléfono:"))
newtrainer["Informacion"][idn]={
                "Nombre": nombren,
                "Apellido": apellidon,
                "Direccion": direccion,
                "Acudiente": acudienten,
                "Numero de celular": numcel,
                "Numero de telefono": numfijo,
                "Estado": {
                "En proceso": False,
                "Inscrito": True,
                "Aprovado": False,
                "Rechazao": False,
                "Cursando": False,
                "Graduado": False,
                "Expulado": False,
                "Retirado": False
                }}
guardarJSON(newtrainer)