import string
import re
import os
import sys


V1      = ""
Votantes= []

D1_Votantes = dict();

def Inv_BaseD(Lista):  
    V1 = open("Prueba.txt",'r');Data="";linea=""
    for linea in V1.read():   
        if linea!="-" or linea!="\n" or linea!=" ":
            if (re.search( "[A-Za-z]",linea)!=None) or (linea.isnumeric()==True):
               Data = Data + linea
        if linea==" ":
            if Data!="":
               Lista.append(Data)
               Data = ""
    V1.close()
    return Lista

def Dicc_BaseD():
    i = 0 ; j = 0 ; Datos_V = [] ; 
    Datos_V = Inv_BaseD(Datos_V)
    while i<=len(Datos_V)-1:
     if i!=2+j and i!=3+j and i<=4+j:
         Votantes.append(Datos_V[i+j])
         print("[i+j] ",Datos_V[i+j])
     if i==2+j:
         Votantes.append(Datos_V[2+j]+" "+Datos_V[3+j])
         print("[i+2] ",Datos_V[2+j]+" "+Datos_V[3+j])
     if i==5+j:
           j+=6;
     i+=1


os.system ("cls")

Dicc_BaseD()

#print(" ",Votantes)    
    
    
    

