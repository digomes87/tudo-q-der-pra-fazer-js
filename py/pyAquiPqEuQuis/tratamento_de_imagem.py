import cv2

ima1 = cv2.imread('1.jpeg', 1) 

print(ima1)

cv2.imshow('image', ima1)
cv2.waitKey(0)
cv2.destroyAllWindons()


