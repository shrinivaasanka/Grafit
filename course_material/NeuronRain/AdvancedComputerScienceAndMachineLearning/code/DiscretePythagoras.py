import numpy as np
import cv2

def draw_hypotenuse(squareside=10):
    frompixel=(0,0)
    topixel=(squareside,squareside)
    img1 = np.zeros((512,512,3), np.uint8)
    cv2.line(img1,(0,0),(squareside,0),(0,255,0),10)
    cv2.line(img1,(0,0),(0,squareside),(0,255,0),10)
    cv2.line(img1,(0,squareside),(squareside,squareside),(0,255,0),10)
    cv2.line(img1,(squareside,0),(squareside,squareside),(0,255,0),10)
    cv2.line(img1,frompixel,topixel,(255,0,0),10)
    cv2.imwrite("DiscretePythagoras.jpeg",img1)

if __name__=="__main__":
    draw_hypotenuse(512)
