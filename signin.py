from tkinter import *
#for image PIL=python-image-library to run .jpg image in our window
from PIL import ImageTk


#functionality

    #for clearing the place holder
def clearName_holder(e):
    if username.get()=='userName':
        username.delete(0,END)

def clearPassword_holder(e):
    if password.get()=='password':
        password.delete(0,END)


#Gui part
Login_win=Tk()
    #to deniy the user max the window
Login_win.resizable(0,0)
Login_win.title('Login page')
Login_win.geometry('1100x617+100+100')

#background image
bgImage=ImageTk.PhotoImage(file='cleanup5.webp')

bgLabel=Label(Login_win,image=bgImage)
bgLabel.place(x=0,y=0)


#header
header=Label(Login_win,text='USER LOGIN',font=("Yahei UI Light Microsoft",25,'bold'),bg='white',fg='cyan3')
header.place(x=710,y=80)

#user inputs
username=Entry(Login_win,width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='cyan3')
username.place(x=650,y=160)
username.insert(0,'userName')

username.bind('<FocusIn>',clearName_holder)

#Frame
f1=Frame(Login_win,width=310,height=2,bg='cyan3')
f1.place(x=650,y=180)

#password
password=Entry(Login_win,width=25,font=("Microsoft Yahei UI Light",11,"bold"),bd=0,fg='cyan3')
password.place(x=650,y=220)
password.insert(0,"password")

password.bind('<FocusIn>',clearPassword_holder)

#Frame
f1=Frame(Login_win,width=310,height=2,bg='cyan3')
f1.place(x=650,y=240)




Login_win.mainloop()
