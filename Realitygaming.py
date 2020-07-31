import cv2 
import pyautogui
import time
count=0
cap=cv2.VideoCapture(0)
tracker= cv2.TrackerCSRT_create()
success,img= cap.read()
img = cv2.flip(img, 1)
bbox= cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)
def drawbox(img,bbox):
    x,y,w,h= int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    global count
    if(x>300 and y>160 and x<340 and y <320):
        count=0
    if(x>0 and y<160):
            print("up")
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
    elif(x>0 and y>320):
            print("down")
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
    if(count<1):
        if(x>340 and y>160):
            print("right")
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            count+=1
        elif(x<300 and y>160):
            print("left")
            pyautogui.keyDown('left')
            pyautogui.keyUp('left')
            count+=1
            time.sleep(0.001)
        
        
    cv2.circle(img,(x,y), 10,(255, 255, 0),3)

while True:
    timer= cv2.getTickCount()
    success,img= cap.read()
    img = cv2.flip(img, 1)
    cv2.line(img,(0,160),(640,160),(0,224,19),2)
    cv2.line(img,(0,320),(640,320),(0,224,19),2)
    cv2.line(img,(300,0),(300,480),(0,224,19),2)
    cv2.line(img,(340,0),(340,480),(0,224,19),2)
    success,bbox= tracker.update(img)
    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"lost",(75,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(7,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    cv2.imshow("video",img)
    if cv2.waitKey(1) == ord('q'):
        break
