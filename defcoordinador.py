import json
def abrirJSON():
    dicFinal={}
    with open('./trainers.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./trainers.json",'w') as outFile:
        json.dump(dic,outFile)

def agregartrainers ():       
newtrainer = abrirJSON()
nomtn = input("Ingrese el nombre del nuevo trainer:")
salonn = input("Ingrese el salon del nuevo trainer :")
fechain = input("Digite la fecha de inicio:")
fechafn = input("Digite la fecha de finalizacion:")
horarion = input("Ingrese el horario:")
rutan =input("Ingrese la ruta a seguir:")
newtrainer["Trainers"][salonn]={
                "Profesor": nomtn,
                "Salon": salonn,
                "Fecha de inicio": fechain,
                "Fecha de finalizacion": fechafn,
                "Horario": horarion,
                "Ruta": rutan}
if rutan=="Java":
            newtrainer["Trainers"][salonn]["Modulos"]=[
            "Introducción a la Programación",
            "Python",
            "HTML/CSS",
            "Scrum",
            "Git",
            "JavaScript",
            "Intro Back",
            "Intro BBDD",
            "MySQL",
            "Java",
            "PostgreSQL",
            "SpringBoot" 
            ] 
elif rutan=="NodeJS":
            newtrainer["Trainers"][salonn]={
            "Modulos": [
            "Introducción a la Programación",
            "Python",
            "HTML/CSS",
            "Scrum",
            "Git",
            "JavaScript",
            "Intro Back",
            "Intro BBDD",
            "MongoDB",
            "MySQL",
            "Express"
        ]}
elif rutan==".NET":
            newtrainer["Trainers"][salonn]={
            "Modulos": [
            "Introducción a la Programación",
            "Python",
            "HTML/CSS",
            "Scrum",
            "Git",
            "JavaScript",
            "Intro Back",
            "Intro BBDD",
            "MongoDB",
            "MySQL",
            "Express"
        ]}

guardarJSON(newtrainer)
