import config
from cv2 import cv2

#capture image
def capture():
    save_image_path="{}captured_image.jpg".format(config.image_path)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite(save_image_path,frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()