from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
from tkinter.ttk import Progressbar
from textwrap import fill
from itertools import cycle
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk, Image
from gnews import GNews
import sqlite3,datetime,webbrowser


def splash_screen() :
    global bg_splash,progress,ttk_style,start_root
    start_root = Tk()

    w_splash = 427
    h_splash = 250
    screen_width = start_root.winfo_screenwidth()/2 - w_splash/2
    screen_height = start_root.winfo_screenheight()/2 - h_splash/2
    #x_coordinate = (screen_width/2)-(w_splash/2)
    #y_coordinate = (screen_height/2)-(h_splash/2)
    start_root.geometry("%dx%d+%d+%d" %(w_splash,h_splash,screen_width,screen_height))

    start_root.overrideredirect(1)

    ttk_style = ttk.Style()
    ttk_style.theme_use('clam')
    ttk_style.configure("red.Horizontal.TProgressbar", foreground='red', background='#777575')
    progress = Progressbar(start_root,orient=HORIZONTAL,length=500,mode='determinate')
    progress.place(x=-10,y=235)
    bg_splash = '#FEEDED'

    Frame(start_root,width=427,height=241,bg=bg_splash).place(x=0,y=0)
    #getst_btn = Button(start_root,width=10,height=1,text='Get Started',command=bar,border=0,fg=bg_splash,bg='white')
    #getst_btn.place(x=170,y=200)

    start_root.after(500,bar)

    cereal_title = Label(start_root,text='CEREAL',fg='#7B6079',bg=bg_splash)
    title_font = ('Calibri (Body)',18,'bold')
    cereal_title.config(font=title_font)
    cereal_title.place(x=50,y=80)

    sub_title = Label(start_root,text='DIGITAL PLANNER',fg='#7B6079',bg=bg_splash)
    sub_font = ('Calibri (Body)',13)
    sub_title.config(font=sub_font)
    sub_title.place(x=50,y=110)
    return start_root
    
def bar():
    loading_lab =Label(start_root,text='Loading...',fg='#7B6079',bg=bg_splash)
    loading_font = ('Calibri (Body)',10)
    loading_lab.config(font=loading_font)
    loading_lab.place(x=18,y=210)
    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        start_root.update_idletasks()
        time.sleep(0.000001)
        r=r+1
    
    start_root.destroy()
    mainwindow()

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('db/cereal_database.db')
    cursor = conn.cursor()

def mainwindow():
    global root,userinfo,pwdinfo,regis_first,regis_last,regis_username,regis_pwd,regis_cfpwd,w,h,add_act_btn,del_act_btn,cycle_act,date_ent_spy,act_name_ent_spy,descript_ent_spy,color_ent_spy
    root = Tk()
    w = 1200
    h = 700
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='black')
    root.title("Cereal Digital Planner")
    root.option_add('*font',"Calibri 24 bold")
    root.rowconfigure((0,1,2,3,4),weight=1)
    root.columnconfigure((0,1,2,3,4),weight=1)
    root.resizable(0,0)
    root.iconbitmap("img/icon.ico")
    add_act_btn = PhotoImage(file="img/add_act_btn.png")
    del_act_btn = PhotoImage(file="img/del_act_btn.png")
    cycle_act = PhotoImage(file="img/cycle_act.png").subsample(3,3)
    userinfo = StringVar()
    pwdinfo = StringVar()
    regis_first = StringVar()
    regis_last = StringVar()
    regis_username = StringVar()
    regis_pwd = StringVar()
    regis_cfpwd = StringVar()
    date_ent_spy = StringVar()
    act_name_ent_spy = StringVar()
    descript_ent_spy = StringVar()
    color_ent_spy = StringVar()
    login_page(root)
    root.mainloop()

images = ["img/img.png","img/img2.png"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def slideShow() :
    img = next(photos)
    photo_frm.config(image=img)
    root.after(5500, slideShow)

def login_page(root) :
    global login_frm,userentry,pwdentry,photo_frm
    # Photo slide
    photo_frm = Label(root)
    root.after(10, lambda: slideShow())
    photo_frm.place(x=0,y=0,width=720,height=700)

    # log in zone
    login_frm = Frame(root,bg="#FEEDED")
    login_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    login_frm.rowconfigure((0,8),weight=2)
    login_frm.columnconfigure((0,1),weight=1)
    login_frm.place(x=720,y=0,width=480,height=700)

    Label(login_frm,text="Cereal Digital Planner",bg="#FEEDED",fg="#7B6079",font="Calibri 26 bold").grid(row=1,column=0,columnspan=2,sticky="news")
    Label(login_frm,text="Username",bg="#FEEDED",fg="#7B6079",font="Calibri 18").grid(row=2,column=0,sticky="ws",padx=10,pady=5)
    userentry = Entry(login_frm,textvariable=userinfo,font="Arial 12",relief=FLAT,bd=0)
    userentry.grid(row=3,column=0,columnspan=2,sticky="new",padx=10,pady=5,ipady=6)
    Label(login_frm,text="Password",bg="#FEEDED",fg="#7B6079",font="Calibri 18").grid(row=4,column=0,sticky="ws",padx=10,pady=5)
    pwdentry = Entry(login_frm,textvariable=pwdinfo,show="●",font="Arial 12",relief=FLAT,bd=0)
    pwdentry.grid(row=5,column=0,columnspan=2,sticky="new",padx=10,pady=5,ipady=6)
    
    Button(login_frm,activebackground="#FEEDED",text="Login",bg="#FEEDED",fg="#7B6079",relief=FLAT,width=10,command=loginclick,bd=0).grid(row=6,column=0,columnspan=2,pady=20,ipady=15,sticky='s',padx=20)
    Button(login_frm,activebackground="#FEEDED",text="Register",bg="#FEEDED",fg="#7B6079",relief=FLAT,width=10,command=regiswindow,bd=0).grid(row=7,column=0,columnspan=2,pady=20,ipady=15,sticky='n',padx=20)

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
                    menu_bar()
                else :
                    messagebox.showwarning("Cereal", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Cereal", "Username not found\n Please register before Login")
            userentry.focus_force()

def menu_bar() :
    global username,menu_frm
    username = userentry.get()
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    menu_frm = Frame(root,bg="#FFD4D4")
    options = ["Home","Calendar", "Activity", "Music", "Timer","Profile"]
    command_list = [home_page,calendar_page,activity_page,music_page,timer_page,profile_page]
    y = 45
    for i in range(6):
        Button(menu_frm, text=options[i],command=command_list[i], font="BahnschriftLight 15", bg="#FFD4D4", fg="#1B1C22", activebackground="#FFD4D4", activeforeground="#1B1C22", bd=0).place(x=25, y=y)
        y += 40
    Button(menu_frm, text="Logout",command=logoutClick, font="BahnschriftLight 15", bg="#FFD4D4", fg="#1B1C22", activebackground="#FFD4D4", activeforeground="#1B1C22", bd=0).place(x=25, y=620)
    menu_frm.place(x=0,y=0,width=215,height=h)
    home_page()

def home_page() :
    global home_frm,username,news_frm,daily_act_frm,date
    login_frm.destroy()

    home_frm = Frame(root,bg="#FEEDED")

    news_frm = Frame(root,bg="#FFDDDD")
    news_frm.rowconfigure((1,2,3,4,5,6,7,8,9),weight=1)
    news_frm.rowconfigure((0),weight=5)
    news_frm.columnconfigure((0,1),weight=1)

    daily_act_frm = Frame(root,bg="#FFDDDD")
    
    get_today = datetime.date.today()
    today = str(get_today)
    date = Label(home_frm,text="Current date : "+today,bg="#FEEDED", fg="#7B6079", font="BahnschriftLight 20")
    date.place(x=560,y=55)

    Label(news_frm,text="News",bg="#FFDDDD", fg="#7B6079", font="BahnschriftLight 20 bold" ).place(x=197,y=17)
    i = 0
    for n in range (3) :
        Label(news_frm,text=news[n]['title'],bg="#FFDDDD", fg="#1B1C22", font="BahnschriftLight 10" ).grid(row=i+1,column=0,columnspan=2,sticky="nw",padx=5,pady=4)
        Label(news_frm,text=news[n]['published date'],bg="#FFDDDD", fg="#7B6079", font="BahnschriftLight 8" ).grid(row=i+2,column=0,columnspan=2,sticky="nw",padx=5,pady=1)
        i += 3
    Button(news_frm, text="Read More",command=lambda:opennews(0), font="BahnschriftLight 10", bg="#FFDDDD", fg="#1B1C22", activebackground="#FFDDDD", activeforeground="#1B1C22", bd=0,relief=FLAT).grid(row=3,column=1,sticky="ne",padx=10,pady=1)
    Button(news_frm, text="Read More",command=lambda:opennews(1), font="BahnschriftLight 10", bg="#FFDDDD", fg="#1B1C22", activebackground="#FFDDDD", activeforeground="#1B1C22", bd=0,relief=FLAT).grid(row=6,column=1,sticky="ne",padx=10,pady=1)
    Button(news_frm, text="Read More",command=lambda:opennews(2), font="BahnschriftLight 10", bg="#FFDDDD", fg="#1B1C22", activebackground="#FFDDDD", activeforeground="#1B1C22", bd=0,relief=FLAT).grid(row=9,column=1,sticky="ne",padx=10,pady=1)


    Label(daily_act_frm,text="Daily Activity",bg="#FFDDDD", fg="#7B6079", font="BahnschriftLight 20 bold").place(x=43,y=17)
    news_frm.place(x=314,y=135,width=469,height=430)
    daily_act_frm.place(x=827,y=135,width=262,height=430)
    home_frm.place(x=215,y=0,width=985,height=h)

def opennews(n) :
    url = news[n]['url']
    webbrowser.open(url,new=1)


def logoutClick() :
    home_frm.destroy()
    menu_frm.destroy()
    news_frm.destroy()
    daily_act_frm.destroy()
    login_page(root)

def calendar_page() :
    global calendar_frm,act_frm,cal
    news_frm.destroy()
    daily_act_frm.destroy()
    home_frm.destroy()
    calendar_frm = Frame(root,bg="#FEEDED")
    
    cal = Calendar(calendar_frm, font="Arial 12", selectmode='day', locale='en_US',showweeknumbers=False,firstweekday="sunday",background="#FF7171",weekendforeground="#FF7171")
    cal.place(x=155,y=63,width=390,height=287)
    
    Label(calendar_frm,image=cycle_act,bg="#FEEDED").place(x=630,y=64)
    Button(calendar_frm,text="",image=add_act_btn,compound=CENTER,bg="#FEEDED",fg="#1B1C22", activebackground="#FEEDED", activeforeground="#1B1C22", bd=0,relief=FLAT,command=add_activity).place(x=640,y=250,width=152,height=44)
    Button(calendar_frm,text="",image=del_act_btn,compound=CENTER,bg="#FEEDED",fg="#1B1C22", activebackground="#FEEDED", activeforeground="#1B1C22", bd=0,relief=FLAT,command=del_activity).place(x=640,y=307,width=152,height=44)
    
    act_frm = Frame(calendar_frm,bg="#FFDDDD")
    act_frm.place(x=155,y=400,width=676,height=233)
    act_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    act_frm.columnconfigure((0,1),weight=1)
    add_activity()
    calendar_frm.place(x=215,y=0,width=985,height=h)

def add_activity() :
    
    Label(act_frm,text="Add Activity",font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22").grid(row=0,column=0,columnspan=2,sticky="news",padx=15,pady=10)
    date = Label(act_frm,text="Date :",font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22")
    date.grid(row=1,column=0,sticky="e",padx=15,pady=10)
    act_name = Label(act_frm,text="Activity Name :",font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22")
    act_name.grid(row=2,column=0,sticky="e",padx=15,pady=10)
    descript = Label(act_frm,text="Description :",font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22")
    descript.grid(row=3,column=0,sticky="e",padx=15,pady=10)
    color = Label(act_frm,text="Color :",font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22")
    color.grid(row=4,column=0,sticky="e",padx=15,pady=10)
    
    date_ent = Entry(act_frm,textvariable=date_ent_spy,font="Arial 12",relief=FLAT,bd=0)
    date_ent.grid(row=1,column=1,sticky="w",padx=15,pady=10)
    act_name_ent = Entry(act_frm,textvariable=act_name_ent_spy,font="Arial 12",relief=FLAT,bd=0)
    act_name_ent.grid(row=2,column=1,sticky="w",padx=15,pady=10)
    descript_ent = Entry(act_frm,textvariable=descript_ent_spy,font="Arial 12",relief=FLAT,bd=0)
    descript_ent.grid(row=3,column=1,sticky="w",padx=15,pady=10)
    color_ent = Entry(act_frm,textvariable=color_ent_spy,font="Arial 12",relief=FLAT,bd=0)
    color_ent.grid(row=4,column=1,sticky="w",padx=15,pady=10)
    date_ent_spy.set(cal.selection_get())
    Button(act_frm,text="Confirm",command=cf_add_act,font="BahnschriftLight 14",bg="#FFDDDD",fg="#1B1C22",bd=0,relief=FLAT).grid(row=5,column=1,sticky="e",padx=15,pady=10)
    # Button เอาแบบปุ่มข้างบน
def cf_add_act() :
    pass

def del_activity() :
    print("del_act")

def activity_page() :
    news_frm.destroy()
    daily_act_frm.destroy()
    home_frm.destroy()
    activity_frm = Frame(root,bg="#FEEDED")
    activity_frm.place(x=215,y=0,width=985,height=h)

def music_page() :
    news_frm.destroy()
    daily_act_frm.destroy()
    home_frm.destroy()
    music_frm = Frame(root,bg="#FEEDED")
    music_frm.place(x=215,y=0,width=985,height=h)

def timer_page() :
    news_frm.destroy()
    daily_act_frm.destroy()
    home_frm.destroy()
    timer_frm = Frame(root,bg="#FEEDED")
    timer_frm.place(x=215,y=0,width=985,height=h)

def profile_page() :
    global profile_top
    sql = "select first_name,last_name,regis_date from Member where username=?"
    cursor.execute(sql,[username])
    result = cursor.fetchone()
    profile_top = Toplevel()
    pro_w = 363
    pro_h = 466
    profile_top.title("Cereal Profile")
    pro_x = profile_top.winfo_screenwidth()/2 - pro_w/2
    pro_y = profile_top.winfo_screenheight()/2 - pro_h/2
    #profile_top.geometry("%dx%d+%d+%d"%(pro_w,pro_h,pro_x,pro_y))
    profile_top.geometry("%dx%d"%(pro_w,pro_h))
    profile_top.config(bg='#FFDDDD')
    profile_top.option_add('*font',"Calibri 24 bold")
    profile_top.iconbitmap("img/pro_icon.ico")
    profile_top.resizable(0,0)
    profile_top.rowconfigure((0,1,2,3,4),weight=1)
    profile_top.columnconfigure((0,1),weight=1)

    profile_ico = PhotoImage(file="img/profile_ico.png").subsample(6,6)
    Label(profile_top,image=profile_ico,bg="#FFDDDD").grid(row=0,column=0,columnspan=2,sticky="news")
    Label(profile_top,text="First name :",bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=1,column=0,padx=2,pady=10,sticky="ne")
    Label(profile_top,text=result[0],bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=1,column=1,padx=2,pady=10,sticky="nw")

    Label(profile_top,text="Last name :",bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=2,column=0,padx=2,pady=10,sticky="ne")
    Label(profile_top,text=result[1],bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=2,column=1,padx=2,pady=10,sticky="nw")

    Label(profile_top,text="Registration date :",bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=3,column=0,padx=2,pady=10,sticky="ne")
    Label(profile_top,text=result[2],bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=3,column=1,padx=2,pady=10,sticky="nw")

    Label(profile_top,text="Username :",bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=4,column=0,padx=2,pady=10,sticky="ne")
    Label(profile_top,text=username,bg="#FFDDDD",font="Calibri 14",fg="#7B6079").grid(row=4,column=1,padx=2,pady=10,sticky="nw")

    Button(profile_top,text="Change Password",bg="#FFDDDD",font="Calibri 14",fg="#3B2E3B",relief=FLAT,bd=1,activebackground="#FFDDDD",command=chg_password).grid(row=5,column=0,padx=2,pady=20,sticky="news")
    Button(profile_top,text="Home",bg="#FFDDDD",font="Calibri 14",fg="#3B2E3B",relief=FLAT,bd=1,activebackground="#FFDDDD",command=profile_top.destroy).grid(row=5,column=1,padx=2,pady=20,sticky="news")

    profile_top.mainloop()


def chg_password() :
    global chgpwd_top,chgpwd,cf_chgpwd,curpwd_ent,newpwd_ent
    chgpwd_top = Toplevel()
    chgpwd_w = 363
    chgpwd_h = 200
    chgpwd_top.title("Change Password")
    chgpwd_x = chgpwd_top.winfo_screenwidth()/2 - chgpwd_w/2
    chgpwd_y = chgpwd_top.winfo_screenheight()/2 - chgpwd_h/2
    #chgpwd_top.geometry("%dx%d+%d+%d"%(chgpwd_w,chgpwd_h,chgpwd_x,chgpwd_y))
    chgpwd_top.geometry("%dx%d"%(chgpwd_w,chgpwd_h))
    chgpwd_top.config(bg='#FFDDDD')
    chgpwd_top.option_add('*font',"Calibri 24 bold")
    chgpwd_top.iconbitmap("img/pro_icon.ico")
    chgpwd_top.rowconfigure((0,1,2,3),weight=1)
    chgpwd_top.columnconfigure((0,1,2),weight=1)
    chgpwd = StringVar()
    cf_chgpwd = StringVar()

    Label(chgpwd_top,text="Change Account Password",bg="#FFDDDD",font="Calibri 18",fg="#7B6079").grid(row=0,column=0,padx=2,pady=5,columnspan=3,sticky="news")
    
    Label(chgpwd_top,text="Current Password",bg="#FFDDDD",font="Calibri 12",fg="#7B6079").grid(row=1,column=0,padx=2,pady=5,sticky="ne")
    curpwd_ent = Entry(chgpwd_top,textvariable=chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,width=25)
    curpwd_ent.grid(row=1,column=1,sticky="n",padx=8,pady=7,columnspan=3)

    Label(chgpwd_top,text="New Password",bg="#FFDDDD",font="Calibri 12",fg="#7B6079").grid(row=2,column=0,padx=2,pady=5,sticky="ne")
    newpwd_ent = Entry(chgpwd_top,textvariable=cf_chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,width=25)
    newpwd_ent.grid(row=2,column=1,sticky="n",padx=8,pady=7,columnspan=3)

    Button(chgpwd_top,text="Confirm",bg="#FFDDDD",font="Calibri 12",fg="#3B2E3B",relief=FLAT,bd=1,activebackground="#FFDDDD",command=confirm_chg).grid(row=3,column=0,sticky="news",padx=8,pady=7,columnspan=3)

    chgpwd_top.mainloop()


def confirm_chg() :
    sql = """
            select password
            from Member
            where username=?"""
    cursor.execute(sql,[username])
    cur_pwd = cursor.fetchone()
    if curpwd_ent.get() == "" :
        messagebox.showerror("Cereal","Please Enter Current Password",parent=chgpwd_top)
        curpwd_ent.focus_force()
    elif newpwd_ent.get() == "" :
        messagebox.showerror("Cereal","Please Enter New Password",parent=chgpwd_top)
        newpwd_ent.focus_force()
    elif cur_pwd[0] == curpwd_ent.get() :
        sql = """
                update Member
                set password=?
                where username=?"""
        cursor.execute(sql,[newpwd_ent.get(),username])
        conn.commit()
        messagebox.showinfo("Cereal","Change Password Successfully",parent=chgpwd_top)
        chgpwd_top.destroy()
    else :
        messagebox.showerror("Cereal","Password Incorrect!",parent=chgpwd_top)
        curpwd_ent.focus_force()
        curpwd_ent.select_range(0,END)

def regiswindow() :
    global regis_frm,userentry,pwdentry,photo_frm,regis_first_ent,regis_last_ent,regis_username_ent,regis_pwd_ent,regis_cfpwd_ent

    photo_frm.destroy()
    login_frm.destroy()
    # Photo slide
    photo_frm = Label(root)
    root.after(10, lambda: slideShow())
    photo_frm.place(x=0,y=0,width=720,height=700)

    # log in zone
    regis_frm = Frame(root,bg="#FFDDDD")
    regis_frm.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regis_frm.rowconfigure((0,12),weight=2)
    regis_frm.columnconfigure((0,1),weight=1)
    regis_frm.place(x=720,y=0,width=480,height=700)

    Label(regis_frm,text="Register for Cereal",bg="#FFDDDD",fg="#7B6079",width=25).grid(row=1,column=0,columnspan=2,sticky="news",pady=20)

    Label(regis_frm,text="First name *",bg="#FFDDDD",fg="#7B6079",font="Arial 15").grid(row=2,column=0,sticky="ws",padx=10,pady=5)
    regis_first_ent = Entry(regis_frm,textvariable=regis_first,width=12,font="Arial 12",relief=FLAT,bd=0)
    regis_first_ent.grid(row=3,column=0,sticky="new",padx=10,pady=5,ipady=6)

    Label(regis_frm,text="Last name *",bg="#FFDDDD",fg="#7B6079",font="Arial 15").grid(row=2,column=1,sticky="ws",pady=5,padx=10)
    regis_last_ent = Entry(regis_frm,textvariable=regis_last,width=12,font="Arial 12",relief=FLAT,bd=0)
    regis_last_ent.grid(row=3,column=1,sticky="new",padx=10,pady=5,ipady=6)

    Label(regis_frm,text="Username *",bg="#FFDDDD",fg="#7B6079",font="Arial 15").grid(row=4,column=0,sticky="ws",pady=5,padx=10)
    regis_username_ent = Entry(regis_frm,textvariable=regis_username,width=25,font="Arial 12",relief=FLAT,bd=0)
    regis_username_ent.grid(row=5,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Label(regis_frm,text="Password *",bg="#FFDDDD",fg="#7B6079",font="Arial 15").grid(row=6,column=0,sticky="ws",pady=5,padx=10)
    regis_pwd_ent = Entry(regis_frm,textvariable=regis_pwd,width=25,show="●",font="Arial 12",relief=FLAT,bd=0)
    regis_pwd_ent.grid(row=7,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Label(regis_frm,text="Confirm Password *",bg="#FFDDDD",fg="#7B6079",font="Arial 15").grid(row=8,column=0,sticky="ws",pady=5,padx=10)
    regis_cfpwd_ent = Entry(regis_frm,textvariable=regis_cfpwd,width=25,show="●",font="Arial 12",relief=FLAT,bd=0)
    regis_cfpwd_ent.grid(row=9,column=0,columnspan=2,sticky="news",padx=10,pady=5)

    Button(regis_frm,activebackground="#FFDDDD",text="Back",bg="#FFDDDD",fg="#7B6079",relief=FLAT,width=10,command=exitRegis,bd=0).grid(row=11,column=0,pady=20,ipady=15,sticky='w',padx=20)
    Button(regis_frm,activebackground="#FFDDDD",text="Register",bg="#FFDDDD",fg="#7B6079",relief=FLAT,width=10,command=registration,bd=0).grid(row=11,column=1,pady=20,ipady=15,sticky='e',padx=20)

def registration() :
    first = regis_first_ent.get().capitalize()
    last = regis_last_ent.get().capitalize()
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
        get_today = datetime.date.today()
        sql = "SELECT username FROM Member WHERE username=?"
        cursor.execute(sql,[username])
        result = cursor.fetchone()
        if result == None :
            sql = """
                    insert into Member
                    values (?,?,?,?,?)
            """
            cursor.execute(sql,[username,cfpassword,first,last,get_today])
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

createconnection()

google_news = GNews()
google_news = GNews(language='th', country='thai', period='1d', max_results=10, exclude_websites=['google.com', 'bbc.com/thai'])
news = google_news.get_news('covid')

start_root = splash_screen()

start_root.mainloop()