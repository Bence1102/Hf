import math
import random

def szamkiiras():
    szam:int = int(input("Kérem adjon meg egy egész számot [200, 920] intervallumban: "))
    if 200 <= szam <= 920:
        elso_szamjegy = int(str(szam)[0])
        print("A szám első számjegye:", elso_szamjegy)
    else:
        print("Hiba: A szám nincs a [200, 920] intervallumban!")
    

    

def negyzetgyok():
    szam:int = int(input("Adj meg egy valós számot: "))

    if szam >= 0:
        gyok_vonas = math.sqrt(szam)
        print("A szám négyzetgyöke:", gyok_vonas)
    else:
        print("Hiba: Negatív számból nem lehet négyzetgyököt vonni!")


def fel6():
    szamok=[]
    i=0
    while i<13:
        rszam:int=int(random.random()*17)-5 
        szamok.append(int(rszam))
        i+=1
    return szamok
def fel6_2(szamok):
    negativ=len([rszam for rszam in szamok if rszam<0])
    pozitiv=len([rszam for rszam in szamok if rszam>0])

    return pozitiv, negativ
def fel6_3(szamok):
    ossz =0
    for rszam in szamok:
        if rszam %2==0:
            ossz+=rszam
    return ossz

def fel6_4(szamok):
    paratlan=0
    paros=0
    for rszam in szamok:
        if rszam %2==0:
            paros+=rszam
        else:
            paratlan+=rszam
    return paratlan, paros

def fel6_5(szamok):
    atlag=0
    for rszam in szamok:
        atlag+=rszam
    if len(szamok)==0:
        return 0
    return atlag/len(szamok)

def fel6_6(szamok):
    if len(szamok)==0:
        return
    max=szamok[0]
    for rszam in szamok:
        if rszam>max:
            max=rszam
    return max


def szamokosszead(szam1=5,szam2=3,szam3=10):
    eredmeny = szam1 + szam2 + szam3
    print(eredmeny)
