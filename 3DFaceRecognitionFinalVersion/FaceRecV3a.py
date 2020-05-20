import os
import cv2 
import uuid
import datetime
import face_alignment
from skimage import io
import pandas
import numpy
import time
from serial import Serial

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)
arduinoData = Serial('com6', 9600)

y = 140
x = 180
h = 250
w = 250

counter = 0

def reg():
    name = input("Your Name ? ")
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
                outfile = 'dataset/%s.jpg' % (str(name))
                cv2.imwrite(outfile, img=frame)

                imgcrop = cv2.imread("dataset/%s.jpg" % (name))
                crop_img = imgcrop[y:y+h, x:x+w]
                cv2.imwrite("dataset/%s.jpg" % (str(name)), crop_img)

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
    input_img = io.imread('dataset/%s.jpg' % (str(name))) 
    preds = fa.get_landmarks(input_img)[-1]
    prediction = pandas.DataFrame(preds)
    csv_hasil = prediction.to_csv('csv/%s.csv' % str(name), index = False) 

def matching():
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
                outfile = 'input.jpg'
                cv2.imwrite(outfile, img=frame)

                imgcrop = cv2.imread("input.jpg")
                crop_img = imgcrop[140:140+250, 180:180+250]
                cv2.imwrite("input.jpg", crop_img)

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

    input_img_matching = io.imread('input.jpg')
    input_matching = fa.get_landmarks(input_img_matching)[-1] #numpy Array

    for filename in os.listdir("csv"):
        if filename.endswith(".csv"):
            db = pandas.read_csv("csv/" + filename)
            db_numpy = db.to_numpy()
            sq_dist = numpy.sum((db_numpy - input_matching)**2, axis=0)
            dist = numpy.sqrt(sq_dist)
            print(dist)

            if((dist[0] < 120 and dist[1] < 120 and dist[2] < 120) or (dist[0] < 120 and dist[1] < 120) or (dist[1] < 120 and dist[2] < 120) or (dist[0] < 120 and dist[2] < 120)):
                print("In")
                counter = 1
                # led_on()
                # time.sleep(4)
            else:
                print("Out")
    if(counter == 1):
        led_on()
        time.sleep(4)
    else:
        led_off()


def led_on():
    arduinoData.write(b'1')

def led_off():
    arduinoData.write(b'0')

while(1):
    led_off()
    counter = 0
    pilihan = input("Register[1] / Existing User[0]")
    if pilihan == "0":
        matching()
    elif pilihan == "1":
        reg()