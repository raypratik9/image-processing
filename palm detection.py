import cv2

face_cascade = cv2.CascadeClassifier('cascade/palm.xml')

cap = cv2.VideoCapture(1)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x1,y1,w1,h1) in faces:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
