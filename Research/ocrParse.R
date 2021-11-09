#!/usr/bin/env Rscript
#link : https://cran.r-project.org/web/packages/tesseract/vignettes/intro.html

#This file converts the pdf to png then reads the image

library(magick)

library(pdftools)

library(tesseract)



#grab the filename

filename <- "/Users/marwayahiaoui/Desktop/ABS_06.28.2021_invoices.pdf"



#Perform OCR text extraction directly this also works

text_extractionOCR<-pdf_ocr_text(

  filename,

  pages = NULL,

  opw = "",

  upw = "",

  language = "eng",

  dpi = 600

)

write(text_extractionOCR, "/Users/marwayahiaoui/Desktop/Image.txt")



##########################################################################

#use pdf_convert to convert to png the NULL its just to keep the default names of the same file

convertedfile_to_image<-pdf_convert(

  filename,

  format = "png",

  pages = NULL,

  filenames = NULL,

  dpi = 72,

  antialias = TRUE,

  opw = "",

  upw = "",

  verbose = TRUE

)

#the image_read will read the scanned blurry image 

input <- image_read(convertedfile_to_image)

#ocr() takes the input #The accuracy of the OCR process depends on the quality of the input image.

#You can often improve results by properly scaling the image, 

#removing noise and artifacts or cropping the area where the text exists

text <- input %>%

  image_resize("2000x") %>%

  image_convert(type = 'Grayscale') %>%

  image_trim(fuzz = 40) %>%

  image_write(format = 'png', density = '300x300') %>%

  tesseract::ocr() 

#write to a text file 

write(text, "Image.txt")
