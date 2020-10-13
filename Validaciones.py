import string
import re
import os


Letra = "Andersons                hola";
 


def Q_Espacio(Letra):  
   L1 = Letra.find(" ")+1
   L2 = (Letra.count(" ")+L1)-1
   if Letra.count(" ")>1:
      N1 = Letra[0:L1]; N2 = Letra[L2:len(Letra)]
      Letra=""; 
      Letra = N1+N2
   return Letra



print("Data : ",Q_Espacio(Letra)) 
