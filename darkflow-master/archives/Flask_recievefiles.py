from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save('uploads/newTest.jpg')
        return '200'
    else:
        return 'Upload Page'

if __name__ == '__main__':
    app.debug = True
    app.run()