def Retorno_Menu():
    Continuar = input("¿Volver al menú? S (para sí) / N (para no)\n>> ")
    if Continuar != "S" and Continuar != "s":
        Rest = input("El programa va a finalizar. ¿Está seguro? S (para sí) / N (para no)\n>> ")
        if Rest != "N" and Rest != "n":
            Continuar = "N"
            print ("El programa ha finalizado.")
        else:
            Continuar = "S"
    return Continuar
#Menu.
import json
from os import close
from typing import KeysView


Continuar = "S"
while Continuar == "S" or Continuar == "s":
    print("Bienvenido al sistema de administración de parqueadero JAVEPARK.")
    print("Escoger opción:")
    Bienvenida = eval(input("1. Realizar registro de nuevo usuario.\n2. Ingreso de vehículo.\n3. Retiro de vehículo.\n4. Impirimir estadísticas.\n>> "))
        
    #Registro=[]    
    if Bienvenida == 1:
        Registro = []
        print ("Para realizar su registro digite todos los datos que se le van solicitar.\n")
        
        valor = input("Nombres y apellidos:\n>> ")
        Registro.append(valor)

        valor = int(input("Número de identificación:\n>> "))
        Registro.append(valor)

        valor = int(input("Tipo de usuario:\nSi Estudiante digite 1.\nSi Profesor digite 2.\nSi  Personal Administrativo digite 3.\n>> "))
        if valor == 1:
            valor = "Estudiante" 
        elif valor == 2:
            valor = "Profesor"
        elif valor == 3:
            valor = "Personal Administrativo"
        Registro.append(valor)

        valor = input("Placa:\n>> ")
        Registro.append(valor)

        valor = int(input("Tipo de vehículo:\nSi Automóvil digite 1.\nSi Automóvil eléctrico digite 2.\nSi Motocicleta digite 3.\nSi Categoria de discapacitados digite 4.\n>> "))
        if valor  == 1:
            valor = "Automóvil"
        elif valor == 2:
            valor = "Automóvil Eléctrico"
        elif valor == 3:
            valor = "Motocicleta"
        elif valor == 4:
            valor = "Discapacitado"
        Registro.append(valor)
        
        valor = int(input("Plan de pago:\nSi Mensual digite 1.\nSi Diario digite 2.\n>> "))
        if valor == 1:
            valor = "Mensualidad"
        else: 
            valor = "Diario"
        Registro.append(valor)
            
        print(Registro)
        Lec = open("usuarios.json", "r", encoding = "utf-8")
        Lectura1 = json.load(Lec)
        actualizado = False
        i = 0
        for a in Lectura1["usuarios"]:
            c = a[1]
            b = Registro[1]
            if b == c:
                for r in range(6):
                    Lectura1["usuarios"][i][r] = Registro[r]
                a = Registro
                print("Datos de usuario existente actualizados.")
                actualizado = True
             
            i+=1

        if actualizado == False: 
            Lectura1["usuarios"].append(Registro)
            print("Nuevo usuario agregado.")   
        print(Lectura1)
        Lec.close() 
        with open("usuarios.json", "w", encoding = ("utf-8")) as file:
            json.dump(Lectura1, file, indent=4, ensure_ascii = False)

            
        Continuar = Retorno_Menu()

    #Ingreso=[]
    elif Bienvenida == 2:
        Placa = input("Digite su placa.\n>>")
        print("\n")
        Lec = open("usuarios.json", "r", encoding = "utf-8")
        Lectura1 = json.load(Lec)
        Lec.close()
        Pregis = False 
        Lista1 = []
        Nombrex = "Visitor"
        Identidex = 1001
        Aux = ""
        for a in Lectura1["usuarios"]:
            w = a [3]
            if Placa == w:
                Pregis = True
                if a[2] == "Estudiante":
                    Aux = "E"
                elif a[2] == "Profesor":
                    Aux = "P"
                elif a[2] == "Personal Administrativo":
                    Aux = "A"

        if Pregis == False:
            #Crear datos.
            Tvehiculo = ""
            print ("Tipo de vehiculo:\nSi es Automóvil digite 1.\nSi es Automóvil electrico digite 2.\nSi es motocicleta digite 3.\nSi categoria de discapacitados digite 4. ")
            print ("\n")
            vehiculo = eval(input("Digita el tipo de vehículo.\n>> "))
            if vehiculo  == 1:
                Tvehiculo = "Automóvil"
            elif vehiculo == 2:
                Tvehiculo = "Automóvil Eléctrico"
            elif vehiculo == 3:
                Tvehiculo = "Motocicleta"
            elif vehiculo == 4:
                Tvehiculo = "Discapacitado" 
            
            Lista1.append(Nombrex)
            Lista1.append(Identidex)
            Lista1.append("Visitante")
            Lista1.append(Placa)
            Lista1.append(Tvehiculo) 
            Lista1.append("Diario")
            Aux = "V"
            Lectura1["usuarios"].append(Lista1)
            with open ("usuarios.json", "w") as file5:
                json.dump(Lectura1,file5,indent=4, ensure_ascii = False)
        
        Lec2 = open("tiposParqueaderos.json", "r", encoding = "utf-8")
        Lectura2 = json.load(Lec2)

        #Compruebo si la opcción es viable.
        bandera = False

        with open ("Disponibilidad" + Tvehiculo + ".json", "r") as lec3: 
            revision = json.load(lec3)
            for p in range (6):
                for x in revision["Piso" + str(p+1)]:
                    for b in x:
                        if b == "O":
                            bandera = True

            if bandera == False:
                print ("No hay sitios disponibles para ese tipo de vehículo.")
                Continuar = Retorno_Menu()
            
            else :
                print ("El ingreso es válido.")
                print ("Los lugares disponibles están señalados con el carácter (O) mientras que los ocupados están señalados por una (X)")
                #Mostrar lugares ocupables.
                for p in range (6):
                    print ("\nPiso " + str(p+1))
                    for x in revision["Piso" + str(p+1)]:
                        Aux2 = ""
                        for i in x:
                            if i == "O":
                                Aux2 += "O "
                            else:
                                Aux2 += "X "

                        print (Aux2)
                print("")
                Pisop = eval(input("Digite el número del piso en el que se va a ubicar.\n>> ")) 
                Fila = eval(input("Ingrese el número de la fila en que se va a ubicar.\n>> "))
                Columna = eval(input("Ingrese el número de la columna en la que se va a ubicar.\n>> "))

                revision["Piso" + str(Pisop)][Fila-1][Columna-1]= Aux

            with open ("Disponibilidad" + Tvehiculo + ".json", "w") as lec3:
                json.dump(revision,lec3)            
            Continuar = Retorno_Menu()


    #Retiro.
    elif Bienvenida == 3:
        PlacaS = input("Digite la placa: \n>> ")
        lec7 = open("usuarios.json", "r", encoding = "utf-8")
        Lectura3 = json.load(lec7)
        lec7.close()
        Ganacia = 0
        PisopS = eval(input("Digite el número del piso en el que estaba ubicado.\n>> ")) 
        FilaS = eval(input("Del piso " + str (PisopS) + " digite la fila en la que se ubico.\n>> " ))
        ColumnaS = eval(input("Del piso " + str (PisopS) + " digite la columna en la que se ubico.\n>> "))
        Tiempo = eval(input("Digite las horas que ha permanecido en el parqueadero:\n>> "))
        print("\n")

        I = 0
        Esta = False
        for a in Lectura3["usuarios"]:
            w = a [3]
            if PlacaS == w:
                Esta = True
                Tvehiculo = a[4]

                if Tvehiculo == "Automóvil":
                    Tvehiculo = "Automovil"

                elif Tvehiculo == "Automóvil Eléctrico":
                    Tvehiculo = "AutomovilElectrico"

                Tusuario = a[2]

                r = a [5]
                if r == "Mensualidad":
                    Ganacia = 0
                    print ("Este usuario no tine cobro.")
                
                

                else:
                
                    if a [2] == "Estudiante":
                        Ganacia = Tiempo * 1.000

                    elif a [2] == "Profesor":
                        Ganacia = Tiempo * 2.000
                    
                    elif a [2] == "Personal Administrativo":
                        Ganacia = Tiempo * 1.500
                    
                    else:                        
                        Ganacia = Tiempo * 3000
                    
                    print ("El cobro es: " + str(Ganacia))
                if a[2] == "Visitante":
                    Tindice = I
            I += 1                 
        if Esta == False:
                print ("El vehiculo de placa " + PlacaS + " no esta dentro del parqueadero.") 

        
        

        lec9 = open("Disponibilidad" + Tvehiculo + ".json", "r")
        revision3 = json.load(lec9)
        lec9.close()
        revision3["Piso" + str(PisopS)][FilaS-1][ColumnaS-1]="O"

        with open ("Disponibilidad" + Tvehiculo + ".json", "w") as lec4:
            json.dump(revision3,lec4) 
        
        if Tusuario == "Visitante":
            del Lectura3["usuarios"][Tindice]
        
        with open("usuarios.json", "w", encoding = ("utf-8")) as file:
            json.dump(Lectura3, file, indent=4, ensure_ascii = False)


        Continuar = Retorno_Menu()

    #Imprimir estadisticas.
    elif Bienvenida == 4:
        lec = open("usuarios.json", "r")
        Lectura4 = json.load(lec)
        vexusuario = [0,0,0,0]
        vexvehiculos = [0,0,0,0]
        ocxpisos = [0,0,0,0,0,0]
        Lusuarios = ["E", "P", "A", "V"]
        Lusuarios2 = ["Estudiante", "Profesor", "Personal Administrativo", "Visitante"]
        Tipos = ["Automovil","AutomovilElectrico","Motocicleta","Discapacitado"]
        for e in range(len(Tipos)):
            with open ("Disponibilidad" + Tipos[e] + ".json", "r") as lec3:      #Verficar usuarios.
                revision = json.load(lec3)
                for p in range (6):
                    for x in revision["Piso" + str(p+1)]:
                        for b in x:
                            for a in range(len(Lusuarios)):
                                if b == Lusuarios[a]:
                                    vexusuario[a] += 1
                            if b == "E" or b == "P" or b == "A" or b == "V":
                                vexvehiculos[e] += 1
                                ocxpisos[p] += 1
        
        pglobal = 0
        for  d in ocxpisos:
            pglobal += d
        pglobal = (pglobal/550) * 100

        plocal = [0,0,0,0,0,0]
        for d in range(len(ocxpisos)-1):
            plocal[d] = ocxpisos[d]
        plocal[5] = ocxpisos[5]/2
        

        Rest = open ("estadisticas.txt", "w")

        Aux3 = "Cantidad de vehículos por usuario:\n" 
        for a in range (4):
            Aux3+= Lusuarios2[a] +": " + str(vexusuario[a]) + "\n"
        Aux3 += "\n"

        Aux3 += "Vehículos estacionados según el tipo:\n" 
        for b in range (4):
            Aux3 += Tipos[b] + ": " + str(vexvehiculos[b]) + "\n"
        Aux3 += "\n"

        Aux3 += "Porcentaje de ocupación global:\n"
        Aux3 += str(pglobal) + "%" + "\n"
        Aux3 += "\n"

        Aux3 += "Porcentaje de ocupación por pisos:\n"
        for p in range (6):
            Aux3 += "Piso " + str(p+1) + ": " + str (plocal[p]) + "%\n"
        Aux3 += "\n"

        a = Rest.write(Aux3)
        Rest.close()
        Continuar = Retorno_Menu()


    else:
        print("Opción no válida.")
        print("")
        Continuar = "S"


    


 
 