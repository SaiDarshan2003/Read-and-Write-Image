1.import cv2
A=cv2.imread("14288_089.png",1)
cv2.imshow("Car",A)
cv2.waitKey(0)
2.import random
import cv2
A=cv2.imread("14288_089.png",1)
for i in range(100):
    for j in range(A.shape[1]):
        A[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("Car",A)
cv2.waitKey(0)
3.import cv2
A=cv2.imread("14288_089.png",0)
cv2.imshow("Car",A)
cv2.waitKey(0)
4.import cv2
A=cv2.imread("14288_089.png",1)
tag=A[50:150,75:90]
A[25:125,50:65]=tag
cv2.imshow("Car",A)
cv2.waitKey(0)
5.import cv2
A=cv2.imread("14288_089.png",1)
cv2.imwrite("14288_089.png",A)
cv2.imshow("Car",A)
cv2.waitKey(0)
6.import cv2
a=cv2.imread('14288_089.png',1)
print(a.shape)