import json
Lec2 = open("tiposParqueaderos.json", "r", encoding = "utf-8")
Lectura2 = json.load(Lec2)
Piso_1 = []
Tipos = ["Automovil","AutomovilElectrico","Motocicleta","Discapacitado"]

for a in range(len(Tipos)):
    Espacios = {}
    for p in range (6):
        Piso = []
        for x in Lectura2["Piso" + str(p+1)]:
            Coordenadas = []
            for b in x:
                if b == a + 1:
                    Coordenadas.append("O")
                else:
                    Coordenadas.append("X")
            Piso.append(Coordenadas)
        Espacios ["Piso" + str(p+1)] = Piso
    with open ("Disponibilidad" + Tipos[a] + ".json", "w") as lec3:
        json.dump(Espacios,lec3)


    