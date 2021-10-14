#Import Subprocess
import subprocess

#Import the Tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x250")


def select_folder():
   win.title("Toyota Invoice Parser")
   path= filedialog.askdirectory(title="Select a Directory where PDF files are located")
   Label(win, text=path, font=13).pack()
   print("Rscript pdf_parser.r "+path)
   
   subprocess.call("Rscript pdf_parser.r "+path, shell=True)
   sys.exit()
   
#Create a label and a Button to Open the dialog
Label(win, text="Select PDF Folder.\n Please Note after your selection the program will terminate. \n Your converted text file will be available in the folder where your pdf is located", font=('Aerial 18 bold')).pack(pady=20)
button= ttk.Button(win, text="Browse", command= select_folder)
button.pack(ipadx=5, pady=15)

win.mainloop()
