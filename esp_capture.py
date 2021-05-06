import config
from cv2 import cv2
from urllib.request import urlopen
import numpy as np
from PIL import Image as im

url='http://192.168.0.111/cam-hi.jpg' #ipaddress of ESP32-CAM

#capture image
def capture():
    save_image_path="{}captured_image.jpg".format(config.image_path)
    result = True
    while(result):
        imgResp=urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        cv2.imwrite(save_image_path,img)
        result = False
    cv2.destroyAllWindows()