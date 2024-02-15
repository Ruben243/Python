import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

gray_image = cv2.imread("imageToText\Captura.PNG", cv2.IMREAD_GRAYSCALE)
_, th = cv2.threshold(gray_image, 138, 255, cv2.THRESH_BINARY)

cv2.imshow("Ti", th)
cv2.waitKey(0)
text = pytesseract.image_to_string(th)
print(text)
