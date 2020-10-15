import string
import re
import os
import sys




D1_Votantes = dict();

def Inv_BaseD(Lista):  
    V1= "";Data="";linea=""; V1 = open("Prueba.txt",'r');
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

def BaseD_L():
    i = None; j = 0
    Datos_V = []; Data = ""; Datos_V = Inv_BaseD(Datos_V) ; Votantes=[]
    for i in Datos_V:
      if i != "*" and j!=2 and j!=3:
          Votantes.append(i)
      elif j==2 or j==3:
           if j==2:
               Data = i +" "
           if j==3:
              Data = Data + i
              Votantes.append(Data)
              Data=""
      if i=="*":
         j=-1
      j+=1
    return Votantes      
 
def BaseD_Dicc():
    Data = ""  ; Data = BaseD_L() ; a = 0 ; b = 4
    for i in range(int(len(Data)/4)):
       #print("Cedula : ",Data[i+a],"Inf : ",Data[a+1:b])
       D1_Votantes[Data[i+a]] = Data[a+1:b]
       a+= 4 ; b+=4 
       
       
       
BaseD_Dicc()       

os.system ("cls")
       
for clave in D1_Votantes:
    print(clave)       
       
            




  
    
    
    

