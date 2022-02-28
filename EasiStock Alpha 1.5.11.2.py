### main indents = 80 col |  sub indents = 60 col |  description = 83 col (text) ###
import tkinter as tk
#from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import os.path
import sqlite3
from os import system
import asyncio
import datetime
import time
from datetime import datetime
global loaded

global d1
global d2
global weak
global special_char
weak = False
today = datetime.now()
d1 = today.strftime("%d/%m/%y")
d2 = today.strftime("%d/%m/%y")
d3 = today.strftime("%H : %M : %S")
special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬" # Provides a "do use" list for checking.

Loading = tk.Tk()

db_exists = os.path.isfile('./EasiStock_Database.db')
db_exists_P = False
logged_in = False
loaded = False
#print(logged_in, "(start of code)") # xyz



NoDB = tk.Tk()
Login=tk.Tk()
MainMenu=tk.Tk()
settings = tk.Tk()
resetPass = tk.Tk()


icon = tk.PhotoImage(file = 'Logo Compact+.png')
Loading.iconphoto(True, icon)
#Loading.iconphoto(True, icon)

w = 1000
h = 600

ws = Login.winfo_screenwidth()
hs = Login.winfo_screenheight()

x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

Login.geometry('%dx%d+%d+%d' % (w, h, x, y))
Loading.geometry('%dx%d+%d+%d' % (1000, 10, x, y))
MainMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
NoDB.geometry('500x280')
settings.geometry('%dx%d+%d+%d' % (w, h, x, y))
resetPass.geometry('%dx%d+%d+%d' % (w, h, x, y))

NoDB.title("ERROR")
Loading.title("Loading, please wait.")
MainMenu.title("EasiStock v1.5.11.2")
Login.title("EasiStock - Please Log In")
settings.title("EasiStock v1.5.11.2 -  Settings")
resetPass.title("EasiStock v1.5.11.2 -  Reset Password")

Login.resizable(0, 0)
NoDB.resizable(0, 0)
Loading.resizable(0, 0)
MainMenu.resizable(0, 0)
resetPass.resizable(0, 0)
settings#.resizable(0, 0)

global ht
ht = 580

def scrollbar(target, w, h):
    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    global frame
    global canvas
    canvas = tk.Canvas(target, borderwidth=0, background="light grey", width=w, height = ht, relief = "groove")
    frame = tk.Frame(canvas, background="light grey", width=w, height = ht, relief = "groove")
    vsb = tk.Scrollbar(target, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(padx=10, pady=80)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

scrollbar(MainMenu, 970, ht)
        
Login.resizable(0, 0)
NoDB.resizable(0, 0)
#Loading.resizable(0, 0)
#MainMenu.resizable(0, 0)

NoDB.withdraw() 
Login.withdraw()
Loading.withdraw()
MainMenu.withdraw()
settings.withdraw()
resetPass.withdraw()

global page_place
global page_count
global page
global exception
global failed
global button_count
global page_bt
global pgs_needed
global x_pg
global y_pg
global check
global row
failed = False
button_count = 0
page = False
exception = False
page_place = MainMenu
page_count = 1
placed = False
page_bt = False
pgs_needed = 0
x_pg = 25
y_pg = 15
check = 0
row = 1
pass_e = 0

# =========================================================================================== BEGINNING OF MAIN CODE ==========================================>>

def ld_bt ():
    print("")

def settings_reset():
    settings.withdraw()
    resetPass.deiconify()

def Disclaimer(index, win):
        #print("Creating Disclaimer buttons with Index:", index)
        version = tk.Label ((index), text = "ES v1.5.11.2 ALPHA BUILD", font = ("Helvetica", 9))
        disclaimer = tk.Label ((index), text = "Content shown in this build is not representative of the final product.", font = ("Helvetica", 9, "italic"))
        #print("Disclaimers have been created.")
        if win == True:
            version.place(x=4, y=580)
            disclaimer.place (x=325, y= 580)

        if win == False:
            version.place(x=4, y=250)
            disclaimer.place (x=230, y= 250)
        #print("Dislaimers have been placed.")

def LogoLabels(current, before, tooltip):
    logo = tk.Button(current, text = "EasiStock.", borderwidth = 0, font=("Tw Cen MT", 34), width =44, command = lambda:[current.withdraw(), before.deiconify()])
    welcome = tk.Label(current, text = tooltip, font=("Tw Cen MT", 20))
    leave= tk.Button(current, text = "\u2190 Return", font = ("Tw Cen MT", 20), borderwidth = 0, command = lambda: [current.withdraw(), before.deiconify()])
    leave.place(x = 5, y = 20)
    logo.place(x=2, y = 0)
    welcome.place(x=422, y = 60)

def ConstantButtons(current):
        global page
        global page_count
        global page_place
        global button_count
        global page_bt
        global pages_needed
        global x_pg
        global y_pg
        print("Constant Widgets being placed.")
        settings_bt = tk.Button(current, text="Settings", activebackground ='grey', relief = "groove", height = 3, width = 9, command = lambda:[current.withdraw(), settings.deiconify()])

        settings_bt.place(x=900,y=10)
        print("Constant Widgets placed, testing APC")
                
def settings_place():
    print("if u see this its too late")
    LogoLabels(settings, MainMenu, "Settings Menu.")
    faq = Button(settings, text = "Help", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", width = 15, borderwidth = 1, command = print("G"))
    pass_change = Button(settings, text = "Change Password", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", borderwidth = 1, command = lambda: [settings.withdraw(), resetPass.deiconify()])
    if weak == True:
        pass_change.config(bg = "green")

    log_out = Button(settings, text = "Log Out", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", width= 15, borderwidth = 1, command = settings_log)

    faq.place(x=376, y= 125)
    pass_change.place(x=376, y=225)
    log_out.place(x=376, y=325)

def resetCheck(new, re, old):
    passed = False
    global txt
    global weak
    print("CHECKING")
    print(old)
    print(pass_e)
    if len(old) == 0:
        messagebox.showerror('EasiStock - Error', "Please enter your old password.")
        return -1
    if old != pass_e:
        messagebox.showerror('EasiStock - Error', "Incorrect password.")
        return -1
    if len(re) == 0:
        messagebox.showerror('EasiStock - Error', "Please re-enter your old password on the second box.")
        return -1
    if old == pass_e:
        if re == old:
            if len(new) == 0:
                messagebox.showerror('EasiStock - Error', "Please enter a new password.")
                return -1
            if old != new:
                if new not in txt: 
                    if any(c in special_char for c in new):
                        if len(new) >=8: 
                            confirm = messagebox.askyesno('EasiStock - Reset Password', "Are you sure you'd like to change your password?")
                            if confirm == True:
                                c.execute("UPDATE Users SET pass = ? WHERE user = ? AND pass = ?", (new, user_e, pass_e))
                                conn.commit()
                                re_pass_e.delete(0,'end')
                                new_pass_e.delete(0,'end')
                                old_pass_e.delete(0,'end')
                                messagebox.showinfo("Change Successful", "Your password has been reset.")
                            else:
                                messagebox.showinfo("Change Unsucessful", "Your cancelled the reset.")
                        else:
                            messagebox.showerror("EasiStock - Error", "Your new password must be more than 8 Characters.")       
                    else:
                        messagebox.showerror('EasiStock - Error', "Please include special characters. (! % £ #)")
                else:
                    messagebox.showerror('EasiStock - Error', "This password is too weak, try to include random letters and special characters.") 
            else:
                messagebox.showerror('EasiStock - Error', "Cannot use the same password, please enter a new one.")
        if re != old :
            messagebox.showerror('EasiStock - Error', "Passwords do not match, please re-type password.")
    if old != pass_e:
        messagebox.showerror('EasiStock - Error', "Incorrect password.")

def reset_place():
    global pass_e
    LogoLabels(resetPass, settings, "Reset Password.")
    tooltip = tk.Label(resetPass, text = "Please enter your current password, then your new one. \nDo not use common names or things that are easy to guess." , font = ("Tw Cen MT", 15))
    tooltip2 = tk.Label(resetPass, text = "Your new password must be more than 8 Characters and include special characters (!, #, £, @) " , font = ("Tw Cen MT", 15), fg= "red")
    tooltip.place(x=270, y = 130)
    tooltip2.place(x = 145, y = 400)
    global  re_pass_e
    global new_pass_e
    global old_pass_e
    
    old_pass = tk.Label (resetPass, text ="Old Password")
    old_pass_e = tk.Entry(resetPass, show = "*", relief = "groove", width = 24)
    re_pass = tk.Label (resetPass, text ="Retype Password")
    re_pass_e = tk.Entry(resetPass, show = "*", relief = "groove", width = 24)
    
    old_pass_e.place(x=426, y=230)
    old_pass.place(x=338, y=228)
        
    re_pass.place(x=320, y=258)
    re_pass_e.place(x=426, y=260)

        
    new_pass= tk.Label (resetPass, text = "New Password")
    new_pass_e = tk.Entry (resetPass, show="*", relief = "groove", width = 24)

    
    cont = tk.Button(resetPass, text = "Continue", height = 1, width = 20, activebackground ='grey', relief = "groove", command = lambda: [resetCheck(new_pass_e.get(), re_pass_e.get(), old_pass_e.get())])


    new_pass.place(x=333, y=290)
    new_pass_e.place(x=426, y=290)
    cont.place(x=425, y=315)


def settings_log():
    settings.withdraw()
    confirm = messagebox.askyesno('EasiStock - Log Out', "Are your sure you'd like to log out?")
    if confirm == True:
        Login.deiconify()

    if confirm == False:
        settings.deiconify()
        

    
reset_place()
settings_place()
Disclaimer(settings, True)
Disclaimer(Login, True)
Disclaimer(MainMenu, True)


# ==============================================================================> \/ DB Check

if db_exists == False:
    def leave():
        exit()

    error_no_db = tk.Label(NoDB, text = 'Sorry, No Database Exists.', font = ("Tw Cen MT", 30))
    error_no_db2 = tk.Label(NoDB, text = "Please create one in the EasiStock Control Panel.")
    leave = tk.Button (NoDB, text = 'Exit', font =("Calibri Bold", 15), relief = "groove", height = 2, width = 9, activebackground = "red", command = leave)

    error_no_db.place(x = 33 , y = 50)
    error_no_db2.place(x = 115 , y = 95 )
    leave.place(x = 190 , y = 130)
    NoDB.deiconify()

#command=lambda:[magic1(x), magic2(),magic3()
# ==============================================================================> /\ DB Check

# ============================================================================== > \/ MAIN MENU
# This is simple page 1, but is where all the product placement automation was
# designed, so spans for lines and lines, if my code goes right, the ABP
# shoulld theoretically be able to spit out new pages just from the
# main menu, which leads to there just being a few windows, then
# a bunch of temporary pages to store data more than 10 places
# into the SQLite3 Database.

# ========================================================== > \/ ABP Product Selection
global count
count = 0
    
def select(index):
        global x_ord
        global count
        global y_ord
        global full
        global numbers
        global results
        global num
        global name
        global stock
        global exception
        global failed
        global first
        global button_count
        print(" --- ABP: Querying Data. Query value: ", index, " ---  ")
        try: # FIRST TRY
                #print("INDEX ", index)
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index])
                num = str(c.fetchone()[0])
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index])
                name = str(c.fetchone()[1])
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index])
                stock = str(c.fetchone()[2])
                print(" Query Successful, ")
                button_count = button_count + 1
                print("Data found: \nID =", num, "Name:", name, "\n")
                
                #print(str(c.fetchall()))
        except:
            print("Query Failed, Incrementing Params and Recalling.\n")
            numbers = numbers + 1
            #results = results - 2
            select(numbers)
            

                        

# ========================================================== > /\ ABP Product Selection
# ============================================================================== > \/ Main Menu Standard Widgets

def Main(page_place):
    global user_e
    global pass_e
    global num
    global name
    global stock
    global product_place
    global page
    global button_count
    global stk_pg
    global ht
    global loaded
    global check
   ### print(user_e)
    ###print("main") # x y z
    MainMenu.withdraw()
    Loading.deiconify()
    c.execute('''SELECT * FROM Users WHERE user = ? AND pass = ?''', [user_e, pass_e])
    first_name = c.fetchone()[1]
    c.execute("SELECT * FROM Products")
    global results
    results = len(c.fetchall())
    ###print(results, "LENGTH")
    
    logo = tk.Label(page_place, text = "EasiStock.", font=("Tw Cen MT", 34))
    welcome = tk.Label(page_place, text = ("Welcome, " + first_name + "."), font=("Tw Cen MT", 12))

# ========================================================== > /\ Main Menu Standard Widgets
# ========================================================== > \/ ABP Pre-Req Functions and Variables
    
    global numbers
    global x_ord
    global y_ord
    global first
    global full
    global exception
    global limit
    global row
    numbers = 0
    x_ord = 10
    y_ord = 20
    first = True
    full = False
    pause = False
    exception = False

    def edit():
        edit_pg = tk.Tk()

        w = 1000
        h = 600
        ws = Login.winfo_screenwidth()
        hs = Login.winfo_screenheight()
        x = (ws/2)-(w/2)
        y = (hs/2)-(h/2)

        edit_pg.iconbitmap('Logo Compact+.ico')
        edit_pg.geometry('%dx%d+%d+%d' % (w, h, x, y))
        edit_pg.title("EasiStock - Edit Product")

        ConstantButtons(edit_pg)

    def dis(k):
            found = False
            ###print(str(k))
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            num = str(c.fetchone()[0])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            name = str(c.fetchone()[1])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            stock = str(c.fetchone()[2])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            price = str(c.fetchone()[3])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            desc = str(c.fetchone()[4])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            date_created = str(c.fetchone()[5])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            date_updated_d = str(c.fetchone()[6])
            c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
            date_updated_t = str(c.fetchone()[7])
            
            day = date_updated_d[0] + date_updated_d[1]
            month = date_updated_d[3] + date_updated_d[4]
            year = date_updated_d[6] + date_updated_d[7]

            hour = date_updated_t[0] + date_updated_t[1]
            minute = date_updated_t[2] + date_updated_t[3]


            update_text = date_updated_d + ",\n" + date_updated_t
            
            if date_updated_d == today.strftime("%d/%m/%y"):
                if hour == today.strftime("%H"):
                    update_text = "A few minutes ago"

                else:
                    update_text = "Today,\n" + date_updated_t

            window_name = "EasiStock - ID: " + num + " | Product: " + name
            prod1=tk.Tk()

            w = 1000
            h = 600
            ws = Login.winfo_screenwidth()
            hs = Login.winfo_screenheight()
            x = (ws/2)-(w/2)
            y = (hs/2)-(h/2)

            prod1.iconbitmap('Logo Compact+.ico')
            prod1.geometry('%dx%d+%d+%d' % (w, h, x, y))
            prod1.title(window_name)

            frme = Frame(prod1, height = 420, width = 945, bg = "light grey") #1st frame (light grey)
            frme2 = Frame(frme, height = 220, width = 800, bg = "grey") # 2nd 
            stock_f = Frame(frme2, height = 50, width = 400, bg = "white")
            stock_p = Frame(frme2, height = 50, width = 370, bg = "white")
            stock_d = Frame(frme2, height = 140, width = 470, bg = "white")


            frme['borderwidth']=3
            frme2['borderwidth']=3
            stock_f['borderwidth']=1
            stock_p['borderwidth']=1
            stock_d['borderwidth']=1
            
            frme['relief'] = 'groove'
            frme2['relief'] = 'groove'
            stock_f['relief'] = 'groove'
            stock_p['relief'] = 'groove'
            stock_d['relief'] = 'groove'
            
            frme.place(x=25,y=100)
            frme2.place(x = 55, y = 130)
            stock_f.place(x=9, y=8)
            stock_p.place(x = 415, y = 8)
            stock_d.place(x=175, y=65)

            lb1 = Label (frme, text = "ID:" + num, font = ("Tw Cen MT", 45), bg = "light grey")
            lb2 = Label (frme, text = "Name: " + name, font = ("Tw Cen MT", 30), bg = "light grey")
            stck = Label (stock_f, text = "Stock: " + stock, font = ("Tw Cen MT", 25), bg = "white")
            prce = Label (stock_p, text = "Price: " + price, font = ("Tw Cen MT", 25), bg = "white")
            dsc_anno = Label(frme, text = "Notes:", font = ("Tw Cen MT", 25), bg = "grey")
            
            dsc = Label (stock_d, text = desc, font = ("Calibri", 10), bg = "white", wraplengt= 460)
            dt_creation = Label (frme, text = "Date Created: " + date_created, font = ("Tw Cen MT", 15), bg = "light grey")
            dt_up = Label (frme, text = "Last Updated: ", font = ("Tw Cen MT", 15), bg = "light grey")
            dt_up_date = Label (frme, text= update_text, font = ("Tw Cen MT", 15), bg = "light grey", anchor = 'w', wraplengt = 110)

            del_prod = Button(prod1, text = "Delete", bg = "light grey", height = 4, width = 30, relief ="groove", command = lambda: messagebox.showinfo("WIP", "Work in Progress"))
            edt_prod = Button(prod1, text = "Edit", bg = "light grey", height = 4, width = 30, relief ="groove", command = lambda: messagebox.showinfo("WIP", "Work in Progress"))
            
            
            ConstantButtons(prod1)
            LogoLabels(prod1, MainMenu, "View Mode.")
            lb1.place(x=414, y = 3 )
            lb2.place(x=300, y = 62 )
            stck.place(x=2, y = 2)
            prce.place(x=2, y = 2 )
            dsc.place(x=2, y = 10 )
            dsc_anno.place(x=135, y = 192 )
            dsc.config(anchor = "ne")
            dt_creation.place(x=50, y = 350 )
            dt_up.place(x=630, y = 350 )
            dt_up_date.place(x=750, y = 350 )
            del_prod.place(x = 235, y = 523)
            edt_prod.place(x = 535, y = 523)
            MainMenu.withdraw()

# ========================================================== > /\ ABP Pre-Req Functions and Variables
# ========================================================== > \/ Automated Button Placement [ABP] (SmartVar >:))

    for x in range(1, results + 1):
        print("\nRESULTS LOOP VAL = ", results, "\n")
        numbers = numbers + 1
        check = check + 1
        ld_bt()
        ###print(results, "IN FORX")
        #print(numbers)
        select(numbers)
        ####print("real id", num, "\n \n")

        if len(name) >15:
                name = name [:10] + "..."
        if len(str(stock)) >5:
                stock = str(stock)[:5] + "..."

        mybutton = tk.Button(frame, text = num + "\n\nName: \n" + name + "\n\n Stock: " + stock, font=("Tw Cen MT", 12), relief = "groove", height = 7, width = 15, background = 'white', command = lambda k = num : dis(k))
        print("BUTTON COUNT IN MAIN FUNCTION ===== ", numbers)
                
        if full == True:
                y_ord = y_ord + 200
                first = True
                x_ord = 10
                full = False
                pause = True
        if full == False:
                if first == False:
                        x_ord = x_ord + 190
                if first == True:
                        first = False
                        x_ord = x_ord + 14

        if check >4 or check == 5:
            pause = False
                        
        if button_count >4:
            button_count = 0
            if pause == False:
                row = row + 1
                if row >3: #600 (default) is for 3 rows, so there's no point adding more than 300 pixels
                    ht = ht + 200
                    canvas.config(height = ht)
                    frame.config(height = ht)
            full = True
        mybutton.place(x=x_ord, y=y_ord)
        print("Button has been placed, in X = ", x_ord, " and Y = ", y_ord)
        if numbers == results - 1:
            loaded = True

    Loading.withdraw()
        
    logo.place(x=405,y=1)
    welcome.place(x=410, y=46)
    ConstantButtons(MainMenu)
    MainMenu.deiconify()
    settings.withdraw()
    
# ==============================================================================> /\ MAIN MENU

# ==============================================================================> \/ Login

if db_exists == True: # if DB already exists, connect to it,
    conn = sqlite3.connect("EasiStock_Database.db") # if it didnt exist it would create one [bad]
    c = conn.cursor()

    logo = tk.Label(Login, text = "EasiStock", font=("Tw Cen MT", 64))
    stock_done = tk.Label(Login, text ="Stock Done", font=("Tw Cen MT", 20))
    fast = tk.Label(Login, text ="Fast.", font=("Tw Cen MT", 20), fg="red")
    instructions = tk.Label(Login, text = "Please enter your Username and Password.")

    user_label = tk.Label (Login, text ="Username")
    user = tk.Entry(Login)
    pass_label = tk.Label (Login, text = "Password")
    password = tk.Entry (Login, show="*", relief = "groove")           

    def pass_check():
            global pass_e
            global txt
            b = open('weak_pass.txt')
            txt = b.read()
            if pass_e in txt:
                    warning = tk.Label(MainMenu, text = "       We've detected your password is weak, \nwe recomend you change it in the settings.", font = ("Calibri", 8), foreground = "red", anchor="w")
                    warning.place(x = 690, y = 20)
                    weak = True

    def db_login_check():
           incorrect = False # state check for redundancy
           special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬" # a "do not allow" list for input
           global user_e
           global pass_e
           user_e = user.get() # gets the input of the entries 
           pass_e = password.get()
           c.execute('''SELECT * FROM Users WHERE user = ? AND pass = ?''', [user_e, pass_e])
           sel = c.fetchall()
           ###print (len(sel)) # xyz # debug info
           ###print(sel)
           #print(first_name)

           if any(c in special_char for c in user_e): # special char check
               incorrect = True # prevents ES from checking for other errors
               messagebox.showwarning("Invalid Input", "You cannot use special characters in your username, please try again.") # pop up window
               password.delete(0, 'end') # clears the entry data
               user.delete(0, 'end')
               
           if incorrect == False: # if passes special char check
               if (len(sel)) == 1: # if input returns any result
                   global logged_in
                   logged_in = True
                   ###print("found record") # xyz
                   user.delete(0, 'end')
                   password.delete(0, 'end')
                   pass_check()
                   Login.withdraw()
                   #MainMenu.deiconify()
                   if loaded == True:
                       print("ALREADY LOADED =====================================================")
                       MainMenu.deiconify()
                       
                   if loaded == False:
                        print("NOT LOADED, LOADING... ================================================")
                        Main(MainMenu)
                        Disclaimer(MainMenu, True)

               if (len(sel)) == 0:
                   ###print("found nuttin") # xyz
                   messagebox.showerror("Error", "The User or Password is incorrect, please try again.")
                   password.delete(0, 'end')
                   user.delete(0, 'end')

    def event(event):
        db_login_check()

    Login_bt = tk.Button(Login, text = "Login", height = 1, width = 20, activebackground ='grey', relief = "groove", command = db_login_check)
    Login.bind('<Return>', event)

    logo.place(x=340,y=100)
    stock_done.place(x=405, y=190)
    fast.place(x=534, y=190)
    user.place(x=438, y=260)
    user_label.place(x=376, y=258)
    password.place(x=438, y=290)
    pass_label.place(x=376, y=290)
    Login_bt.place(x=425, y=315)

    Login.deiconify()

# ==============================================================================> /\ Login


