import cv2
import RPi.GPIO as gp
import numpy as np

def capture():
    cam = cv2.VideoCapture(0,cv2.CAP_V4L)

    cam.set(3,256) # w
    cam.set(4,256) # h
    gp.setmode(gp.BCM)
    gp.setwarnings(False)
    gp.setup(17,gp.IN) 


    while(True) :
        ret, frame = cam.read()

        cv2.imshow('Video Test',frame)

        if gp.input(17) == 0:
            break
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    rgb = cv2.resize(rgb,(128,128))
    pix = np.array(rgb)
    return pix