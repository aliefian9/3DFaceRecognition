import face_alignment
from skimage import io
import pandas
import numpy
import os
import sys


fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)
fa2 = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', flip_input=True)

# Ubah ke csv
# for filename in os.listdir("dataset"):
#     if filename.endswith(".jpg"):
#         print(filename)
#         database = io.imread("dataset/" + filename)
#         preds = fa2.get_landmarks(database)[-1]
#         prediction = pandas.DataFrame(preds)
#         cvs_hasil = prediction.to_csv("csvHasil2d/" + filename + ".csv", index=False)

for filename in os.listdir("Input"):
    ctrTrue = 0
    if filename.endswith(".jpg"):
        print("now testing " + filename)
        input_img = io.imread('Input/' + filename)
        inp = fa.get_landmarks(input_img)[-1]
    for csvname in os.listdir("csvHasil"):
        if csvname.endswith(".csv"):
            db = pandas.read_csv("csvHasil/" + csvname)
            db_numpy = db.to_numpy()
            sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
            dist = numpy.sqrt(sq_dist)
            
            if((dist[0] < 120 and dist[1] < 120 and dist[2] < 120) or (dist[0] < 120 and dist[1] < 120) or (dist[1] < 120 and dist[2] < 120) or (dist[0] < 120 and dist[2] < 120)):
                print(csvname + " is as same as " + filename)
                ctrTrue = ctrTrue + 1
    print(ctrTrue)

for filename in os.listdir("Input"):
    ctrTrue = 0
    if filename.endswith(".jpg"):
        print("now testing " + filename)
        input_img = io.imread('Input/' + filename)
        inp = fa2.get_landmarks(input_img)[-1]
    for csvname in os.listdir("csvHasil"):
        if csvname.endswith(".csv"):
            db = pandas.read_csv("csvHasil2d/" + csvname)
            db_numpy = db.to_numpy()
            sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
            dist = numpy.sqrt(sq_dist)
            
            if(dist[0] < 120 and dist[1] < 120):
                print(csvname + " is as same as " + filename)
                ctrTrue = ctrTrue + 1
    print(ctrTrue)