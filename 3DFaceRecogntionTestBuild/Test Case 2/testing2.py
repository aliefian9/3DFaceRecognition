import face_alignment
from skimage import io
import pandas
import numpy
import os
import sys


fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)

# Ubah ke csv
# for filename in os.listdir("database"):
#     if filename.endswith(".jpg"):
#         print(filename)
#         database = io.imread("database/" + filename)
#         preds = fa.get_landmarks(database)[-1]
#         prediction = pandas.DataFrame(preds)
#         cvs_hasil = prediction.to_csv("csvDatabase/" + filename + ".csv", index=False)

for filename in os.listdir("input"):
    ctrTrue = 0
    if filename.endswith(".jpg"):
        print("now testing " + filename)
        input_img = io.imread('input/' + filename)
        inp = fa.get_landmarks(input_img)[-1]
    for csvname in os.listdir("csvDatabase"):
        if csvname.endswith(".csv"):
            db = pandas.read_csv("csvDatabase/" + csvname)
            db_numpy = db.to_numpy()
            sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
            dist = numpy.sqrt(sq_dist)
            print(dist)
            
            if((dist[0] < 120 and dist[1] < 120 and dist[2] < 120)):
                print(csvname + " is as same as " + filename)
                ctrTrue = ctrTrue + 1
    print(ctrTrue)