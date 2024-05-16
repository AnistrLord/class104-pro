import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img ,"SUN" , (20,200) , cv2.FONT_HERSHEY_TRIPLEX , 1 , color = (0,0,0))
cv2.putText(img ,"Mercury" , (110,200) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))
cv2.putText(img ,"Venus" , (190,200) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))
cv2.putText(img ,"Earth" , (285,185) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))
cv2.putText(img ,"Mars" , (380,200) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))
cv2.putText(img ,"Jupiter" , (490,200) , cv2.FONT_HERSHEY_TRIPLEX , 0.7 , color = (0,0,0))
cv2.putText(img ,"Saturn" , (768,215) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))
cv2.putText(img ,"Uranus" , (960,215) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (0,0,0))
cv2.putText(img ,"Nepatune" , (1100,215) , cv2.FONT_HERSHEY_TRIPLEX , 0.5 , color = (255,255,255))


cv2.imshow("Solar System", img)

cv2.waitKey(0)

