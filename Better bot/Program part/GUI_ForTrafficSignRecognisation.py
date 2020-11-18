import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2, time
import numpy as np
##################### LOAD THE TRAINED MODEL TO CLASSIFY SIGN #####################
from keras.models import load_model
model = load_model('traffic_recognition.h5py')


##################### SETUP THE SCREEN #####################

frameWidth = 640  # CAMERA RESOLUTION
frameHeight = 480
brightness = 180
threshold = 0.75  # PROBABLITY THRESHOLD
font = cv2.FONT_HERSHEY_SIMPLEX


##################### SETUP THE VIDEO CAMERA #####################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)


##################### DICTONARY TO LABEL THE TRAFFIC SIGNS #####################

classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',
            3:'Speed limit (50km/h)',
            4:'Speed limit (60km/h)',
            5:'Speed limit (70km/h)',
            6:'Speed limit (80km/h)',
            7:'End of speed limit (80km/h)',
            8:'Speed limit (100km/h)',
            9:'Speed limit (120km/h)',
            10:'No passing',
            11:'No passing veh over 3.5 tons',
            12:'Right-of-way at intersection',
            13:'Priority road',
            14:'Yield',
            15:'Stop',
            16:'No vehicles',
            17:'Veh > 3.5 tons prohibited',
            18:'No entry',
            19:'General caution',
            20:'Dangerous curve left',
            21:'Dangerous curve right',
            22:'Double curve',
            23:'Bumpy road',
            24:'Slippery road',
            25:'Road narrows on the right',
            26:'Road work',
            27:'Traffic signals',
            28:'Pedestrians',
            29:'Children crossing',
            30:'Bicycles crossing',
            31:'Beware of ice/snow',
            32:'Wild animals crossing',
            33:'End speed + passing limits',
            34:'Turn right ahead',
            35:'Turn left ahead',
            36:'Ahead only',
            37:'Go straight or right',
            38:'Go straight or left',
            39:'Keep right',
            40:'Keep left',
            41:'Roundabout mandatory',
            42:'End of no passing',
            43:'End no passing veh > 3.5 tons' }


#####################  FUNCTIONS FOR PREPROCESSING #####################

def returnRedness(img):
	yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
	y,u,v=cv2.split(yuv)
	return v

def Threshold(img,T=150):
	_,img=cv2.threshold(img,T,255,cv2.THRESH_BINARY)
	return img

def findContour(img):
	contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	return contours

def findBiggestContour(contours):
	m = 0
	c = [cv2.contourArea(i) for i in contours]
	return contours[c.index(max(c))]

def boundaryBox(img,contours):
    x,y,w,h=cv2.boundingRect(contours)
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    sign=img[y:(y+h) , x:(x+w)]
    return img,sign




while True:
    time.sleep(0.05)
############################### READ IMAGE ###############################
    success, imgOrignal = cap.read()

############################## PROCESS IMAGE ##############################
    global img

    redness = returnRedness(imgOrignal) # step 1 --> specify the redness of the image
    thresh = Threshold(redness)
   
    try:
        contours = findContour(thresh)
        big = findBiggestContour(contours)
        if cv2.contourArea(big) > 3000:
            img, sign = boundaryBox(imgOrignal, big)
            img = cv2.cvtColor(imgOrignal, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            image = img.resize((30, 30))
            image = np.expand_dims(image, axis=0)
            image = np.array(image)
            pred = model.predict_classes([image])[0]
            sign = classes[pred + 1]
            probabilityValue = np.amax(pred)
            if probabilityValue > threshold:
                cv2.putText(imgOrignal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(imgOrignal, str(pred) + " " + str(sign), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow("Result", imgOrignal)
    except:
        pass
  
    if cv2.waitKey(1) == ord('q'):
        break


