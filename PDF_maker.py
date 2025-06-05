'''This file will be used to combine my PDF's for all my document.
I had a problem where i had to download too many different files for 
my job applications'''
from pypdf import PdfWriter

merger = PdfWriter()

#picking the files i want to combine/merge
input1 = open(path, 'rb')
input2 = open(path'rb')

#Appending to new file and selecting which specific pages i want from my pdf
merger.append(fileobj=input1, pages=[0, 2, 3, 4])
merger.append(fileobj=input2, pages=[0, 2, 3, 4])



output = open(path,'wb')
merger.write(output)

merger.close()