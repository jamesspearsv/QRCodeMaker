from tkinter import *
import qrcode

def makeCode (url, fileName):
    img = qrcode.make(url)
    img.save(f"{fileName}.png", "PNG")

def getInput():
    url = urlEntry.get()
    fileName = fileNameEntry.get()
    makeCode(url, fileName)

#Create app window
app = Tk()
app.title("QR Code Maker")
app.geometry("375x300")

#URL widget
urlLabel = Label(app, text='URL:', font=('bold', 14), pady=20, padx=20) #Lable widget for URL
urlLabel.grid(row=0, column=0) #places widget in window
urlEntry = Entry(app) #Entry widget for URL
urlEntry.grid(row=0, column=1)

#File name widget
fileNameLabel = Label(app, text='File Name:', font=('bold', 14), pady=20, padx=20) #Lable widget for fileName
fileNameLabel.grid(row=1, column=0) #places widget in window
fileNameEntry = Entry(app) #Entry widget for fileName
fileNameEntry.grid(row=1, column=1)

#Make Code button
btn = Button(app, text='Make Code', command=getInput)
btn.grid(row=2, column=1)

#Copyright text
copyrightLabel = Label(app, text='James Spears, 2020', font=('bold', 14), pady=20, padx=20) #Lable widget for URL
copyrightLabel.grid(row=3, column=1) #places widget in window

#Source Code text -> TODO implement link with button binding.
#sourceCode = Label(app, text='Source code:\nhttps://github.com/jamesspearsv/QRCodeMaker', font=('bold', 14), pady=20, padx=20) #Lable widget for URL
#sourceCode.grid(row=3, column=0) #places widget in window

#Start program
app.mainloop()