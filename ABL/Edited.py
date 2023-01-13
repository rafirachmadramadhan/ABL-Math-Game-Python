from tkinter import *
from tkinter_custom_button import *
from tkinter import messagebox
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import scrolledtext
import random

def raise_frame(frame):
    frame.tkraise()

level=0
life=5

jawaban = [
    9,
    11,
    14,
    17,
    20,
    17,
    22,
    25,
    26,
    28,
    31,
    34,
    39,
    45,
    47,
    53,
    57,
    61,
    64,
    68
]

tombolpasti= [
    3,
    7,
    5,
    8,
    4,
    6,
    4,
    8,
    7,
    13,
    16,
    11,
    23,
    29,
    35,
    9,
    11,
    14,
    17,
    15
]

# def kiri():
#     x=[]
#     for i in range(jawaban[level]-tombolpasti[level],jawaban[level]-tombolpasti[level]+6):
#         x+=[i]
#     random.shuffle(x)
#     return x

# def kanan():     
#     y=[]
#     for j in range(tombolpasti[level],tombolpasti[level]+6):
#         y+=[j]
#     random.shuffle(y)
#     return y

# kiri=kiri()
# kanan=kanan()


def cetak(nilai):
    l.delete(0,END)
    l.insert(0, str(nilai))
def cetak2(nilai):
    s.delete(0,END)
    s.insert(0, str(nilai))
def cetak3(nilai):
    r.delete(0,END)
    r.insert(0, str(nilai))

def cek():
    # global jawabanuser
    global level,life
    if level<5:
        try:    
            z = int(l.get()) + int(s.get())
        except:
            return     
    elif level>4 and level<10:
        try:    
            z = int(l.get()) - int(s.get())
        except:
            return          
    elif level>9 and level<15:    
        try:    
            z = int(l.get()) + int(s.get())
        except:
            return      
    elif level>14 and level<20:     
        try:    
            z = int(l.get()) - int(s.get())
        except:
            return      
        
    
    if z == jawaban[level]:
        level+=1
        
        if level>0 and level<5:
            messagebox.showinfo("Wuih... Betul", "Eeehhh! pintar banget si")
        elif level>4 and level<10:
            messagebox.showinfo("Wuih... Betul", "Titisannya einstein ya? Jenius!")
        elif level>9 and level<15:
            messagebox.showinfo("Wuih... Betul", "Inimah diatas Superior!!")
        elif level>14 and level<19:
            messagebox.showinfo("Wuih... Betul", "Inimah diatas Jenius!!")
        elif level==19:
            messagebox.showinfo("Wuih... Betul", "Fix otak einstein")
        elif level==20:
            raise_frame(f5)
            level = 0
            life = 5
            TkinterCustomButton(master=f5, text='Back', text_font=("Segoe Print", 12),cursor="hand2", 
            command=lambda:raise_frame(f1),
            height=25,width=90).place(x= 25 , y=25)
            
        ngacak()
        ssss.config(text=jawaban[level])
        displevel.config(text=f"level: {level+1}")
        
    else:
        life-=1
        if level<5:
            if life>3:
                messagebox.showerror("Yah... Salah", "Sepertinya anda kurang pintar\nCoba Lagi!!!!")
            elif life<4 and life>0:
                messagebox.showerror("Yah... Salah lagi", "Sepertinya tidak pintar\nCoba Lagi!!!!")
        elif level>4:
            if life>3:
                messagebox.showerror("Yah... Salah", "Yook bisa yok!")
            elif life<4 and life>0:
                messagebox.showerror("Yah... Salah lagi", "Sulit si emang")
        if life==0:
            level=0
            messagebox.showerror("Yah... GAme Over", "Sulit si emang permainnanya")
            ngacak()
            ssss.config(text=jawaban[level])
            displevel.config(text=f"level: {level+1}")
            life=5
            for i in range(life):
                Label(f2,image=ipng,bg="mistyrose").place(x=20*i,y=570)
            
        for i in range(life+1):
            Label(f2,image=ipng2,bg="mistyrose").place(x=20*i,y=570)
        for i in range(life):
            Label(f2,image=ipng,bg="mistyrose").place(x=20*i,y=570)
             
def ngacak():
    global t1,t2,t3,t4,t5,t6,t1l,t2l,t3l,t4l,t5l,t6l,operasi1,operasi2
    x=[]
    for i in range(jawaban[level]-tombolpasti[level],jawaban[level]-tombolpasti[level]+6):
        x+=[i]
    random.shuffle(x)
    y=[]
    for j in range(tombolpasti[level],tombolpasti[level]+6):
        y+=[j]
    random.shuffle(y)
    kiri=x
    kanan=y
    if level<30:
        t1=TkinterCustomButton(master=f2,text=kiri[0],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[0]),cursor="hand2")
        t1.place(x=50, y=240)
        t2=TkinterCustomButton(master=f2,text=kiri[1],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[1]),cursor="hand2")
        t2.place(x=125, y=240)
        t3=TkinterCustomButton(master=f2,text=kiri[2],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[2]),cursor="hand2")
        t3.place(x=50, y=340)
        t4=TkinterCustomButton(master=f2,text=kiri[3],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[3]),cursor="hand2")
        t4.place(x=125, y=340)
        t5=TkinterCustomButton(master=f2,text=kiri[4],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[4]),cursor="hand2")
        t5.place(x=50, y=440)
        t6=TkinterCustomButton(master=f2,text=kiri[5],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[5]),cursor="hand2")
        t6.place(x=125 ,y=440)

        t1l=TkinterCustomButton(master=f2,text=kanan[0],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[0]),cursor="hand2")
        t1l.place(x=300 ,y=240)
        t2l=TkinterCustomButton(master=f2,text=kanan[1],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[1]),cursor="hand2")
        t2l.place(x=375 ,y=240)
        t3l=TkinterCustomButton(master=f2,text=kanan[2],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[2]),cursor="hand2")
        t3l.place(x=300 ,y=340)
        t4l=TkinterCustomButton(master=f2,text=kanan[3],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[3]),cursor="hand2")
        t4l.place(x=375 ,y=340)
        t5l=TkinterCustomButton(master=f2,text=kanan[4],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[4]),cursor="hand2")
        t5l.place(x=300 ,y=440)
        t6l=TkinterCustomButton(master=f2,text=kanan[5],bg='salmon',
        text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[5]),cursor="hand2")
        t6l.place(x=375 ,y=440)
    operasi2.place_configure(x=600,y=600)
    operasi1.place_configure(x=235 ,y=140)
    operasi1.config(text="+")
    l.place_configure(x=70, y=150)
    s.place_configure(x=315 ,y=150)
    r.place_configure(x=600 ,y=600)
    l.delete(0,END)
    s.delete(0,END)
    # r.delete(0,END)
    # t1.place_configure(x=50, y=240)
    # t2.place_configure(x=125, y=240)
    # t3.place_configure(x=50, y=340)
    # t4.place_configure(x=125, y=340)
    # t5.place_configure(x=50, y=440)
    # t6.place_configure(x=125 ,y=440)
    # t1l.place_configure(x=300 ,y=240)
    # t2l.place_configure(x=375 ,y=240)
    # t3l.place_configure(x=300 ,y=340)
    # t4l.place_configure(x=375 ,y=340)
    # t5l.place_configure(x=300 ,y=440)
    # t6l.place_configure(x=375 ,y=440)
    # t1m.place_configure(x=600 ,y=600)
    # t2m.place_configure(x=600 ,y=600)
    # t3m.place_configure(x=600 ,y=600)
    # t4m.place_configure(x=600 ,y=600)
    # t5m.place_configure(x=600 ,y=600)
    # t6m.place_configure(x=600 ,y=600)
    if level>4:
        x=[]
        for i in range(jawaban[level]+tombolpasti[level],jawaban[level]+tombolpasti[level]+6):
            x+=[i]
        random.shuffle(x)
        y=[]
        for j in range(tombolpasti[level],tombolpasti[level]+6):
            y+=[j]
        random.shuffle(y)
        kiri=x
        kanan=y
        if level<30:
            t1=TkinterCustomButton(master=f2,text=kiri[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[0]),cursor="hand2")
            t1.place(x=50, y=240)
            t2=TkinterCustomButton(master=f2,text=kiri[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[1]),cursor="hand2")
            t2.place(x=125, y=240)
            t3=TkinterCustomButton(master=f2,text=kiri[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[2]),cursor="hand2")
            t3.place(x=50, y=340)
            t4=TkinterCustomButton(master=f2,text=kiri[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[3]),cursor="hand2")
            t4.place(x=125, y=340)
            t5=TkinterCustomButton(master=f2,text=kiri[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[4]),cursor="hand2")
            t5.place(x=50, y=440)
            t6=TkinterCustomButton(master=f2,text=kiri[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[5]),cursor="hand2")
            t6.place(x=125 ,y=440)

            t1l=TkinterCustomButton(master=f2,text=kanan[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[0]),cursor="hand2")
            t1l.place(x=300 ,y=240)
            t2l=TkinterCustomButton(master=f2,text=kanan[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[1]),cursor="hand2")
            t2l.place(x=375 ,y=240)
            t3l=TkinterCustomButton(master=f2,text=kanan[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[2]),cursor="hand2")
            t3l.place(x=300 ,y=340)
            t4l=TkinterCustomButton(master=f2,text=kanan[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[3]),cursor="hand2")
            t4l.place(x=375 ,y=340)
            t5l=TkinterCustomButton(master=f2,text=kanan[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[4]),cursor="hand2")
            t5l.place(x=300 ,y=440)
            t6l=TkinterCustomButton(master=f2,text=kanan[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[5]),cursor="hand2")
            t6l.place(x=375 ,y=440)
            operasi1.config(text="-")
            # operasi2.config(text="+")
    if level>9:
        x=[]
        for i in range(jawaban[level]-tombolpasti[level],jawaban[level]-tombolpasti[level]+6):
            x+=[i]
        random.shuffle(x)
        y=[]
        for j in range(tombolpasti[level],tombolpasti[level]+6):
            y+=[j]
        random.shuffle(y)
        kiri=x
        kanan=y
        if level<30:
            t1=TkinterCustomButton(master=f2,text=kiri[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[0]),cursor="hand2")
            t1.place(x=50, y=240)
            t2=TkinterCustomButton(master=f2,text=kiri[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[1]),cursor="hand2")
            t2.place(x=125, y=240)
            t3=TkinterCustomButton(master=f2,text=kiri[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[2]),cursor="hand2")
            t3.place(x=50, y=340)
            t4=TkinterCustomButton(master=f2,text=kiri[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[3]),cursor="hand2")
            t4.place(x=125, y=340)
            t5=TkinterCustomButton(master=f2,text=kiri[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[4]),cursor="hand2")
            t5.place(x=50, y=440)
            t6=TkinterCustomButton(master=f2,text=kiri[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[5]),cursor="hand2")
            t6.place(x=125 ,y=440)
    
            t1l=TkinterCustomButton(master=f2,text=kanan[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[0]),cursor="hand2")
            t1l.place(x=300 ,y=240)
            t2l=TkinterCustomButton(master=f2,text=kanan[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[1]),cursor="hand2")
            t2l.place(x=375 ,y=240)
            t3l=TkinterCustomButton(master=f2,text=kanan[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[2]),cursor="hand2")
            t3l.place(x=300 ,y=340)
            t4l=TkinterCustomButton(master=f2,text=kanan[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[3]),cursor="hand2")
            t4l.place(x=375 ,y=340)
            t5l=TkinterCustomButton(master=f2,text=kanan[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[4]),cursor="hand2")
            t5l.place(x=300 ,y=440)
            t6l=TkinterCustomButton(master=f2,text=kanan[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[5]),cursor="hand2")
            t6l.place(x=375 ,y=440)
            operasi1.config(text="-")
            # operasi2.config(text="+")
        operasi1.config(text="+")
        # operasi2.config(text="x")
    if level>14:
        x=[]
        for i in range(jawaban[level]+tombolpasti[level],jawaban[level]+tombolpasti[level]+6):
            x+=[i]
        random.shuffle(x)
        y=[]
        for j in range(tombolpasti[level],tombolpasti[level]+6):
            y+=[j]
        random.shuffle(y)
        kiri=x
        kanan=y
        if level<30:
            t1=TkinterCustomButton(master=f2,text=kiri[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[0]),cursor="hand2")
            t1.place(x=50, y=240)
            t2=TkinterCustomButton(master=f2,text=kiri[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[1]),cursor="hand2")
            t2.place(x=125, y=240)
            t3=TkinterCustomButton(master=f2,text=kiri[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[2]),cursor="hand2")
            t3.place(x=50, y=340)
            t4=TkinterCustomButton(master=f2,text=kiri[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[3]),cursor="hand2")
            t4.place(x=125, y=340)
            t5=TkinterCustomButton(master=f2,text=kiri[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[4]),cursor="hand2")
            t5.place(x=50, y=440)
            t6=TkinterCustomButton(master=f2,text=kiri[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[5]),cursor="hand2")
            t6.place(x=125 ,y=440)
    
            t1l=TkinterCustomButton(master=f2,text=kanan[0],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[0]),cursor="hand2")
            t1l.place(x=300 ,y=240)
            t2l=TkinterCustomButton(master=f2,text=kanan[1],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[1]),cursor="hand2")
            t2l.place(x=375 ,y=240)
            t3l=TkinterCustomButton(master=f2,text=kanan[2],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[2]),cursor="hand2")
            t3l.place(x=300 ,y=340)
            t4l=TkinterCustomButton(master=f2,text=kanan[3],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[3]),cursor="hand2")
            t4l.place(x=375 ,y=340)
            t5l=TkinterCustomButton(master=f2,text=kanan[4],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[4]),cursor="hand2")
            t5l.place(x=300 ,y=440)
            t6l=TkinterCustomButton(master=f2,text=kanan[5],bg='salmon',
            text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[5]),cursor="hand2")
            t6l.place(x=375 ,y=440)
            operasi1.config(text="-")
            # operasi2.config(text="+")
        operasi1.config(text="-")
        # operasi2.config(text="/")
    
    
status = "Music On"
def onoff():
    global status
    if status=="Music On":
        mixer.music.stop()
        status = "Music Off"
        pleymusic.set_text(text=status)
    elif status=="Music Off":
        mixer.music.play(-1) 
        status = "Music On"
        pleymusic.set_text(text=status)


root = Tk()
root.config(height=600, width=500, cursor="heart")
root.title("ABL (Asyik Banget Loh)")
root.resizable(False,False)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)


for frame in (f1, f2, f3, f4, f5):
    frame.config(bg="mistyrose", width=500,height=600)
    frame.place(x=0,y=0)

#MainMenu===================================================================
img3 = Image.open("ABL.png")
ipopw3 = img3.resize((500,600))
ipng3=ImageTk.PhotoImage(ipopw3)
Label(f1,image=ipng3,bg="mistyrose").place(x=0,y=0)
TkinterCustomButton(master=f1,text='Start', 
                    command=lambda:raise_frame(f2),
                    text_font=("Segoe Print",12), cursor="hand2").place(x=190,y=250)
TkinterCustomButton(master=f1,text='Setting', 
                    command=lambda:raise_frame(f4), 
                    text_font=("Segoe Print",12), cursor="hand2").place(x=190,y=325)
TkinterCustomButton(master=f1,text='About', 
                    command=lambda:raise_frame(f3), 
                    text_font=("Segoe Print",12), cursor="hand2").place(x=190,y=400)
TkinterCustomButton(master=f1,text='Quit', 
                    command=lambda:root.quit(), 
                    text_font=("Segoe Print",12), cursor="hand2").place(x=190,y=475)
#============================================================================

        
#MainGameplay===========================================================================================
if level < 20:
    ssss=Label(f2, text=jawaban[level], font=("Segoe Print",24),
               height=1, width=24,bg="#fdd3c5")
    ssss.place(x=0 ,y=60)
    displevel=Label(f2, text=f"level: {level+1}", font=("Segoe Print",14),bg="mistyrose")
    displevel.place(x= 410 , y=15)
    operasi1 = Label(f2, text="+", font=("Segoe Print",24), height=1,
          bg="mistyrose")
    operasi1.place(x=235 ,y=140)  
    operasi2=Label(f2, text="+", font=("Segoe Print",24), 
                   height=1,bg="mistyrose")
    operasi2.place(x=600,y=600)    
    l=Entry(f2, font=("Segoe Print", 20),width=5, justify=CENTER,
            relief=RAISED, bg="#2874A6",fg="white",insertbackground="#2874A6")
    l.bind("<Key>", lambda e:"break" )
    l.place(x=70, y=150)
    s=Entry(f2, font=("Segoe Print", 20),width=5, justify=CENTER,
            relief=RAISED, bg="#2874A6",fg="white",insertbackground="#2874A6")
    s.bind("<Key>", lambda e:"break" )
    s.place(x=323 ,y=150)
    r=Entry(f2, font=("Segoe Print", 20),width=5, justify=CENTER,
            relief=RAISED, bg="#2874A6",fg="white",insertbackground="#2874A6")
    r.bind("<Key>", lambda e:"break" )
    r.place(x=600 ,y=600)
    TkinterCustomButton(master=f2, text='Check', text_font=("Segoe Print", 12),cursor="hand2", 
                        command=cek,height=25,
                        width=100).place(x= 200, y=550)   
    TkinterCustomButton(master=f2, text='Back', text_font=("Segoe Print", 12),cursor="hand2", 
                        command=lambda:raise_frame(f1),
                        height=25,width=90).place(x= 25 , y=25)
    img = Image.open("qwe.png")
    ipopw = img.resize((20,20))
    ipng=ImageTk.PhotoImage(ipopw)
    img2 = Image.open("qwe2.png")
    ipopw2 = img2.resize((20,20))
    ipng2=ImageTk.PhotoImage(ipopw2)
    for i in range(life):
        nyaw=Label(f2,image=ipng,bg="mistyrose").place(x=20*i,y=570)
#==================================================================================================


#TombolJawaban=====================================================================================
ngacak()
# if level<30:
#     t1=TkinterCustomButton(master=f2,text=kiri[0],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[0]),cursor="hand2")
#     t1.place(x=50, y=240)
#     t2=TkinterCustomButton(master=f2,text=kiri[1],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[1]),cursor="hand2")
#     t2.place(x=125, y=240)
#     t3=TkinterCustomButton(master=f2,text=kiri[2],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[2]),cursor="hand2")
#     t3.place(x=50, y=340)
#     t4=TkinterCustomButton(master=f2,text=kiri[3],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[3]),cursor="hand2")
#     t4.place(x=125, y=340)
#     t5=TkinterCustomButton(master=f2,text=kiri[4],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[4]),cursor="hand2")
#     t5.place(x=50, y=440)
#     t6=TkinterCustomButton(master=f2,text=kiri[5],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(kiri[5]),cursor="hand2")
#     t6.place(x=125 ,y=440)

#     t1l=TkinterCustomButton(master=f2,text=kanan[0],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[0]),cursor="hand2")
#     t1l.place(x=300 ,y=240)
#     t2l=TkinterCustomButton(master=f2,text=kanan[1],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[1]),cursor="hand2")
#     t2l.place(x=375 ,y=240)
#     t3l=TkinterCustomButton(master=f2,text=kanan[2],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[2]),cursor="hand2")
#     t3l.place(x=300 ,y=340)
#     t4l=TkinterCustomButton(master=f2,text=kanan[3],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[3]),cursor="hand2")
#     t4l.place(x=375 ,y=340)
#     t5l=TkinterCustomButton(master=f2,text=kanan[4],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[4]),cursor="hand2")
#     t5l.place(x=300 ,y=440)
#     t6l=TkinterCustomButton(master=f2,text=kanan[5],bg='salmon',
#     text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(kanan[5]),cursor="hand2")
#     t6l.place(x=375 ,y=440)

    # t1m=TkinterCustomButton(master=f2,text=tombol[level][6],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][12]),cursor="hand2")
    # t2m=TkinterCustomButton(master=f2,text=tombol[level][7],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][13]),cursor="hand2")
    # t3m=TkinterCustomButton(master=f2,text=tombol[level][8],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][14]),cursor="hand2")
    # t4m=TkinterCustomButton(master=f2,text=tombol[level][9],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][15]),cursor="hand2")
    # t5m=TkinterCustomButton(master=f2,text=tombol[level][10],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][16]),cursor="hand2")
    # t6m=TkinterCustomButton(master=f2,text=tombol[level][11],bg='salmon',
    # text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][17]),cursor="hand2")
#===============================================================================================


#About================================================================================================
TkinterCustomButton(master=f3, text='Back', text_font=("Segoe Print", 12), cursor="hand2", 
                    command=lambda:raise_frame(f1),height=25,width=90).place(x= 25 , y=25)

tentang = scrolledtext.ScrolledText(f3,width = 43, height = 20, 
                                      font = ("Times New Roman",15)) 
tentang.place(x=25,y=120)
tentang.insert(INSERT,
"""\
Program ini kami dedikasikan untuk project akhir kamidalam mata kuliah bahasa pemrograman. 
Program kami merupakan sebuah game. Game ini kamiberi nama ABL atau singkatan dari Asyik Banget Loh. Kami memberi nama game kami ABL karena game 
kami adalah game yang asikk.

Cara Main:
ABL dapat dimainkan dengan cara memilih kombinasi angka yang sesuai dengan operasi dan nilai akhir yang tertera di layar. Angka-angka tersebut dapat dipilih 
dari tombol-tombol yang terdapat di bawah kotak 
jawaban. Setelah memilih kombinasi angka yang 
dirasa benar, klik tombol "check", jika jawaban benar akan dilanjutkan ke level selanjutnya, sedangkan jika 
jawaban salah anda dapat mencobanya lagi 
(jika health anda masih tersisa).
Terdapat 5 health yang ada di permainan ini, yang 
mana health akan berkurang jika anda melakukan 
pengecekan pada kombinasi angka yang tidak tepat. 
Jika health telah habis maka game akan terulang dari 
level 1.




""")

tentang.configure(state ='disabled')
#=========================================================================================================


#Setting================================================================
Label(f4, text='Setting',bg="mistyrose",
      width=11,height=2,
      font=("Cambria",22,"bold")).place(x=155,y=50)         
pleymusic=TkinterCustomButton(master=f4,text=status,cursor="hand2",command=onoff,
                              width=400)
pleymusic.place(x=50, y=130)
TkinterCustomButton(master=f4, text='Back', text_font=("Segoe Print", 12), 
                    command=lambda:raise_frame(f1),
                    height=25,width=90).place(x= 25 , y=25)
#===========================================================================

#Music======================================================================
mixer.init()
mixer.music.load("Fluffing-a-Duck.mp3")
mixer.music.play(-1)
#===========================================================================
img = Image.open("WIN.png")
win = img.resize((500,600))
iwin= ImageTk.PhotoImage(win)
Label(f5, image=iwin).place(x=0,y=0)
raise_frame(f1)
root.mainloop()