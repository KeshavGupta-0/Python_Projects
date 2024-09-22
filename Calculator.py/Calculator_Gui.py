from tkinter import *
import Calculator_Code as cc
window=Tk()


window.config(background="black")
window.title("Calculator")

class func():
    def equal():
        global a
        a=entry.get()
        f=open("Calculator.txt","a")
        f.write(f"{entry.get()}={cc.calc.cal(a)}|")
        f.close()
        entry.delete(0,END)
        entry.insert(END,cc.calc.cal(a))
        
    def dele():
        entry.delete(len(entry.get())-1,END)

    def ac():
        entry.delete(0,END)
        f=open("Calculator.txt","w")
        f.write("")
        f.close()

    def buto1():
        entry.insert(END,"1")

    def buto2():
        entry.insert(END,"2")

    def buto3():
        entry.insert(END,"1")

    def buto4():
        entry.insert(END,"4")

    def buto5():
        entry.insert(END,"5")

    def buto6():
        entry.insert(END,"6")

    def buto7():
        entry.insert(END,"7")

    def buto8():
        entry.insert(END,"8")

    def buto9():
        entry.insert(END,"9")

    def buto0():
        entry.insert(END,"0")

    def buto00():
        entry.insert(END,"00")

    def butodot():
        entry.insert(END,".")

    def butoplus():
        entry.insert(END,"+")

    def butominus():
        entry.insert(END,"-")
    
    def butodiv():
        entry.insert(END,"/")
    
    def butomul():
        entry.insert(END,"x")
    
    def butopercent():
        entry.insert(END,"%")

    def history():
        f=open("Calculator.txt","r")
        entry.delete(0,END)
        entry.insert(END,f.read())


#Entry
entry=Entry(window,font=("Comic Sans MS",30),bg="Black",fg="Grey",relief=RAISED,border=10,insertbackground="white")
entry.grid(row=0,column=0,columnspan=3,sticky="nsew")
entry.icursor(len(entry.get()))


#Buttons

but1=Button(text=1,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto1)
but1.grid(row=4,column=0,sticky="nsew")

but2=Button(text=2,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto2)
but2.grid(row=4,column=1,sticky="nsew")

but3=Button(text=3,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto3)
but3.grid(row=4,column=2,sticky="nsew")

but4=Button(text=4,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto4)
but4.grid(row=3,column=0,sticky="nsew")

but5=Button(text=5,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto5)
but5.grid(row=3,column=1,sticky="nsew")

but6=Button(text=6,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto6)
but6.grid(row=3,column=2,sticky="nsew")

but7=Button(text=7,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto7)
but7.grid(row=2,column=0,sticky="nsew")

but8=Button(text=8,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto8)
but8.grid(row=2,column=1,sticky="nsew")

but9=Button(text=9,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto9)
but9.grid(row=2,column=2,sticky="nsew")

but0=Button(text="0",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto0)
but0.grid(row=5,column=1,sticky="nsew")

but00=Button(text="00",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.buto00)
but00.grid(row=5,column=0,sticky="nsew")

butdot=Button(text=".",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butodot)
butdot.grid(row=5,column=2,sticky="nsew")

butac=Button(text="AC",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.ac)
butac.grid(row=1,column=0,sticky="nsew")

buteq=Button(text="=",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.equal)
buteq.grid(row=5,column=3,sticky="nsew")

butplus=Button(text="+",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butoplus)
butplus.grid(row=4,column=3,sticky="nsew")

butmin=Button(text="-",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butominus)
butmin.grid(row=3,column=3,sticky="nsew")

butmul=Button(text="X",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butomul)
butmul.grid(row=2,column=3,sticky="nsew")

butdiv=Button(text="/",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butodiv)
butdiv.grid(row=1,column=3,sticky="nsew")

butpercent=Button(text="%",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.butopercent)
butpercent.grid(row=1,column=1,sticky="nsew")

butdele=Button(text="DEL",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.dele)
butdele.grid(row=1,column=2,sticky="nsew")

buthis=Button(text="HIS",font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=func.history)
buthis.grid(row=0,column=3,sticky="nsew")

window.mainloop()