def matriz(A,B):

 C=list()    
 fila=len(A)+1
 columna=len(B)+1
 for i in range(fila):
     C.append([0]*(columna))

 j=0
 #Cargo primer fila con la palabra a convertir
 for i in range(len(A)):
     j=i+1
     C[0][j]=A[i]
 z=0
 #Cargo la primer columna con la palabra que queremos
 for i in range(len(A)):
    for j in range(len(B)):
        z=j+1
        C[z][0]=B[j]
        
 return C