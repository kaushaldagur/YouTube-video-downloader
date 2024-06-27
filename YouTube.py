from tkinter import *
from pytube import YouTube
import tkinter.messagebox as tmsg
import time

def Links_video():
        try:
                res=["720p","480p","360p","240p","144p"]
                global linkVar
                print(linkVar.get())
                global LinkEnrty
                svar.set("Getting Videos...")
                sbar.update()
                yt=YouTube(linkVar.get())
                Links_video.videosLink=yt.streams.filter(progressive=True)
                VIDval=0
                Links_video.VIDvar=IntVar()
                for Vres in res:
                        try:
                                a=Links_video.videosLink.get_by_resolution(Vres)
                                if a!=None:
                                        Radiobutton(F2,text=Vres + " mp4",variable=Links_video.VIDvar,value=VIDval).pack()
                                        VIDval+=1
                                svar.set('Plaese select from above options!!')
                                sbar.update()
                        except:
                                pass
        except:
                svar.set('Getting Videos...')
                sbar.update()
                time.sleep(2)
                Label(F2,text="Oops ;-; Video Not Found\nCheck Connection and Link!!").pack()
                svar.set('Ready...')
                sbar.update()


def LinksAudioDownload():
        try:
                global linkVar
                print(linkVar.get())
                global LinkEnrty
                svar.set('Getting Audio...')
                sbar.update()
                yt=YouTube(linkVar.get())
                audioLink=yt.streams.filter(only_audio=True)
                finalAudlink=audioLink[0]
                svar.set('Downloading Audio...')
                sbar.update()
                time.sleep(1)
                finalAudlink.download("/storage/emulated/0/YT downloads(aman)2")
                svar.set('Downloaded Successfully :)')
                sbar.update()
                time.sleep(2)
                svar.set('Ready...')
                sbar.update()
        except:
                Label(F2,text="Oops ;-; Audio Not Found\nCheck Connection and Link!!").pack()

def VIDdownload():
        try:
                svar.set('Downoading Video...')
                sbar.update()
                finalVidlink=Links_video.videosLink[Links_video.VIDvar.get()]
                finalVidlink.download("/storage/emulated/0/YT downloads(aman)2")
                svar.set('Downloaded Successfully :)')
                sbar.update()
                time.sleep(2)
                svar.set('Ready...')
                sbar.update()
        except:
                tmsg.showinfo(";-;","Seems Nothing was selected\nClick on\nGet Videos > Select the Resolution > Download")


root = Tk()
root.title("YouTube Video Downloader")
root.geometry("1000x600")

Label(root,text="YouTube Video Downloader",font=("default 15 bold")).pack()

F1=Frame(root)

linkVar=StringVar()
Label(F1,text="Paste Link Here:",font=("default 9 bold"),pady=30).pack()
LinkEntry=Entry(F1,textvariable=linkVar,width=50)
LinkEntry.pack()
VidButton=Button(F1,text="Get Videos",command=Links_video)
VidButton.pack(anchor=W,pady=5)
AudButton=Button(F1,text="Download MP3 Format",command=LinksAudioDownload)
AudButton.pack(anchor=W,pady=5)

F1.pack()

F2=Frame(root,relief=SUNKEN,highlightbackground="black",highlightthickness=3)

F2.pack()

F3=Frame(root)
Button(F3,text="Download VIDEO",command=VIDdownload).pack(pady=10)
F3.pack()
svar=StringVar()
svar.set("Ready")
sbar=Label(root,textvariable=svar,relief=SUNKEN)
sbar.pack(side=BOTTOM,fill=X)
root.mainloop()
