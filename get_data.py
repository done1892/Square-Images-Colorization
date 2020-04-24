import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
import re
import json
from requests import get
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import cv2 as cv

def scrape_google_image(url, name_folder):
    """This function scrapes images from an URL coming from google 
       images and save them into a specified folder.
       
    Args: 
        url: Google images url.
        name_folder: name of the new folder.
        
    Return:
        images folder in the current file system
    """
    # Delete previous homonyms folder and create it if doesn't exist
    if os.path.exists(str(name_folder)):
        shutil.rmtree(name_folder, ignore_errors=True)
        os.makedirs(str(name_folder))
    else:
        os.makedirs(str(name_folder))
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for num in range(len(html_soup.find_all('a'))):
        stringa = html_soup.find_all('a')[num].find_all('img')
        search = re.search('src="(.+?)" style', str(stringa))
        if search is not None:
            link = search[1]
            response = get(link)
            img=np.asarray(Image.open(BytesIO(response.content)))
            img = cv.resize(img, (450,300))
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            cv.imwrite(name_folder+'/img_'+str(num)+'.jpg', img)


if __name__ == '__main__':
    import argparse
    import yaml

    parser = argparse.ArgumentParser()
    parser.add_argument('--dest_folder', dest='dest_folder', type=str, required=True, help='folder name of scraped images.')
    args = parser.parse_args()

    with open('url.yaml') as file:
        google_url = yaml.load(file, Loader=yaml.FullLoader)
    
    scrape_google_image(url=google_url['url'], name_folder=args.dest_folder)