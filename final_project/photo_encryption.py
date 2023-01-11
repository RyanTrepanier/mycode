"""This program interacts with NASA APIs and encrpyts images pulled from them | Author: Ryan Trepanier"""

from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import io
import json
import numpy as np
import requests
import os
import urllib.request
from urllib.request import urlopen
import sys

images = []
API = "https://api.nasa.gov/planetary/apod?"
key = 16#get_random_bytes(16)

def getcreds():
    with open("/home/student/mycode/final_project/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
        nasacreds = "&api_key=" + nasacreds.strip("\n")
    return nasacreds

def encrypt(plaintxt, img):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintxt, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext': ct})
    ct_img = Image.open(img.filename, data=Image.frombytes(mode='RGB', data=ct_bytes, size=img.size))
    ct_img.show()
    return result


def decrypt(key, result):
    try:
        b64 = json.loads(result)
        iv = b64encode(b64['iv'])
        ct = b64encode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        pt_img = Image.open(io.BytesIO(pt))
        pt_img.show()
    except (ValueError, KeyError):
        print("Incorrect decryption")


def main():

    # retrieve photo URLs from NASA API
    nasacreds = getcreds()
    start = "&start_date=2022-12-05"
    end = "&end_date=2023-01-10"
    apodresp = requests.get(API + start + end + nasacreds)
    apod = apodresp.json()
    i = 0

    # display images and put in /final_project
    for image in apod:
        try:
            images.append(image['hdurl'])
        except:
            images.append(image['url'])
        urllib.request.urlretrieve(images[i], "/home/student/mycode/final_project/"+images[i].rsplit('/', 1)[1])
        img = Image.open("/home/student/mycode/final_project/"+images[i].rsplit('/', 1)[1]) 
        img.show()
        
        # Encrypt photos
        # USE    for pic in os.listdir(pathtoproject)
        # with open(img.filename, 'rb') as im:
        #     f = im.read()
        #     b = bytearray(f) 
        #     enc = encrypt(b, img)
        i += 1
    
    
        
    


if __name__ == "__main__":
    main()