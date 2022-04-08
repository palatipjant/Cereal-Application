btnState = False
    top_lab = Frame(home_frm,bg="#6667AB")
    top_lab.place(x=0,y=0,width=1200,height=53)
    navbarBtn = Button(home_frm, image=navIcon, bg="#6667AB", activebackground="#6667AB", bd=0, padx=20, command=switch)
    navbarBtn.place(x=10, y=10)
    navRoot = Frame(home_frm, bg="#D2D2DD", height=1000, width=300)
    navRoot.place(x=-300, y=0)
    Label(navRoot, font="Bahnschrift 15", bg="#6667AB", fg="black", height=2, width=300, padx=20).place(x=0, y=0)
    y = 80
    options = ["Calendar", "Activity", "Music", "Timer","Profile"]
    command_list = [calendar_page,activity_page,music_page,timer_page,profile_page]
    for i in range(5):
        Button(navRoot, text=options[i],command=command_list[i], font="BahnschriftLight 15", bg="#D2D2DD", fg="#1B1C22", activebackground="#D2D2DD", activeforeground="#1B1C22", bd=0).place(x=25, y=y)
        y += 40
    Button(navRoot, text="Logout",command=logoutClick, font="BahnschriftLight 15", bg="#D2D2DD", fg="#1B1C22", activebackground="#D2D2DD", activeforeground="#1B1C22", bd=0).place(x=25, y=650)
    closeBtn = Button(navRoot, image=closeIcon, bg="#6667AB", activebackground="#6667AB", bd=0, command=switch)
    closeBtn.place(x=250, y=10)


def switch():
    global btnState
    color = {"nero": "#252726"}
    if btnState is True:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            home_frm.update()
        top_lab.config(bg="#6667AB")
        home_frm.config(bg="#8D8DAA")
        root.config(bg="gray17")
        btnState = False
    else:
        home_frm.config(bg=color["nero"])
        root.config(bg=color["nero"])
        top_lab.config(bg=color["nero"])
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            home_frm.update()
        btnState = True