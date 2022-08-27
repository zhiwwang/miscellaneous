import cv2

image0=cv2.imread('C:/Users/Xuanbo/Desktop/Screenshots/ee277671-4f8c-4f1e-ad0b-a12a050127dc.jpg')
image1=cv2.imread('C:/Users/Xuanbo/Desktop/Screenshots1/ee277671-4f8c-4f1e-ad0b-a12a050127dc.heic')
image2=cv2.imread('C:/Users/Xuanbo/Desktop/Screenshots2/ee277671-4f8c-4f1e-ad0b-a12a050127dc.jpg')
image3=cv2.imread('C:/Users/Xuanbo/Desktop/Screenshots3/ee277671-4f8c-4f1e-ad0b-a12a050127dc.heic')

subtracted = cv2.subtract(image0,image2)#
subtracted = cv2.bitwise_not(subtracted)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)