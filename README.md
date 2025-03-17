## CV Project

### Dataset - Animal-10

link: https://www.kaggle.com/datasets/alessiocorrado99/animals10

Create folder ./data and unzip file inside folder so you will have next structure ./data/raw-img/...

Then run Rename.py to change folder names to English.

### Running Training.ipynb

To run this file currently you need 
- torch
- torchvision
- matplotlib
- sklearn

This code will use GPU for training, so you should install pytorch and torchvision with CUDA support.

My model have 5 conv layers with 3 dense layers.
