from tkinter import *
from tkinter import ttk
import random
from PIL import Image,ImageTk, ImageDraw, ImageFilter
import json
t=[]
x=0
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def focus_next_window(self,event):
        event.widget.tk_focusNext().focus()
        return("break")
    def prev(self):
        global x
        x=x-1
        if x<=0:
            x=1329
        self.disp(x)
        #print(x)
       
            
    def nex(self):
        global x
        x=x+1
        if x>=1329:
            x=0
        self.disp(x)
        #print(x)
        
    def disp(self,x):
        with open('thirukkural.json', 'r',encoding='utf-8') as f:
            distros_dict = json.load(f)
        s=distros_dict['kural'][x]['Line1']
        t=distros_dict['kural'][x]['Line2']
        l=len(distros_dict['kural'][x]['mk'])
        meantam=distros_dict['kural'][x]['mk'][:int(l/2)]
        meantam1=distros_dict['kural'][x]['mk'][int(l/2):]
        translation=distros_dict['kural'][x]['Translation']
        self.bLabel['text']=" "*1920
        self.cLabel['text']=" "*1920
        self.dLabel['text']=" "*1920
        self.dLabel1['text']=" "*1920
        self.eLabel['text']=" "*1920
        self.bLabel['text'] = s
        self.cLabel['text'] = t
        self.dLabel['text'] = meantam
        self.dLabel1['text'] = meantam1
        self.eLabel['text'] = translation
        self.kuralLabel['text'] ="Kural ["+str(x+1)+"/1330]"
    def rnd(self):
        global x
        x=random.randint(0,1330)
        self.disp(x)
        #print(x)
    def selectcombo(self,event):
        global x
        x=int(self.kuralnos.get())-1
        self.disp(x)
    def create_widgets(self):
        global x
        image = Image.open("THIRU.png")
        image.putalpha(78)
        photo=ImageTk.PhotoImage(image)
        label = Label(self,image = photo)
        label.image = photo # keep a reference!
        label.grid(row=0,column=0,columnspan=600,rowspan=600)
        with open('thirukkural.json', 'r',encoding='utf-8') as f:
            distros_dict = json.load(f)
        s=distros_dict['kural'][x]['Line1']
        t=distros_dict['kural'][x]['Line2']
        l=len(distros_dict['kural'][x]['mk'])
        meantam=distros_dict['kural'][x]['mk'][:int(l/2)]
        meantam1=distros_dict['kural'][x]['mk'][int(l/2):]
        translation=distros_dict['kural'][x]['Translation']
        image1 = Image.open("THIRU.png")
        photo5=ImageTk.PhotoImage(image1)
        self.plabel = Label(self,image = photo5)
        self.plabel.image = photo5 # keep a reference!
        self.plabel.grid(row=1,column=1,pady=10,sticky=W)
        self.aLabel=Label(self,text='Thirukkural By Thiruvalluvar ',fg="dark blue",font="Verdana 32 bold italic")
        self.aLabel.grid(row=1,column=2,pady=10,sticky=W)
        self.bLabel=Label(self,text=s,fg="dark green",font="Latha 20 bold italic")
        self.bLabel.grid(row=2,column=1,columnspan=100,pady=10,sticky=W)
        self.cLabel=Label(self,text=t,fg="dark green",font="Latha 20 bold italic")
        self.cLabel.grid(row=3,column=1,columnspan=100,pady=10,sticky=W)
        self.dLabel=Label(self,text=meantam,fg="#897654",font="Latha 12 bold")
        self.dLabel.grid(row=4,column=1,columnspan=300,pady=10,sticky=W)
        self.dLabel1=Label(self,text=meantam1,fg="#897654",font="Latha 12 bold")
        self.dLabel1.grid(row=5,column=1,columnspan=300,pady=10,sticky=W)
        self.eLabel=Label(self,text=translation,fg="#ff6576",font="Verdana 12 bold")
        self.eLabel.grid(row=6,column=1,columnspan=300,pady=10,sticky=W)
        self.prevButton=Button(self,text="Previous",command=self.prev)
        self.prevButton.grid(row=7,column=1,pady=10,sticky=W)
        self.kuralnums=[x+1 for x in range (0,1330)]
        self.kuralnos=ttk.Combobox(self, values=self.kuralnums)
        self.kuralnos.bind("<<ComboboxSelected>>", self.selectcombo)
        self.kuralnos.bind("<Return>", self.selectcombo)
        self.kuralnos.grid(row=7,column=2,pady=10,sticky=W)
        self.nextButton=Button(self,text="Next",command=self.nex)
        self.nextButton.grid(row=7,column=3,pady=10,sticky=W)
        self.subButton=Button(self,text="Random Quote",command=self.rnd)
        self.subButton.grid(row=8,column=1,pady=10,sticky=W)
        self.kuralLabel=Label(self,text="Kural ["+str(x+1)+"/1330]",fg="dark red",font="Verdana 12 bold")
        self.kuralLabel.grid(row=8,column=2,pady=10,sticky=W)
        self.quitButton=Button(self,text="Exit Application",command=root.destroy)
        self.quitButton.grid(row=8,column=3,pady=10,sticky=W)
        
        
root=Tk()
root.geometry("1024x600")
root.overrideredirect(1) 
#root.iconbitmap('thiru.ico') can uncomment for windows OS alone
app=Application(root)
root.mainloop()
