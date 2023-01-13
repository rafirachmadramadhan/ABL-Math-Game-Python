from tkinter import *
from tkinter_custom_button import *
from tkinter import messagebox
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import scrolledtext

def raise_frame(frame):
    frame.tkraise()

level=0
life=5
tombol = [
            [1, 3, 6, 7, 9, 10, 13, 15, 18, 19, 20, 22], #+
            [5, 9, 11, 14, 17, 18, 23, 25, 26, 36, 39, 41],
            [2, 6, 11, 19, 27, 38, 43, 51, 59, 61, 65, 68],
            [4, 13, 19, 24, 27, 36, 41, 58, 64, 73, 78, 81],
            [3, 17, 24, 33, 41, 45, 54, 69, 82, 89, 91, 97],
            [50, 86, 25, 39, 12, 72, 8, 27, 79, 3, 57, 34, 92, 56, 89, 8, 60, 71], #+, +
            [18, 64, 92, 114, 56, 37, 112, 4, 31, 11, 58, 63, 73, 113, 5, 35, 83, 47], 
            [89, 17, 150, 42, 13, 89, 112, 45, 134, 68, 12, 23, 124, 51, 9, 7, 82, 78],
            [78, 127, 46, 116, 5, 54, 102, 61, 98, 16, 3, 1, 50, 114, 80, 77, 91, 11],
            [105, 99, 80, 10, 82, 13, 112, 4, 111, 1, 39, 5, 105, 41, 47, 121, 86, 146],
            [28, 30, 32, 34, 36, 43, 4, 6, 8, 7, 9, 11, 55, 61, 54, 73, 67, 79], #x+
            [13, 7, 12, 8, 11, 6, 21, 30, 22, 33, 29, 27, 15, 5, 9, 3, 13, 2],
            [86, 72, 93, 83, 75, 97, 12, 11, 2, 5, 13, 3, 41, 44, 38, 36, 46, 28],
            [8, 12, 16, 4, 18, 11, 25, 10, 17, 16, 7, 23, 79, 55, 86, 56, 70, 74],
            [33, 27, 21, 28, 42, 34, 8, 11, 19, 6, 4, 7, 20, 24, 16, 27, 21, 19],
            [91, 75, 44, 53, 65, 43, 24, 33, 57, 59, 15, 11, 17,  14, 61, 71, 39, 16],#+x
            [41, 34, 111, 73, 19, 27, 17, 61, 35, 16, 39, 41, 71, 13, 12, 66, 31, 14],
            [103, 49, 56, 37, 84, 71, 89, 18, 6, 91, 23, 33, 17, 5 , 31, 25, 29, 54],
            [24, 88, 34, 105, 133, 20, 40, 26, 37, 28, 12, 32,27 , 16, 6, 17, 13, 25],
            [81, 129, 56, 87, 39, 65, 48, 114, 82, 59, 30, 53, 33, 12, 19, 17, 14, 6], 
            [751, 231, 685, 32, 368, 88, 1044, 1391, 1233, 1362, 1792, 1695, 21, 22, 7, 13, 19, 23], #+/
            [492, 71, 208, 480, 553, 908, 1575, 1303, 1831, 2091, 1650, 1771, 10, 11, 25, 8, 18, 16],
            [143, 247, 289, 372, 209, 211, 2238, 1055, 1753, 2353, 2172, 1209, 6, 19, 14, 12, 18, 7],
            [565, 826, 677, 543, 915, 704, 2349, 1639,1685 , 1850, 1920, 2382, 3, 15, 12, 7, 11, 9],
            [398, 162, 122, 650, 876, 776, 1717, 2368, 1976,1985, 1216, 2092, 10, 13, 2, 12, 16, 22],
            [1219, 2145, 2886, 1689, 2614, 1255, 41, 61, 53, 37, 25, 31, 22, 59, 12, 83, 54, 51, 40], #/x
            [1122, 2496, 1616, 1132, 2967, 2681, 77, 78, 91, 38, 52, 102, 64, 22, 47, 38, 61, 34],
            [1442, 2675, 2212, 1638, 2659, 2258, 103, 76, 109, 88, 105, 91, 74, 23, 31, 52, 29, 67],
            [2687, 1731, 1619, 2519, 2023, 1634, 123, 119, 144, 139, 132, 121, 57, 41, 85, 32, 81, 59],
            [2878, 2669, 2572, 1166, 2498, 1505, 32, 59, 62, 53, 54, 26, 30, 83, 93, 16, 37, 57]
]


jawaban = [
    24, #9, 15, +
    43, #18, 25
    71, #6, 65
    83, #19, 64
    99, #45 54
    109, #12, 8, 89, ++
    123, #18, 58, 47
    163, #42, 112, 9
    178, #127, 1, 50
    185, #99, 39, 47
    211, #36, 4, 67,x+
    225, #8, 27, 9
    238, #97, 2, 44 
    271, #12, 16, 79
    293, #34, 8, 21
    581, #53, 33, 16,+x
    567, #34, 41, 13
    646, #71, 23, 25
    780, #24, 28, 27
    855, #39, 48, 17
    338, #231, 1391, 13,+/
    232, #71, 1771, 11
    505, #143, 2172, 6
    965, #704, 2349, 9
    952, #876, 1216, 16
    3978, #2886, 37, 51, /x
    2048, #2496, 78, 64
    1206, #1638, 91,67
    544, #2023, 119, 32
    1254, #1166, 53, 57
]

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
            z = int(l.get()) + int(s.get()) + int(r.get())
        except:
            return          
    elif level>9 and level<15:    
        try:    
            z = int(l.get()) * int(s.get()) + int(r.get())
        except:
            return      
    elif level>14 and level<20:     
        try:    
            z = int(l.get()) + int(s.get()) * int(r.get())
        except:
            return     
    elif level>19 and level<25:     
        try:    
            z = int(l.get()) + int(s.get()) / int(r.get())
        except:
            return     
    elif level>24 and level<30:     
        try:    
            z = int(l.get()) / int(s.get()) * int(r.get())
        except:
            return     
        
    
    if z == jawaban[level]:
        level+=1
        if level>0 and level<5:
            messagebox.showinfo("Wuih... Betul", "Okelah! kamu cukup pintar")
        elif level>4 and level<10:
            messagebox.showinfo("Wuih... Betul", "Kelihatannya kamu pintar")
        elif level>9 and level<15:
            messagebox.showinfo("Wuih... Betul", "Boleh boleh, kamu beneran pintar")
        elif level>14 and level<20:
            messagebox.showinfo("Wuih... Betul", "Eeehhh! pintar banget si")
        elif level>19 and level<26:
            messagebox.showinfo("Wuih... Betul", "Titisannya einstein ya? Jenius!")
        elif level>25 and level<29:
            messagebox.showinfo("Wuih... Betul", "Inimah diatas Jenius!!")
        elif level==29:
            messagebox.showinfo("Wuih... Betul", "Fix otak einstein")
        elif level==30:
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
    t1.set_text(text=tombol[level][0])
    t2.set_text(text=tombol[level][1])
    t3.set_text(text=tombol[level][2])
    t4.set_text(text=tombol[level][3])
    t5.set_text(text=tombol[level][4])
    t6.set_text(text=tombol[level][5])
    t1l.set_text(text=tombol[level][6])
    t2l.set_text(text=tombol[level][7])
    t3l.set_text(text=tombol[level][8])
    t4l.set_text(text=tombol[level][9])
    t5l.set_text(text=tombol[level][10])
    t6l.set_text(text=tombol[level][11])
    operasi2.place_configure(x=600,y=600)
    operasi1.place_configure(x=235 ,y=140)
    operasi1.config(text="+")
    l.place_configure(x=70, y=150)
    s.place_configure(x=315 ,y=150)
    r.place_configure(x=600 ,y=600)
    l.delete(0,END)
    s.delete(0,END)
    r.delete(0,END)
    t1.place_configure(x=50, y=240)
    t2.place_configure(x=125, y=240)
    t3.place_configure(x=50, y=340)
    t4.place_configure(x=125, y=340)
    t5.place_configure(x=50, y=440)
    t6.place_configure(x=125 ,y=440)
    t1l.place_configure(x=300 ,y=240)
    t2l.place_configure(x=375 ,y=240)
    t3l.place_configure(x=300 ,y=340)
    t4l.place_configure(x=375 ,y=340)
    t5l.place_configure(x=300 ,y=440)
    t6l.place_configure(x=375 ,y=440)
    t1m.place_configure(x=600 ,y=600)
    t2m.place_configure(x=600 ,y=600)
    t3m.place_configure(x=600 ,y=600)
    t4m.place_configure(x=600 ,y=600)
    t5m.place_configure(x=600 ,y=600)
    t6m.place_configure(x=600 ,y=600)
    if level > 4:
        #operasinya=====================================================
        operasi1.place_configure(x=155 ,y=140)
        operasi2.place_configure(x=325 ,y=140)
        #entry nya======================================================================================
        l.place_configure(x=27, y=150)
        s.place_configure(x=200, y=150)
        r.place_configure(x=370 ,y=150)
        #tombolnya=======================================================================================
        t1m.place_configure(x=346 ,y=240)
        t2m.place_configure(x=423 ,y=240)
        t3m.place_configure(x=346 ,y=340)
        t4m.place_configure(x=423, y=340)
        t5m.place_configure(x=346 ,y=440)
        t6m.place_configure(x=423 ,y=440)
        t1.place_configure(x=10 ,y=240)
        t2.place_configure(x=87, y=240)
        t3.place_configure(x=10 ,y=340)
        t4.place_configure(x=87 ,y=340)
        t5.place_configure(x=10,y=440)
        t6.place_configure(x=87 ,y=440)
        t1l.place_configure(x=178 ,y=240)
        t2l.place_configure(x=255 ,y=240)
        t3l.place_configure(x=178 ,y=340)
        t4l.place_configure(x=255 ,y=340)
        t5l.place_configure(x=178 ,y=440)
        t6l.place_configure(x=255 ,y=440)
        t1m.set_text(tombol[level][12])
        t2m.set_text(tombol[level][13])
        t3m.set_text(tombol[level][14])
        t4m.set_text(tombol[level][15])
        t5m.set_text(tombol[level][16])
        t6m.set_text(tombol[level][17])
    if level>9:
        operasi1.config(text="x")
        operasi2.config(text="+")
    if level>14:
        operasi1.config(text="+")
        operasi2.config(text="x")
    if level>19:
        operasi1.config(text="+")
        operasi2.config(text="/")
    if level>24:
        operasi1.config(text="/")
        operasi2.config(text="x")
    
    
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
if level < 30:
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
if level<30:
    t1=TkinterCustomButton(master=f2,text=tombol[level][0],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][0]),cursor="hand2")
    t1.place(x=50, y=240)
    t2=TkinterCustomButton(master=f2,text=tombol[level][1],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][1]),cursor="hand2")
    t2.place(x=125, y=240)
    t3=TkinterCustomButton(master=f2,text=tombol[level][2],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][2]),cursor="hand2")
    t3.place(x=50, y=340)
    t4=TkinterCustomButton(master=f2,text=tombol[level][3],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][3]),cursor="hand2")
    t4.place(x=125, y=340)
    t5=TkinterCustomButton(master=f2,text=tombol[level][4],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][4]),cursor="hand2")
    t5.place(x=50, y=440)
    t6=TkinterCustomButton(master=f2,text=tombol[level][5],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak(tombol[level][5]),cursor="hand2")
    t6.place(x=125 ,y=440)

    t1l=TkinterCustomButton(master=f2,text=tombol[level][6],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][6]),cursor="hand2")
    t1l.place(x=300 ,y=240)
    t2l=TkinterCustomButton(master=f2,text=tombol[level][7],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][7]),cursor="hand2")
    t2l.place(x=375 ,y=240)
    t3l=TkinterCustomButton(master=f2,text=tombol[level][8],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][8]),cursor="hand2")
    t3l.place(x=300 ,y=340)
    t4l=TkinterCustomButton(master=f2,text=tombol[level][9],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][9]),cursor="hand2")
    t4l.place(x=375 ,y=340)
    t5l=TkinterCustomButton(master=f2,text=tombol[level][10],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][10]),cursor="hand2")
    t5l.place(x=300 ,y=440)
    t6l=TkinterCustomButton(master=f2,text=tombol[level][11],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak2(tombol[level][11]),cursor="hand2")
    t6l.place(x=375 ,y=440)

    t1m=TkinterCustomButton(master=f2,text=tombol[level][6],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][12]),cursor="hand2")
    t2m=TkinterCustomButton(master=f2,text=tombol[level][7],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][13]),cursor="hand2")
    t3m=TkinterCustomButton(master=f2,text=tombol[level][8],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][14]),cursor="hand2")
    t4m=TkinterCustomButton(master=f2,text=tombol[level][9],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][15]),cursor="hand2")
    t5m=TkinterCustomButton(master=f2,text=tombol[level][10],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][16]),cursor="hand2")
    t6m=TkinterCustomButton(master=f2,text=tombol[level][11],bg='salmon',
    text_font=('Segoe Print',16),width=67,height=75,command=lambda:cetak3(tombol[level][17]),cursor="hand2")
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