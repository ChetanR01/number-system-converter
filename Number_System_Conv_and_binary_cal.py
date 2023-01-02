"""
A Number System Conversion and calculation
Devloped by
Chetan Rathod
Email- chetan7744rathod@gmail.com
Thank You For Exploring My Project
"""


from tkinter import* 
import tkinter.messagebox as msgbox
import webbrowser

def refresh():
    text_op.delete(0.0,END)



def display_msg():
    msgbox.showinfo(title='Thank You', message='Thank You for testing My Project.\nPlease provide your valuable feedback.\n(option available in Menu bar) \n\n  Have A Nice Day !\n\n\t\t -- Chetan Rathod')
    gui.destroy()

def bin_dec_main():
    li=[]
    a = equation.get()
    # To check input is binary no. or not
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        checkpt="T"
    else :
        checkpt="F"
        
    if checkpt== "T":
        sr="\n Steps to calculate decimal of binary number : "
        sr1_li = []
        po =len(a)-1
        for i in a:
            b=int(i)
            di = b*(2**po)
            sr1= "("+str(b)+"x"+str(2)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\nThe Decimal of given Binary Number is :"+str(add)
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def oct_dec_main():
    checkpt=""
    test=""
    li=[]
    a = equation.get()
    try:
        a= int(a)
        checkpt="T"
    except ValueError:
        msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input !")

    # to check input is octal or not 
    if checkpt=="T":
        a= str(a)
        for i in a:
            i=int(i)
            if 0<=i<=7:
                val="T"
                test+=str(val)
            else:
                val="F"
                test+=str(val)
        compval= len(a)*"T"

    if compval==test:
        sr="\n Steps to Convert given Ocatl to Decimal number : "
        sr1_li = []
        po =len(a)-1
    
        for i in a:
            b=int(i)
            di = b*(8**po)
            sr1= "("+str(b)+"x"+str(8)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\nThe Decimal of given Octal Number is :"+str(add)
        
       
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input ")

def hex_dec_main():
    li=[]
    sr1_li= []
    a = equation.get()
    
    # to check empty condition
    # if a=="":
    #     msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input ")


    test=""
    comprli=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    for cr in a:
        if (any(cr in i for i in comprli)):
            val="T"
            test+=str(val)
        else:
            val="F"
            test+=str(val)
    compval= len(a)*"T"
    
    if compval==test and a!="":
        # This step works properly
        sr= "\n Steps to Convert Hexadeciaml to Decimal Number: "   
        po =len(a)-1
        for i in a:
            if i=="A":
                i=10
            elif i=="B":
                i=11
            elif i=="C":
                i=12
            elif i=="D":
                i=13
            elif i=="E":
                i=14
            elif i=="F":
                i=15
        
            b=int(i)
            di = b*(16**po)
            sr1= "("+str(b)+"x"+str(16)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)


        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
        sr2= "\n"+"Adding all these elements"+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\nThe Decimal of given Hexadecimal Number is :"+str(add)
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def dec_bin():
    a = equation.get()
    checkpt= ""
    try:
        a =int(a)
        checkpt= "T"
    except ValueError:
        print("It's not int")
    
    if checkpt == "T":
        a=int(a)
        sr1= "\n Steps to calculate binary of decimal number"
        sr2="\n \t Quotient         \t\t\t\t Remainder"
        if a==0:
            sr="\n \tBinary of 00 is "+str(0000)
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//2 != 0:
                b = a%2 
                a = a//2
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t1"
            li.append(1)
        li.reverse()
        sr3="\n Binary of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        

        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input ") 

def dec_oct():
    a = equation.get()
    checkpt= ""
    try:
        a =int(a)
        checkpt= "T"
    except ValueError:
        print("It's not int")
    
    if checkpt == "T":
        a=int(a)
        sr1= "\n Steps to calculate Octal of decimal number"
        sr2="\n \t Quotient    \t\t\t\t    Remainder"
        if a==0:
            sr="\n \t Octal of 00 is "+str(0000)
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//8 != 0:
                b = a%8 
                a = a//8
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t"+str(a)
            li.append(a)
        li.reverse()
        sr3="\n Octal of Entered Decimal Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)


    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input ")

def dec_hex():
    a = equation.get()
    checkpt= ""
    try:
        a =int(a)
        checkpt= "T"
    except ValueError:
        print("It's not int")
    
    if checkpt == "T":
        a=int(a)
        sr1= "\n Steps to calculate Hexadeci of decimal number"
        sr2="\n \t Quotient \t \t\t\t \t Remainder"
        if a ==0 or 16>a>9:
            if a==0:
                sr="\n \t Hexadecimal of 00 is "+str(0000)
                text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
                text_op.grid(row=1,column=0,padx=70,pady=5)
                text_op.insert(END,sr)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)
            else:
                sr="\n \t Hexadecimal of "+str(a) +" is : "
                if a==10:
                    a= "A"
                elif a==11:
                    a ="B"
                elif a == 12:
                    a = "C"
                elif a ==13:
                    a ="D"
                elif a ==14:
                    a = "E"
                elif a==15:
                    a = "F"
                text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
                text_op.grid(row=1,column=0,padx=70,pady=5)
                text_op.insert(END,sr+a)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)

        else:  
            li= []
            sr4_li= []
            while a//16 != 0:
                b = a%16 
                a = a//16
                if b==10:
                    b= "A"
                elif b==11:
                    b="B"
                elif b== 12:
                    b= "C"
                elif b==13:
                    b="D"
                elif b==14:
                    b= "E"
                elif b==15:
                    b= "F"
                sr4= "\t"+str(a)+"\t\t\t\t \t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t \t\t\t \t"+str(a)
            li.append(a)
        li.reverse()
        sr3="\n Hexadecimal of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def oct_bin():
    # octal to dec
    checkpt=""
    test=""
    li=[]
    a = equation.get()
    try:
        a= int(a)
        checkpt="T"
    except ValueError:
        msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input !")

    # to check input is octal or not 
    if checkpt=="T":
        a= str(a)
        for i in a:
            i=int(i)
            if 0<=i<=7:
                val="T"
                test+=str(val)
            else:
                val="F"
                test+=str(val)
    compval= len(a)*"T"

    if compval==test:
        s1 =" 'To convert octal number to binary\n 1st we convert it to decimal and then to binary' "
        sr="\n \nSteps to Convert given Octal to Decimal number : "
        sr1_li = []
        po =len(a)-1
        for i in a:
            b=int(i)
            di = b*(8**po)
            sr1= "("+str(b)+"x"+str(8)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
        sr2='\n \nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given octal Number :"+str(add)
        
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,    command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
   
        a = add
        sr1= "\n \nSteps to calculate binary of decimal number"
        sr2="\n  \tQuotient        \t\t\t\tRemainder"
        if a ==0 :
            sr="\n\tBinary of 00 is "+str(0000)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,     command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//2 != 0:
                b = a%2 
                a = a//2
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t1"
            li.append(1)
        li.reverse()
        sr3="\n \nBinary of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def oct_hex():
    checkpt=""
    test=""
    li=[]
    a = equation.get()
    try:
        a= int(a)
        checkpt="T"
    except ValueError:
        msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input !")

    # to check input is octal or not 
    if checkpt=="T":
        a= str(a)
        for i in a:
            i=int(i)
            if 0<=i<=7:
                val="T"
                test+=str(val)
            else:
                val="F"
                test+=str(val)
    compval= len(a)*"T"

    if compval==test:
        s1="\n\n To convert given Octal to Hexadecimal \n1st we convert it to Decimal and then to Hexadecimal "
        sr="\n\n Steps to Convert given Octal to Decimal number : "
        sr1_li = []
        po =len(a)-1
    
        for i in a:
            b=int(i)
            di = b*(8**po)
            sr1= "("+str(b)+"x"+str(8)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\n\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Octal Number is :"+str(add)

        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,    command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

        a = add
        sr1= "\n\n Steps to Convert Decimal to Hexadecimal  number"
        sr2="\n\n\t  Quotient        \t\t\t\tRemainder"
        if a ==0 or 16>a>9:
            if a==0:
                sr="\n \t Hexadecimal of 00 is "+str(0000)
                text_op.insert(END,sr)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)
            else:
                sr="\n \t Hexadecimal of "+str(a) +" is : "
                if a==10:
                    a= "A"
                elif a==11:
                    a ="B"
                elif a == 12:
                    a = "C"
                elif a ==13:
                    a ="D"
                elif a ==14:
                    a = "E"
                elif a==15:
                    a = "F"
                text_op.insert(END,sr+a)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//16 != 0:
                b = a%16 
                a = a//16
                if b==10:
                    b= "A"
                elif b==11:
                    b="B"
                elif b== 12:
                    b= "C"
                elif b==13:
                    b="D"
                elif b==14:
                    b= "E"
                elif b==15:
                    b= "F"
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            if a>10:
                li.append(a)
            else:
                if a==10:
                    a= "A"
                elif a==11:
                    a="B"
                elif a== 12:
                    a= "C"
                elif a==13:
                    a="D"
                elif a==14:
                    a= "E"
                elif a==15:
                    a= "F"
                li.append(a)
            sr5 ="     \t 0 \t\t\t\t  \t"+str(a)

        li.reverse()
        sr3="\n Hexadecimal of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def bin_oct():
    li=[]
    a = equation.get()
    # To check input is binary no. or not
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        checkpt="T"
    else :
        checkpt="F"
        
    if checkpt== "T":
        s1="\n To Convert Binary to Octal \n1st we convert it to Decimal then to Octal  "
        sr="\n\n Steps to calculate decimal of binary number : "
        sr1_li = []
        po =len(a)-1
    
        for i in a:
            b=int(i)
            di = b*(2**po)
            sr1= "("+str(b)+"x"+str(2)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\n\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Binary Number is :"+str(add)

        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    
        a = add
        sr1= "\n\n Steps to calculate Octal of decimal number"
        sr2="\n\n\t  Quotient        \t\t\t\tRemainder"
        if a ==0:
            sr="\n \t Octal of 00 is "+str(0000)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//8 != 0:
                b = a%8 
                a = a//8
                sr4= "\t"+str(a)+"\t\t\t\t \t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t\t\t\t  \t"+str(a)
            li.append(a)
        li.reverse()
        sr3="\n\n Octal of Entered Decimal Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"

        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)
        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def bin_hex():
    li=[]
    a = equation.get()
    # To check input is binary no. or not
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        checkpt="T"
    else :
        checkpt="F"
        
    if checkpt== "T":
        s1="\n To Convert Binary to Hexadecimal \n1st we convert it to Decimal\and then to Hexadecimal "
        sr="\n\n Steps to calculate decimal of binary number : "
        sr1_li = []
        po =len(a)-1
    
        for i in a:
            b=int(i)
            di = b*(2**po)
            sr1= "("+str(b)+"x"+str(2)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\n\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Binary Number is :"+str(add)
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)


        a = add
        sr1= "\n\n Steps to calculate Hexadecimal of decimal number"
        sr2="\n\n  \tQuotient        \t\t\t\tRemainder"
        if a ==0 or 16>a>9:
            if a==0:
                sr="\n \t Hexadecimal of 00 is "+str(0000)
                text_op.insert(END,sr)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)
            else:
                sr="\n \t Hexadecimal of "+str(a) +" is : "
                if a==10:
                    a= "A"
                elif a==11:
                    a ="B"
                elif a == 12:
                    a = "C"
                elif a ==13:
                    a ="D"
                elif a ==14:
                    a = "E"
                elif a==15:
                    a = "F"
                text_op.insert(END,sr+a)
                def refresh():
                    text_op.delete(0.0,END)
                refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
                refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//16 != 0:
                b = a%16 
                a = a//16
                if b==10:
                    b= "A"
                elif b==11:
                    b="B"
                elif b== 12:
                    b= "C"
                elif b==13:
                    b="D"
                elif b==14:
                    b= "E"
                elif b==15:
                    b= "F"
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t"+str(a)
            li.append(a)
        li.reverse()
        sr3="\n Hexadecimal of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"

        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)


    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def hex_oct():
    li=[]
    sr1_li= []
    a = equation.get()
    
    test=""
    comprli=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    for cr in a:
        if (any(cr in i for i in comprli)):
            val="T"
            test+=str(val)
        else:
            val="F"
            test+=str(val)
    compval= len(a)*"T"
    
    if compval==test and a!="":
        s1= "\n To convert Hexadecimal to Octal \n1st we convert it to Decimal and then to Octal"   
        sr= "\n\n Steps to Convert Hexadeciaml to Decimal Number: "   
        po =len(a)-1
        for i in a:
            if i=="A":
                i=10
            elif i=="B":
                i=11
            elif i=="C":
                i=12
            elif i=="D":
                i=13
            elif i=="E":
                i=14
            elif i=="F":
                i=15
        
            b=int(i)
            di = b*(16**po)
            sr1= "("+str(b)+"x"+str(16)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)


        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
        sr2= "\n\n"+"Adding all these elements"+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Hexadecimal Number is :"+str(add)
        
        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    
   
        a = add
        sr1= "\n \nSteps to calculate Octal of decimal number"
        sr2="\n\n  \tQuotient       \t\t\t\t Remainder"
        if a==0:
            sr="\n \t Octal of 00 is "+str(0000)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)
        else:  
            li= []
            sr4_li= []
            while a//8 != 0:
                b = a%8 
                a = a//8
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t"+str(a)
            li.append(a)
        li.reverse()
        sr3="\n \nOctal of Entered Decimal Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"
        
        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def hex_bin():
    li=[]
    sr1_li= []
    a = equation.get()
    
    test=""
    comprli=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    for cr in a:
        if (any(cr in i for i in comprli)):
            val="T"
            test+=str(val)
        else:
            val="F"
            test+=str(val)
    compval= len(a)*"T"
    
    if compval==test and a!="":
        s1= "\n To Convert Hexadecimal to Binary \n1st We convert it to Decimal and then to Binary "   
        sr= "\n \nSteps to Convert Hexadeciaml to Decimal Number: "   
        po =len(a)-1
    
        for i in a:
            if i=="A":
                i=10
            elif i=="B":
                i=11
            elif i=="C":
                i=12
            elif i=="D":
                i=13
            elif i=="E":
                i=14
            elif i=="F":
                i=15
        
            b=int(i)
            di = b*(16**po)
            sr1= "("+str(b)+"x"+str(16)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)


        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
        sr2= "\n\n"+"Adding all these elements"+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Hexadecimal Number is :"+str(add)

        hor_scroll = Scrollbar(ter_op)
        hor_scroll.grid(row=1,column=1)

        text_op= Text(ter_op,yscrollcommand=hor_scroll.set,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+sr+sr1_str+sr2+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)


        a = add
        sr1= "\n\n Steps to calculate binary of decimal number"
        sr2="\n \n \tQuotient        \t\t\t\tRemainder"
        if a ==0 :
            sr="\n\tBinary of 00 is "+str(0000)
            text_op.insert(END,sr)
            def refresh():
                text_op.delete(0.0,END)
            refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7,     command=refresh)
            refresh_bt.grid(row=0, column=1,ipadx=17)

        else:  
            li= []
            sr4_li= []
            while a//2 != 0:
                b = a%2 
                a = a//2
                sr4= "\t"+str(a)+"\t \t\t\t\t"+str(b)
                li.append(b)
                sr4_li.append(sr4)
            sr5 ="     \t 0 \t  \t\t\t\t1"
            li.append(1)
        li.reverse()
        sr3="\n \nBinary of Entered Number is :"+str(li)

        sr4_str= "\n "
        for i in sr4_li:
            sr4_str += i+"\n"

        text_op.insert(END,sr1+sr2+sr4_str+sr5+sr3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)

    else:
        msgbox.showerror(title= "Invalid Input",message="Please Provide Valid Input !")

# ASCII

def bin_ascii():
    li=[]
    a = equation.get()
    # To check input is binary no. or not
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        checkpt="T"
    else :
        checkpt="F"
        
    if checkpt== "T":
        sr0="To Find ASCII value of binary, first we convert it to Decimal"
        sr="\n \nSteps to calculate decimal of binary number : "
        sr1_li = []
        po =len(a)-1
        for i in a:
            b=int(i)
            di = b*(2**po)
            sr1= "("+str(b)+"x"+str(2)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\n\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Binary Number is :"+str(add)
        
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr0+sr+sr1_str+sr2+sr3)
        if add>55238:
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"Sorry something went wrong !\n We are unable to show ASCII value of Number Greater Than 55238")
        elif add<32:
            msgbox.showerror(title="Error",message="ASCII NOT FOUND OF GIVEN NUMBER! "+str(add))

        elif add>=32:
            a=chr(add)
            text_op.insert(END,"\n\nASCII value of given Number is: "+str(a))
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")


def dec_ascii():
    add = equation.get()
    checkpt= ""
    try:
        add =int(add)
        checkpt= "T"
    except ValueError:
        print("It's not int")
    
    if checkpt == "T":
        add=int(add)

        if add>55238:
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"Sorry something went wrong !\n We are unable to show ASCII value of Number Greater Than 55238")

        elif add<32:
            msgbox.showerror(title="Error",message="ASCII NOT FOUND OF GIVEN NUMBER!  "+str(add))
        
        elif add>=32:
            a=chr(add)
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"ASCII value of given Number is: "+str(a))


        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input !")

def oct_ascii():
    checkpt=""
    test=""
    li=[]
    a = equation.get()
    try:
        a= int(a)
        checkpt="T"
    except ValueError:
        print("Error")
        # msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input !")

    # to check input is octal or not 
    if checkpt=="T":
        a= str(a)
        for i in a:
            i=int(i)
            if 0<=i<=7:
                val="T"
                test+=str(val)
            else:
                val="F"
                test+=str(val)
    compval= len(a)*"T"

    if compval==test:
        sr0="To Find ASCII value of Octal, first we convert it to Decimal"
        sr="\n \nSteps to Convert given Octal to Decimal number : "
        sr1_li = []
        po =len(a)-1
    
        for i in a:
            b=int(i)
            di = b*(8**po)
            sr1= "("+str(b)+"x"+str(8)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)
        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
    
        sr2='\n\nAdding all these elements'+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Octal Number is :"+str(add)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr0+sr+sr1_str+sr2+sr3)
        if add>55238:
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"Sorry something went wrong !\n We are unable to show ASCII value of Number Greater Than 55238")
        elif add<32:
            msgbox.showerror(title="Error",message="ASCII NOT FOUND OF GIVEN NUMBER! "+str(add))
            
        elif add>=32:
            a=chr(add)
            text_op.insert(END,"\n\nASCII value of given Number is: "+str(a))
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

def hex_ascii():
    li=[]
    sr1_li= []
    a = equation.get()
    test=""
    comprli=("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
    for cr in a:
        if (any(cr in i for i in comprli)):
            val="T"
            test+=str(val)
        else:
            val="F"
            test+=str(val)
    compval= len(a)*"T"
    
    if compval==test and a!="":
        sr0="To Find ASCII value of Hexadecimal, first we convert it to Decimal"
        sr= "\n\n Steps to Convert Hexadeciaml to Decimal Number: "   
        po =len(a)-1
        for i in a:
            if i=="A":
                i=10
            elif i=="B":
                i=11
            elif i=="C":
                i=12
            elif i=="D":
                i=13
            elif i=="E":
                i=14
            elif i=="F":
                i=15
        
            b=int(i)
            di = b*(16**po)
            sr1= "("+str(b)+"x"+str(16)+"^"+str(po)+"="+str(di)+") +"
            sr1_li.append(sr1)
            po-=1
            li.append(di)


        sr1_str= "\n "
        for i in sr1_li:
            sr1_str += i
        
        sr2= "\n\n"+"Adding all these elements"+str(li)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        sr3= "\n\nThe Decimal of given Hexadecimal Number is :"+str(add)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,sr0+sr+sr1_str+sr2+sr3)
        if add>55238:
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"Sorry something went wrong !\n We are unable to show ASCII value of Number Greater Than 55238")
        elif add<32:
            msgbox.showerror(title="Error",message="ASCII NOT FOUND OF GIVEN NUMBER! "+str(add))
            
        elif add>=32:
            a=chr(add)
            text_op.insert(END,"\n\nASCII value of given Number is: "+str(a))
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input  !")

def ascii_dec():
    val= equation.get()
    li=""
    for i in val:
        a = ord(i)
        li+=" "+str(a)

    text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
    text_op.grid(row=1,column=0,padx=70,pady=5)
    text_op.insert(END,"Decimal value of given ASCII is: "+str(li))
    def refresh():
        text_op.delete(0.0,END)
    refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
    refresh_bt.grid(row=0, column=1,ipadx=17)

def ascii_bin():
    val= equation.get()
    if len(val)==1:
        a = ord(val)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,"Decimal value of given ASCII is: "+str(a))
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Correct Input")

    sr0="\nTo find Binary, first we convert given ASCII to decimal and then to Binary"
    sr1= "\n\n Steps to calculate binary of decimal number"
    sr2="\n\n\t  Quotient\t   \t\t\tRemainder"
    if len(val)==1:  
        li= []
        sr4_li= []
        while a//2 != 0:
            b = a%2 
            a = a//2
            sr4= "\t"+str(a)+"\t\t\t   \t"+str(b)
            li.append(b)
            sr4_li.append(sr4)
        sr5 ="     \t 0\t\t\t   \t1"
        li.append(1)
    li.reverse()
    sr3="\n\n Binary of Entered Number is :"+str(li)

    sr4_str= "\n "
    for i in sr4_li:
        sr4_str += i+"\n"
    text_op.insert(END,sr0+sr1+sr2+sr4_str+sr5+sr3)
    def refresh():
        text_op.delete(0.0,END)
    refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
    refresh_bt.grid(row=0, column=1,ipadx=17)

def ascii_oct():
    val= equation.get()
    if len(val)==1:
        a = ord(val)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,"Decimal value of given ASCII is: "+str(a))
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Correct Input")

    sr0="\nTo find Octal, first we convert given ASCII to decimal and then to Octal"
    sr1= "\n\n Steps to calculate Octal of decimal number"
    sr2="\n\n\t  Quotient\t   \t\t\tRemainder"
        
    if len(val)==1:  
        li= []
        sr4_li= []
        while a//8 != 0:
            b = a%8 
            a = a//8
            sr4= "\t"+str(a)+"\t   \t\t\t"+str(b)
            li.append(b)
            sr4_li.append(sr4)
        sr5 ="     \t 0\t   \t\t\t"+str(a)
        li.append(a)
    li.reverse()
    sr3="\n Octal of Entered Decimal Number is :"+str(li)

    sr4_str= "\n "
    for i in sr4_li:
        sr4_str += i+"\n"
        
    text_op.insert(END,sr0+sr1+sr2+sr4_str+sr5+sr3)
    def refresh():
        text_op.delete(0.0,END)
    refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
    refresh_bt.grid(row=0, column=1,ipadx=17)

def ascii_hex():
    val= equation.get()
    if len(val)==1:
        a = ord(val)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,"Decimal value of given ASCII is: "+str(a))
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Correct Input")

    sr0="\nTo find Octal, first we convert given ASCII to decimal and then to Octal"
    sr1= "\n\n Steps to calculate Octal of decimal number"
    sr2="\n\n\t  Quotient\t   \t\t\tRemainder"
    if len(val)==1:  
        li= []
        sr4_li= []
        while a//16 != 0:
            b = a%16 
            a = a//16
            if b==10:
                b= "A"
            elif b==11:
                b="B"
            elif b== 12:
                b= "C"
            elif b==13:
                b="D"
            elif b==14:
                b= "E"
            elif b==15:
                b= "F"
            sr4= "\t"+str(a)+"\t   \t\t\t"+str(b)
            li.append(b)
            sr4_li.append(sr4)
        sr5 ="     \t 0\t   \t\t\t"+str(a)
        li.append(a)
    li.reverse()
    sr3="\n\n Binary of Entered Number is :"+str(li)

    sr4_str= "\n "
    for i in sr4_li:
        sr4_str += i+"\n"
    
    text_op.insert(END,sr0+sr1+sr2+sr4_str+sr5+sr3)
    def refresh():
        text_op.delete(0.0,END)
    refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
    refresh_bt.grid(row=0, column=1,ipadx=17)


# Binary arithmatics

# main opration 
def dec_bin_1(a):
    if a==0:
        li=0
    else:
        li= []
        while a//2 != 0:
            b = a%2 
            a = a//2
            li.append(b)
        li.append(1)
        li.reverse()
    return li

def bin_dec(bin):
    li=[]
    po =len(bin)-1
    for i in bin:
        b=int(i)
        di = b*(2**po)
        po-=1
        li.append(di)
    add =0
    for i in li:
        no = int(i)
        add = add+no
    return add

def check_bin(a):
    # To check input is binary no. or not
    p = set(a)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        checkpt="T"
    else:
        checkpt="F"
    return checkpt

def bin_add():
    bin1= equation.get()
    check1 = check_bin(bin1)

    bin2= equation1.get()
    check2 = check_bin(bin2)

    if str(check1)+str(check2)=="TT":
        s1 = bin1+"\n+"
        s2 =bin2
        d1=bin_dec(bin1)
        d2=bin_dec(bin2)
        add = d1+d2
        result=dec_bin_1(add)
        s3="\n--------------------"
        s4= "\n"+str(result)+" \t\nIs the addition of above binary number. "

        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+s2+s3+s4)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input", message="Please Provide Valid Input  !")

def bin_sub():
    bin1= equation.get()
    check1 = check_bin(bin1)

    bin2= equation1.get()
    check2 = check_bin(bin2)

    if str(check1)+str(check2)=="TT":
        s1 = bin1+"\n-"
        s2 =bin2
        d1=bin_dec(bin1)
        d2=bin_dec(bin2)
        if d1>d2:
            add = d1-d2
            result=dec_bin_1(add)
            s3="\n--------------------"
            s4= "\n"+str(result)+" \t\nIs the Substraction of above binary number. "
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,s1+s2+s3+s4)
        else:
            text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
            text_op.grid(row=1,column=0,padx=70,pady=5)
            text_op.insert(END,"Sorry, We are Unable to solve this, Please provide first input greter than second input")
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

def bin_multi():
    bin1= equation.get()
    check1 = check_bin(bin1)

    bin2= equation1.get()
    check2 = check_bin(bin2)

    if str(check1)+str(check2)=="TT":
        s1 = bin1+"\n*"
        s2 =bin2
        d1=bin_dec(bin1)
        d2=bin_dec(bin2)
        add = d1*d2
        result=dec_bin_1(add)
        s3="\n--------------------"
        s4= "\n"+str(result)+" \t\nIs the Multiplication of above binary number. "
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+s2+s3+s4)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

def bin_div():
    bin1= equation.get()
    check1 = check_bin(bin1)

    bin2= equation1.get()
    check2 = check_bin(bin2)

    if str(check1)+str(check2)=="TT":
        s1 = bin1+"\n/"
        s2 =bin2
        d1=bin_dec(bin1)
        d2=bin_dec(bin2)
        add = d1/d2
        rem= add%2
        add-=rem
        bin_rem = dec_bin_1(rem)
        result=dec_bin_1(add)
        s3="\n--------------------"
        s4= "\n"+str(result)+" \t\nIs the Division of above binary number. \n And\t"+str(bin_rem)+"\tIs reminder"
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+s2+s3+s4)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

# compliments
def one_compl():
    li=""
    a = equation.get()
    check1 = check_bin(a)
    if check1=="T":
        for i in a:
            if i =='0':
                i = 1
            elif i =='1':
                i = 0
            li = li+str(i)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,"\nOnce's Compliment of given Binary No is : "+str(li))
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

def two_compl():
    bin=""
    a = equation.get()
    check1= check_bin(a)
    if check1 =="T":
        for i in a:
            if i =='0':
                i = 1
            elif i =='1':
                i = 0
            bin = bin+str(i)
        s1="\nOnce's Compliment of given Binary No is : "+str(bin)
        li=[]
        po =len(bin)-1
        for i in bin:
            b=int(i)
            di = b*(2**po)
            po-=1
            li.append(di)
        add =0
        for i in li:
            no = int(i)
            add = add+no
        add+=1
        li= []
        while add//2 != 0:
            b = add%2 
            add = add//2
            li.append(b)
        li.append(1)
        lip = li.reverse()
        s2="\nAfter Adding 1 in one's compliment"
        s3= "\nTwo's Compliment is : "+str(li)
        text_op= Text(ter_op,font="Calbri 12 bold",wrap="word")
        text_op.grid(row=1,column=0,padx=70,pady=5)
        text_op.insert(END,s1+s2+s3)
        def refresh():
            text_op.delete(0.0,END)
        refresh_bt = Button(ter_op, text='Clear', fg='black', bg='white',height=1, width=7, command=refresh)
        refresh_bt.grid(row=0, column=1,ipadx=17)
    else:
        msgbox.showerror(title="Invalid Input",message="Please Provide Valid Input  !")

# menu bar Functions

def about():
    about_tab = Tk()
    # about_tab.config(bg="cyan")
    about_tab.title("About Page")
    about_tab.geometry("480x200")

    Main_label= Label(about_tab,text="About Me",font="Calbri 20 bold",fg="white",bg="black")
    Main_label.grid(row=0,column=0,padx=160,pady=20)

    link1 = Label(about_tab, text="I'm Chetan Rathod, \nSecond Year Computer Engineering of\n Zeal College Of Engineering And Research, Pune\n Pursuing Engineering Under the Savitribai Phule Pune university \nLove Coding In Python",font="Calbri 12 ", fg="black")
    link1.grid(row=1,column=0,padx=5,pady=10,columnspan=5)
    
    about_tab.mainloop()

def contact():
    def callback(url):
        webbrowser.open_new(url)

    root = Tk()
    root.geometry("400x200")
    root.title("Contact Me")

    link1 = Label(root, text="Email: chetan0101career@gmail.com",font="Calbri 12 bold", fg="black", cursor="hand2")
    Main_label= Label(root,text="Contact Me",font="Calbri 20 bold",fg="white",bg="black")
    Main_label.grid(row=0,column=0,padx=120,pady=10)

    link1.grid(row=2,column=0,padx=5,pady=2,columnspan=5)
    link1.bind("<Button-1>", lambda e: callback("http://mailto:chetan01010career@gmail.com"))

    link2 = Label(root, text="Linkedin", fg="black", cursor="hand2",bg="cyan",relief=SUNKEN)
    link2.grid(row=3,column=0,padx=5,pady=2,columnspan=5)
    link2.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/chetan-rathod-8b0a14207/"))

    link3 = Label(root, text="Instagram", fg="black", cursor="hand2",bg="cyan",relief=SUNKEN)
    link3.grid(row=4,column=0,padx=5,pady=2,columnspan=5)
    link3.bind("<Button-1>", lambda e: callback("https://www.instagram.com/chetan_rathod_01/"))

    link4 = Label(root, text="Youtube", fg="black", cursor="hand2",bg="cyan",relief=SUNKEN)
    link4.grid(row=5,column=0,padx=5,pady=2,columnspan=5)
    link4.bind("<Button-1>", lambda e: callback("https://www.youtube.com/channel/UCJ_QxI3rnrC04K0SzvIJvlg"))

def project():
    pro =Tk()
    pro.geometry("600x300")
    pro.title("About Project")

    main_label = Label(pro,text="About Project",fg="white",bg="black",font="Helvetica 20 bold")
    main_label.grid(row=0,columnspan=10,column=5,pady=10,padx=200)

    info_lable= Label(pro,text="This is Number System Converter And Binary Calculator GUI SoftWare. I have developed this software in Python Language using Tkinter Library. \n_____ Features Of this Software: _____\n # Do all 12 types of Number System Convertion.\n # Finds ASCII value of all four Number Systems.\n # Convert ASCII Value to all fou Number Systems.\n # Do all four basic Arithmatic Oprations on Binary Numbers.\n # Find One's and Two's Complement.\n # Do all the above listed oprations with explainations and steps.",font="calbri 12",fg="black",bg="white",wraplength=500)
    info_lable.grid(row=2,column=5,columnspan=10,rowspan=5)

    pro.mainloop()

def suggest():
    def callback(url):
        webbrowser.open_new(url)

    sug =Tk()
    sug.geometry("400x200")
    sug.title("Suggestion/Feedback")

    main_label = Label(sug,text="Suggestion/Feedback",fg="white",bg="black",font="Helvetica 20 bold")
    main_label.grid(row=0,columnspan=10,column=5,pady=10,padx=50)

    info_lable= Label(sug,text="Please Click Below and \nfill the Google form for your suggestion/feedback.",font="calbri 12 bold",fg="black")
    info_lable.grid(row=2,column=5,columnspan=10,rowspan=5)

    link2 = Label(sug, text="Click Here", fg="black", cursor="hand2",bg="cyan",relief=SUNKEN)
    link2.grid(row=7,column=5,padx=5,pady=20,columnspan=10)
    link2.bind("<Button-1>", lambda e: callback("https://forms.gle/2jBtoZughEenFrkB8"))

    sug.mainloop()

def report():
    def callback(url):
        webbrowser.open_new(url)

    sug =Tk()
    sug.geometry("400x200")
    sug.title("Report Issue")

    main_label = Label(sug,text="Report Issue",fg="white",bg="black",font="Helvetica 20 bold")
    main_label.grid(row=0,columnspan=10,column=5,pady=10,padx=100)

    info_lable= Label(sug,text="Please Click Below and \nfill the Google form to Report Issue.",font="calbri 12 bold",fg="black")
    info_lable.grid(row=2,column=5,columnspan=10,rowspan=5)

    link2 = Label(sug, text="Click Here", fg="black", cursor="hand2",bg="cyan",relief=SUNKEN)
    link2.grid(row=7,column=5,padx=5,pady=20,columnspan=10)
    link2.bind("<Button-1>", lambda e: callback("https://forms.gle/ALU9NZeavrf1vZyH9"))

    sug.mainloop()



if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="cyan")


	# set the title of GUI window
	gui.title("Number System Converter and Binary Calculator        - Developed By Chetan Rathod")

	# set the configuration of GUI window
	gui.geometry("1000x800")
	gui.maxsize(width=1000,height=800)

	equation = StringVar()

	main_manu = Menu(gui,bg="blue",fg="white")
	main_manu.add_command(label="About Me",command=about)
	main_manu.add_command(label="Contact Me",command=contact)
	main_manu.add_command(label="About Project",command=project)
	main_manu.add_command(label="Report Issue",command=report)
	main_manu.add_command(label="Suggestion/Feedback",command=suggest)
	gui.config(menu=main_manu)
	
	head_fr = Frame(gui, bg='cyan',borderwidth=8,border=5,relief=SUNKEN)
	head_fr.grid(row=0,column=0)


	no_conv = Frame(head_fr, bg='grey',borderwidth=8,border=5,relief=SUNKEN)
	no_conv.grid(row=0,column=0)

	ter_op = Frame(gui, bg='grey', width=5,border=10,borderwidth=15,relief=RAISED)
	ter_op.grid(row=7, column=0,columnspan=5)
    
    

	ter_lab = Label(ter_op, text='Steps and Calculations : ',font="Helvetica 15 bold", fg='black', bg='white',height=1, width=7)
	ter_lab.grid(row=0, column=0,ipadx=100)

	expression_field = Entry(no_conv, textvariable=equation)

	expression_field.grid(columnspan=2, ipadx=70,row=1,column=1)

	num_lab = Label(no_conv,text="Input Box : ",fg="white",bg="grey")
	num_lab.grid(row=1,column=0,columnspan=1,ipadx=40)
    
    
    
	h1 = Label(no_conv, text='Number Conversion',font="calbri 10 bold", fg='white', bg='black',height=1, width=50)
	h1.grid(row=0,columnspan=3)
    
	bin_dec_bt = Button(no_conv, text='Binary to Decimal', fg='black', bg='white',height=1, width=20,command=bin_dec_main)
	bin_dec_bt.grid(row=2, column=0)

	oct_dec_bt = Button(no_conv, text='Octal to Decimal', fg='black', bg='white',height=1, width=20,command=oct_dec_main)
	oct_dec_bt.grid(row=2, column=1)

	hex_dec_bt = Button(no_conv, text='Hexadecimal to Decimal', fg='black', bg='white',height=1, width=20,command=hex_dec_main)
	hex_dec_bt.grid(row=2, column=2)

	dec_bin_bt = Button(no_conv, text='Decimal to Binary', fg='black', bg='white',height=1, width=20,command=dec_bin)
	dec_bin_bt.grid(row=3, column=0)

	dec_oct_bt = Button(no_conv, text='Decimal to Octal', fg='black', bg='white',height=1, width=20,command=dec_oct)
	dec_oct_bt.grid(row=3, column=1)

	dec_hex_bt = Button(no_conv, text='Decimal to Hexadecimal', fg='black', bg='white',height=1, width=20,command=dec_hex)
	dec_hex_bt.grid(row=3, column=2)

	oct_bin_bt = Button(no_conv, text='Octal to Binary', fg='black', bg='white',height=1, width=20,command=oct_bin)
	oct_bin_bt.grid(row=4, column=0)

	oct_hex_bt = Button(no_conv, text='Octal to Hexadecimal', fg='black', bg='white',height=1, width=20,command=oct_hex)
	oct_hex_bt.grid(row=4, column=1)

	bin_oct_bt = Button(no_conv, text='Binary to Octal', fg='black', bg='white',height=1, width=20,command=bin_oct)
	bin_oct_bt.grid(row=4, column=2)

	bin_hex_bt = Button(no_conv, text='Binary to Hexadecimal', fg='black', bg='white',height=1, width=20,command=bin_hex)
	bin_hex_bt.grid(row=5, column=0)

	hex_oct_bt = Button(no_conv, text='Hexadecimal to Octal', fg='black', bg='white',width=20,command=hex_oct)
	hex_oct_bt.grid(row=5, column=2)

	hex_bin_bt = Button(no_conv, text='Hexadecimal to Binary', fg='black', bg='white', width=20,command=hex_bin)
	hex_bin_bt.grid(row=5, column=1)
        


	f_ascii = Frame(head_fr, bg='grey',borderwidth=8,border=5,relief=SUNKEN)
	f_ascii.grid(row=0, column=4)



	bin_ascii_bt = Button(f_ascii, text='Binary to ASCII', fg='black', bg='white',height=1, width=7,command=bin_ascii)
	bin_ascii_bt.grid(row=2, column=5,ipadx=22)

	dec_ascii_bt = Button(f_ascii, text='Decimal to ASCII', fg='black', bg='white',height=1, width=7,command=dec_ascii)
	dec_ascii_bt.grid(row=3, column=5,ipadx=22)

	oct_ascii_bt = Button(f_ascii, text='Octal to ASCII', fg='black', bg='white',height=1, width=7,command=oct_ascii)
	oct_ascii_bt.grid(row=4, column=5,ipadx=22)

	hex_ascii_bt = Button(f_ascii, text='Hexa to ASCII', fg='black', bg='white',height=1, width=7,command=hex_ascii)
	hex_ascii_bt.grid(row=5, column=5,ipadx=22)


	ascii_bin_bt = Button(f_ascii, text='ASCII to Binary', fg='black', bg='white',height=1, width=7,command=ascii_bin)
	ascii_bin_bt.grid(row=2, column=6,ipadx=22)


	ascii_dec_bt = Button(f_ascii, text='ASCII to Decimal', fg='black', bg='white',height=1, width=7,command=ascii_dec)
	ascii_dec_bt.grid(row=3, column=6,ipadx=22)

	ascii_oct_bt = Button(f_ascii, text='ASCII to Octal', fg='black', bg='white',height=1, width=7,command=ascii_oct)
	ascii_oct_bt.grid(row=4, column=6,ipadx=22)

	ascii_hex_bt = Button(f_ascii, text='ASCII to Hexa', fg='black', bg='white',height=1, width=7,command=ascii_hex)
	ascii_hex_bt.grid(row=5, column=6,ipadx=22)


	bin_fr = Frame( head_fr, bg='grey',border=5,borderwidth=8,relief=SUNKEN)
	bin_fr.grid(row=0, column=7)

	bin_arth_leb = Label(bin_fr, text='Binary Arithmatic',font="calbri 10 bold", fg='white', bg='black',height=1, width=7)
	bin_arth_leb.grid(row=0, column=7,ipadx=30)


	bin_add_bt = Button(bin_fr, text='Addition', fg='black', bg='white',height=1, width=7,command=bin_add)
	bin_add_bt.grid(row=2, column=7,ipadx=30)

	bin_sub_bt = Button(bin_fr, text='Subtraction', fg='black', bg='white',height=1, width=7,command=bin_sub)
	bin_sub_bt.grid(row=3, column=7,ipadx=30)

    
	bin_multi_bt = Button(bin_fr, text='Multiplication', fg='black', bg='white',height=1, width=7,command=bin_multi)
	bin_multi_bt.grid(row=4, column=7,ipadx=30)

	bin_div_bt = Button(bin_fr, text=' Division ', fg='black', bg='white',height=1, width=7,command=bin_div)
	bin_div_bt.grid(row=5, column=7,ipadx=30)


	h2 = Label(f_ascii,text='ASCII Conversion',font="calbri 10 bold", fg='white', bg='black',height=1, width=7)
	h2.grid(row=0, column=5,columnspan=2,ipadx=70)


	
	equation1 = StringVar()

	sec_input = Entry(bin_fr, textvariable=equation1)
	sec_input.grid(row=1, column=7)



	f_compl = Frame(head_fr, bg='grey',border=5,borderwidth=8,relief=SUNKEN)
	f_compl.grid(row=0, column=8)

	h4 = Label(f_compl,text='Compliments', fg='white', bg='black',font="calbri 10 bold",height=1, width=7,borderwidth=8,border=5,relief=SUNKEN)
	h4.grid(row=0, column=8,columnspan=1,ipadx=40,ipady=10)

	text_op = Text(ter_op,font="Calbri 12 bold",wrap="word")
	text_op.grid(row=1,column=0,padx=50,pady=3)


	gui.protocol('WM_DELETE_WINDOW', display_msg)

	one_compl_bt = Button(f_compl, text="One's Compliment", fg='black', bg='white',height=1, width=7,command=one_compl)
	one_compl_bt.grid(row=2, column=8,rowspan=2,ipadx=40,ipady=10)
    
	two_compl_bt = Button(f_compl, text="Two's Compliment", fg='black', bg='white',height=1, width=7,command=two_compl)
	two_compl_bt.grid(row=4, column=8,rowspan=2,ipadx=40,ipady=10)
    
	sec_inp_bx = Label(f_ascii,text="  Input Box-2 :",bg="grey",fg="white")
	sec_inp_bx.grid(row=1,column=5,columnspan=2)


	gui.mainloop()


