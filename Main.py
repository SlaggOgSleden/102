import math
from datetime import datetime
import matplotlib.pyplot as plt
import re

f1 = open("102/datasett/temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r")
f2 = open("102/datasett/trykk_og_temperaturlogg_rune_time.csv.txt", "r")
t1 = f1.read()
t2 = f2.read()

def Split(f):
    x = re.split(';|\n', f)
    return x

def Sorter(x,z,f):
    o = []
    fS = Split(f)
    y = int(len(fS)/(x))-1
    for i in range(y):
        for h in range(x+1):
            if (h == z) and i != 0:
                o.append(fS[z+(i*x)])
    return o

def FormaterDato(x,Fin):
    o =[]

    for i in range(len(x)):
        if Fin == 0:
            o.append(datetime.strptime(x[i],'%d.%m.%Y %H:%M'))
        if Fin == 1:
            o.append(datetime.strptime(x[i],'%m.%d.%Y %H:%M'))
    return o

def FormaterFloat(x):
    o = []
    for i in range(len(x)):
        o.append(float(x[i].translate({44: 46})))
    return o

def Gjennomsnitt(x,y,n):
    for i in range(len(x)):
        for u in range(n):
            g =+ x[i-n]
            h =+ x[i+n]
    gT = g / n
    T = x[i]
    fT = h / n

    print(gT,T,fT)


Dato1 = FormaterDato(Sorter(5,2,t1),0)#Sorter Dato Fil 1
Temp1 = FormaterFloat(Sorter(5,3,t1)) #Sorter Dato Fil 1
Trykk1 = FormaterFloat(Sorter(5,4,t1)) #Sorter Dato Fil 1

Dato2 = FormaterDato(Sorter(5,0,t2),1)
Temp2 = FormaterFloat(Sorter(5,4,t2))
Trykk2 = FormaterFloat(Sorter(5,3,t2))

plt.plot(Dato1,Temp1)
plt.plot(Dato2,Temp2)
plt.show()

Gjennomsnitt(Temp1,Dato1,30)