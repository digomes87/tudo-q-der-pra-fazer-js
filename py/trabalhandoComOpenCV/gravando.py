""" 
    aqui temos um docstring
"""

import cv2

captura = cv2.VideoCapture(0)
forc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('gravacao.avi', forc, 20.0, (680, 500))

print(captura.isOpened())

while captura.isOpened():
    ret, frame, = captura.read()

    if ret:
        print(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# aqui um comentario atoa

captura.release()
out.release()
cv2.destroyAllWindons()

# nao esta salvando o video em formato valido ou o video em si nao esta sendo processado
