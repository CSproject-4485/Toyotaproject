#regular expression lib
#pip install regex
import re
import sys
import os
import pandas as pd

class carObj:

    def __init__(self, vin_num, count):
        self.vin_num = vin_num
        self.count = count

    def vin_total(self,vin_total):
        self.vin_total = vin_total

    def getList(self):
        return '{}'.format(self.vin_list)
    

def append_list(string,list,count):
        list.append(string)
        count += len(list)
        return list

#Searches string for words with 17 characters
#Essentialy vin
directory_filepath = "C:\\Users\D'artagnan wong\Desktop\CS Project"
vin = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')
license_car = re.compile(r'license:')
payment = re.compile(r'Due:')
#payment2 = re.compile(r'AMOUNT ')

vin_list = []
license_list = []
payment_list = []
count = 0
for files in os.listdir(directory_filepath):
    if files.endswith(".txt"):
        file = os.path.join(directory_filepath, files)

        with open (file, 'r') as f:
            contents = f.read()

            vin_matches = vin.finditer(contents)
            license_matches = license_car.finditer(contents)
            payment_matches = payment.finditer(contents)
            #payment_matches_2 = payment2.finditer(contents)

            for match in vin_matches:
                vin_string = contents[match.start():match.end()]
                append_list(vin_string,vin_list,count)
       
            
            for match in license_matches:
                license_string = contents[match.end():match.end()+7]
                append_list(license_string,license_list,count)
         
            for match in payment_matches:
                payment_string = contents[match.end():match.end()+9]
                append_list(payment_string,payment_list,count)         