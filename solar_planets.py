import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(100,80),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0))
cv2.putText(img,"Mercury",(120,240),cv2.FONT_HERSHEY_PLAIN,0.8,(255,0,0))
cv2.putText(img,"Venus",(195,255),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
cv2.putText(img,"Earth",(285,260),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
cv2.putText(img,"Mars",(380,255),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
cv2.putText(img,"Jupiter",(500,390),cv2.FONT_HERSHEY_PLAIN,2.7,(255,0,0))
cv2.putText(img,"Satrun",(750,330),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0))
cv2.putText(img,"Uranus",(950,310),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0))
cv2.putText(img,"Neptune",(1100,310),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0))


cv2.imshow("output",img)
cv2.imwrite("solar_systemwithnames.jpg",img)
cv2.waitKey(0)