from tkinter import *
window=Tk()

window.config(background="black")
window.title("Calculator")

class func():

    def __init__(self):
        #Entry
        self.entry=Entry(window,font=("Comic Sans MS",15),bg="Black",fg="Grey",relief=RAISED,border=6,insertbackground="white")
        self.entry.grid(row=0,column=0,columnspan=3,sticky="nsew")
        self.entry.icursor(len(self.entry.get()))

        for i in range(6):
            window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            window.grid_columnconfigure(i, weight=1)

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
        self.entry.delete(0,END)
        with open("Calculator.txt","r") as f:
            self.entry.insert(END,f.read())

    def equal(self,_=None):
        try:
            a=self.entry.get()
            if "x" in a:
                a=a.replace("x","*")
            if "%" not in a:
                with open("Calculator.txt","a") as f:
                    f.write(f"{self.entry.get()}={eval(a)}|")
                self.entry.delete(0,END)
                self.entry.insert(END,eval(a))
            else:
                c="%"
                b=a.find(c)
                if (a[b+1:])=="":
                    with open("Calculator.txt","a") as f:
                        f.write(f"{self.entry.get()}={round((float(a[:b])/100*1),2)}|")
                        self.entry.delete(0,END)
                        self.entry.insert(END,round((float(a[:b])/100*1),2))
                else:
                    with open("Calculator.txt","a") as f:
                        f.write(f"{self.entry.get()}={round((float(a[:b])*(float(a[b+1:])))/100,2)}|")
                        self.entry.delete(0,END)
                        self.entry.insert(END,round((float(a[:b])*(float(a[b+1:])))/100,2))
        except ValueError:
            self.entry.delete(0,END)
            self.entry.insert(END,"Invalid Input")
            with open("Calculator.txt","a") as f:
                f.write(f"{self.entry.get()}=Invalid Input")
        except SyntaxError:
                self.entry.delete(0,END)
                self.entry.insert(END,"Invalid Input")
                with open("Calculator.txt","a") as f:
                    f.write(f"{self.entry.get()}=Invalid Input")

    def dele(self,_=None):
        self.entry.delete(len(self.entry.get())-1,END)

    def ac(self,_=None):
        self.entry.delete(0,END)
        with open("Calculator.txt","w") as f:
            f.write("")

    def create_button(self,text,command,row,col):
        button=Button(text=text,font=("Comic Sans MS",15,"bold"),bg="blue",fg="white",
                    activebackground="grey",padx=3,pady=3,relief=RAISED,border=6,width=2,height=1,command=lambda t=text: command(t))
        button.grid(row=row,column=col,sticky="nsew")
            
    def insert_text(self,t):
        self.entry.insert(END,t)

buto=func()
buto.buttons()
window.mainloop()
