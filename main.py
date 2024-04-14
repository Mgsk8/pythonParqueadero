tauto = 0
tmoto = 0
ingresocarro = []
ingresomoto = []
acumulador1 = 0
acumulador2 = 0
totalm = 0
totalc = 0
cuentat = 0
def menu():
    opc = 1
    while opc > 0 and opc < 7:
        print("menú principal")
        print("1. tarifas")
        print("2. ingresar vehiculo")
        print("3. buscar vehiculo")
        print("4. mostrar vehiculos")
        print("5. salida vehiculo")
        print("6. cuadre de caja")
        print("7. salir")
        opc = int(input("ingrese una opcion: "))
        if opc==1:
            tarifas()
        if opc==2:
            ingresarvehiculo()
        if opc==3:
            buscarvehiculo()
        if opc==4:
            mostrar()
        if opc==5:
            salida()
        if opc==6:
            cuadre()
def tarifas():
    opc = 1
    while opc > 0 and opc < 4:
        print("1. ingresar tarifas")
        print("2. mostrar tarifas")
        print("3. modificar tarifas")
        print("4. regresar al menu principal")
        opc = int(input("ingrese una opcion: "))
        if opc==1:
            ingresartarifas()
        if opc==2:
            mostrartarifa()
        if opc==3:
            modificartarifa()

def ingresartarifas():
    opc = 1
    while opc>0 and opc<3:
        print("1. ingresar tarifa automovil")
        print("2. ingresar tarifa motocicleta")
        print("3. regresar al sub menu tarifas")
        opc = int(input("ingrese una opcion: "))
        if opc==1:
            global tauto
            tauto = float(input("ingrese el valor a cobrar por minuto para automoviles: "))
        if opc==2:
            global tmoto
            tmoto = float(input("ingrese el valor a cobrar por minuto para motocicletas: "))

def mostrartarifa():
    print("valor por minuto auto: ",tauto)
    print("valor por minuto moto: ",tmoto)
def modificartarifa():
    opc = 1
    while opc>0 and opc<3:
        print("1. modificar tarifa automovil")
        print("2. modificar tarifa motocicleta")
        print("3. regresar al sub menú tarifas")
        opc = int(input("ingrese una opción: "))
        if opc==1:
            modificarauto()
        if opc==2:
            modificarmoto()
def modificarauto():
    global tauto
    tauto = float(input("ingrese el nuevo valor a cobrar por minuto para automóviles: "))
def modificarmoto():
    global tmoto
    tmoto = float(input("ingrese el nuevo valor a cobrar por minuto para motocicletas: "))
def ingresarvehiculo():
    datos = []
    tipo = input("tipo de vehiculo (ingrese a si es auto o m si es moto): ")
    if tipo=="a":
        numero = input("ingrese la placa AAA###: ")
    if tipo=="m":
        numero = input("ingrese la placa AAA##A: ")
    horaentrada = int(input("en formato 24 horas ingrese la hora de entrada (hhmm): "))
    nombre = input("ingrese el nombre del cliente: ")
    horasalida = ""
    C = ""
    total = ""
    n = len(ingresocarro)
    for i in range(n):
        if ingresocarro[i][1]==numero:
            print()
            print("la placa ya esta registrada")
            print()
            menu()
    s = len(ingresomoto)
    for j in range(s):
        if ingresomoto[j][1]==numero:
            print()
            print("la placa ya esta registrada")
            print()
            menu()
    if tipo=="a":
        datos.append(tipo)
        datos.append(numero)
        datos.append(horaentrada)
        datos.append(nombre)
        datos.append(horasalida)
        datos.append(C)
        datos.append(total)
        ingresocarro.append(datos)

    if tipo=="m":
        datos.append(tipo)
        datos.append(numero)
        datos.append(horaentrada)
        datos.append(nombre)
        datos.append(horasalida)
        datos.append(C)
        datos.append(total)
        ingresomoto.append(datos)
def buscarvehiculo():
    opc = 1
    while opc > 0 and opc < 3:
        print("1. buscar motos")
        print("2. buscar carro")
        print("3. regresar al menú principal")
        opc = int(input("ingrese una opcion: "))
        if opc==1:
            buscarmoto()
        if opc==2:
            buscarcarro()

def buscarmoto():
    numero = input("ingrese el numero de la placa: ")
    n = len(ingresomoto)
    contador = 0
    for i in range(n):
        if ingresomoto[i][1]==numero:
            print("numero de placa: ",numero)
            print("vehiculo tipo: moto")
            print("hora de ingreso: ",ingresomoto[i][2])
            print("hora de salida: ",ingresomoto[i][4])
            print("nombre: ",ingresomoto[i][3])
            print("numero minutos:",ingresomoto[i][5])
            print("total:",ingresomoto[i][6])
            contador+=1
    if contador==0:
        print("vehiculo no encontrado")
def buscarcarro():
    numero = input("ingrese el numero de la placa: ")
    n = len(ingresocarro)
    contador = 0
    for i in range(n):
        if ingresocarro[i][1] == numero:
            print("numero de placa: ", numero)
            print("vehiculo tipo: carro")
            print("hora de ingreso: ", ingresocarro[i][2])
            print("hora de salida: ", ingresocarro[i][4])
            print("nombre: ", ingresocarro[i][3])
            print("numero minutos:", ingresocarro[i][5])
            print("total:", ingresocarro[i][6])
            contador+=1
    if contador==0:
        print("vehiculo no encontrado")
def mostrar():
    opc = 1
    while opc > 0 and opc < 3:
        print("1. mostrar todos los automoviles")
        print("2. mostrar todos las motos")
        print("3. regresar al menú principal")
        opc = int(input("ingrese una opcion: "))
        if opc==1:
            mostrarauto()
        if opc==2:
            mostrarmoto()

def mostrarauto():
    n = len(ingresocarro)
    print("")
    print("tipo de vehiculo : automoviles")
    print("placa", "ingreso", "salida", "minuto", "total")
    for i in range(n):
        print(ingresocarro[i][1]," ",ingresocarro[i][2]," ",ingresocarro[i][4]," ",ingresocarro[i][5],"  ",ingresocarro[i][6],end="  ")
        print()
    print()
def mostrarmoto():
    n = len(ingresomoto)
    print("")
    print("tipo de vehiculo : motocicleta")
    print("placa","ingreso","salida","minuto","total")
    for i in range(n):
        print(ingresomoto[i][1]," ",ingresomoto[i][2]," ",ingresomoto[i][4]," ",ingresomoto[i][5],"  ",ingresomoto[i][6],end="  ")
        print()
    print()
def salida():
    global acumulador1
    global acumulador2
    tipo = input("tipo de vehiculo (a o m): ")
    if tipo=="a":
        numero = input("ingrese el numero de la placa AAA### : ")
        n = len(ingresocarro)
        contador1 = 0
        for i in range(n):
            if ingresocarro[i][1] == numero:
                horasalida = int(input("en formato 24 horas ingrese la hora de salida(hsms): "))
                he = ingresocarro[i][2] // 100
                me = ingresocarro[i][2] % 100
                hs = horasalida // 100
                ms = horasalida % 100
                A = (he * 60) + me
                B = (hs * 60) + ms
                if B > A:
                    C = B - A
                total = C * tauto
                ingresocarro[i][4] = horasalida
                ingresocarro[i][5] = C
                ingresocarro[i][6] = total
                acumulador1 += total
                contador1 += 1
        if contador1==0:
            print("el vehiculo no esta registrado")

    if tipo=="m":
        numero = input("ingrese el numero de la placa AAA##A: ")
        n = len(ingresomoto)
        contador2 = 0
        for i in range(n):
            if ingresomoto[i][1] == numero:
                horasalida = int(input("en formato 24 horas ingrese la hora de salida(hsms): "))
                he = ingresomoto[i][2] // 100
                me = ingresomoto[i][2] % 100
                hs = horasalida // 100
                ms = horasalida % 100
                A = (he * 60) + me
                B = (hs * 60) + ms
                if B > A:
                    C = B - A
                total = C * tmoto
                ingresomoto[i][4] = horasalida
                ingresomoto[i][5] = C
                ingresomoto[i][6] = total
                acumulador2 += total
                contador2+=1
        if contador2==0:
            print("el vehiculo no esta registrado")
def cuadre():
    global totalm
    global totalc
    global cuentat
    totalc = acumulador1
    totalm = acumulador2
    cuentat = acumulador1 + acumulador2
    if totalm!=0:
        print("total automoviles = ",totalc)
    else:
        print("total vehiculos = ", totalc)
        print("asegurese de haber registrado la salida del vehiculo")
    if totalc!=0:
        print("total motocicletas = ",totalm)
    else:
        print("total motocicletas = ",totalm)
        print("asegurese de haber registrado la salida del vehiculo")
    if cuentat!=0:
        print("total vehiculos = ",cuentat)
    else:
        print("total vehiculos = ", cuentat)
        print("asegurese de haber registrado la salida del vehiculo")
menu()