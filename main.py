#!/usr/bin/env python
#https://docs.python.org/2/howto/argparse.html
#this application
import json
import os
import sys
import pprint
import argparse
from PIL import Image
pp = pprint.PrettyPrinter()

# VAULT_ADDR =  os.environ.get('VAULT_ADDR', 'http://localhost:8200')

def crawlDirectories(inputPath):
    for dirpath, dirnames, files in os.walk(inputPath):
        pp.pprint(f'Found directory: {dirpath}')
        for file_name in files:
            file, ext = os.path.splitext(dirpath+os.sep+file_name)
            pp.pprint(ext)
            if ext in [".png",".jpg",".jpeg"]:
                convertImage(dirpath+os.sep+file_name)
            
def convertImage(infile):
    file, ext = os.path.splitext(infile)
    pp.pprint(file)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP", quality=70 )
    os.remove(infile)

def main():
    pp.pprint("Starting")
    crawlDirectories("/Users/guy/Downloads/Personal/Pictures")
    

if __name__ == '__main__':
    main()
