---

# Square Images Colorization

This repo contains a project focused on the developing of a colorization system for images depicting (not only) cities squares. This project is under development. The idea is to produce two different models: the first based on an autoencoder structure and the second gans-based. 

## Setup the deep learning environment

### Setup the virtual environment for the project

`$ conda create -n venv python=3.7.4 anaconda`

### Add the virtualenv as a jupyter kernel

`$ ipython kernel install --name "image_colorization" --user`

### Install Pytorch.

`$ conda install pytorch torchvision cudatoolkit=10.0 -c pytorch`

### Change cudatoolkit preference if you have another CUDA version. If you don't have gpu:

`$ conda install pytorch torchvision cpuonly -c pytorch`

### Install requirements

`$ pip install -r requirements.txt`

#
 
## PROJECT ROADMAP

The first part of this project consists of "data acquisition" regarding images of cities squares. To this intend a script to scrape images from google image has been developed. To use it, place **get_data.py** and **url.yaml** files in the same directory and specify the google image page url you intend to scrape in url.yaml.

`$ python get_data.py --dest_folder [name of destination folder]`

Furthermore, [Instagram-Scraper](https://github.com/rarcega/instagram-scraper) has been used to get more data and search them by the hashtag. Hashtag searched are _piazzedimilano_, _piazzeditalia_ and _citysquares_.

#

## - AutoEncoder Results

![alt text](https://github.com/done1892/Square-Images-Colorization/blob/master/autoencoders/results_ae299x299_trainedmore2.png)

## - Pix2pix

The gan's based approch relies on **Pix2pix** architecture, following [this](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) implementation. Other images have been captured with _Instagram scraper_ and added to the training dataset in order to improve the model generalization capability. 
The model has been trained for 105 epochs with a learning rate of 0.0002 and Adam optimizer. For other training details, please refer to the original implementation.
Below, it's possible to look at some results:

![alt text](https://github.com/done1892/Square-Images-Colorization/blob/master/pix2pix/showres.jpg)

The **Pix2pix** model has also been tested on the same images tested on **Autoencoder** previously developed.

![alt text](https://github.com/done1892/Square-Images-Colorization/blob/master/pix2pix/showres2.jpg)

Looking at these images we can say the the **Autoencoder** performs better on vintage photo while **Pix2pix** gets betters results, not only on cities squares images, but also on landscapes and so on, giving lively colors to the input.
