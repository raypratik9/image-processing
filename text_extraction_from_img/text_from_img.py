import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('img.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)

config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(img, config=config) 

print(text)

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)



