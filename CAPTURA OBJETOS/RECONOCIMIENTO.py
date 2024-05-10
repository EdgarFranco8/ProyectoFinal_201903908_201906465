import cv2
import os

dataPath = 'C:/Users/Dave BF/Desktop/Data'  # Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

object_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
object_recognizer.read('modeloLBPHObject.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detected_desodorante = False  # Variable para rastrear si se detectó el desodorante
show_object_label = False     # Variable para controlar la visibilidad del nombre del objeto

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección y reconocimiento de objetos
    label, _ = object_recognizer.predict(gray)  # Desempaqueta solo el primer valor, descartando la medida de confianza
    
    if label != -1 and imagePaths[label] == "Desodorante":
        object_label = "Desodorante"
        detected_desodorante = True
    else:
        object_label = "Desconocido"
        detected_desodorante = False
    
    if show_object_label:
        cv2.putText(frame, '{}'.format(object_label), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    
    # Detectar la pulsación de la tecla 's' para alternar la visibilidad del nombre del objeto
    if cv2.waitKeyEx(1) == ord('s'):
        show_object_label = not show_object_label
    
    if cv2.waitKeyEx(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()


