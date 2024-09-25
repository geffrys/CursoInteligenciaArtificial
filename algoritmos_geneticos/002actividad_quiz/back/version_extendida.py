import numpy as np
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from PIL import Image
import random as rd

# Cargar imagen de referencia
url = "https://photoshop-kopona.com/uploads/posts/2019-01/1546709726_butterfly_081.jpg"
rta = requests.get(url)
imagen = Image.open(BytesIO(rta.content))
imgArrayOriginal = np.array(imagen)

# Parámetros del algoritmo genético
num_generaciones = 10  # Aumentar el número de generaciones para mayor precisión
tamaño_poblacion = 50    # Tamaño de la población
tasa_mutacion = 0.01     # Probabilidad de que un píxel mute
tasa_cruce = 0.5         # Probabilidad de cruzar píxeles entre dos padres

# Función de aptitud: entre menor sea la diferencia con la imagen de referencia, mejor
def fitness(img):
    return -np.sum(np.abs(imgArrayOriginal - img))  # Se usa el error absoluto como medida de distancia

# Generar un individuo (imagen aleatoria)
def generar_individuo():
    return np.random.randint(0, 256, imgArrayOriginal.shape, dtype=np.uint8)

# Cruce: toma píxeles de dos padres y crea un hijo
def cruce(padre1, padre2):
    hijo = np.copy(padre1)
    for i in range(len(padre1)):
        for j in range(len(padre1[0])):
            if rd.random() < tasa_cruce:
                hijo[i][j] = padre2[i][j]
    return hijo

# Mutación: altera píxeles aleatorios en la imagen
def mutacion(individuo):
    for i in range(len(individuo)):
        for j in range(len(individuo[0])):
            if rd.random() < tasa_mutacion:
                individuo[i][j] = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
    return individuo

# Generar población inicial de imágenes aleatorias
poblacion = [generar_individuo() for _ in range(tamaño_poblacion)]

# Algoritmo genético
for generacion in range(num_generaciones):
    # Evaluar aptitud de cada individuo en la población
    poblacion = sorted(poblacion, key=fitness, reverse=True)
    
    # Mostrar la mejor imagen cada 50 generaciones
    if generacion % 50 == 0:
        mejor_individuo = poblacion[0]
        print(f"Generación {generacion+1}, Mejor Aptitud: {fitness(mejor_individuo)}")
        plt.imshow(mejor_individuo)
        plt.title(f"Generación {generacion+1}")
        plt.show()
    
    # Seleccionar la mitad superior de la población
    poblacion = poblacion[:tamaño_poblacion//2]
    
    # Generar nueva población mediante cruce y mutación
    nuevos_individuos = []
    while len(nuevos_individuos) + len(poblacion) < tamaño_poblacion:
        padre1, padre2 = rd.sample(poblacion, 2)
        hijo = cruce(padre1, padre2)
        hijo = mutacion(hijo)
        nuevos_individuos.append(hijo)
    
    # Reemplazar la vieja población con la nueva
    poblacion.extend(nuevos_individuos)

# Mostrar el mejor resultado final
mejor_individuo_final = poblacion[0]
plt.imshow(mejor_individuo_final)
plt.title("Mejor Resultado Final")
plt.show()
