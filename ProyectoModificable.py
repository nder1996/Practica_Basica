import string
import re
import os


Votantes=[];Lider_V=[]

def BaseD(DatosV):
   #Si Hay Algun Error
   #except NameError:
   try:
       Votantes = open("DVotantes.txt", "a+")
       Votantes.write("%s\n"%(DatosV))
       Votantes.close()
   except:
     print("Error Al Llenar Los Datos Al Archivo")

def InvBase():
    try:
      linea="";i=0
      DatosV = open("DVotantes.txt","r")
      print("\n")
      for linea in DatosV.readlines():
         Votantes.append(linea)
      DatosV.close()
    except:
      print("Error Al Almacenar Los Datos Al Archivo")

def ValidadorC(Variable,Tipo):
    Busq = re.search(r'[\d]',Variable)
    if Tipo==1:
       if Busq==None:
        os.system ("cls")
        print("------------------------------------------------") 
        print("Ingrese Solo Numeros Para Llenar Este Campo")
        print("----------------------------------------------\n") 
        IngresarD()
    if Tipo==0:
        if Busq!=None:
          os.system ("cls")
          print("----------------------------------------------") 
          print("Ingrese Solo Letras Para Llenar Este Campo")
          print("--------------------------------------------\n") 
          IngresarD()

def GuardarD(Nombre,Apellido,Cedula,Cedula_l,DatosV):
  Nombre=Nombre+"-";Apellido=Apellido+"-";Cedula=Cedula+"-";Cedula_l=Cedula_l+"-"
  DatosV.append(Cedula);DatosV.append(Cedula_l);DatosV.append(Apellido);DatosV.append(Nombre);
  print("DATOS DE VOTANTE : ",DatosV);
  BaseD(DatosV) 

def MostrarD():
    print("\nNombre               : ",Votantes[0]);print("\nApellido             : ",Votantes[1]);print("\n# De Cedula          : ",Votantes[2]);print("\n# Cedula De Su Lider : ",Votantes[3])
    print("\n")

def BuscarV(Cedula):
   try:
      Votantes = open("DVotantes.txt","r");c=0
      for linea in Votantes.readline():
         print("#: ",c," ",linea)
         c+=1
      Votantes.close()
   except:
      print("Error Al Buscar Los Datos Al Archivo") 

def IngresarD():    
   DatosV=[]
   """
   Nombre  = input("\nIngrese Su Nombre    : ")
   ValidadorC(Nombre,0);
   Apellido= input("\nIngrese Su Apellido  : ")
   ValidadorC(Apellido,0);
   Cedula = input("\nIngrese Su # Cedula  : ")
   Cedula = Cedula.replace(" ", "")
   ValidadorC(Cedula,1);
   Cedula_l= input("\nIngrese El # Cedula De Su Lider : ")
   Cedula_l= Cedula_l.replace(" ", "")
   ValidadorC(Cedula_l,1);
   #GuardarD(Nombre,Apellido,Cedula,Cedula_l)
   """
   GuardarD("ANDER","AREVALOKK MPOLL kkkk","1236547000555","77777777123498007",DatosV)
   


InvBase()
print("Votantes : ",Votantes[0][0])

#IngresarD()
#InvBase()
#print("VOTANTES : ",Votantes)
#Dato=None;TDatos(Dato)
#IngresarD()
#BaseD(["1081827159","0000012345","ANDERSONS","AREVALO MADRID"])
#DatosV=[]
#InvBase()
#print("VOTANTES : ",Votantes[0])
#i=2;Nombre=""
"""
while Votantes[0][i]!="-":
   Nombre = str(Nombre) + str(Votantes[0][i])
   i+=1
Apellido="";i+=5
while Votantes[0][i]!="-":
   Apellido = str(Apellido) + str(Votantes[0][i])
   i+=1

print("Apellido : ",len(Apellido));
#print("Eliminado N : ",Votantes)
"""
#BuscarV("1081827159")

