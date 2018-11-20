
# import requests
import os, sys, io
import re
import logging
import datetime
from pathlib import Path
import csv

Output_Path = str(os.path.join(os.getcwd(), 'Outputs'))
Storage_Path = str(os.path.join(Output_Path,"APOPND_THSR_Ok.csv"))

class Apoload():

    def __init__(self, target_file_path):
        self.Apoload_Thsr(target_file_path)

    def Get_Latitude_Longitude(self, str):
        if(str.find(",")==-1):
            return []
        else:
            return str.split(",")


    def Apoload_Thsr(self,target_file_path):

        latilongis = [] # Latitude and longitude
        with open(target_file_path, newline='') as csvfile:
            # Read CSV
            rows = csv.reader(csvfile)

            # Get Latitude-and-longitude row and parse
            for row in rows:
                if(len(row) > 0 and row[0]=="經緯座標"):
                    cleanRow = [x.replace("\r\n","") for x in row]
                    for val in cleanRow[1:len(row)]:
                        if val:
                            latilongi = self.Get_Latitude_Longitude(val)    
                            print(latilongi)
                            latilongis.append(latilongi)
            
            # Output to the other CSV file
            outputStr = str(latilongis)
            print(outputStr)
            f = open(Storage_Path, "w")
            f.write(outputStr)

        


