
def remplazo_FIFO(string_random):

    procesos = string_random
    procesos_en_memoria = []

    marcos = [[],[],[],[],[]]                   #Lista que contendra las listas de los marcos
    fallos = 0                                  #Numero de fallos
    lista_fallos = []                           #Lista que contiene las posiciones de los fallos

    for i in range(len(procesos)):              #Se llenan los arreglos con placholders
        for j in range(len(marcos)):
            marcos[j].append(0)

    for proceso in range(len(procesos)):
        if (proceso == 0) :                     #Si es el primer proceso simplemente se añade a memoria
            marcos[0][0] = procesos[0]          #El primer marco toma el proceso en la primera posicion
            fallos += 1                         #Se incrementa el numero de fallos
            lista_fallos.append("X")        #Se añade la posicion a la lista de fallos
            procesos_en_memoria.append(procesos[0]) #Se añade el proceso a una fila de procesos
        else:
            for marco in range(len(marcos)):
                marcos[marco][proceso] = marcos[marco][proceso-1] #Se copia el tiempo pasado
            helper = procesos_en_memoria.count(procesos[proceso]) #Se Revisa si el proceso se encuentra en memoria
            added = False
            if (helper == 1):                                     #Si se encuentra el proceso en la fila de procesos en memoria esto significa que no se tiene que hacer nada
                added = True
                lista_fallos.append(" ")

            if(added == False):
                still_zeros = False
                for marco in range(len(marcos)):         #Se revisa si aun existen placeholders en el tiempo actual
                    if(marcos[marco][proceso] == 0):
                        still_zeros = True
                add = False
                count = 0
                if(still_zeros == True):                #Si aun hay placeholders en el tiempo actual, se cuenta el fallo y se agrega el proceso
                    while(add == False):
                        if(marcos[count][proceso] == 0):
                            marcos[count][proceso] = procesos[proceso]      #Se añade el proceso en la primera pocision donde se encuentre un placeholder
                            fallos +=1                                      #Se incrementa el numero de fallos
                            procesos_en_memoria.append(procesos[proceso])   #Se agrega el proceso al final de la lista de procesos en memoria
                            lista_fallos.append("X")                    #Se agrega la posicion a la lista de posiciones de fallos
                            add = True                                      #Se cambia la variable de control para pasar a la siguiente iteracion de los procesos
                        else:
                            count +=1
                else:
                    proceso_a_eliminar = procesos_en_memoria.pop(0)         #Se obtiene el proceso a eliminar del principio de la fila
                    for marco in range(len(marcos)):
                        if(marcos[marco][proceso] == proceso_a_eliminar):   #Cuando se encuentre el proceso a eliminar se intercambia por el actual
                            marcos[marco][proceso] = procesos[proceso]
                            fallos += 1                                     #Se incrementan los fallos
                            lista_fallos.append("X")                    #Se agrega la posicion del fallo
                            procesos_en_memoria.append(procesos[proceso])   #Se agrega el nuevo proceso a la lista de procesos en memoria



    #Se agregan los encabezados de la tabla, ademas de especificar el marco para despues imprimirse
    marcos[0].insert(0,"Marco 0: ")
    marcos[1].insert(0,"Marco 1: ")
    marcos[2].insert(0,"Marco 2: ")
    marcos[3].insert(0,"Marco 3: ")
    marcos[4].insert(0,"Marco 4: ")
    marcos.append(lista_fallos)                 # Se adiciona , para visualizacion , la lista que contiene X donde hubo fallos 
    marcos[5].insert(0,"Fallo  : ")
    procesos.insert(0,"Marcos")
    rendimiento = (30-fallos)/30                #Se obtiene el rendimiento
    return rendimiento, marcos, procesos

if __name__ == "__main__":
    print('Porfavor ejecute el archivo "main.py" para ver el algoritmo en acción')