# Square Images Colorization

This repo contains a project focused on the developing of a colorization system for images depicting cities squares. This project is under development. The idea is to produce two different models: the first based on an autoencoder structure and the second gans-based. 

Now, I'm scraping data from the internet to get more data as possible to train my models.

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

The first part of this project consists of "data acquisition" regarding images of cities squares. To this intend a script to scrape images from google image has been developed. Furthermore, [Instagram-Scraper](https://github.com/rarcega/instagram-scraper) has been used to get more data and search them by the hashtag. Hashtag searched are 'piazzedimilano'

