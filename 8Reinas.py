from simpleai.search import CspProblem
from simpleai.search.csp import min_conflicts
import matplotlib.pyplot as plt
import numpy as np

# Definimos las variables: una variable por cada columna (0 a 7)
variables = list(range(8))

# Los dominios serán las filas (de 0 a 7), es decir, las posibles posiciones de las reinas
dominios = {var: list(range(8)) for var in variables}

# Definimos las restricciones que aseguran que las reinas no se ataquen
def restricciones(variables, valores):
    columna1, columna2 = variables
    fila1, fila2 = valores

    # Las reinas no deben estar en la misma fila
    if fila1 == fila2:
        return False
    # Las reinas no deben estar en la misma diagonal
    if abs(columna1 - columna2) == abs(fila1 - fila2):
        return False
    return True

# Creamos una lista de todas las combinaciones de pares de variables (columnas)
pares_de_variables = [
    (var1, var2)
    for var1 in variables for var2 in variables if var1 < var2
]

# Creamos el problema con las variables, dominios y restricciones
problema = CspProblem(variables, dominios, [(par, restricciones) for par in pares_de_variables])

# Resolvemos el problema utilizando el algoritmo min_conflicts
resultado = min_conflicts(problema)

# Mostrar el resultado
print("Posiciones de las reinas en el tablero (columna: fila):")
for columna, fila in resultado.items():
    print(f"Columna {columna}: Fila {fila}")

# Función para mostrar el tablero visualmente en consola
def mostrar_tablero(resultado):
    tablero = [['.' for _ in range(8)] for _ in range(8)]
    for columna, fila in resultado.items():
        tablero[fila][columna] = 'Q'
    
    for fila in tablero:
        print(' '.join(fila))

# Mostrar el tablero en consola
print("\nTablero de ajedrez:")
mostrar_tablero(resultado)

# Función para mostrar el tablero gráficamente con Matplotlib
def mostrar_tablero_grafico(resultado):
    fig, ax = plt.subplots()

    # Crear un tablero de ajedrez de 8x8
    tablero = np.zeros((8, 8))

    # Colorear las casillas alternas para el tablero
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                tablero[i, j] = 1

    ax.imshow(tablero, cmap='gray')

    # Colocar las reinas en el tablero
    for columna, fila in resultado.items():
        ax.text(columna, fila, '♛', fontsize=35, ha='center', va='center', color='red')

    # Configurar los ejes
    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(False)

    plt.show()

# Mostrar el tablero gráficamente
mostrar_tablero_grafico(resultado)
