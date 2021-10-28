import sys
import os
import re
from collections import Counter
import pandas as pd

directory_filepath = "C:\\Users\D'artagnan wong\Desktop\\toyota"
vin = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')
payment = re.compile(r'Due:')
payment2 = re.compile(r'THIS AMOUNT\s*\d')
#payment3 = re.compile(r'TOTAL CHARGES  ')
payment4 = re.compile(r'\( \d')
license_car = re.compile(r'license:')
decimal_payment = re.compile(r'(?:\.\d+)?')

vin_list = []
license_list = []
payment_list = []
count = 0


def append_list(string,list,count):
        list.append(string)
        count = len(list)
        return list, count


#Loop through all the files in the directory
for files in os.listdir(directory_filepath):
    if files.endswith(".txt"):
        file = os.path.join(directory_filepath, files)

        with open (file, 'r', encoding='utf-8') as f:
            contents = f.read()

            vin_matches = vin.finditer(contents)
            license_matches = license_car.finditer(contents)
            payment_matches = payment.finditer(contents)
            payment_matches2 = payment2.finditer(contents)
            #payment_matches3 = payment3.finditer(contents)
            payment_matches4 = payment4.finditer(contents)
            #payment_matches_2 = payment2.finditer(contents)

            for match in vin_matches:
                vin_string = contents[match.start():match.end()]
                append_list(vin_string,vin_list,count)
                vin_list = list(dict.fromkeys(vin_list))
                count = len(vin_list)
                               


            for match in license_matches:
                license_string = contents[match.end():match.end()+7]
                if(len(license_string) == 0):
                    continue
                else:
                    append_list(license_string,license_list,count)


            for match in payment_matches:

                payment_string = contents[match.end():match.end()+8]
                print(file)
                print('count:')
              
                # using split() + join()
                # remove additional space from string 
                payment_string = " ".join(payment_string.split())


                if(payment_string.find("$") == -1):
                    payment_string = '$'+ payment_string
               
                append_list(payment_string,payment_list,count)

                if(count != len(payment_string)):
                    payment_list = list(dict.fromkeys(payment_list))
                else:
                    print(count)
                    print(len(payment_list)) 


                



            for match in payment_matches2:
                payment_string = contents[match.end()-2:match.end()+7]
                # using split() + join()
                # remove additional space from string 
                print(file)
                print('count:')
                
                payment_string = " ".join(payment_string.split())

                
                payment_string = re.sub('[a-zA-Z\s]', '', payment_string)

                if(payment_string.find("$") == -1):
                    payment_string = '$'+ payment_string




               # payment_list = list(dict.fromkeys(payment_list))
                append_list(payment_string,payment_list,count)

                
                
                # if(count == len(payment_string)):
                #     payment_list = list(dict.fromkeys(payment_list))
                # else:
                #     print(count)
                #     print(len(payment_list))
                
                


            # for match in payment_matches3:
            #     payment_string = contents[match.end():match.end()+21]

            #     # using split() + join()
            #     # remove additional space from string 
            #     payment_string = " ".join(payment_string.split())

            #     append_list(payment_string,payment_list,count)
            #     #print(str(res))

            for match in payment_matches4:
                payment_string = contents[match.start()+2:match.end()+5]

                # using split() + join()
                # remove additional space from string 
                print(file)
                print('count:')
                print(count)
                
                payment_string = " ".join(payment_string.split())
                #payment_list = list(dict.fromkeys(payment_list))

               

                append_list(payment_string,payment_list,count)


                             
                if(count != len(payment_string)):
                    payment_list = list(dict.fromkeys(payment_list))
                else:
                    print(count)
                    print(len(payment_list))
                    
                
                if(payment_string.find("$") == -1):
                    payment_string = '$'+ payment_string
                
                   
                    

        #os.remove(file)

# vin_list = list(dict.fromkeys(vin_list))
#payment_list = list(dict.fromkeys(payment_list))


print(vin_list)
print(payment_list)

df = pd.DataFrame(vin_list,columns=['Vin'])
# df = df.assign(License=license_list)
df = df.assign(Payment=payment_list)

print(df)

df.to_csv('output.csv')