### main indents = 80 col |  sub indents = 60 col |  description = 83 col (text) ###
import tkinter as tk
#from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import os.path
import sqlite3
import smtplib
import random
from os import system
import asyncio
import datetime
import time
import webbrowser
import socket
import json
from urllib.request import urlopen
from datetime import datetime
global loaded

global d1
global d2
global d3
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

print (d3, d2)

NoDB = tk.Tk()
Login=tk.Tk()
MainMenu=tk.Tk()
settings = tk.Tk()
resetPass = tk.Tk()
global edit_pg
edit_pg = tk.Tk()
faq = tk.Tk()
edit_faq = tk.Tk()
Lockout = tk.Tk()

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
edit_pg.geometry('%dx%d+%d+%d' % (w, h, x, y))
NoDB.geometry('500x280')
settings.geometry('%dx%d+%d+%d' % (w, h, x, y))
resetPass.geometry('%dx%d+%d+%d' % (w, h, x, y))
faq.geometry('%dx%d+%d+%d' % (w, h, x, y))
edit_faq.geometry('%dx%d+%d+%d' % (w, h, x, y))
Lockout.geometry('500x280')

NoDB.title("ERROR")
Loading.title("Loading, please wait.")
MainMenu.title("EasiStock v1.5.13.3")
Login.title("EasiStock - Please Log In")
settings.title("EasiStock v1.5.13.3 -  Settings")
edit_pg.title("EasiStock - Edit Product")
resetPass.title("EasiStock v1.5.13.3 -  Reset Password")
faq.title("EasiStock - Questions & Help")
edit_faq.title("EasiStock - Questions & Help | Editing / Creating Conditions")
Lockout.title("ERROR")

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
faq.resizable(0, 0)
edit_faq.resizable(0, 0)
Lockout.resizable(0, 0)
Loading.resizable(0, 0)
MainMenu.resizable(0, 0)

NoDB.withdraw() 
Login.withdraw()
Loading.withdraw()
MainMenu.withdraw()
settings.withdraw()
resetPass.withdraw()
edit_pg.withdraw()
faq.withdraw()
edit_faq.withdraw()
Lockout.withdraw()

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
def ld_bt():
    print("")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def get_ip(addr=''):
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    city = data['city']
    country=data['country']
    region=data['region']

    ip = ('IP : {3} \nRegion : {0} \nCountry : {1} \nCity : {2}'.format(region,country,city,IP))
    return ip

gmail_user = 'easistudios@gmail.com'
gmail_password = 'F@=UrGd4b&k!C6y+'

def send_email(to, subject, body, method):
    rand_int = random.randint(1111,99999)
    #to = recipient
    #if method == "lock":
        #print("Lockout email preset chosen.")
        #subject = 'EasiStock - Unusual Login Activity'
        #body = "Hello, \nThere has been multiple login attempts to your EasiStock Account at " +  str(current_time) + ", Today. Shown below is the location of the login attempt: \n\n" + get_ip() + "\n\nIf you'd like to change your password, please click forget password (WIP) on the EasiStock program and you will be sent a OTP (One-Time-Password) to change your password. \n\nBest Regards, \nEasiStock."
    try:
        gmail_user = 'easistudios@gmail.com'
        gmail_password = 'F@=UrGd4b&k!C6y+'
        sent_from = gmail_user

        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
 
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)

global to
global subject
global body
global sent_from
global email_txt
to = ['null']
subject = "null"
body = "null"
sent_from = gmail_user


def settings_reset():
    settings.withdraw()
    resetPass.deiconify()

def Disclaimer(index, win):
        #print("Creating Disclaimer buttons with Index:", index)
        version = tk.Label ((index), text = "ES v1.5.13.3 DEV BUILD", font = ("Helvetica", 9))
        disclaimer = tk.Label ((index), text = "Content shown in the dev build may not work as expected.", font = ("Helvetica", 9, "italic"))
        #print("Disclaimers have been created.")
        if win == True:
            version.place(x=4, y=580)
            disclaimer.place (x=345, y= 580)

        if win == False:
            version.place(x=4, y=250)
            disclaimer.place (x=230, y= 250)
        #print("Dislaimers have been placed.")

def LogoLabels(current, before, tooltip):
    logo = tk.Button(current, text = "EasiStock.", borderwidth = 0, font=("Tw Cen MT", 34), width =44, command = lambda:[current.withdraw(), before.deiconify()])
    welcome = tk.Label(current, text = tooltip, font=("Tw Cen MT", 20))
    feedback = Label(current, text = "Provide Feedback Here!", fg="blue", cursor="hand2")
    feedback.pack()
    feedback.bind("<Button-1>", lambda e: webbrowser.open_new("https://forms.office.com/r/qaeHHjwvZq"))
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
        b1 = tk.Button(current, text="Page 1", activebackground ='grey', height = 1, relief = "groove", width = 5, command = lambda:[current.withdraw(), MainMenu.deiconify()]) # creates button to reference page

        settings_bt.place(x=900,y=10)
        #b1.place(x=25,y=15)
        print("Constant Widgets placed, testing APC")

def lockout_place():
    def leave():
        exit()
    error_lock = tk.Label(Lockout, text = 'LOCKED OUT.', font = ("Tw Cen MT", 30))
    error_lock2 = tk.Label(Lockout, text = "You have reached 5 tries and been locked out.")
    leave = tk.Button (Lockout, text = 'Exit', font =("Calibri Bold", 15), relief = "groove", height = 2, width = 9, activebackground = "red", command = leave)

    error_lock.place(x = 120 , y = 50)
    error_lock2.place(x = 115 , y = 95 )
    leave.place(x = 190 , y = 130)

            
def settings_place():
    print("if u see this its too late")
    LogoLabels(settings, MainMenu, "Settings Menu.")
    faq_bt = Button(settings, text = "Help", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", width = 15, borderwidth = 1, command = lambda: [settings.withdraw(), faq.deiconify()])
    pass_change = Button(settings, text = "Change Password", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", borderwidth = 1, command = lambda: [settings.withdraw(), resetPass.deiconify()])
    if weak == True:
        pass_change.config(bg = "green")

    log_out = Button(settings, text = "Log Out", font = ("Tw Cen MT", 25), relief = "groove", bg = "light grey", width= 15, borderwidth = 1, command = settings_log)

    faq_bt.place(x=376, y= 125)
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
    global re_pass_e
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

def Edit_FaQ():
    LogoLabels(edit_faq, faq, "Editing and Creating")
    print("WIP")
    frame = Frame(edit_faq, bg = "light grey", height = 450, width = 600, relief = "groove", borderwidth = 3)
    frame.pack(side = RIGHT, pady= 100, padx = 50)
    frame2 = Frame(edit_faq, bg = "light grey", height = 450, width = 600, relief = "groove", borderwidth = 3)
    frame2.pack(side = LEFT, pady= 100, padx = 100) # change this back to 50 when continuing to Final

    q1 = Label(frame, text = "Editing", font = ("Calibri", 30, "bold"), wraplength = 800, bg = "light grey")
    q2 = Label(frame, text = "NAME: \n1:Cannot be the same as your previous name. \n\n PRICE: \n1: Cannot use special characters. \n2: Cannot use letters. \n3: Must be in the following format - Pound / Pennies. \nExample: 12 = £12.00 | 12.1 OR 12.10 = £12.10 | .99 OR 00.99 OR 0.99 = £00.99. \n\DESCRIPTION: \n1: Input cannot be more than 500 characters. \n\n STOCK: \n1: Cannot use special characters (!£$?/_). \n2: Cannot use letters (ABC).  ", wraplength = 800, bg = "light grey")
    q3 = Label(frame2, text = "Creating", font = ("Calibri", 30, "bold"), wraplen = 800, bg = "light grey")
    q4 = Label(frame2, text = "How do I add products? \nThis is a feature coming very soon.", wraplength = 800, bg = "light grey")
        
    q1.pack(side = TOP, pady = 1)
    q2.pack(side = TOP, pady = 5)
    q3.pack(side = TOP, pady = 10)
    q4.pack(side = TOP, pady = 5)

def FaQ_place():
    LogoLabels(faq, settings, "Help & Questions.")
    frame = Frame(faq, bg = "light grey", height = 450, width = 600, relief = "groove", borderwidth = 3)
    frame.pack(side = TOP, pady= 100)

    q1 = Label(frame, text = "How do I add products? \nThis is a feature coming very soon.", wraplength = 800, bg = "light grey")
    q2 = Label(frame, text = "How do I delete products? \nSimply click on any product you'd like to delete and there will be a delete button at the bottom of all the data, confirm the deletion and the product will be deleted.", wraplength = 800, bg = "light grey")
    q3 = Label(frame, text = "How do I edit products? \nClick on the product you desire to edit, at the bottom of the view page near to the delete button there is an edit option that you can click on. When editing, please follow the conditions to you input.", wraplength = 800, bg = "light grey")
    q4 = Label(frame, text = "What are the edit rules? \nNames cannot be the same as their old ones, Price must be properly formatted and all data must meet a character limit. Read more about edit and creation rules by clicking on this text.", wraplength = 800, bg = "light grey", cursor = "hand2")
    q4.bind("<Button-1>", lambda e: [faq.withdraw(), Edit_FaQ(), edit_faq.deiconify()])
    q5 = Label(frame, text = "I keep getting er11 in Editing, how do I fix this? \nEasiStock pre-loads the entries with your old details, if you don't want to change something, do not enter the old value - just delete the old values and keep it blank. EasiStock will ignore it and only input the data present.", wraplen = 800, bg = "light grey")
    q1 = Label(frame, text = "How do I add products? \nThis is a feature coming very soon.", wraplength = 800, bg = "light grey")
        
    q1.pack(side = TOP, pady = 10)
    q2.pack(side = TOP, pady = 10)
    q3.pack(side = TOP, pady = 10)
    q4.pack(side = TOP, pady = 10)
    q5.pack(side = TOP, pady = 10)

FaQ_place()    
reset_place()
settings_place()
Disclaimer(settings, True)
Disclaimer(faq, True)
Disclaimer(edit_pg, True)
Disclaimer(Login, True)
Disclaimer(MainMenu, True)
lockout_place()


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

def query(val, index):
    c.execute('''SELECT * FROM Products WHERE product_id = ?''', [val])
    return str(c.fetchone()[index])

def Main(page_place, after_del):
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
    #if len(str(c.fetchall())) >1:
    first_name = str(c.fetchone()[1])
    c.execute("SELECT * FROM Products")
    global results
    results = len(c.fetchall())
    ###print(results, "LENGTH")
    
    logo = tk.Label(page_place, text = "EasiStock.", font=("Tw Cen MT", 34))
    welcome = tk.Label(page_place, text = ("Welcome, " + first_name + "."), font=("Tw Cen MT", 12))
    refresh = Button(MainMenu, text = "⟳", font = ("Tw Cen MT", 15), bg = "light grey", width = 3, command = lambda: Main(MainMenu, False))
    refresh.place(x = 480, y = 530 )

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
    button_count = 0
    x_ord = 10
    y_ord = 20
    first = True
    full = False
    pause = False
    exception = False

    def price_format(entry, db): # ================================== Price Formatting Function
        try:
            if len(entry.get()) == 0:
                return ("Please Enter Price.")
        except:
            try:
                if len(entry) == 0:
                    return ("Please Enter Price.")
            except:
                return("Presence Error")

        try:
            try:
                frm_flt = "£{:,.2f}".format(float(entry.get()))
            except ValueError:
                return("Already Formatted")
        except:
            try:
                frm_flt = "£{:,.2f}".format(float(entry))
            except ValueError:
                return("Already Formatted")
        frm_flt_out = "Null"
        if len(frm_flt) >15:
            frm_flt_out = frm_flt [:15] + "..."
        else:
            frm_flt_out = frm_flt
        if db == True:
            return frm_flt
        else:
            return frm_flt_out
            
        #except:
            #return ("Unknown Error")

    def edit(k): # ================================================= > Editing Page

        prod1.withdraw()

        frme = Frame(edit_pg, height = 420, width = 945, bg = "light grey") #1st frame (light grey)
        frme2 = Frame(frme, height = 300, width = 800, bg = "grey") # 2nd
        
        stock_f = Entry(frme2, font = ("Tw Cen MT", 20), bg = "white", relief = "groove")
        stock_p = Entry(frme2, font = ("Tw Cen MT", 20), bg = "white", relief = "groove")
        stock_n = Entry(frme2, font = ("Tw Cen MT", 20), bg = "white", relief = "groove")
        desc = Text(frme2, font = ("Calibri", 10))
        desc.insert(END, query(k,4))
        stock_f.insert(END, query(k,2))
        stock_p.insert(END, query(k,3)[1:])
        stock_n.insert(END, query(k,1))
        
        stock_d = Frame(frme2, height = 220, width = 320, bg = "white")
        before = Frame(edit_pg, height = 40, width = 945, bg = "light grey", relief = "groove", borderwidth=3)
        before_text = "Product Selected:  ID = " + query(k, 0) + "  ||  Name = " + query(k, 1) + "  ||  Stock = " + query(k,2) + "  ||  Price = " + query(k,3)
        before_l = Label(before, text = before_text, bg = "light grey", justify = 'center')

        desc_e = desc.get("1.0", END)
        stock_e = stock_f.get()
        price_e = stock_p.get()


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

        stock_L = Label (frme2, text = "Stock:", font = ("Tw Cen MT", 25), bg = "grey")
        price_L = Label (frme2, text = "Price:", font = ("Tw Cen MT", 25), bg = "grey")
        desc_L = Label (frme2, text = "Description:", font = ("Tw Cen MT", 25), bg = "grey")
        name_L = Label(frme2, text = "Name:", font = ("Tw Cen MT", 25), bg = "grey")
            
        price_F = Label(frme2, text = "Waiting...", font = ("Tw Cen MT", 25), bg = "grey", wraplen = 290)
        price_FB = Button (frme2, text = "Format", font = ("Tw Cen MT", 25), bg = "light grey", command = lambda: price_F.config(text = price_format(stock_p, False)))
            
        confirm = Button(frme, text = "Save", font = ("Tw Cen MT", 25), width = 10, height = 1, bg = "grey", command = lambda: edit_check(k, desc.get("1.0", END), stock_f.get(), stock_p.get(), stock_n.get()))
            
        frme.place(x=25,y=100)
        frme2.place(x = 55, y = 30)
        
        stock_f.place(x=120, y=115)
        stock_L.place(x=20, y=105)
        
        stock_p.place(x = 120, y = 180)
        price_L.place(x=20, y = 165)
        
        #stock_d.place(x=450, y=50)
        desc_L.place(x= 540, y = 2)
        desc.place(x=450, y=50, height = 230, width = 320)

        name_L.place(x = 20, y = 50)
        stock_n.place(x = 120, y = 50)

        confirm.place(x = 395, y = 335)
        price_FB.place(x = 20, y = 232, height = 50)
        price_F.place(x=150, y = 232)

        before.place(x = 25, y = 530)
        before_l.pack( expand = False)

        LogoLabels(edit_pg, prod1, "Edit.")
        edit_pg.deiconify()

    def edit_check(k, desc, stock, price, name): # =========================================================== Product Editing Input Checks
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        name_db = str(c.fetchone()[1])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        stock_db = str(c.fetchone()[2])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        price_db = str(c.fetchone()[3])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        desc_db = str(c.fetchone()[4])

        #print(mybutton.winfo_rootx(), mybutton.winfo_rooty())

        errors = 0
        price_in = price_db
        desc_error = False
        stock_error = False
        price_error = False
        
        print("DSC", desc, "STK", stock, "PRC", price)

        price_val = "N/A"
        stock_val = "N/A"
        desc_val = "N/A"
        name_val = "N/A"
        
        er01 = "Invalid stock input, please enter a number, not a letter/s.  Error Code = er01"
        
        er02 = "Invalid price format, cannot use special characters (!'@:%^&*).  Error Code = er02"
        er03 = "Invalid price format, cannot use letters (ABC).  Error Code = er03"
        er04 = "Invalid price format, please input in the following format. 12.99 (£12.99) or 4.2 (£4.20).  Error Code = er04"
        er05 = "Inavlid price format, cannot use letters (ABC) or special characters (!'@:%^&*).  Error Code = er05"
        
        er07 =  "Invalid Description input, input is too long (Maximum = 500 Characters) \nYour character count = ", str(len(desc)) + ".  Error Code = er07"

        er08 = "Invalid stock input, cannot use letters (ABC).  Error Code = er08"
        er09 = "Invalid stock input, cannot use special characters (!'@:%^&*).  Error Code = er09"
        er10 = "Inavlid stock input, cannot use letters (ABC) or special characters (!'@:%^&*).  Error Code = er10"

        er11 = "Invalid name input, cannot use previous name.  Error Code = er11"

        forbidden_S = "!@#%^&*()-+?_=,<>/{}[]:;`¬"
        forbidden_A = "abcdefghijklmnopqrstuvwxyz"

        def char_check(val, errors):
            if errors ==0:
                if any(c in forbidden_S for c in val) and any(c in forbidden_A for c in val):
                    errors = errors + 1
                    return 1

                else:
                    if any(c in forbidden_S for c in val):
                        errors = errors + 1
                        return 2

                    if any(c in forbidden_A for c in val):
                        errors = errors + 1
                        return 3

        if len(stock) == 0:
            print("skipped stock")
            stock = stock_db
        else:
            if errors ==0:
                if char_check(stock, errors) == 1:
                    stock_val = er010
                elif char_check(stock, errors) == 2:
                    stock_val = er09
                elif char_check(stock, errors) == 3:
                    stock_val = er08
        

        if len(price) == 0:
            print("skipped price")
            price_in = price_db
        else:
            if errors ==0:
                if char_check(price, errors) == 1:
                    price_val = er05
                    price_in = price_db
                elif char_check(price, errors) == 2:
                    price_val = er02
                    price_in = price_db
                elif char_check(price, errors) == 3:
                    price_val = er03
                    price_in = price_db
                if price_format(price, False) == "Unknown Error" or price_format(price, False) == "Presence Error":
                    errors = error + 1
                    price_val = er04
                
                    
                    
        if len(desc) == 0:
            print("skipped desc")
            desc = desc_db
        else:
            if len(desc) >= 500:
                desc_error = True
                errors = errors + 1
                desc_val = er07
                print("error + 1 (er06)")

        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        old = str(c.fetchone()[1])

        if len(name) == 0:
            print("skipped name")
            name = name_db
        else:
            if name == old:
                print("NAME ERROR")
                errors = errors + 1
                name_val = er11
                
        #if errors == 1:
        err_txt = "Please correct an error: \n\nPrice:\n " + str(price_val) + "\n\nStock: \n" + str(stock_val) + "\n\nDescription: \n" + str(desc_val) + "\n\nName: \n" + str(name_val)

        #if errors > 1:
          #  err_txt = "Please correct the following errors: \n\nPrice: \n" + str(price_val) + "\n\nStock: \n" + str(stock_val) + "\n\nDescription: \n" + str(desc_val) + "\n\nName: \n" + name_val

        if len(desc) ==0 or len(price) ==0 or len(stock) ==0 or len(name) == 0:
            messagebox.showinfo("EasiStock", "No changes have been made.")
            edit_pg.withdraw()
            prod1.deiconify()

        else:
            if errors == 0:
                confirm = messagebox.askyesno("EasiStock - Save?", "All data is valid. \nAre you sure you'd like to save?")
                if confirm == True:
                    c.execute('''SELECT * FROM Users WHERE user = ?''', (user_e,))
                    user = c.fetchone()[0]
                    print(user)
                    print("NME:", name, "\nDSC", desc, "\nSTK", stock, "\nPRC", price)
                    
                    #print("name:", name, "\nstock:", stock, "\nprice:", price, "\nday", d2, "and time", d3)
                    frm_flt = "£{:,.2f}".format(float(price))
                    print(frm_flt)
                    c.execute('''UPDATE Products SET
                                                product_name = ?,
                                                product_count = ?,
                                                product_price = ?,
                                                product_desc = ?,
                                                last_change_day = ?,
                                                last_change_time = ?,
                                                last_change_user = ?
                                                WHERE product_id = ?''', (name, stock, frm_flt, desc, d2, d3, user, k))
                    conn.commit()
                    loaded = False
                    messagebox.showinfo("EasiStock - Changes Made", "Changes have been made. Press OK to load products.")
                    edit_pg.withdraw()
                    Loading.deiconify()
                    Main(MainMenu, False)
                    if loaded == False:
                        MainMenu.deiconify()

                    

                if confirm == False:
                    edit_pg.withdraw()
                    prod1.deiconify()

            else:
                messagebox.showerror("EasiStock - Error", err_txt)
            
    def del_prod(k):
        global after_del
        #global mybutton
        confirm = messagebox.askyesno("EasiStock - Delete?", "Are you sure you'd like to delete this product? All data will be lost.")

        if confirm == True:
            c.execute('''DELETE FROM Products WHERE product_id = ?''', (k,))
            conn.commit()
            loaded = False
            messagebox.showinfo("EasiStock - Changes Made", "This product has been deleted. Press OK to load products.")
            edit_pg.withdraw()
            Loading.deiconify()
            #for x in range (results):
            mybutton.destroy()
            Main(MainMenu, True)
            #if loaded == False:
            c.execute("SELECT * FROM Products")
            results = len(c.fetchall())
            ###print(results, "LENGTH")
            MainMenu.deiconify()

            

        if confirm == False:
            messagebox.showerror("EasiStock", "Deletion Cancelled.")
            

    def dis(k, del_st):
            found = False
            ###print(str(k))
            #print("======================== delete is not ===================")
            if del_st == True:
                print("========================  DELETE IS  ===================")
                k = int(k) + 1

            else:
                print("======================== delete is not ===================")
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
            global prod1
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
            prce = Label (stock_p, text = "Price :" + price, font = ("Tw Cen MT", 25), bg = "white")
            dsc_anno = Label(frme, text = "Notes:", font = ("Tw Cen MT", 25), bg = "grey")
            
            dsc = Label (stock_d, text = desc, font = ("Calibri", 10), bg = "white", wraplengt= 460)
            dt_creation = Label (frme, text = "Date Created: " + date_created, font = ("Tw Cen MT", 15), bg = "light grey")
            dt_up = Label (frme, text = "Last Updated: ", font = ("Tw Cen MT", 15), bg = "light grey")
            dt_up_date = Label (frme, text= update_text, font = ("Tw Cen MT", 15), bg = "light grey", anchor = 'w', wraplengt = 110)

            del_bt = Button(prod1, text = "Delete", bg = "light grey", height = 4, width = 30, relief ="groove", command = lambda: [del_prod(k)])
            edt_bt = Button(prod1, text = "Edit", bg = "light grey", height = 4, width = 30, relief ="groove", command = lambda: [edit(k)])
            
            
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
            del_bt.place(x = 235, y = 523)
            edt_bt.place(x = 535, y = 523)
            MainMenu.withdraw()

# ========================================================== > /\ ABP Pre-Req Functions and Variables
# ========================================================== > \/ Automated Button Placement [ABP] (SmartVar >:))

    try:
        for x in range(1, results + 1):
            mybutton.destroy()

    except:
        print("buttons not found")

    numbers = 0

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

        mybutton = tk.Button(frame, text = num + "\n\nName: \n" + name + "\n\n Stock: " + stock, font=("Tw Cen MT", 12), relief = "groove", height = 7, width = 15, background = 'white', command = lambda k = num : dis(k, after_del))
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
    tries = 0

    logo = tk.Label(Login, text = "EasiStock", font=("Tw Cen MT", 64))
    stock_done = tk.Label(Login, text ="Stock Done", font=("Tw Cen MT", 20))
    fast = tk.Label(Login, text ="Fast.", font=("Tw Cen MT", 20), fg="red")
    instructions = tk.Label(Login, text = "Please enter your Username and Password.")

    def click_me():
        print(val_chk.get())

    #global val_chk
    #val_chk=tk.IntVar()
    #show_password = tk.Checkbutton(Login, text = "Show Password", variable=val_chk, offvalue = 0, onvalue = 1)
    #show_password.pack()
 
    #check_input = tk.Button(Login,text="Click here",command=click_me)
    #check_input.pack()
    
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
           c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
           sel_user = c.fetchall()
           print(sel_user, "USER")
           c.execute('''SELECT * FROM Users WHERE user = ? AND pass = ?''', [user_e, pass_e])
           sel = c.fetchall()

           if any(c in special_char for c in user_e): # special char check
               incorrect = True # prevents ES from checking for other errors
               messagebox.showwarning("Invalid Input", "You cannot use special characters in your username, please try again.") # pop up window
               password.delete(0, 'end') # clears the entry data
               user.delete(0, 'end')
               
           if incorrect == False: # if passes special char check
               if (len(str(sel))) >= 3: # if input returns any result
                   print(str(sel), "THIS IS THE RECORD")
                   global logged_in
                   logged_in = True
                   print("found record") # xyz
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
                        Main(MainMenu, False)
                        Disclaimer(MainMenu, True)

               if (len(sel)) == 0:
                   global tries
                   tries = tries + 1
                   messagebox.showerror("Error", "The User or Password is incorrect, please try again.")
                   password.delete(0, 'end')
                   user.delete(0, 'end')
                   print(sel_user, "USERNAME")
                   if len(sel_user) == 1 and len(sel) == 0:
                       c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
                       sel_name = c.fetchone()[1]
                       print("we got one")
                       if tries == 2:
                           print("found nuttin") # xyz
                           Login.withdraw()
                           subject = 'EasiStock - Unusual Login Activity'
                           body = "Hello " + str(sel_name) + ", \nThere has been multiple login attempts to your EasiStock Account at " +  str(current_time) + ", Today. Shown below is the location of the login attempt: \n\n" + get_ip() + "\n\nIf you'd like to change your password, please click forget password (WIP) on the EasiStock program and you will be sent a OTP (One-Time-Password) to change your password. \n\nBest Regards, \nEasiStock."
                           to = ['joogzj@gmail.com']
                           send_email(to, subject, body, "lock")
                           Lockout.deiconify()

                           
                   else:
                       if tries == 5:
                           Login.withdraw()
                           Lockout.deiconify()

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


