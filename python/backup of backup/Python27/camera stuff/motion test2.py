import cv2
from datetime import datetime

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName)

cam.set(3,640)
cam.set(4,480)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    cv2.imshow( winName, diffImg(t_minus, t, t_plus))

    dimg=diffImg(t_minus, t, t_plus)
    
    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    print cv2.countNonZero(diffImg(t_minus, t, t_plus))
    
    if cv2.countNonZero(diffImg(t_minus, t, t_plus)) >170000:
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', dimg)
    
    key = cv2.waitKey(10)
    if key == 27:
        cam.release()
        cv2.destroyWindow(winName)
        break
