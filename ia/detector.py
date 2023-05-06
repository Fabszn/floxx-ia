from ultralytics import YOLO

def runIA(name):


    # Load a model
    model = YOLO("./model/yolov8n-face.pt")  # load a pretrained model (recommended for training)

    
    results = model("./ia/test2.jpeg")  # predict on an image

    numberOfPerson = 0
    for result in results:
        numberOfPerson = len(result.boxes)
        print(numberOfPerson)  # Boxes object for bbox outputs

    return numberOfPerson
    #success = model.export(format="onnx")  # export the model to ONNX format
