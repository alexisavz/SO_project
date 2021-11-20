from tabulate import tabulate
from fifo import get_random_stream          # para no repetir codigo utilizamos la funcion en el modulo FIFO.py


procesos = get_random_stream(num_solicitudes=30)
procesos_en_memoria = []

marcos = [[],[],[],[],[]]                   #Lista que contendra las listas de los marcos
fallos = 0                                  #Numero de fallos
lista_fallos = []                           #Lista que contiene las posiciones de los fallos

for i in range(len(procesos)):              #Se llenan los arreglos con placeholders
    for j in range(len(marcos)):
        marcos[j].append(0)

print(range(len(procesos)))

for proceso in range(len(procesos)):
    if (proceso == 0) :                         #Si es el primer proceso simplemente se añade a memoria
            marcos[0][0] = procesos[0]          #El primer marco toma el proceso en la primera posicion
            fallos += 1                         #Se incrementa el numero de fallos
            lista_fallos.append("X")            #Se añade la posicion a la lista de fallos
            procesos_en_memoria.append(procesos[0]) #Se añade el proceso a una lista de procesos usados donde el primero es el menos reciente
    else:
        for marco in range(len(marcos)):
             marcos[marco][proceso] = marcos[marco][proceso-1]       # Se copia el tiempo pasado
        if(procesos[proceso] in procesos_en_memoria):       # Si el proceso ya esta en memoria
            procesos_en_memoria.remove(procesos[proceso])   # Se remueve de la lista de usados (en caso de que este en medio)
            procesos_en_memoria.append(procesos[proceso])   # Se añade al final de la lista por que es el recien usado
            lista_fallos.append(" ")                        # Se añade un espacio en blanco de que no hubo fallo
        elif(procesos[proceso not in procesos_en_memoria]):             # Si no esta el proceso en memoria
            done = False
            fallos += 1                                                 # Se incrementa el numero de fallos
            lista_fallos.append("X")                                    # Se añade la posicion a la lista de fallos
            for marco in range(len(marcos)):                            # Se revisa si aun existen placeholders en el tiempo actual
                    if(marcos[marco][proceso] == 0):                    # En cuanto se encuentre un 0 solo lo pone en esa posicion
                        marcos[marco][proceso] = procesos[proceso] 
                        procesos_en_memoria.append(procesos[proceso])   # Se añade al final de la lista por que es el recien usado 
                        done = True                                     # Para que ya no pase por el loop siguiente
                        break                                           # Y se escapa del loop
            # Si no hay placeholders se busca el el menos reciente (primer elemento) en el marco 
            # temp = procesos_en_memoria[0]                               # el primero de elemento es el que se reemplazara 
            for marco in range(len(marcos)):                            # Se revisa en donde esta el menos reciente en los marcos
                    if (done):                                          # Si si habia 0s no es necesario este loop
                        break
                    else:                                               # Si no habia 0s falta el reemplazo         
                        if(marcos[marco][proceso] == procesos_en_memoria[0]):
                            marcos[marco][proceso] = procesos[proceso]  # Se hace el reemplazo
                            procesos_en_memoria.remove(procesos_en_memoria[0])   # Se remueve de la lista de procesos en memoria
                            procesos_en_memoria.append(procesos[proceso])        # Se añade al final al recien usado
                            break  

#Se agregan los encabezados de la tabla, ademas de especificar el marco para despues imprimirse
marcos[0].insert(0,"Marco 0: ")
marcos[1].insert(0,"Marco 1: ")
marcos[2].insert(0,"Marco 2: ")
marcos[3].insert(0,"Marco 3: ")
marcos[4].insert(0,"Marco 4: ")
procesos.insert(0,"Marcos")
rendimiento = (30-fallos)/30                #Se obtiene el rendimiento

print('Utilizando el algoritmo de reemplazo LRU :')
print(tabulate(marcos, headers=procesos))
print("El rendimiento del algoritmo es de: " + str(rendimiento))
