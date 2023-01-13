"""This program interacts with NASA APIs and encrpyts/decrypts
     images pulled from them | Author: Ryan Trepanier"""

from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
from urllib.request import urlopen 
import json
import os
import math
import requests
import sys
import urllib.request


images = []
results = {}
API = "https://api.nasa.gov/planetary/apod?"


def getcreds():
    with open("/home/student/mycode/final_project/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
        nasacreds = "&api_key=" + nasacreds.strip("\n")
    return nasacreds

def getimages():
    # retrieve photo URLs from NASA API
    print("\n\n*****Grabbing Astronomy Pictures of the Day from NASA API...this may take a minute*****\n\n")
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
        im, h = urllib.request.urlretrieve(images[i])
        img = Image.open(im)
        img.save("/home/student/mycode/final_project/plaintext_images/"+images[i].rsplit('/', 1)[1])
        img.show()
        i += 1
    print("Success!!\n\n")

def getkey():
    key = get_random_bytes(16)
    return key

def encrypt(key):
    print("*****Encrypting photos*****\n\n")
    count = 1
    for pic in os.listdir("/home/student/mycode/final_project/plaintext_images"):
        if pic.endswith("png") or pic.endswith("jpg"):
            path = "/home/student/mycode/final_project/plaintext_images/" + pic
            with open(path, 'rb') as file1:  
                data = file1.read()
                cipher = AES.new(key, AES.MODE_CFB)
                ct_bytes = cipher.encrypt(data) 
                encrypted_filename = "enc_" + pic
                iv = b64encode(cipher.iv).decode('utf-8')
                ct = b64encode(ct_bytes).decode('utf-8')                                    
                results.update({encrypted_filename: {'iv':iv, 'ciphertext':ct}})  

                # the following lines make the encrypted images 'visible'                                
                num_bytes = len(ct)                                                         
                num_pixels = int((num_bytes+2)/3)
                W = H = int(math.ceil(num_pixels ** 0.5))
                imagedata = ct_bytes + b'\0' * (W*H*3 - len(ct_bytes))
                image = Image.frombytes('RGB', (W,H), imagedata)
                image.save("/home/student/mycode/final_project/encrypted/"+encrypted_filename)
        print(f"Photo {count} encrypted successfully")
        count += 1


def decrypt(key):
    i = 0 
    print("\n\n*****Decrypting photos*****\n\n")
    for pic in os.listdir("/home/student/mycode/final_project/encrypted"):
        if pic.endswith("png") or pic.endswith("jpg") and pic.startswith("enc"):
            path = "/home/student/mycode/final_project/encrypted/" + pic
            with open(path, 'rb') as file1:
                b64 = results[pic]
                iv = b64decode(b64['iv'])
                ct = b64decode(b64['ciphertext'])
                cipher = AES.new(key, AES.MODE_CFB, iv=iv)
                pt = cipher.decrypt(ct)
                decrypted_filename = "/home/student/mycode/final_project/decrypted/"+pic.replace("enc", "dec")
                with open(decrypted_filename, 'wb') as file2:
                    file2.write(pt)
        i += 1
        print(f"Photo {i} decrypted successfully")
    print("\n\nAll done! Check the images out in their respective folders.")


def main():
    getimages()
    key = getkey()
    encrypt(key)
    decrypt(key)
    

if __name__ == "__main__":
    main()