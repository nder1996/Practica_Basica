import re
import os
import string



def TData(Votante,i,a,List,data,j):
  for j in range(4):
      while Votante[i]!="-":
           if i>=a:
              data=data+Votante[i]
           i+=1
      if Votante[i]=="-":
          print("VOTANTE : ",data)
          List.append(data)
          data=""
          a = a+1 ; i = i+5
    
      





D_Votante = "['1236547000-', '123498007-', 'AREVALOKK MPOLL-', 'ANDERSONS-']" ; List=[]

TData(D_Votante,0,2,List,"",0)



