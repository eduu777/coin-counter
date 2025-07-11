from collections import defaultdict
from email.policy import default

import cv2
from ultralytics import YOLO

webcam = cv2.VideoCapture(0)

#model = YOLO('yolov8n.pt')
model = YOLO("weights/best.pt")

valores = {
    0: 0.05,
    1: 0.10,
    2: 0.25,
    3: 0.50,
    4: 1.00,
}

track_history = defaultdict(lambda: [])
seguir = False

while True:
    success, img = webcam.read()

    if success:
        qtdMoedas = 0
        sumMoedas = 0.0
        if seguir:
            results = model.track(img, persist=True)

        else:
            results = model(img)

        for result in results:
            boxes = result.boxes

            if boxes:
                for box in boxes.cls:
                    key = int(box.item())
                    if key in valores:
                        qtdMoedas += 1
                        sumMoedas += valores[key]

            img = result.plot()

        texto = f"Moedas: {qtdMoedas} | soma: {sumMoedas:.2f}"
        cv2.putText(img, texto, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Tela", img)

        key = cv2.waitKey(2)
        if key == 27: break

webcam.release()
cv2.destroyAllWindows()
print("WebCam Desligada")
