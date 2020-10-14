
import string
import re
import os
import sys



V1 = "" ; V2 = "" ; k=0 ; linea=""
Votantes=[]
Data = ""



V1 = open("Prueba.txt",'r')
for linea in V1.read():   
   if linea!="-" or linea!="\n" or linea!=" ":
      if (re.search( "[A-Za-z]",linea)!=None) or (linea.isnumeric()==True):
           Data = Data + linea
   if linea==" ":
           Votantes.append(Data)
           Data = ""

           

 
 
print("->",Votantes) 
#print("----",linea) 
V1.close()
   