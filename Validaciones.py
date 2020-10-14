import string
import re
import os
import sys



V = "" ; Votantes=[] ; Datos = "" ;i=0;j=0;Com=""
V    = open("Prueba.txt","r") 
Data = V.readlines()
Votantes.close() 
   


Datos = V[0]

while Datos[i]!="*": 
  while Datos[j]!="-":
      Com = Com + Datos[j]
      j+=1
  Votantes.append(Com)
  Com=""  

 
print("Actualizacion : ",D_V)  
