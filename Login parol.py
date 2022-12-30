from tkinter import *
 
def login():
    foydalanuvchinomi=inp1.get()
    parol=inp2.get()
    if (foydalanuvchinomi=="" and parol==""):
        messagebox.showerror("","Login va parolni kiriting")
    elif (foydalanuvchinomi=="Texnokun.uz" and parol=="sirli masalliqning siri "):
        messagebox.showinfo("","Sirli masalliqning siri unda hech qanday sirning yo‘qligida.")
    else:
        messagebox.showerror("",'Siz usta "Ping" ning sirini bilolmaysiz')

root=Tk()
root.title('Login')
root.geometry('300x200')

global inp1
global inp2

Label(root,text="foydalanuvchi nomi").place(x=20,y=20)
Label(root,text="Parol").place(x=20,y=70)
 
inp1=Entry(root,bd=6)
inp1.place(x=140,y=20)

inp2=Entry(root,bd=6)
inp2.place(x=140,y=70)
Button(root,text="Sir",command=login,height=3,width=13,bd=5).place(x=100,y=120)
root.mainloop()
