# coding: utf-8

import requests
from bs4 import BeautifulSoup

import os, sys, io
import re
import logging
import datetime
from pathlib import Path
import writefile as W
import pandas as pd

# path = str(Path(os.getcwd()).parent)
Output_Path = str(os.path.join(os.getcwd(), 'Outputs'))
Log_Path = str(os.path.join(Output_Path,"Apopnd.log"))
Storage_Path = str(os.path.join(Output_Path,"APOPND_THSR.csv"))

print (Output_Path)
print (Log_Path)
print (Storage_Path)


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)-4s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers = [logging.FileHandler(Log_Path, 'w', 'utf-8'),])


class Apopnd(): #主要抓的地方
    def __init__(self):
        pass

    def Apopnd_Thsr(self):
        logging.info("Start downloading TSRC file...")    
        url = "http://www.hsr.gov.tw/public/files/artsinfo/1499995129-0.csv" # Target URL
        res = requests.post(url,verify=False)
        logging.info("Download URL : " + res.url)
        if(res.status_code == 200):
            # Filename = 'APOPND_THSR.csv' 
            # Storage_Path = Output_Path + "/data/xml/" 
            # print(res.text)
            try:
                # W.WritetoFile(res.text,Storage_Path,'')
                f = open(Storage_Path, "w")
                f.write(res.text)
                string = 'APOPND_THSR.csv is Saving Done.' 
                logging.info(string) 
            except:
                string = 'APOPND_THSR.xml is Saving Failed.'
                logging.info(string)

        return Storage_Path        
