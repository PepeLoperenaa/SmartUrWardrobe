# Object Recognition
In this README you can find an explanation on how the object recognition algorithm was set up, trained and how it works.
All mentioned files will be added to this folder and linked.
The explanation will be split up into the following steps:
*1. Setup*, *2. Dataset and Annotations*, *3. Training*, *4. Inferring* and *5. Usage*.

## 1. Setup
**System specifics:** OS = Windows 10; CPU = Intel i5 (have to look up at home); RAM = 8GB; GPU = NVIDIA GeForce GTX 1060, 6GB.
  
The first step of the setup is installing tensorflow-gpu. For this the steps below should be followed in the same order.
- Remove all NVIDIA Drivers
- Install [Python version 3.6](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64-webinstall.exe)
- Install [Visual Studio](https://visualstudio.microsoft.com/de/vs/?rr=https%3A%2F%2Fwww.google.com%2F) in order to get Visual C++ build tools 
- Install [CUDA version 10.0](https://developer.nvidia.com/cuda-10.0-download-archive)
- Download [cuDNN version 7.4 for CUDA 10.0](https://developer.nvidia.com/rdp/cudnn-archive) *! An account needs to be created in order to download cuDNN !*
- Extract files from downloaded cuDNN folder and copy them into the corresponding folders in **C:\Program Files\NVIDIA GPU Computing Toolkit**
- Install [Anaconda - Python 3.7 version](https://www.anaconda.com/distribution/)

---
For the following open Command Prompt and follow steps as below.
- Type in `conda`, run, no errors should occur.
- Make a virtual environment (ve) by running `conda create -n name python=3.6`  
*! Replace ***name*** with whatever you want to call your ve. !*
- Activate ve with the command: `activate name`
- Now to install tensorflow-gpu on the ve: `pip install --ignore-installed --upgrade tensorflow-gpu`
- Continue with installing additional libraries: 
`pip install keras`, 
`pip install numpy`, 
`pip install matplotlib`, 
`pip install cython`

## 2. Dataset and Annotations

## 3. Training
Google "how to train your ai":
![ai](https://pixel.nymag.com/imgs/daily/vulture/2019/02/19/19-how-to-train-dragon.w700.h700.jpg)
## 4. Inferring
## 5. Usage
