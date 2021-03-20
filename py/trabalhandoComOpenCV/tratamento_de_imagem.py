import cv2

ima1 = cv2.imread('1.jpeg', 1) 

print(ima1)

cv2.imshow('image', ima1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#fazendo copia da foto com efeito
cv2.imwrite('Euu.jpeg', ima1)



video = cv2.VideoCapture(0)

while(True):
    ret , frame = video.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindons()

