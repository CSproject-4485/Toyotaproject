
####
# helpful URL:https://data.library.virginia.edu/reading-pdf-files-into-r-for-text-mining/ 
 # title: "R script"
#output: try parding pdf's 
#Author: Marwa Yahiaoui
#####
## must install.packages("pdftools")  in console 
library(pdftools)
library(tm)
setwd("/Users/marwayahiaoui/Desktop/invoices-samples")

#Reading one file only testing 

file2<- "/Users/marwayahiaoui/Desktop/invoices-samples/invoice22.pdf"
print(paste("All info on this file using pdf_info:"))
pdf_info(file2)

file2read<-pdf_text(file2)
file2read

#####reading all files from folder#########################

#vector of PDF file  using list.files function. 
#only choose files ending with “pdf”

pdf_filesFolder <- list.files("~/Desktop/invoices-samples", pattern = "pdf$", full.names = T)
print(paste("Name of pdf file:", pdf_filesFolder))

folderPath =file.path("/Users/marwayahiaoui/Desktop/invoices-samples")
folderPath

length1 = length(dir(folderPath))
print(paste("Length of folder is :", length1, "files"))

dirpdf = dir(folderPath)
dirpdf[1]
dirpdf[2]
dirpdf[3]
dirpdf[4]

#use lapply() to apply pdf_text or other pdftools function 
#iteractively across each of the files
PDFreader = function(x){
  t = pdf_text (x)
  page_2 =t   #extracting text pdf_text.
}
folder =file.path("/Users/marwayahiaoui/Desktop/invoices-samples")
folder

length1 = length(dir(folder))
length1

results=lapply(pdf_filesFolder, PDFreader)
results #can just print everything  here
length(results)
write(unlist(results),"~/Desktop/invoices-samples/test0.csv")
write(unlist(results),"~/Desktop/invoices-samples/test2.txt")
#Using the lapply function, 
#to each element in the “files” vector and create an object called “results”.

print(paste("The length of each vector corresponds to the number of pages in the PDF file, apply to each element:"))
lapply(results, length)


######try with loop python ########## somehow not doing all invoices not sure why!!!

length(pdf_filesFolder)
##ok only when i take the i then it works with unlist 
for(i in 1:length(pdf_filesFolder)){
  pdf1= file.path("/Users/marwayahiaoui/Desktop/invoices-samples", dirpdf[i])
  write((unlist(results[i])), "~/Desktop/invoices-samples/test3.txt")
}

##################################
fileNames = Sys.glob("*.pdf")  # shell pattern matching to select files.
fileNames
for (fileName in fileNames) {
  # read data:
  sample = pdf_text(fileName)
  write(sample,
        "~/Desktop/invoices-samples/test4.txt")
}

