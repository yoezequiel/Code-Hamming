# 2**p >=p+d+1
valor=(input("Ingresa los datos separados por una coma:  "))
datos=valor.split(",")
D = []
for element in datos:
    D.append(int(element))

d=[1,"p3",1,1,0,"p2",0,"p1","p0"]

d[0]=D[0]
d[2]=D[1]
d[3]=D[2]
d[4]=D[3]
d[6]=D[4]

p=4

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
    print("La cantidad de unos es par.")
    d[8]=0
else:
    print("La cantidad de unos no es par.")
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
    print("La cantidad de unos es par.")
    d[7]=0
else:
    print("La cantidad de unos no es par.")
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
    print("La cantidad de unos es par.")
    d[5]=0
else:
    print("La cantidad de unos no es par.")
    d[5]=1

#P3

if d[0]==0:
    p3.append(0)
else:
    p3.append(1)


cantidad_unos = p3.count(1)
if cantidad_unos % 2 == 0:
    print("La cantidad de unos es par.")
    d[1]=0
else:
    print("La cantidad de unos no es par.")
    d[1]=1

print(d)