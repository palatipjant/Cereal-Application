from textwrap import fill
from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
from itertools import cycle
from PIL import ImageTk, Image
import tkmacosx,calendar,sqlite3,pygame,datetime,time

def mainwindow() :
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='black')
    root.title("Cereal Digital Planner")
    root.option_add('*font',"Arial 24 bold")
    root.rowconfigure((0,1,2,3,4),weight=1)
    root.columnconfigure((0,1,2,3,4),weight=1)
    root.resizable(0,0)
    return root

images = ["img/img.png","img/img2.png"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('db/cereal_database.db')
    cursor = conn.cursor()

def slideShow() :
    img = next(photos)
    photo_frm.config(image=img)
    root.after(5000, slideShow) # 5 sec

def login_page(root) :
    global login_frm,userentry,pwdentry,photo_frm
    # Photo slide
    photo_frm = Label(root)
    root.after(10, lambda: slideShow())
    photo_frm.place(x=0,y=0,width=720,height=700)

    # log in zone
    login_frm = Frame(root,bg="#8D8DAA")
    login_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    login_frm.rowconfigure((0,8),weight=2)
    login_frm.columnconfigure((0,1),weight=1)
    login_frm.place(x=720,y=0,width=480,height=700)

    Label(login_frm,text="Cereal Digital Planner",bg="#8D8DAA",fg="white",font="Calibri 26 bold").grid(row=1,column=0,columnspan=2,sticky="news")
    Label(login_frm,text="Username",bg="#8D8DAA",fg="white",font="Calibri 18").grid(row=2,column=0,sticky="ws",padx=10,pady=5)
    userentry = Entry(login_frm,textvariable=userinfo,font="Arial 12")
    userentry.grid(row=3,column=0,columnspan=2,sticky="new",padx=10,pady=5,ipady=6)
    Label(login_frm,text="Password",bg="#8D8DAA",fg="white",font="Calibri 18").grid(row=4,column=0,sticky="ws",padx=10,pady=5)
    pwdentry = Entry(login_frm,textvariable=pwdinfo,show="●",font="Arial 12")
    pwdentry.grid(row=5,column=0,columnspan=2,sticky="new",padx=10,pady=5,ipady=6)

    Button(login_frm,activebackground="#8D8DAA",text="Login",bg="#8D8DAA",fg="white",relief=FLAT,width=10,command=loginclick,bd=0).grid(row=6,column=0,columnspan=2,pady=20,ipady=15,sticky='s',padx=20)
    Button(login_frm,activebackground="#8D8DAA",text="Register",bg="#8D8DAA",fg="white",relief=FLAT,width=10,command=regiswindow,bd=0).grid(row=7,column=0,columnspan=2,pady=20,ipady=15,sticky='n',padx=20)


def loginclick() :
    global user
    user = userentry.get()
    pwd = pwdentry.get()
    
    if user == "" :
        messagebox.showwarning("Cereal", "Please Enter Username")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM Member WHERE username=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Cereal", "Please enter password")
                pwdentry.focus_force()
            else :
                sql = "SELECT * FROM Member WHERE username=? and password=? "
                cursor.execute(sql, [user, pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Cereal", "Login Successfully")
                    home_page()
                else :
                    messagebox.showwarning("Cereal", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Cereal", "Username not found\n Please register before Login")
            userentry.focus_force()

def home_page() :
    global home_frm
    login_frm.destroy()
    home_frm = Frame(root,bg="#FEEDED")
    menu_frm = Frame(root,bg="#FFD4D4")
    
    options = ["Calendar", "Activity", "Music", "Timer","Profile"]
    command_list = [calendar_page,activity_page,music_page,timer_page,profile_page]
    y = 45
    for i in range(5):
        Button(menu_frm, text=options[i],command=command_list[i], font="BahnschriftLight 15", bg="#FFD4D4", fg="#1B1C22", activebackground="#FFD4D4", activeforeground="#1B1C22", bd=0).place(x=25, y=y)
        y += 40
    Button(menu_frm, text="Logout",command=logoutClick, font="BahnschriftLight 15", bg="#FFD4D4", fg="#1B1C22", activebackground="#FFD4D4", activeforeground="#1B1C22", bd=0).place(x=25, y=600)
    
    menu_frm.place(x=0,y=0,width=250,height=h)
    home_frm.place(x=250,y=0,width=950,height=h)

def logoutClick() :
    home_frm.destroy()
    login_page(root)

def calendar_page() :
    print("calendar_page")

def activity_page() :
    print("activity_page")

def music_page() :
    print("music_page")

def timer_page() :
    print("timer_page")

def profile_page() :
    print("profile_page")

def regiswindow() :
    global regis_frm,userentry,pwdentry,photo_frm,regis_first_ent,regis_last_ent,regis_username_ent,regis_pwd_ent,regis_cfpwd_ent

    photo_frm.destroy()
    login_frm.destroy()
    # Photo slide
    photo_frm = Label(root)
    root.after(10, lambda: slideShow())
    photo_frm.place(x=0,y=0,width=720,height=700)

    # log in zone
    regis_frm = Frame(root,bg="#8D8DAA")
    regis_frm.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regis_frm.rowconfigure((0,12),weight=2)
    regis_frm.columnconfigure((0,1),weight=1)
    regis_frm.place(x=720,y=0,width=480,height=700)

    Label(regis_frm,text="Register for Cereal",bg="#8D8DAA",fg="white",width=25).grid(row=1,column=0,columnspan=2,sticky="news",pady=20)

    Label(regis_frm,text="First name *",bg="#8D8DAA",fg="white",font="Arial 15").grid(row=2,column=0,sticky="ws",padx=10,pady=5)
    regis_first_ent = Entry(regis_frm,textvariable=regis_first,width=12,font="Arial 12")
    regis_first_ent.grid(row=3,column=0,sticky="new",padx=10,pady=5,ipady=6)

    Label(regis_frm,text="Last name *",bg="#8D8DAA",fg="white",font="Arial 15").grid(row=2,column=1,sticky="ws",pady=5,padx=10)
    regis_last_ent = Entry(regis_frm,textvariable=regis_last,width=12,font="Arial 12")
    regis_last_ent.grid(row=3,column=1,sticky="new",padx=10,pady=5,ipady=6)

    Label(regis_frm,text="Username *",bg="#8D8DAA",fg="white",font="Arial 15").grid(row=4,column=0,sticky="ws",pady=5,padx=10)
    regis_username_ent = Entry(regis_frm,textvariable=regis_username,width=25,font="Arial 12")
    regis_username_ent.grid(row=5,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Label(regis_frm,text="Password *",bg="#8D8DAA",fg="white",font="Arial 15").grid(row=6,column=0,sticky="ws",pady=5,padx=10)
    regis_pwd_ent = Entry(regis_frm,textvariable=regis_pwd,width=25,show="●",font="Arial 12")
    regis_pwd_ent.grid(row=7,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Label(regis_frm,text="Confirm Password *",bg="#8D8DAA",fg="white",font="Arial 15").grid(row=8,column=0,sticky="ws",pady=5,padx=10)
    regis_cfpwd_ent = Entry(regis_frm,textvariable=regis_cfpwd,width=25,show="●",font="Arial 12")
    regis_cfpwd_ent.grid(row=9,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Button(regis_frm,activebackground="#8D8DAA",text="Back",bg="#8D8DAA",fg="white",relief=FLAT,width=10,command=exitRegis,bd=0).grid(row=11,column=0,pady=20,ipady=15,sticky='w',padx=20)
    Button(regis_frm,activebackground="#8D8DAA",text="Register",bg="#8D8DAA",fg="white",relief=FLAT,width=10,command=registration,bd=0).grid(row=11,column=1,pady=20,ipady=15,sticky='e',padx=20)

def registration() :
    first = regis_first_ent.get()
    last = regis_last_ent.get()
    username = regis_username_ent.get()
    password = regis_pwd_ent.get()
    cfpassword = regis_cfpwd_ent.get()
# if all of register is blank
    if first == "":
        messagebox.showwarning("Cereal","Please enter your First name.")
        regis_first_ent.focus_force()
    elif last == "":
        messagebox.showwarning("Cereal","Please enter your Last name.")
        regis_last_ent.focus_force()
    elif username == "":
        messagebox.showwarning("Cereal","Please enter your Username.")
        regis_username_ent.focus_force()
    elif password == "":
        messagebox.showwarning("Cereal","Please enter your Password.")
        regis_pwd_ent.focus_force()
    elif cfpassword == "":
        messagebox.showwarning("Cereal","Please enter your Confirm Password.")
        regis_pwd_ent.focus_force()
# check confirm password
    elif password != cfpassword :
        messagebox.showwarning("Cereal","This password dosn't match.")
        regis_cfpwd_ent.focus_force()
# check if email already have in database  
    else : 
        sql = "SELECT username FROM Member WHERE username=?"
        cursor.execute(sql,[username])
        result = cursor.fetchone()
        if result == None :
            sql = """
                    insert into Member
                    values (?,?,?,?)
            """
            cursor.execute(sql,[username,cfpassword,first,last])
            conn.commit()
            messagebox.showinfo("Cereal","Register successfully")
            regis_first_ent.delete(0,END)
            regis_last_ent.delete(0,END)
            regis_username_ent.delete(0,END)
            regis_pwd_ent.delete(0,END)
            regis_cfpwd_ent.delete(0,END)
            login_page(root)
        else :
            messagebox.showwarning("Cereal","This Email was already exist")
            regis_username_ent.focus_force()
            regis_username_ent.select_range(0,END)

def exitRegis() :
    regis_frm.destroy()
    photo_frm.destroy()
    login_page(root)



photo_w = 720
photo_h = 700
w = 1200
h = 700

createconnection()
root = mainwindow()
navIcon = PhotoImage(file="img/menu.png")
closeIcon = PhotoImage(file="img/close.png")
userinfo = StringVar()
pwdinfo = StringVar()
regis_first = StringVar()
regis_last = StringVar()
regis_username = StringVar()
regis_pwd = StringVar()
regis_cfpwd = StringVar()

login_page(root)
root.mainloop()