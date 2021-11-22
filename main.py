from tabulate import tabulate
from fifo import remplazo_FIFO
from lru import lru_method
import random


def get_random_stream(num_solicitudes):
    # elegir entre el rango deseado, en este caso 10 procesos distintos
    result_str = ''.join(random.choice('ABCDEFGHIJ') for i in range(num_solicitudes))
    return list(result_str)

solicitudes = get_random_stream(30)

if __name__ == "__main__":
    print("Elige que algoritmo quieres ver en pantalla")
    print("1  -> FIFO")
    print("2  -> LRU")
    number = input()
    if number == "1":
        rendimiento_FIFO , marcos_FIFO, procesos_FIFO = remplazo_FIFO(solicitudes)
        print('Utilizando el algoritmo de reemplazo FIFO :')
        print(tabulate(marcos_FIFO, headers= procesos_FIFO))
        print("El rendimiento de este algoritmo es: ", rendimiento_FIFO)
    elif number =="2":
        rendimiento_LRU , marcos_LRU, procesos_LRU = lru_method(solicitudes)
        print('Utilizando el algoritmo de reemplazo LRU :')
        print(tabulate(marcos_LRU, headers= procesos_LRU))
        print("El rendimiento de este algoritmo es: ", rendimiento_LRU)
    

  

