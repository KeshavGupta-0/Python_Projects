class calc():
    def cal(a):
        global op
        if "+" in a:
            c="+"
            b=a.find(c)
            op=float(a[:b])+float(a[b+1:])
        elif "-" in a:
            c="-"
            b=a.find(c)
            op=float(a[:b])-float(a[b+1:])
        elif "/" in a:
            c="/"
            b=a.find(c)
            op=float(a[:b])/float(a[b+1:])
        elif "x" in a:
            c="x"
            b=a.find("x")
            op=float(a[:b])*float(a[b+1:])
        elif "%" in a:
            c="%"
            b=a.find(c)
            if (a[b+1:])=="":
                op=float(a[:b])/100*1
            else:
                op=float(a[:b])*(float(a[b+1:]))/100
        return (round(op,2))#to return solution as float upto two decimal places