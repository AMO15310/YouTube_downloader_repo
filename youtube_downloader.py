#import libraries

from tkinter import *
from pytube import YouTube
#create main window

root =Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('YouTube Downloader')

#create window content a label
Label(root,text='Youtube Video Downloader',font='arial 20 bold').pack()

#create field to enter the link
link = StringVar()
Label(root,text='Paste your link here',font='arial 15 bold',bg = 'green').place(x=160,y=60)
link_enter = Entry(root,width=70,textvariable = link).place(x=32,y=90)


#create the download function
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)


    #create a download button
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
#root = Tk()
#execute program
root.mainloop()
