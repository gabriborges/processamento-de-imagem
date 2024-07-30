import cv2

unique_faces = set()
total_unique_faces = 0
trackers = []

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, min_size=(30, 30)):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors, minSize=min_size)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords.append((x, y, w, h))
    return coords

def is_close(coord1, coord2, threshold=50):
    x1, y1, w1, h1 = coord1
    x2, y2, w2, h2 = coord2
    center1 = (x1 + w1 // 2, y1 + h1 // 2)
    center2 = (x2 + w2 // 2, y2 + h2 // 2)
    distance = ((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2) ** 0.5
    return distance < threshold

def detect_and_track(img, faceCascade):
    global unique_faces, total_unique_faces, trackers
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    
    for tracker in trackers:
        success, bbox = tracker.update(img)
        if success:
            x, y, w, h = map(int, bbox)
            # cv2.rectangle(img, (x, y), (x + w, y + h), color['green'], 2)
    
    coords = draw_boundary(img, faceCascade, 1.1, 14, color['blue'], "Face")
    
    for coord in coords:
        if not any(is_close(coord, existing_coord) for existing_coord in unique_faces):
            unique_faces.add(tuple(coord))
            total_unique_faces += 1
            
            tracker = cv2.TrackerKCF_create()
            tracker.init(img, tuple(coord))
            trackers.append(tracker)
    
    return img

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture('video/mogwai.mp4')

while True:
    ret, img = video_capture.read()
    if not ret:
        break

    img = detect_and_track(img, faceCascade)
    cv2.imshow("face detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

print(f"Total de faces únicas detectadas: {total_unique_faces}")