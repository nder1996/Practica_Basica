
import string
import re
import os
import sys



V1 = "" ; V2 = "" ; k=0 ; linea="" ; i=0 ; j=0
Votante=[] ; Com_Votantes=[]

Data = ""



V1 = open("Prueba.txt",'r')

for linea in V1.read():   
   if linea!="-" or linea!="\n" or linea!=" ":
      if (re.search( "[A-Za-z]",linea)!=None) or (linea.isnumeric()==True):
           Data = Data + linea
   if linea==" ":
          if Data!="":
             Com_Votantes.append(Data)
             Data = ""
   if linea=="*":
      Com_Votantes.append("*")

V1.close()

os.system ("cls")

while i<=len(Com_Votantes)-1:
     print("Votantes{I} : ",Com_Votantes[i])
     if i!=2+j and i!=3+j and i<=4+j:
         Votante.append(Com_Votantes[i+j])
     if i==2+j:
         Votante.append(Com_Votantes[2+j]+" "+Com_Votantes[3+j])
     if i==5: 
           j+=6;
     i+=1

 
print("->",Votante)
#print("----",linea) 
V1.close()
   