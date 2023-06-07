# Calcular 4
def calcular_4():
    valor = input("Ingresa los datos separados por una coma: ")
    datos = valor.split(",")
    D = []
    for element in datos:
        D.append(int(element))

    d = ["m3", "m2", "m1", "p2", "m0", "p1", "p0"]

    d[0] = D[0]
    d[1] = D[1]
    d[2] = D[2]
    d[4] = D[3]

    p0 = ["0", ]
    p1 = ["0", ]
    p2 = ["0", ]

    # P0
    if d[4] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[2] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[0] == 0:
        p0.append(0)
    else:
        p0.append(1)

    cantidad_unos = p0.count(1)
    if cantidad_unos % 2 == 0:
        d[6] = 0
    else:
        d[6] = 1

    # P1
    if d[4] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[1] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[0] == 0:
        p1.append(0)
    else:
        p1.append(1)

    cantidad_unos = p1.count(1)

    if cantidad_unos % 2 == 0:
        d[5] = 0
    else:
        d[5] = 1

    # P2
    if d[2] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[1] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[0] == 0:
        p2.append(0)
    else:
        p2.append(1)

    cantidad_unos = p2.count(1)

    if cantidad_unos % 2 == 0:
        d[3] = 0
    else:
        d[3] = 1

    print(d)

def calcular_5():
    valor=(input("Ingresa los datos separados por una coma:  "))
    datos=valor.split(",")
    D = []
    for element in datos:
        D.append(int(element))

    d=["m4","p3","m3","m2","m1","p2","m0","p1","p0"]

    d[0]=D[0]
    d[2]=D[1]
    d[3]=D[2]
    d[4]=D[3]
    d[6]=D[4]

    p0=["0",]
    p1=["0",]
    p2=["0",]
    p3=["0",]

    # P0
    if d[6]==0:
        p0.append(0)
    else:
        p0.append(1) 

    if d[4]==0:
        p0.append(0)
    else:
        p0.append(1)

    if d[2]==0:
        p0.append(0)
    else:
        p0.append(1)

    if d[0]==0:
        p0.append(0)
    else:
        p0.append(1)


    cantidad_unos = p0.count(1)

    if cantidad_unos % 2 == 0:
        d[8]=0
    else:
        d[8]=1

    #P1
    if d[6]==0:
        p1.append(0)
    else:
        p1.append(1)

    if d[3]==0:
        p1.append(0)
    else:
        p1.append(1)

    if d[2]==0:
        p1.append(0)
    else:
        p1.append(1)

    cantidad_unos = p1.count(1)

    if cantidad_unos % 2 == 0:
        d[7]=0
    else:
        d[7]=1

    #P2

    if d[4]==0:
        p2.append(0)
    else:
        p2.append(1)

    if d[3]==0:
        p2.append(0)
    else:
        p2.append(1)

    if d[2]==0:
        p2.append(0)
    else:
        p2.append(1)


    cantidad_unos = p2.count(1)

    if cantidad_unos % 2 == 0:
        d[5]=0
    else:
        d[5]=1

    #P3

    if d[0]==0:
        p3.append(0)
    else:
        p3.append(1)


    cantidad_unos = p3.count(1)
    if cantidad_unos % 2 == 0:
        d[1]=0
    else:
        d[1]=1

    print(d)

#calcular 6
def calcular_6():
    valor = input("Ingresa los datos separados por una coma: ")
    datos = valor.split(",")
    D = []
    for element in datos:
        D.append(int(element))

    d = ["m5", "m4", "p3", "m3", "m2", "m1", "p2", "m0", "p1", "p0"]

    d[0] = D[0]
    d[1] = D[1]
    d[3] = D[2]
    d[4] = D[3]
    d[5] = D[4]
    d[7] = D[5]

    p0 = ["0", ]
    p1 = ["0", ]
    p2 = ["0", ]
    p3 = ["0", ]

    # P0
    if d[7] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[5] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[3] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[1] == 0:
        p0.append(0)
    else:
        p0.append(1)

    cantidad_unos = p0.count(1)

    if cantidad_unos % 2 == 0:
        d[9] = 0
    else:
        d[9] = 1

    # P1
    if d[7] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[4] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[3] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[0] == 0:
        p1.append(0)
    else:
        p1.append(1)

    cantidad_unos = p1.count(1)

    if cantidad_unos % 2 == 0:
        d[8] = 0
    else:
        d[8] = 1

    # P2
    if d[5] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[4] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[3] == 0:
        p2.append(0)
    else:
        p2.append(1)

    cantidad_unos = p2.count(1)

    if cantidad_unos % 2 == 0:
        d[6] = 0
    else:
        d[6] = 1

    # P3
    if d[1] == 0:
        p3.append(0)
    else:
        p3.append(1)

    if d[0] == 0:
        p3.append(0)
    else:
        p3.append(1)

    cantidad_unos = p3.count(1)
    if cantidad_unos % 2 == 0:
        d[2] = 0
    else:
        d[2] = 1

    print(d)

#calcular 7
def calcular_7():
    valor = input("Ingresa los datos separados por una coma: ")
    datos = valor.split(",")
    D = []
    for element in datos:
        D.append(int(element))

    d = ["m6", "m5", "m4", "p3", "m3", "m2", "m1", "p2", "m0", "p1", "p0"]

    d[0] = D[0]
    d[1] = D[1]
    d[2] = D[2]
    d[4] = D[3]
    d[5] = D[4]
    d[6] = D[5]
    d[8] = D[6]

    p0 = ["0", ]
    p1 = ["0", ]
    p2 = ["0", ]
    p3 = ["0", ]

    # P0
    if d[8] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[6] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[4] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[2] == 0:
        p0.append(0)
    else:
        p0.append(1)

    if d[0] == 0:
        p0.append(0)
    else:
        p0.append(1)

    cantidad_unos = p0.count(1)

    if cantidad_unos % 2 == 0:
        d[10] = 0
    else:
        d[10] = 1

    # P1
    if d[8] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[5] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[4] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[1] == 0:
        p1.append(0)
    else:
        p1.append(1)

    if d[0] == 0:
        p1.append(0)
    else:
        p1.append(1)

    cantidad_unos = p1.count(1)

    if cantidad_unos % 2 == 0:
        d[9] = 0
    else:
        d[9] = 1

    # P2
    if d[6] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[5] == 0:
        p2.append(0)
    else:
        p2.append(1)

    if d[4] == 0:
        p2.append(0)
    else:
        p2.append(1)

    cantidad_unos = p2.count(1)

    if cantidad_unos % 2 == 0:
        d[7] = 0
    else:
        d[7] = 1

    # P3
    if d[2] == 0:
        p3.append(0)
    else:
        p3.append(1)

    if d[1] == 0:
        p3.append(0)
    else:
        p3.append(1)

    if d[0] == 0:
        p3.append(0)
    else:
        p3.append(1)

    cantidad_unos = p3.count(1)
    if cantidad_unos % 2 == 0:
        d[3] = 0
    else:
        d[3] = 1

    print(d)

opción = input("Ingrese la cantidad de bits: ")
if opción == '4':
    calcular_4()
elif opción == '5':
    calcular_5()
elif opción == '6':
    calcular_6()
elif opción == '7':
    calcular_7()
else:
    print("Opción inválida. Por favor, ingrese '4' o '5' o '6' o '7'.")
