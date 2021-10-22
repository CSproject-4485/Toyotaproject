#regular expression lib
#pip install regex
import re
import sys
import os
import pandas as pd


class carObj:

    def __init__(self, vin_num):
        self.vin_num = vin_num

    def vin_total(self,vin_total):
        self.vin_total = vin_total

    def getList(self):
        return '{}'.format(self.vin_num)

#Searches string for words with 17 characters
#Essentialy vin
directory_filepath = '/Users/waldo/Desktop/db'
vin = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')

vin_list = []
count = 0
for files in os.listdir(directory_filepath):
    if files.endswith(".txt"):
        file = os.path.join(directory_filepath, files)
        #print(file)

        with open (file, 'r') as f:
            contents = f.read()

            vin_matches = vin.finditer(contents)

            for match in vin_matches:
                vin_string = contents[match.start():match.end()]
                vin_list.append(vin_string)
                count += len(vin_list)




print(vin_list)

# vin_table = {
#     "vin": ['ABC123']
# }

# df = pd.DataFrame(vin_table)

# print(df)

# df = pd.DataFrame()

df = pd.DataFrame(vin_list,columns=['Vin'])

print(df)

df.to_csv('dummy.csv')