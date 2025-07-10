from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")

    model.train(data="moedas.yaml", epochs=30)
    metrics = model.val()

if __name__ == '__main__':
    main()