from random import randint
import cv2 as cv

global drawings
drawings = []

left_button_down = False
color = 0

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]

def draw_circle(event, x, y, flags, param):
    global drawings, left_button_down
    if event == cv.EVENT_LBUTTONDOWN:
        left_button_down = True
    elif event == cv.EVENT_LBUTTONUP:
        left_button_down = False
    if left_button_down:
        drawings.append((x, y, color))
        

capture = cv.VideoCapture("videos/coc.mp4")

frame_width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourrcc = cv.VideoWriter_fourcc(*'avc1')
    output = cv.VideoWriter("video.mp4", fourrcc, int(fps), (int(frame_width), int(frame_height)), False)
    
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:
            for point in drawings:
                 cv.circle(frame, (point[0],point[1]), 3, COLORS[point[2]], -1)
            cv.namedWindow('Input')
            cv.setMouseCallback('Input',draw_circle)
            cv.imshow('Input', frame)
            output.write(frame)
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
            elif cv.waitKey(20) & 0xFF == ord('c'):
                if color<4:
                    color+=1
                else:
                    color=0
            elif cv.waitKey(20) & 0xFF == ord(' '):
                drawings=[]

        else: break
        

capture.release()
output.release()
cv.destroyAllWindows()