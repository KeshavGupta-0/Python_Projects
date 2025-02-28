from tkinter import *
import Calculator_Code as cc
window=Tk()

window.config(background="black")
window.title("Calculator")

class func():

    def __init__(self):
        #Entry
        self.entry=Entry(window,font=("Comic Sans MS",30),bg="Black",fg="Grey",relief=RAISED,border=10,insertbackground="white")
        self.entry.grid(row=0,column=0,columnspan=3,sticky="nsew")
        self.entry.icursor(len(self.entry.get()))

    def buttons(self):
        buttons = [
            ('1', self.insert_text, 4, 0), ('2', self.insert_text, 4, 1), ('3', self.insert_text, 4, 2),
            ('4', self.insert_text, 3, 0), ('5', self.insert_text, 3, 1), ('6', self.insert_text, 3, 2),
            ('7', self.insert_text, 2, 0), ('8', self.insert_text, 2, 1), ('9', self.insert_text, 2, 2),
            ('0', self.insert_text, 5, 1), ('00', self.insert_text, 5, 0), ('.', self.insert_text, 5, 2),
            ('AC',self.ac, 1, 0), ('=', self.equal, 5, 3), ('+', self.insert_text, 4, 3),
            ('-', self.insert_text, 3, 3), ('x', self.insert_text, 2, 3), ('/', self.insert_text, 1, 3),
            ('%', self.insert_text, 1, 1), ('DEL', self.dele, 1, 2), ('HIS', self.history, 0, 3)
            ]
        for text,command,row,col in buttons:
                self.create_button(text,command,row,col)

    def history(self,_=None):
        f=open("Calculator.txt","r")
        self.entry.delete(0,END)
        self.entry.insert(END,f.read())

    def equal(self,_=None):
        a=self.entry.get()
        f=open("Calculator.txt","a")
        f.write(f"{self.entry.get()}={cc.calc.cal(a)}|")
        f.close()
        self.entry.delete(0,END)
        self.entry.insert(END,cc.calc.cal(a))
            
    def dele(self,_=None):
        self.entry.delete(len(self.entry.get())-1,END)

    def ac(self,_=None):
        self.entry.delete(0,END)
        f=open("Calculator.txt","w")
        f.write("")
        f.close()

    def create_button(self,text,command,row,col):
        button=Button(text=text,font=("Comic Sans MS",20,"bold"),bg="blue",fg="white",
                    activebackground="grey",padx=10,pady=10,relief=RAISED,border=10,width=5,height=1,command=lambda t=text: command(t))
        button.grid(row=row,column=col,sticky="nsew")
            
    def insert_text(self,t):
        self.entry.insert(END,t)

buto=func()
buto.buttons()
window.mainloop()
