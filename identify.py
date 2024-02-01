import cv2
import numpy as np

def detect_object_from_image(image_path):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f]

    layer_names = net.getUnconnectedOutLayersNames()

    captured_image = cv2.imread(image_path)

    height, width, channels = captured_image.shape

    blob = cv2.dnn.blobFromImage(captured_image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(layer_names)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    detected_item = ""
    max_confidence = 0.0

    for i in range(len(boxes)):
        if i in indices:
            confidence = confidences[i]
            if confidence > max_confidence:
                max_confidence = confidence
                label = str(classes[class_ids[i]])
                detected_item = label

    return detected_item
