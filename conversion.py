from matriz import *

pal1=input("Ingrese una palabra: ")
pal2=input("Ingrese la segunda palabra: ")
A=list(pal1)
B=list(pal2)
#Tabla cargada
#A representa la primer fila
#B representa la primer columna
#El primer elemento de la matriz es 0
tabla=list()
tabla=matriz(A,B)

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if(i==j and tabla[0][j]==tabla[i][0]):
            tabla[i][j]=tabla[j][0]

print(tabla)


