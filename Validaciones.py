import string
import re
import os
import sys


V1 = ""; V2 = "";k=0;Votantes=[];

V1    = open("Prueba.txt","r") 
V2 = V1.readlines()
V1.close() 
   

while k<=len(V2):
    Datos=""; Com =""; i=0 ;j=0
    Datos = V2[0]
    while i<=2:
       while Datos[j]!="-":
          Com = Com + Datos[j]
          j+=1
       Com = Com.replace(" ","")
       Votantes.append(Com)
       Com="";i+=1;j+=1
    if len(Votantes)%3==0:
       Com = ""
       Com = Datos[j:Datos.find("*")]
       Com = Com.replace(" ","")
       Votantes.append(Com)
    k+=1  
 
print("Actualizacion : ",Votantes)  
