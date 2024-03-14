import cv2 as cv
import numpy as np
from random import randint

logomarca = cv.imread("images/logomarca.png", cv.IMREAD_UNCHANGED)
frame_count = 0

capture = cv.VideoCapture("videos/coc.mp4")

frame_width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv.CAP_PROP_FPS)

logomarca_resize = cv.resize(logomarca, (int(np.round(frame_width*0.2)), (int(np.round(logomarca.shape[0]*0.6)))))
logomarca_height, logomarca_width = logomarca_resize.shape[:2]

print(frame_width, frame_height)
print(logomarca_width, logomarca_height)

logomarca_position_range_x_end = frame_width - logomarca_width
logomarca_position_range_y_end = frame_height - logomarca_height
# logomarca_position_range_x_end = 500
# logomarca_position_range_y_end = 500

logomarca_position_x = 0
logomarca_position_y = 0

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourrcc = cv.VideoWriter_fourcc(*'avc1')
    output = cv.VideoWriter("video.mp4", fourrcc, int(fps), (int(frame_width), int(frame_height)), False)
    
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:

            frame_count += 1
            
            for x in range(0,logomarca_height ):
                for y in range(0, logomarca_width):
                    if logomarca_resize[x, y][0] < 254 and logomarca_resize[x, y][1] < 254 and logomarca_resize[x, y][2] < 254:
                        try:
                            frame[x+logomarca_position_x, y+logomarca_position_y][0:3] = frame[x+logomarca_position_x, y+logomarca_position_y][0:3] + logomarca_resize[x, y][0:3]
                        except:
                            break

            cv.namedWindow('Input')
            
            cv.imshow('Input', frame)
            output.write(frame)

            if frame_count >= 100:
                logomarca_position_x = min(randint(0, logomarca_position_range_x_end), logomarca_position_range_x_end)
                logomarca_position_y = min(randint(0, logomarca_position_range_y_end), logomarca_position_range_y_end)
                frame_count = 0

            if cv.waitKey(10) & 0xFF == ord('q'):
                break
    
        else: break
        

capture.release()
output.release()
cv.destroyAllWindows()