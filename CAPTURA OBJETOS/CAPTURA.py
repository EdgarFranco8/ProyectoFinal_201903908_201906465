import cv2
import os

objectName = 'Desodorante'
dataPath = 'C:/Users/Dave BF/Desktop/Data'  # Cambia a la ruta donde hayas almacenado Data
objectPath = os.path.join(dataPath, objectName)

if not os.path.exists(objectPath):
    print('Carpeta creada: ', objectPath)
    os.makedirs(objectPath)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

count = 0
capture_image = False  # Variable para controlar la captura de imágenes

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:  # 27 es el código ASCII para la tecla "Esc"
        break
    elif k == ord('s'):
        capture_image = True

    if capture_image:
        cv2.imwrite(os.path.join(objectPath, 'object_{}.jpg'.format(count)), frame)
        count += 1
        print('Imagen capturada: object_{}.jpg'.format(count))
        capture_image = False

cap.release()
cv2.destroyAllWindows()
