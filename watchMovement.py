import RPi.GPIO as GPIO
import time
import subprocess
import requests
import json

#initial GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#The input pin from PIR
INPUT_PIN = 7
#The local files that the images will be saved to
LOCAL_FILE = "/home/pi/images/"
#the address of the page the image will be uploaded to
UPLOAD_ADDRESS = "http://192.168.0.145:4000/posts/store"
#setup the input pin as an input
GPIO.setup(INPUT_PIN, GPIO.IN)

#the loop to listen for input
while True:
  #get the value of the input pin
  readIn = GPIO.input(INPUT_PIN)
  #check if INPUT_PIN is on 
  if readIn == 1:
    #create image file name
    fileName = LOCAL_FILE + time.ctime() + ".jpg"   
    #run command to capture image
    print(fileName)
    print(subprocess.check_call(["fswebcam", "-r", "1280x720", fileName]))
    #upload to server
    response = requests.post(UPLOAD_ADDRESS, files={'image':open(fileName, 'rb')})
    print(response.text)
    #wait before checking again to prevent overloading
    time.sleep(5)
  else:
    #wait before checking again 
    time.sleep(0.1)


