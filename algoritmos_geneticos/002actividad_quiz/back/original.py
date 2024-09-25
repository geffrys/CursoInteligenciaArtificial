import numpy as np
from io import BytesIO
import requests
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image
import random as rd

url = "https://photoshop-kopona.com/uploads/posts/2019-01/1546709726_butterfly_081.jpg"
rta = requests.get(url)
imagen = Image.open(BytesIO(rta.content))

imgArrayOriginal = np.array(imagen)
print(imgArrayOriginal.shape)
plt.imshow(imgArrayOriginal)
print(imgArrayOriginal[300][300])
print(imgArrayOriginal[300][300][1])
print("FINALIZO.")
imgAleatoria=np.array(imagen)
for i in range(len(imgAleatoria)):
  for j in range(len(imgAleatoria[0])):
   for ij in range(3):
    imgAleatoria[i][j][ij]=rd.randint(0, 255)
plt.title("Imagen Aleatoria")
plt.imshow(imgAleatoria)
plt.show()

imgLineaNegra=np.array(imagen)
for i in range(len(imgLineaNegra)):
  for j in range(len(imgLineaNegra)):
    imgLineaNegra[300][i]=[0,0,255]
    imgLineaNegra[j][300]=[255,0,0]
plt.imshow(imgLineaNegra)
plt.show()


imgNoBlue=np.array(imagen)
for i in range(len(imgNoBlue)):
  for j in range(len(imgNoBlue[0])):
   imgNoBlue[i][j][2]=0
plt.imshow(imgNoBlue)
plt.show()


imgNoRed=np.array(imagen)
for i in range(len(imgNoRed)):
  for j in range(len(imgNoRed[0])):
   imgNoRed[i][j][0]=0
plt.imshow(imgNoRed)
plt.show()


imgNoGreen=np.array(imagen)
for i in range(len(imgNoGreen)):
  for j in range(len(imgNoGreen[0])):
   imgNoGreen[i][j][1]=0
plt.imshow(imgNoGreen)
plt.show()


imgSoloRed=np.array(imagen)
for i in range(len(imgSoloRed)):
  for j in range(len(imgSoloRed[0])):
   imgSoloRed[i][j][1]=0
   imgSoloRed[i][j][2]=0
plt.imshow(imgSoloRed)
plt.show()


imgSoloBlue=np.array(imagen)
for i in range(len(imgSoloBlue)):
  for j in range(len(imgSoloBlue[0])):
   imgSoloBlue[i][j][0]=0
   imgSoloBlue[i][j][1]=0
plt.imshow(imgSoloBlue)
plt.show()


imgSoloGreen=np.array(imagen)
for i in range(len(imgSoloGreen)):
  for j in range(len(imgSoloGreen[0])):
   imgSoloGreen[i][j][0]=0
   imgSoloGreen[i][j][2]=0
plt.imshow(imgSoloGreen)
plt.show()


imgEscalaGrises=np.array(imagen)
for i in range(len(imgEscalaGrises)):
  for j in range(len(imgEscalaGrises[0])):
    imgEscalaGrises[i][j]=(imgEscalaGrises[i][j][0])*0.3 + (imgEscalaGrises[i][j][1])*0.6 +(imgEscalaGrises[i][j][2])*0.1
plt.imshow(imgEscalaGrises)
plt.show()
