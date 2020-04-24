# Square Images Colorization

This repo contains a project focused on the developing of a colorization system for images depicting cities squares. This project is under development. The idea is to produce two different models: the first based on an autoencoder structure and the second gans-based. 

## Setup the deep learning environment

### Setup the virtual environment for the project

`$ conda create -n venv python=3.7.4 anaconda`

### Add the virtualenv as a jupyter kernel

`$ ipython kernel install --name "image_colorization" --user`

### Install Pytorch.

`$ conda install pytorch torchvision cudatoolkit=10.0 -c pytorch`

### Change cudatoolkit preference if you have another version of CUDA. If you don't have gpu:

`$ conda install pytorch torchvision cpuonly -c pytorch`

### Install requirements

`$ pip install -r requirements.txt`

#
 
## PROJECT ROADMAP

The first part of this project consists of "data acquisition" regarding images of cities squares. To this intend a script to scrape images from google image has been developed. To use it, place get_data.py and url.yaml files in the same directory and specify the google image page url you intend to scrape in url.yaml.

`$ python get_data.py --dest_folder [name of destination folder]`

Furthermore, [Instagram-Scraper](https://github.com/rarcega/instagram-scraper) has been used to get more data and search them by the hashtag. Hashtag searched are _piazzedimilano_, _piazzeditalia_ and _citysquares_.

#

## - AutoEncoder Results

![alt text](https://github.com/done1892/Square-Images-Colorization/blob/master/autoencoders/results_ae299x299_trainedmore2.png)
