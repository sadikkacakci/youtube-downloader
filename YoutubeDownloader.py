from tkinter import *
from pytube import YouTube 
from tkinter import messagebox
import os
root = Tk()

root.title("Youtube Downloader")
root.geometry('300x200')
root.configure(background="white")
root.resizable(False,False) 


def downloadMP3(link):
    SAVE_PATH = " "
    my_video = YouTube(link)
    d_video = my_video.streams.filter(only_audio=True).first()
    try:
        out_file = d_video.download(output_path=SAVE_PATH)
    except: 
        messagebox.showinfo("Hata!","İndirme işlemi gerçekleştirilemedi. İnternet bağlantınızı veya linki kontrol edin.") 
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


def downloadMP4(link):
    SAVE_PATH = " "
    my_video = YouTube(link)
    d_video = my_video.streams.get_highest_resolution()
    try: 
        d_video.download(SAVE_PATH) 
    except: 
        messagebox.showinfo("Hata!","İndirme işlemi gerçekleştirilemedi. İnternet bağlantınızı veya linki kontrol edin.") 
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')

def clearEntry():
    entry1.delete(0,"end")


entry1 = Entry(root,width = 50,fg ="black",bg = "white",borderwidth=2,font = ("Arial",10))
entry1.pack(padx=30, pady=40)
entry1.insert(0,"Enter the link...")

entry1.bind("<FocusIn>", lambda event:clearEntry())

download_button_mp4 = Button(root,text= "Download MP4",command= lambda: downloadMP4(entry1.get()),height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10))
download_button_mp4.place(relx=0.5, rely=0.5, anchor=CENTER)

download_button_mp3 = Button(root,text= "Download MP3",command= lambda: downloadMP3(entry1.get()),height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10))
download_button_mp3.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()