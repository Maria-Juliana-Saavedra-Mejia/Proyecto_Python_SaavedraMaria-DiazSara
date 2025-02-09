import json
def abrirJSON():
    dicFinal={}
    with open('./camper.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./camper.json",'w') as outFile:
        json.dump(dic,outFile)

        

