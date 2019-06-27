import requests

url = "http://127.0.0.1:5000/upload"
files = {'files': open('uploads/Wed_Jun_26_164634_2019.jpg', 'rb')}
r = requests.post(url, files=files)