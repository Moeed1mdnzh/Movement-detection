import cv2
import numpy as np

#day mode is 60
#night mode is 40
def none(x):
    pass

mode = 60
cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")
_,img = cap.read()
img2 = img
cv2.createTrackbar("Mode","Frame",0,1,none)
while True:
    _,img = cap.read()
    gray = np.zeros(img.shape, dtype="uint8")
    add = cv2.add(img,gray)
    image = cv2.subtract(add,img2)
    black = np.zeros(image.shape,dtype='uint8')
    full = np.ones(image.shape,dtype='uint8') * mode
    q1 = image >= black
    q2 = image <= full
    cv2.imshow("Frame",img)
    cv2.imshow("Frame2",image)
    if True:
        if q1.all() and q2.all():
            pass
        else:
            cv2.putText(add,"Something happened",(150,210),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),4)
            cv2.imshow("Frame",add)
    img2 = img
    k = cv2.waitKey(30) & 0xff
    if k == ord('e'):
        break
    s = cv2.getTrackbarPos("Mode",'Frame')

    if s == 0:
        mode = 60
    else:
        mode = 40


cv2.destroyAllWindows()
cap.release()
