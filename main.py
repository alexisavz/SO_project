from tabulate import tabulate
from fifo import remplazo_FIFO

rendimiento , matriz_FIFO = remplazo_FIFO()

if __name__ == "__main__":
    print('Utilizando el algoritmo de reemplazo FIFO :')
    print(matriz_FIFO)
    print("El rendimiento del algoritmo es de: " + str(rendimiento))