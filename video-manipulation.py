import cv2

# Cascades
haar_cascade = 'cascade_model/classifier/stage0.xml'
video = 'demo_vides/break.mp4'
    
cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

# reads frames from a video
ret, frames = cap.read()
      
# convert frames to gray scale 
gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
      
# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)