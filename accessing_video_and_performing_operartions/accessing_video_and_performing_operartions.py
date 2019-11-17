import numpy as np
import cv2

cap = cv2.VideoCapture(0)
def access_camera():
    
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    """
    For example, I can check the frame width and height by cap.get(3) and cap.get(4).
    It gives me 640x480 by default. But I want to modify it to 320x240.
    Just use ret = cap.set(3,320) and ret = cap.set(4,240).
   """

def save_video():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

#save_video()

def drawing_shapes():
    """
    Learn to draw different geometric shapes with OpenCV
    You will learn these functions : cv2.line(), cv2.circle(), 
    cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.
    """
    
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('image')

    # Draw a diagonal blue line with thickness of 5 px
    img1 = cv2.line(img,(0,0),(511,511),(255,0,0),5)

    img2 = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

    img3 = cv2.circle(img,(447,63), 63, (0,0,255), -1)

    img4 = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

    pts_for_polygon = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts_for_polygon = pts_for_polygon.reshape((-1,1,2))
    img5 = cv2.polylines(img,[pts_for_polygon],True,(0,255,255))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

#drawing_shapes()
def nothing(x):
    pass

def maniputaion():
    img = np.zeros((300,512,3), np.uint8)
    cv2.imshow('img',gray)

    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]

    cv2.destroyAllWindows()

#maniputaion()