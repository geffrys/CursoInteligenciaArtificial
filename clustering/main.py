import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

vinos = pd.read_csv('datasetvinos.csv', engine='python')
print(vinos.info())
print(vinos.head())
vinos_variables = vinos.drop(['Vino'], axis=1) # Eliminamos la columna vino pues no es reelenvante para el clustering
print(vinos_variables.describe()) # Estadistica descriptiva de los datos

vinos_normalizados = (vinos_variables - vinos_variables.min()) / (vinos_variables.max() - vinos_variables.min()) # Dejar los valores normalizados en rangos de 0 a 1


# Encontrar el numero de clusters optimo, con la tecnica de codo de Jambu
wcss = [] # Suma de los cuadrados de las distancias de los puntos a los centroides
for i in range(1, 11): # Numero de clusters a probar, en este caso de 1 a 10
    kmeans = KMeans(n_clusters=i, max_iter=300)
    kmeans.fit(vinos_normalizados)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Codo de Jambu')
plt.xlabel('Numero de clusters')
plt.ylabel('WCSS')
# plt.show() # Se selecciona la cantidad de clusters donde la curva se empieza a aplanar

clustering = KMeans(n_clusters=3, max_iter=300)
clustering.fit(vinos_normalizados)
# Los resultados del clustering se guardan en la columna KMeans_Clusters
print('CLUSTERS')
vinos['KMeans_Clusters'] = clustering.labels_
print(vinos.head())

# visualizacion de los clusters
from sklearn.decomposition import PCA
pca = PCA(n_components=2) # Reducir las dimensiones de los datos a 2
pca_vinos = pca.fit_transform(vinos_normalizados) # Aplicar PCA a los datos normalizados
pca_vinos_df = pd.DataFrame(data=pca_vinos, columns=['Componente1', 'Componente2']) # Crear un dataframe con los datos de PCA
pca_nombres_vinos = pd.concat([pca_vinos_df, vinos[['KMeans_Clusters']]], axis=1)

# Graficar los clusters
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Componente 1', fontsize=15)
ax.set_ylabel('Componente 2', fontsize=15)
ax.set_title('Componentes principales', fontsize=20)
colores = ['blue', 'red', 'green']
ax.scatter(x=pca_nombres_vinos['Componente1'], y=pca_nombres_vinos['Componente2'], c=pca_nombres_vinos['KMeans_Clusters'], cmap='viridis', s=50)
plt.show()




