from flask import Flask
from flask import request
app = Flask(__name__)
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import jsonpickle
import os

##%config InlineBackend.figure_format = 'svg'
app = Flask(__name__)

options = {
    'model': 'cfg/yolo-voc-c1.cfg',
    'load': 76260,
    'threshold': 0.5
}

tfnet = TFNet(options)

@app.route('/')
def index():
	return 'Hello and welcome'

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save('uploads/newTest.jpg')
        return '200'
    else:
        return 'Upload Page'
		
@app.route('/main')
def img2():
	img = cv2.imread('uploads/newTest.jpg')
	result = tfnet.return_predict(img)
	yass = False
	if len(result) > 0:
		yass = True
		
	if yass == True:
		return 'Wheelchair detected'
	else:
		return 'No wheelchair'	
		
if __name__ == '__main__':
    app.debug = True
    app.run()