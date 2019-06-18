from flask import Flask, request, Response
import jsonpickle
import os

UPLOAD_FOLDER = '/home/fighting/python/watchjpg/server/'

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index_page():
    return 'This is for uploading the file from Rasp'

# route http posts to this method
@app.route('/posts/store', methods=['GET', 'POST'])
def upload_file():
    response = {'message': ''}
    print(request.method)
    if request.method == 'GET':
        response = {'message': 'You have to use POST to upload the file'}
    else:
        if 'file' not in request.files:
            response = {'message': 'file is not exist'}
        uploaded_file = request.files['image']

        if uploaded_file.filename == '':
            response = {'message': 'file is not exist'}

        uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
        response = {'message': 'image is uploaded, successfully'}

    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)