import numpy as np
import matplotlib.pyplot as plt
import math

diferencias = []
def Inicializar(n):
    x = n
    for i in range(0,n):
        diferencias.append([])
        for j in range(0,n):
            diferencias[i].append(None)
Inicializar(5)
for i in range(0,5):
    print(diferencias[i])