import cv2

img = cv2.imread("  ") #import image location here

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 50,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 5, 5)

color = cv2.bilateralFilter(img, 1, 50, 50)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

