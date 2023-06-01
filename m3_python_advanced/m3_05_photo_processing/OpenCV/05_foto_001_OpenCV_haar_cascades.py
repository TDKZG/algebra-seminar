"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              OpenCV Library
                    Haar Cascades object detection
                    Repositorij modela: https://github.com/opencv/opencv/tree/master/data/haarcascades
                    Teorija i primjer: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
"""

import cv2

lica_haar_cascade = cv2.CascadeClassifier(
    "m3_05_foto/OpenCV/haarcascade_frontalface_default.xml"
)

fotografija = cv2.imread("m3_05_foto/Fotografije/Algebra_greyp.jpg")

cb_fotografija = cv2.cvtColor(fotografija, cv2.COLOR_BGR2GRAY)

prepoznata_lica = lica_haar_cascade.detectMultiScale(
    cb_fotografija, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
)

print(f"Pronasao sam {len(prepoznata_lica)} lica")


for pravokutnik in prepoznata_lica:
    x, y, w, h = pravokutnik
    cv2.rectangle(fotografija, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Pronadena lica", fotografija)
cv2.waitKey(0)
