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
        if linea=="*":
           Lista.append("*") 
    V1.close()
    return Lista

def Dicc_BaseD():
    i = None; j = 0
    Datos_V = []; Data = ""; Datos_V = Inv_BaseD(Datos_V)
    for i in Datos_V:
      if i != "*" and j!=2 and j!=3:
        # print("i -> ",i)
      elif j==2 or j==3:
           if j==2:
               Data = i +" "
           if j==3:
              Data = Data + i
              #print("j -> ",Data)
              Data=""
      if i=="*":
         j=-1
      j+=1      
           

os.system ("cls")



Dicc_BaseD()

  
    
    
    

