from ultralytics import YOLO


model = YOLO("./model/yolov8n-face.pt")  # load a pretrained model (recommended for training)

def runIA(image):



    results = model(image)  # predict on an image

    numberOfPerson = 0
    for result in results:
        numberOfPerson = len(result.boxes)
        print(numberOfPerson)  # Boxes object for bbox outputs

    return numberOfPerson
    #success = model.export(format="onnx")  # export the model to ONNX format
