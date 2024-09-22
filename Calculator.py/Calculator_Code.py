class calc():
    def cal(a):
        global op
        if "+" in a:
            c="+"
            b=a.find(c)
            if a[b+1:]=="":
                op=a
            else:
                op=round((float(a[:b])+float(a[b+1:])),2)
        elif "-" in a and a.find("-")!=0:
            c="-"
            b=a.find(c)
            if a[b+1:]=="":
                op=a
            else:
                op=round((float(a[:b])-float(a[b+1:])),2)
        elif "/" in a:
            c="/"
            b=a.find(c)
            if a[b+1:]=="":
                op=a
            else:
                op=round((float(a[:b])/float(a[b+1:])),2)
        elif "x" in a:
            c="x"
            b=a.find("x")
            if a[b+1:]=="":
                op=a
            else:
                op=round((float(a[:b])*(float(a[b+1:]))),2)
        elif "%" in a:
            c="%"
            b=a.find(c)
            if (a[b+1:])=="":
                op=round((float(a[:b])/100*1),2)
            else:
                op=round((float(a[:b])*(float(a[b+1:])))/100,2)
        else:
            op=a
        return op#to return solution as float upto two decimal places