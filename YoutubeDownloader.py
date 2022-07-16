from tkinter import *
from pytube import YouTube 
from tkinter import messagebox
root = Tk()

root.title("Youtube Downloader")
root.geometry('300x200')
root.configure(background="white")
root.resizable(False,False) 


def download(link):
    SAVE_PATH = ""
    my_video = YouTube(link)
    d_video = my_video.streams.get_highest_resolution()
    try: 
    # downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        messagebox.showinfo("Hata!","İndirme işlemi gerçekleştirilemedi. İnternet bağlantınızı veya linki kontrol edin.") 
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')

def clearEntry():
    entry1.delete(0,"end")


entry1 = Entry(root,width = 50,fg ="black",bg = "white",borderwidth=2,font = ("Arial",10))
entry1.pack(padx=30, pady=40)
entry1.insert(0,"Linki giriniz...")

entry1.bind("<FocusIn>", lambda event:clearEntry())

download_button = Button(root,text= "İndir",command= lambda: download(entry1.get()),height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10))
download_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()