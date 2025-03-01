import random
def Num_Rock(b):
    if b==1:
        Comp="Rock"
    elif b==2:
        Comp="Paper"
    elif b==3:
        Comp="Scissor"
    return Comp
def Record(n):
    with open(f"{name}","a") as f:
                f=f.write(str(n))
def Game():
    #Computer Turn
    a=random.randint(1,3)
    Comp=Num_Rock(a)
    b=int(input("Enter your input by pressing the number:\n=>Rocks(1)\n=>Paper(2)\n=>Scissor(3)\n"))
    You=Num_Rock(b)
    print(f"I chose {Comp}")
    print(f"You chose {You}")
    #Game Rules
    if Comp==You:
        print("Draw for now.")
        Record("D")
    elif Comp=="Rock":
        if You=="Paper":
            print("Ah Shit! You win")
            Record("W")
        elif You=="Scissor":
            print("HeHe! I win")
            Record("L")
    elif Comp=="Paper":
        if You=="Rock":
            print("HeHe! I win")
            Record("L")
        elif You=="Scissor":
            print("Ah Shit! You win")
            Record("W")
    elif Comp=="Scissor":
        if You=="Rock":
            print("Ah Shit! You win")
            Record("W")
        elif You=="Paper":
            print("HeHe! I win")
            Record("L")
name=input("Tell me your name:\n")
print(f"Welcome,{name}\nI will surely defeat you")
a=0
while a>=0:
    Game()
    c=int(input("Do you want to play again?Reply by Pressing the number:\n=>Yes(1)\n=>No(2)\n"))
    if c==1:
        continue
    elif c==2:
        break
print("Thank You for playing!")
with open(f"{name}","r") as f:
    f=f.read()
print(f"Your score is {f.count("W")-f.count("L")}")
print(f"Wins=>{f.count("W")}\nLoss=>{f.count("L")}\nDraw=>{f.count("D")}")
input("Press Enter to exit screen.")
