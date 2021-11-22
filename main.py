from tabulate import tabulate
from fifo import remplazo_FIFO
from lru import lru_method
import random


def get_random_stream(num_solicitudes):
    # elegir entre el rango deseado, en este caso 10 procesos distintos
    result_str = ''.join(random.choice('ABCDEFGHIJ') for i in range(num_solicitudes))
    return list(result_str)

solicitudes = get_random_stream(30)
rendimiento_FIFO , matriz_FIFO = remplazo_FIFO(solicitudes)
rendimiento_LRU , matriz_LRU = lru_method(solicitudes)

if __name__ == "_main_":
    print('Utilizando el algoritmo de reemplazo FIFO :')
    print(matriz_FIFO)
    print("El rendimiento del algoritmo es de: " + str(rendimiento_FIFO))
    print('Utilizando el algoritmo de reemplazo LRU :')
    print(matriz_LRU)

