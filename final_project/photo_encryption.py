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
#key = get_random_bytes(16)
blocksize = 16
keysize = 16
key = os.urandom(keysize)
iv = os.urandom(blocksize)

def getcreds():
    with open("/home/student/mycode/final_project/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
        nasacreds = "&api_key=" + nasacreds.strip("\n")
    return nasacreds

def encrypt(plaintxt):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintxt, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext': ct})
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

    # display images and put in /final_project
    i = 0
    for image in apod:
        try:
            images.append(image['hdurl'])
        except:
            images.append(image['url'])
        urllib.request.urlretrieve(images[i], "/home/student/mycode/final_project/plaintext_images"+images[i].rsplit('/', 1)[1])
        img = Image.open("/home/student/mycode/final_project/plaintext_images"+images[i].rsplit('/', 1)[1]) 
        img.show()
        i += 1
    
    # ENCRYPT
    for pic in os.listdir("/home/student/mycode/final_project/plaintext_images"):
        if pic.endswith("png") or pic.endswith("jpg"):
            path = "/home/student/mycode/final_project/plaintext_images/" + pic
            with open(path, 'rb') as file1:  
                data = file1.read()
                cipher = AES.new(key, AES.MODE_CBC, iv)
                ciphertext = cipher.encrypt(pad(data, blocksize))
                encrypted_filename = "enc_" + pic
                with open("/home/student/mycode/final_project/encrypted/"+encrypted_filename, 'wb') as file2:
                    file2.write(ciphertext)


    # DECRYPT 
    for pic in os.listdir("/home/student/mycode/final_project/encrypted"):
        if pic.endswith("png") or pic.endswith("jpg") and pic.startswith("enc"):
            path = "/home/student/mycode/final_project/encrypted/" + pic
            with open(path, 'rb') as file1:
                data = file1.read()
                cipher2 = AES.new(key, AES.MODE_CBC, iv)
                decrypted_data = unpad(cipher2.decrypt(data), blocksize)
                decrypted_filename = "/home/student/mycode/final_project/decrypted/"+pic.replace("enc", "dec")
                with open(decrypted_filename, 'wb') as file2:
                    file2.write(decrypted_data)

    # CLEAN UP
    for garbage in os.listdir("/home/student/mycode/final_project"):
        if os.path.isfile(garbage) and garbage.startswith("plaintext_images"):
            os.remove(garbage)


if __name__ == "__main__":
    main()