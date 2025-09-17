import cv2

cap = cv2.VideoCapture('video1.avi')
font = cv2.FONT_HERSHEY_COMPLEX
car_cascade = cv2.CascadeClassifier('cars.xml')
v = 0
while True:

    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        v+=1
        cv2.putText(frames,str(v), (30, 30), font, 1, (0,0,255), 1, cv2.LINE_AA)


    cv2.imshow('video2', frames)

    
    if cv2.waitKey(33) == 27:
        print(v)
        break

cv2.destroyAllWindows()
