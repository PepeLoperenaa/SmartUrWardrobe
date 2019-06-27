from flask import Flask
from flask import request
import requests as req
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
url_on = 'http://192.168.178.24/LED/ON'
url_off = 'http://192.168.178.24/LED/OFF'

options = {
    'model': 'cfg/yolo-voc-c1.cfg',##linking of the config file
    'load': 76260,##number of the checkpoint to load the weights of the model from
    'threshold': 0.5##limit of confidence in the recognition of object
}

tfnet = TFNet(options)##runs tf with the above specified settings

@app.route('/')
def index():
	return 'placeholder page to check connection'

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']##requests the files defined as image
        f.save('uploads/newTest.jpg')##saves the file sent to the location with the given name
        return 'success'
    else:
        return 'failiure'
		
@app.route('/main')
def img2():
	img = cv2.imread('uploads/newTest.jpg')##read the images specifics through cv2
	result = tfnet.return_predict(img)##uses the running model to predict if the image contains a wheelchair
	isWheelchair = False
	
	if len(result) > 0:##check the length of the result to see if there's a wheelchair on the image
		isWheelchair = True
		
	if isWheelchair == True:##192.168.178.24
		resp = req.get(url_on)
		return 'Wheelchair detected'
	else:
		resp = req.get(url_off)
		return 'No wheelchair detected'	
		
if __name__ == '__main__':
    app.debug = True
    app.run()