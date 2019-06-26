from flask import Flask
app = Flask(__name__)
import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

##%config InlineBackend.figure_format = 'svg'


options = {
    'model': 'cfg/yolo-voc-c1.cfg',
    'load': 76260,
    'threshold': 0.1
}

tfnet = TFNet(options)



img = cv2.imread('not_wh.jpg')
result = tfnet.return_predict(img)

yass = False
if len(result) > 0:
    yass = True

@app.route('/')
def img1():
	if yass == True:
		return 'Wheelchair detected'
	else:
		return 'No wheelchair'

@app.route('/a')
def img2():
	img = cv2.imread('wh.jpg')
	result = tfnet.return_predict(img)
	yass = False
	if len(result) > 0:
		yass = True
		
	if yass == True:
		return 'Wheelchair detected'
	else:
		return 'No wheelchair'