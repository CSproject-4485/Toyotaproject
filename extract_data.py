#test.py
import sys
import os
import re

arg = sys.argv[1]
directory_filepath = arg
vin = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')
payment = re.compile(r'Due:')
payment2 = re.compile(r'AMOUNT ')
decimal_payment = re.compile(r'(?:\.\d+)?')

#Loop through all the files in the directory
for files in os.listdir(directory_filepath):
    if files.endswith(".txt"):
        file = os.path.join(directory_filepath, files)
        print(file)

        with open (file, 'r') as f:
            contents = f.read()

            vin_matches = vin.finditer(contents)
            payment_matches = payment.finditer(contents)
            payment_matches_2 = payment2.finditer(contents)
            decimal_payment_ = decimal_payment.finditer(contents)
                

            for match in vin_matches:
                vin_string = contents[match.start():match.end()]
                print("VIN ", vin_string)
                
            for match in payment_matches:
                pay_string = contents[match.end():match.end()+9]
                print("Payments ", pay_string)
                
            for match in payment_matches_2:
                pay_string_2 = contents[match.start():match.end()+40]
                if  len(pay_string_2)>0:
                    print("Payments 2 ", pay_string_2)
                    
            for match in payment_matches_2:
                decimal = contents[match.end():match.end()+9]
                print("Payments Decimal ", decimal)
        
        
        
        
        os.remove(file)


