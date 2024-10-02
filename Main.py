import math
import datetime

with open("102/datasett/temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as f1:
    t1 = f1.read




x1 = [0] #Klokkeslett fil 1
y11 = [0] #Temperatur fil 1
y12 = [0] #Trykk fil 1


def SplitLinjer(f):
    x = f.splitlines(";")
    return x

def LesDato(x,f):
    for i in range(100):
        if((i-1) % 3):
            g = f.readlines(i)
            print(g)


def LesTrykk(x,f):



def LesTemp(x,f):



