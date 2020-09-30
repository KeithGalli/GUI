from tkinter import *


def values():
    print("\nStudent Details")
    print(f"\tStudent Name:- {fs1value.get()} {fs2value.get()} {fs3value.get()}")
    print(f"\tGender:- {genvalue.get()}")
    print(f"\tDate of Birth:- {dobvalue.get()}")
    print(f"\tPhone Number:- {phvalue.get()}")
    print(f"\tEmail Address:- {emavalue.get()}")
    print(f"\tResidential Address:- {addrvalue.get()}")
    print(f"\tCity:- {ctyvalue.get()}, State:- {statvalue.get()}")
    print(f"\tPostal / Zip Code:- {zipcvalue.get()}\n")
    
    #passing the data to a .txt file:


    with open("FormData.txt","a") as f:
        f.write(f"Student Details\n")
        f.write(f"\tStudent Name:- {fs1value.get()} {fs2value.get()} {fs3value.get()}\n")
        f.write(f"\tGender:- {genvalue.get()}\n")
        f.write(f"\tDate of Birth:- {dobvalue.get()}\n")
        f.write(f"\tPhone Number:- {phvalue.get()}\n")
        f.write(f"\tEmail Address:- {emavalue.get()}\n")
        f.write(f"\tResidential Address:- {addrvalue.get()}\n")
        f.write(f"\tCity:- {ctyvalue.get()}, State:- {statvalue.get()}\n")
        f.write(f"\tPostal / Zip Code:- {zipcvalue.get()}\n\n")
        f.write("")
root=Tk()
root.geometry("850x799")



'''
Creating Icon and title
'''
# to change the defalut Tkinter ICon
photo=PhotoImage(file="C:\\Users\\91762\\Desktop\\VS Code\\tkinter tutorials\\tut10\\dance.png")

# Setting icon of master window 
root.iconphoto(False,photo)

root.title("Deepraj Dance Academy - Registration Form 2020")

'''
Creating the BOdy
'''
# Frame for header
f1=Frame(root,bg="#E4E46C",borderwidth=10,relief=SUNKEN)
f1.grid(row=100,column=100)
# header
body=Label(f1,text="REGISTRATION FORM 2020",font="robotoslab 30 bold",fg="#17AFCF",)
body.grid(row=10,column=170,rowspan=12,sticky=N)

'''
FILLUP FORM
'''
#STUDENT DETAILS
nam=Label(root,text="Student Details",font="robotoslab 27 bold",fg="#EE601D")
nam.grid(row=700,column=100)

fst=Label(root,text="First Name",font="Roboto 16 ",fg="black")
fst.grid(row=1000,column=1)

fs2=Label(root,text="Middle Name",font="Roboto 16 ",fg="black")
fs2.grid(row=1001,column=1)

fs3=Label(root,text="Last Name",font="Roboto 16 ",fg="black")
fs3.grid(row=1002,column=1)

fs1value=StringVar()
fs2value=StringVar()
fs3value=StringVar()

fs1entry=Entry(root,textvariable=fs1value,width=40)
fs2entry=Entry(root,textvariable=fs2value,width=40)
fs3entry=Entry(root,textvariable=fs3value,width=40)

fs1entry.grid(row=1000,column=100,columnspan=5,padx=10,pady=10)
fs2entry.grid(row=1001,column=100,columnspan=5,padx=10,pady=10)
fs3entry.grid(row=1002,column=100,columnspan=5,padx=10,pady=10)

gen=Label(root,text="Gender",font="Roboto 16 ",fg="black")
gen.grid(row=1005,column=1)

genvalue=StringVar()
genentry=Entry(root,textvariable=genvalue,width=17)
genentry.grid(row=1005,column=100,padx=10,pady=10)

dob=Label(root,text="Date of Birth",font="robotoslab 16",fg="black")
dob.grid(row=1006,column=1)
dobvalue=StringVar()
dobentry=Entry(root,textvariable=dobvalue,width=40)
dobentry.grid(row=1006,column=100,padx=10,pady=10)

ph=Label(root,text="Phone Number",font="robotoslab 16",fg="black")
ph.grid(row=1007,column=1)
phvalue=StringVar()
phentry=Entry(root,textvariable=phvalue,width=40)
phentry.grid(row=1007,column=100,padx=10,pady=10)


ema=Label(root,text="Email ID",font="robotoslab 16",fg="black")
ema.grid(row=1008,column=1)
emavalue=StringVar()
emaentry=Entry(root,textvariable=emavalue,width=40)
emaentry.grid(row=1008,column=100,padx=10,pady=10)

addr=Label(root,text="Address",font="robotoslab 16",fg="black")
addr.grid(row=1009,column=1)
addrvalue=StringVar()
addrentry=Entry(root,width=40,textvariable=addrvalue)
addrentry.grid(row=1009,column=100,ipadx=30,ipady=20)

cty=Label(root,text="City",font="robotoslab 16",fg="black")
cty.grid(row=1010,column=1)
ctyvalue=StringVar()
ctyentry=Entry(root,textvariable=ctyvalue,width=40)
ctyentry.grid(row=1010,column=100,padx=10,pady=10)

stat=Label(root,text="State",font="robotoslab 16",fg="black")
stat.grid(row=1011,column=1)
statvalue=StringVar()
statentry=Entry(root,textvariable=statvalue,width=40)
statentry.grid(row=1011,column=100,padx=10,pady=10)

zipc=Label(root,text="Postal \ Zip\nCode",font="robotoslab 16",fg="black")
zipc.grid(row=1012,column=1)
zipcvalue=StringVar()
zipcentry=Entry(root,textvariable=zipcvalue,width=40)
zipcentry.grid(row=1012,column=100,padx=10,pady=10,ipady=15)

Button(text="Submit\nForm",font="comicsansms 19 bold",command=values).grid(row=1100,column=105)

frd=Label(text="Registration Ends Soon*")
frd.grid(row=1500,column=105)





root.mainloop()
