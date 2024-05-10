import cv2
import os
import numpy as np

dataPath = 'C:/Users/Dave BF/Desktop/Data'  # Cambia a la ruta donde hayas almacenado Data
objectList = os.listdir(dataPath)
print('Lista de objetos: ', objectList)

labels = []
objectsData = []
label = 0

for nameDir in objectList:
    objectPath = dataPath + '/' + nameDir
    print('Leyendo las imágenes')

    for fileName in os.listdir(objectPath):
        print('Objetos: ', nameDir + '/' + fileName)
        labels.append(label)
        objectsData.append(cv2.imread(objectPath+'/'+fileName, cv2.IMREAD_GRAYSCALE))  # Leer imágenes en escala de grises
    label = label + 1

# Métodos para entrenar el reconocedor
object_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de objetos
print("Entrenando...")
object_recognizer.train(objectsData, np.array(labels))

# Almacenando el modelo obtenido
object_recognizer.write('modeloLBPHObject.xml')
print("Modelo almacenado...")
