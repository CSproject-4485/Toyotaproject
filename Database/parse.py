#regular expression lib
#pip install regex
import re
import sys
import os

#Searches string for words with 17 characters
#Essentialy vin
vin = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')

with open ('test2.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    vin_matches = vin.finditer(contents)

    for match in vin_matches:
        #print(match)
        vin_string = contents[match.start():match.end()]




class carObj:

    def init(self, vin_num):
        self.vin_num = vin_num

p1 = carObj(vin_string)