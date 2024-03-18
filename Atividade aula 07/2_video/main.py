from random import randint
import cv2 as cv
import numpy as np

#video
capture = cv.VideoCapture("videos/coc.mp4")

frame_width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)

#imagem    
logo = cv.imread('image.png')           
img_height, img_width = int(frame_height), int(frame_width)

logo = cv.resize(logo, (img_width, img_height))
logo_grey = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(logo_grey, 150, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

logo_res = cv.bitwise_and(logo, logo, mask=mask_inv)


if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourrcc = cv.VideoWriter_fourcc(*'avc1')
    output = cv.VideoWriter("video.mp4", fourrcc, int(fps), (int(frame_width), int(frame_height)), False)
    
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:
            cv.namedWindow('Input')
            res = cv.add(frame, logo_res)
            cv.imshow('Input', res)
            output.write(res)
            if cv.waitKey(10) & 0xFF == ord('q'):
                break

        else: break
        

capture.release()
output.release()
cv.destroyAllWindows()