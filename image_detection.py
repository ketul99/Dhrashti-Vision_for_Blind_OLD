import config
from keras.preprocessing.image import img_to_array
from cv2 import cv2
import numpy as np
import argparse
import list_to_string

proto="{}deploy.prototxt".format(config.model_path)
models="{}mobilenet_iter_73000.caffemodel".format(config.model_path)
ap=argparse.ArgumentParser(description='Program to run MobileNet-SSD object detection network ') 
ap.add_argument('-i','--image',type=str,help='{}Red_Vespa_Scooter.jpg'.format(config.model_path))   
ap.add_argument('-p','--prototxt',help='{}deploy.prototxt.txt'.format(config.model_path))  
ap.add_argument('-m', '--model',help='{}mobilenet_iter_73000.caffemodel'.format(config.model_path))   
ap.add_argument('-c','--confidence',type=float,default=0.2,help='minimum probability threshold to filter weak detections')

args, unknown = ap.parse_known_args()
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
        "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("[INFO] loading model…")
print(args.image)
net = cv2.dnn.readNetFromCaffe(proto, models)

def image_detection():

    image1 = cv2.imread(config.image_path+"captured_image.jpg")
    image = img_to_array(image1)
    ans=[]

    (h, w) = image.shape[:2]
    gt=1
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    print("[INFO] computing object detections…")
    net.setInput(blob)
    detections = net.forward()
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence >= args.confidence:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            ans.append(CLASSES[idx])
            print("[INFO] {}".format(label)) 
        cv2.rectangle(image1,(startX, startY),(endX, endY),(0,0,255), 2)
        y = startY - 15 if startY - 15  < 15 else startY + 15     
        cv2.putText(image1, label, (startX, y),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    cv2.imshow("Output", image1)
    cv2.imwrite('{}predicted_output.jpg'.format(config.image_path),image1)
    cv2.waitKey(100)

    output=list_to_string.list_to_string(ans)
    return output