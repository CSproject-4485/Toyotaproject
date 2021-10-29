import sys
import os
import re
import pandas as pd

#Read in the directory passed in with the script
arg = sys.argv[1]
directory_filepath = arg

#Create the patterns which we can use to extract fields
vin_number = re.compile(r'\w\w\w\w\w\w\w\w\w\w\w\w\w\w\d\d\d')
date = re.compile(r'Date')
payment_due_pattern = re.compile(r'Due:')
payment_amount_pattern = re.compile(r'THIS AMOUNT\s*\d')
payment_decimal_pattern = re.compile(r'\( \d')
database = []

def extract(pattern, file_contents, start_bytes, end_bytes):
    pattern_list = []
    pattern_match = pattern.finditer(file_contents)
    for matches in pattern_match:
        extracted_data = file_contents[matches.start()+start_bytes:matches.end()+end_bytes]
        pattern_list.append(extracted_data)
    return pattern_list
    
def find_service_type(file_contents):
#    if file_contents.contains("oil"):
#        return True
#    else:
#        return False
    return "Parking"

def find_payments(file_contents, vin_list):
    payment_list = []
    payment_phrase_due= payment_due_pattern.finditer(file_contents)
    payment_phrase_amount = payment_amount_pattern.finditer(file_contents)
    payment_phrase_decimal = payment_decimal_pattern.finditer(file_contents)
    
    for match in payment_phrase_due:
         payment_string = " ".join(contents[match.end():match.end()+8].split())
         cleaned_payment = '$'+payment_string  if payment_string.find("$") == -1 else payment_string
         payment_list.append(cleaned_payment)
    
    if len(payment_list) == len(vin_list):
        return payment_list
    
    for match in payment_phrase_amount:
        payment_string = " ".join(contents[match.end()-2:match.end()+7].split())
        payment_string = re.sub('[a-zA-Z\s]', '', payment_string)
        cleaned_payment = '$'+payment_string  if payment_string.find("$") == -1 else payment_string
        payment_list.append(cleaned_payment)
    
    if len(payment_list) == len(vin_list):
        return payment_list
    
    for match in payment_phrase_decimal:
         payment_string = " ".join(contents[match.end()-1:match.end()+5].split())
         cleaned_payment = '$'+payment_string  if payment_string.find("$") == -1 else payment_string
         payment_list.append(cleaned_payment)
    
    if len(payment_list) > len(vin_list):
        payment_list = payment_list[:len(vin_list)]
    elif len(payment_list) < len(vin_list):
        diff = len(vin_list) - len(payment_list)
        for i in range(diff):
            payment_list.append("UNKNOWN")
    return payment_list
    
#Loop through all the files in the directory
for files in os.listdir(directory_filepath):
    if files.endswith(".txt"):
        file = os.path.join(directory_filepath, files)
        
        if os.stat(file).st_size <100:
            print("Convert ERROR ",files,"\n")
            os.remove(file)
            continue
        else:
            print("Convert SUCCESS: ", file)

        with open (file, 'r') as f:
            contents = f.read()
            
            extracted_vins = extract(vin_number, contents, 0, 0)
            
            potential_date = re.findall(r'(\d+/\d+/\d+)',contents)
            date = "UNKNOWN"
            if len(potential_date)>0:
                date = potential_date[0]
            else:
                file_name = files.split("_")
                for parts in file_name:
                    if '.' in parts and len(parts) > 6:
                        date = parts
                        break
            
            service_type = find_service_type(contents)
            
            payments_list = find_payments(contents,extracted_vins)
            
            invoice_name = files.split("_")[0]
            
            dictionary = {}
            count = 0
            for vin in extracted_vins:
                if vin in dictionary:
                    count+=1
                else:
                    dictionary[vin] = payments_list[count]
                    count+=1
                    
            for keys in dictionary:
                vin = keys
                amount = dictionary[keys]
                database.append( tuple((vin, amount, date, service_type, invoice_name)) )
            
        print(dictionary)
        #print("VINs: ",extracted_vins)
       # print("Payments: ", payments_list)
        print("Date: ", date)
        print("Type of service: ", service_type)
        print("Invoice Name: ", invoice_name)
        
        print("\n")
        os.remove(file)
        
#print(database)

vin_records = []
payment_records = []
date_records = []
service_type_records = []
invoice_name_records = []
for records in database:
    vin_records.append(records[0])
    payment_records.append(records[1])
    date_records.append(records[2])
    service_type_records.append(records[3])
    invoice_name_records.append(records[4])
    

df = pd.DataFrame(vin_records,columns=['VIN'])
df = df.assign(Payment=payment_records)
df = df.assign(Date=date_records)
df = df.assign(Service=service_type_records)
df = df.assign(Invoice_Name=invoice_name_records)

print(df)

df.to_csv('output.csv')
