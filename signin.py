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

    #password
def hide():
    openeye.config(file='closeye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)




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

#eye button
openeye=PhotoImage(file="openeye.png")
eyeButton=Button(Login_win,image=openeye,bd=0,bg='white',activebackground="white",cursor='hand2',command=hide)
eyeButton.place(x=927,y=214)

#forgot button
resahutButton=Button(Login_win,text='Forgot password?',bd=0,bg='white',activebackground="white",cursor='hand2',font=("Microsoft Yahei UI Light",9,"bold"),fg='cyan3',activeforeground="cyan3")
resahutButton.place(x=842,y=255)

#Login Button
LoginButton=Button(Login_win,text='Login',bd=0,width=24,activebackground="cyan3",font=('Open Sans',16,'bold'),fg='white',bg='cyan3',activeforeground="white",cursor='hand2')

LoginButton.place(x=650,y=350)

#or

orLable=Label(Login_win,text='---------------------OR-------------------',font=('Open Sans',16,'bold'),fg='cyan3',bg='white')

orLable.place(x=650,y=410)

#logo
fb_logo=PhotoImage(file='facebook.png')
fbLabel=Label(Login_win,image=fb_logo,bg='white')
fbLabel.place(x=680,y=460)

go2_logo=PhotoImage(file='google.png')
goLabel=Label(Login_win,image=go2_logo,bg='white')
goLabel.place(x=800,y=460)


twi_logo=PhotoImage(file='twitter.png')
twLabel=Label(Login_win,image=twi_logo,bg='white')
twLabel.place(x=900,y=460)




Login_win.mainloop()
