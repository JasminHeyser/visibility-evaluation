
# import the necessary packages
import cv2




# resize image

def rescaleimage(img,scale):
    width = int(img.shape[1]* scale)
    hight = int(img.shape[0]* scale)
    dimensions = (width, hight)
    return cv2.resize(img,dimensions, interpolation=cv2.INTER_AREA)

    