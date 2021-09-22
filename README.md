# [Toyota PDF Invoice Analyzer](Toyota Financial Services - Vendor Cost Data Standardization.pdf)

Toyota receives thousands of PDFs in an email format. These invoices can be from many different sources including service stations, cleaning services, vehicle repair shops and so on. There is no way to standardize this data currently and get a cost breakdown of what services are provided and how much a car costs in a month. 





## Current Approach : 

* R Scripts are being used with the pdftools library to translate the PDFs into text files.
The text files have all the pdf data in a text format that can then be easily manipulated by a program.

* The initial PDFs are downloaded from a sharepoint library using a sharepoint api and a python script,  and then stored in a folder on the local machine.

* A mySQL database will be made on Azure free tier that will be able to organize the data and then represent it in a csv format

* The stretch goal is to have an application that will employ docker and scripts that call each other, and a front end that can then be used to query for certain things. 
