
#!/usr/bin/env Rscript
absolute_file_path = commandArgs(trailingOnly=TRUE)

## must install.packages("pdftools")  in console 
library(pdftools)
library(tm)

pdf_folder<-dir(absolute_file_path) # Store the absolute path as a directory
pdf_count<-0 # Pdf count is 0 so far.

for (files in 1:length(pdf_folder)) # Loop through all the pdfs in the pdf folder
{
    if(grepl("pdf", pdf_folder[files]))
  {
    filename<-paste("/", pdf_folder[files], sep='') #Add a slash to the filename
    file_handle<-paste(absolute_file_path, filename, sep='') # Grab the file name 

    file_read<-pdf_text(file_handle) #Convert the pdf into text

    pdf_count = pdf_count +1 # Increase the count of the PDF that have been parsed

    file_name_without_tag<-substr(filename,1,nchar(filename)-4) # Get rid of the .pdf

    print(file_name_without_tag)
    file_number<- paste("_", pdf_count, sep='')

    converted_file_tag<-paste(file_name_without_tag,paste(file_number,".txt", sep=''))
    converted_file_destination<-paste(absolute_file_path,converted_file_tag, sep='')

    write(unlist(file_read), converted_file_destination)
  }
}
#Control heads back to the main window
