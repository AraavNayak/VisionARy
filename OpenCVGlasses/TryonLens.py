import cv2
import cvzone
import keyboard
#import _tkinter

print("Welcome to VisionARy's virtual AR glasses simulator.\nThis simulator enables users to try out various glasses in real time.\nPress 'd' to see the next glasses in the list and 's' to see the previous glasses in the list, and press 'q' to quit.\n")
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
num=1
numGlasses = 29

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText('Christmas', (10,50), font, 3, (0, 255, 0), 2, cv2.LINE_AA)

while True:
    k=cv2.waitKey(1)
    if k==ord('d'):
        if num < numGlasses:
            num+=1
    if k==ord('s'):
        if(num > 1):
            num-=1

    if(num<=29 and num >= 0):
            overlay = cv2.imread('Glasses/glass{}.png'.format(num), cv2.IMREAD_UNCHANGED)
         
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay,(w,int(h*0.7)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
    cv2.putText(frame, 'Displaying ' + str(num) + '/' + str(numGlasses), (50, 100), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('VisionARy', frame)
    if cv2.waitKey(10) == ord('q') or num>29:
        break
  
cap.release()
cv2.destroyAllWindows()
