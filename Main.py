import pytesseract
import cv2
print("Hello World")

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cv2.imshow(img)