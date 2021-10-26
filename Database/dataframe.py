import re
import sys
import os
from parse import *
import pandas as pd


#print(vin_list)


df = pd.DataFrame(vin_list,columns=['Vin'])
df = df.assign(License=license_list)
df = df.assign(Payment=payment_list)

print(df)

df.to_csv('dummy.csv')