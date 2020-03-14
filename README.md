# Square Images Colorization

This repo contains an example of an images colorization system for images depicting cities squares.

## Setup the virtual enviroment for the project

`$ conda create -n venv python=3.7.4 anaconda`

## Add the virtualenv as a jupyter kernel

`$ ipython kernel install --name "image_colorization" --user`

## Install Pytorch.

`$ conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`

## Change cudatoolkit preference if you have another version of CUDA. If you don't have gpu:

`$ conda install pytorch torchvision cpuonly -c pytorch`

## Install requirements

`$ pip install -r requirements.txt`
 
