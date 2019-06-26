# Object Recognition
Here you can find an explanation on how the object recognition algorithm was set up, trained and how it works.
All mentioned files will be added to this folder or linked.
The explanation will be split up into the following steps:
*1. Setup*, *2. Dataset and Annotations*, *3. Training* and *4. Inferring*.

## 1. Setup
**System specifics:** OS = Windows 10; CPU = Intel i5-7400 (3.00GHz); RAM = 8GB; GPU = NVIDIA GeForce GTX 1060, 6GB.
  
### **Preperation**
The first step of the setup is installing a virtual environment and the requirements to run tensorflow-gpu. For this the steps below should be followed in the same order.
- Remove all NVIDIA Drivers
- Install [Python version 3.6](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64-webinstall.exe)
- Install [Visual Studio](https://visualstudio.microsoft.com/de/vs/?rr=https%3A%2F%2Fwww.google.com%2F) in order to get Visual C++ build tools OR
- Install [Visual Studio C++ Build Tools](https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe) 
 and [Visual Studio Build Tools](https://download.microsoft.com/download/E/E/D/EEDF18A8-4AED-4CE0-BEBE-70A83094FC5A/BuildTools_Full.exe)
- Install [CUDA version 10.0](https://developer.nvidia.com/cuda-10.0-download-archive)
- Download [cuDNN version 7.4 for CUDA 10.0](https://developer.nvidia.com/rdp/cudnn-archive) *! An account needs to be created in order to download cuDNN !*
- Extract files from downloaded cuDNN folder and copy them into the corresponding folders in **C:\Program Files\NVIDIA GPU Computing Toolkit**
- Install [Anaconda](https://www.anaconda.com/distribution/) - Python 3.7 version

---
### **Open Command Prompt and follow steps as below.**
- Type in `conda`, run, no errors should occur.
- Make a virtual environment (ve) by running <br>`conda create -n name python=3.6`  
*! Replace ***name*** with whatever you want to call your ve !*
- Activate ve with the command: <br>`activate name`
- Now to install tensorflow-gpu on the ve: <br>`pip install --ignore-installed --upgrade tensorflow-gpu`
- Continue with installing additional libraries: <br>
`pip install keras`, <br>
`pip install numpy`, <br>
`pip install matplotlib`, <br> 
`pip install cython`<br>
  
- Download [OpenCV](https://www.lfd.uci.edu/~gohlke/pythonlibs/) *(**Find:** opencv_python‑4.1.0‑cp36‑cp36m‑win_amd64.whl)*
- Install OpenCV with <br>`pip install path_to_file`<br> *! Replace path_to_file with the actual path to the file !* 
- Download / clone the [Darkflow Repo](https://github.com/thtrieu/darkflow) and store locally <br> *! Don't forget to extract if you download !*
- In cmd navigate into the darkflow folder and run <br>`python setup.py build_ext --inplace`
- You should be able to find the folder **build** in the darkflow folder now
- Download [YOLOv2 608x608 weights](https://pjreddie.com/darknet/yolov2/) 
- Create a **bin** folder in the darkflow folder and put the downloaded weights in there

---

### **Test the setup**
- Download a test [Video](https://www.videvo.net/video/people-cycling-over-westminster-bridge/5604/) and save it in the darkflow folder as video.mp4
- In cmd run <br> `python flow --model cfg/yolo.cfg --load bin/yolo.weights --demo video.mp4 --gpu 0.8 --saveVideo` <br> *! Your names for the .cfg and .weights files might differ, look them up in corresponding folders !*
- When done a new videofile (video.avi) should appear in the darkflow folder, start it, there should be bounding boxes, labels and confidence surrounding the objects

## 2. Dataset and Annotations
- Create a new folder *e.g. training* in the darkflow folder and create another folder for your dataset *e.g. images*
- Now download a lot of images for the object you want to train on. You can use the Google Chrome Extension [Fatkun](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) for example.
- Clean up: Remove images that you do not find suitable
- Save all the images in the *images* folder you've created previously and rename them using [rename.py](https://github.com/PepeLoperenaa/ProjectInnovate/edit/master/ObjectRecognition/rename.py)
- Now use [box.py](https://github.com/PepeLoperenaa/ProjectInnovate/edit/master/ObjectRecognition/box.py) & [generate_xml.py](https://github.com/PepeLoperenaa/ProjectInnovate/edit/master/ObjectRecognition/generate_xml.py) to draw the bounding boxes around the object in each image. <br> *(One after the other an image from the dataset will be opened. Draw the bounding box around the object in the image. **Start in the top-left corner!** If there are multiple objects press Ctrl to generate a new bounding box. When done press q to go to the next file.)* <br> Thanks to Mark Jay for the [templates](https://github.com/markjay4k/YOLO-series) for box.py, generate_xml.py and for his [tutorial series](https://www.youtube.com/watch?v=PyjBd7IDYZs&list=PLX-LrBk6h3wSGvuTnxB2Kj358XfctL4BM). 
- In an annotations folder an XML file, containing the position of the bounding box of the object, for each image will be stored. Use rename.py for the annotations as well. <br> *! Be sure to use the correct file extension (.xml) in rename.py !*

## 3. Training

![ai](https://pixel.nymag.com/imgs/daily/vulture/2019/02/19/19-how-to-train-dragon.w300.h100.jpg)

- First modify the cfg file: <br>
    1. ) In */darkflow/cfg/* make a copy of *tiny-yolo-voc.cfg* <br>
    2. ) In the last layer under [region] change the number of classes to your number of classes. <br>
    3. ) In [convolutional], right above, change filters to *5 x (numberOfClasses + 5)*
- Download tiny-yolo-voc.weights from the [yolo website](https://pjreddie.com/darknet/yolov2/)
- Change labels in labels.txt to the names of the objects you want to recognise
- In the local darkflow folder in */darkflow/net/build.py* add the following code under the imports: <br>
  ```python
  config = tf.ConfigProto()
  config.gpu_options.allow_growth = True
  sess = tf.Session(config=config)
  ```
- In cmd navigate to your darkflow folder and run the following: `python flow --model cfg/tiny-yolo-voc.cfg --load weights/tiny-yolo-voc.weights --train --annotation training/annotations --dataset training/wheelchairs --gpu 0.8 --batch 8 --epoch 1000` <br>
*! Make sure the paths to your model, weights, annotations and dataset are correct, batch, gpu and epoch can be modified !* <br>

There will be checkpoits stored every 250 steps, you can find them in the ckpt folder. If, for some reason the training stops and you want to resume from the last checkpoint replace the weights with -1.

Since I ran out of space on the drive the darkflow folder was on, I wrote a [script to move files to another directory](https://github.com/PepeLoperenaa/ProjectInnovate/blob/master/ObjectRecognition/move.py).

Every step you will be shown the moving avg loss. The closer to 0 that gets the better. At some point it will stop getting lower, though. In general if you've reached below 1 it should be good enough to use and you can stop training.
  
## 4. Inferring
- Open [OR-Wheelchairs.ipynb](https://github.com/PepeLoperenaa/ProjectInnovate/blob/master/ObjectRecognition/OR-Wheelchairs.ipynb) in Jupyter Notebook.
- Specify which model (cfg) you use, as weights put in the number of the last checkpoint and specify the threshold *(e.g 0.3 means the model must be at least 30% confident to recognise the object)*
- Our last checkpoint after training on wheelchairs: [Wheelchair Weights](https://drive.google.com/open?id=1ZjmDXtqJCVp05jWAcdNLtqIX3Hbeyrfw)
