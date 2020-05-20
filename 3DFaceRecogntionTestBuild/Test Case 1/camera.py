import cv2 
import uuid
import datetime
from skimage import io
import pandas

y = 140
x = 180
h = 250
w = 250

key = cv2.waitKey()
webcam = cv2.VideoCapture(1)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            outfile = "input.jpg"
            cv2.imwrite(outfile, img=frame)
            img = cv2.imread('input.jpg', cv2.IMREAD_UNCHANGED)

            imgcrop = cv2.imread("input.jpg")
            crop_img = img[y:y+h, x:x+w]
            cv2.imwrite("Input/jasonInput.jpg", crop_img)
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

