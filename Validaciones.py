import string
import re
import os
import sys



V1 = "";V2=""; Votantes=[] ; Datos = "" ;i=0;j=0;Com=""
V1    = open("Prueba.txt","r") 
V2 = V1.readlines()
V1.close() 
   


Datos = V2[0]

while i<=2:
  while Datos[j]!="-":
      Com = Com + Datos[j]
      j+=1
  Votantes.append(Com)
  Com=""  
  i+=1
  j+=1
if len(Votantes)==3:
      Com = ""
      Com = Datos[j:Datos.find("*")]
      Votantes.append(Com)
      #print("DATOS : ",Com)
      
 
print("Actualizacion : ",Votantes)  
