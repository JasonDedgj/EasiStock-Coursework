### main indents = 80 col |  sub indents = 60 col |  description = 83 col (text) ###
# xyz = Dev Build Only, delete these on public Builds

# ========== ANNOTATION INFO ==========
# Whilst I will try to annotate everything, some
# things may have been pasted from other sources.
# I will try to explain them, but if I cannot I willl use
# the comment "Foreign Code" to signify its use.

# ==============================================================================> \/ IMPORT MODULES ====

import tkinter as tk # ========== For GUIs
from tkinter import ttk #
from tkinter import messagebox #
from tkinter import * #
import os.path # For checking files exist
import sqlite3 # For DB
import smtplib # For Emailing System (Uses SMTP Protocol)
import random # For Code Generation System (Emails)
from os import system
import asyncio # Not Needed
import random # Not Needed
import datetime # For Date Related data
import time # Not Needed
import webbrowser # For IP (Pings IP Website for Details)
import socket # Part of Emailing System
import json # Part of Emailing System
from urllib.request import urlopen # Part of IP System
from datetime import datetime # Not Needed
import bcrypt # For Hashing

# ==============================================================================> /\ IMPORT MODULES ====
# ==============================================================================> \/ DB Variable Pre-Req ====

global loaded
global d1
global d2
global d3
global weak
global special_char
weak = False # For Weak Passwords (in weak_pass.txt)
today = datetime.now()
d1 = today.strftime("%d/%m/%y") # Creates DD/MM/YYY variable
d2 = today.strftime("%d/%m/%y") # Not Needed ->->->->
d3 = today.strftime("%H : %M : %S") # Creates Hour/Min/Second variable
special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬" # Provides a "do use" list for checking.

Loading = tk.Tk() # Window Creation for Loading Screen

db_exists = os.path.isfile('./EasiStock_Database.db')# Checks if DB exists in root dir
db_exists_P = False # Not Needed
logged_in = False # Variable for if user is logged in or not
loaded = False # Variable for if Products have been loaded, this is how the loading screen appears.
#print(logged_in, "(start of code)") # xyz

print (d3, d2) # xyz

# ==============================================================================> /\ DB Variable Pre-Req ====
# ==============================================================================> \/ Window Creation and Pre-Req ====

NoDB = tk.Tk() # For when No DB is found
Login=tk.Tk() # Login Screen
MainMenu=tk.Tk() # Main Menu Screen
settings = tk.Tk() # Settings Screen
resetPass = tk.Tk() # Reset Password Screen
global edit_pg # Not Needed
edit_pg = tk.Tk() # Editing Products Screen
faq = tk.Tk() # FaQ Screen
edit_faq = tk.Tk() # Deeper FaQ Screen
Lockout = tk.Tk() # Locked Out Screen
create_prd = tk.Tk() # Product Creation Screen

icon = tk.PhotoImage(file = 'Logo Compact+.png') # Sets the file location of the Logo being used
Loading.iconphoto(True, icon) # Universally sets the icon of the WIndow to the Logo
#Loading.iconphoto(True, icon)

w = 1000 # Sets the width of every Window
h = 600 # Sets the length of every Window

ws = Login.winfo_screenwidth() # Gets users Screen Width
hs = Login.winfo_screenheight() # Gets users Screen Height

x = (ws/2)-(w/2) # Finds the center of the users width
y = (hs/2)-(h/2) # Finds the center of the users length

Login.geometry('%dx%d+%d+%d' % (w, h, x, y)) # Sets the size of the screen and always makes the screen sit in the middle.
Loading.geometry('%dx%d+%d+%d' % (1000, 10, x, y))
MainMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
edit_pg.geometry('%dx%d+%d+%d' % (w, h, x, y))
NoDB.geometry('500x280')
settings.geometry('%dx%d+%d+%d' % (w, h, x, y))
resetPass.geometry('%dx%d+%d+%d' % (w, h, x, y))
faq.geometry('%dx%d+%d+%d' % (w, h, x, y))
edit_faq.geometry('%dx%d+%d+%d' % (w, h, x, y))
Lockout.geometry('500x280')
create_prd.geometry('%dx%d+%d+%d' % (w, h, x, y))

NoDB.title("ERROR") # Sets the window title
Loading.title(" Loading, please wait.  ⟳ ")
MainMenu.title("EasiStock v3.10.18.15")
Login.title("EasiStock - Please Log In")
settings.title("EasiStock v3.10.18.15 -  Settings")
edit_pg.title("EasiStock - Edit Product")
resetPass.title("EasiStock v3.10.18.15 -  Reset Password")
faq.title("EasiStock - Questions & Help")
edit_faq.title("EasiStock - Questions & Help | Editing / Creating Conditions")
Lockout.title("ERROR")
create_prd.title("EasiStock - Create a Product.")

Login.config(bg="grey10") # Sets the window background
Loading.config(bg="grey10")
NoDB.config(bg="grey10")
MainMenu.config(bg="grey10")
settings.config(bg="grey10")
edit_pg.config(bg="grey10")
edit_faq.config(bg="grey10")
resetPass.config(bg="grey10")
Lockout.config(bg="grey10")
faq.config(bg="grey10")
create_prd.config(bg="grey10")

# ==========================================================> \/ Scrollbar Function

global ht
ht = 580 # Sets the scroll height for products

def scrollbar(target, w, h): # Foreign Code
    def onFrameConfigure(canvas): # Foreign Code
        '''Reset the scroll region to encompass the inner frame''' # Foreign Code
        canvas.configure(scrollregion=canvas.bbox("all")) # Foreign Code

    global frame
    global canvas
    canvas = tk.Canvas(target, borderwidth=0, background="grey15", width=w, height = ht, relief = "flat", takefocus = 0) # Foreign Code
    frame = tk.Frame(canvas, background="grey15", width=w, height = ht, relief = "flat", takefocus = 0) # Foreign Code
    vsb = ttk.Scrollbar(target, orient="vertical", command=canvas.yview) # Foreign Code
    canvas.configure(yscrollcommand=vsb.set) # Foreign Code

    vsb.pack(side="right", fill="y") # Foreign Code
    canvas.pack(padx=5, pady=80) # Foreign Code
    canvas.create_window((4,4), window=frame, anchor="nw") # Foreign Code

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas)) # Foreign Code

scrollbar(MainMenu, 950, ht) # Foreign Code

# ==========================================================> /\ Scrollbar Function
        
Login.resizable(0, 0) # Makes Window non-rezisable and not maximised 
NoDB.resizable(0, 0)
faq.resizable(0, 0)
edit_faq.resizable(0, 0)
Lockout.resizable(0, 0)
Loading.resizable(0, 0)
MainMenu.resizable(0, 0)
create_prd.resizable(0, 0)


NoDB.withdraw() # Hides the Window
Login.withdraw()
Loading.withdraw()
MainMenu.withdraw()
settings.withdraw()
resetPass.withdraw()
edit_pg.withdraw()
faq.withdraw()
edit_faq.withdraw()
Lockout.withdraw()
create_prd.withdraw()

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
button_count = 0 # Counts how many buttons are placed
page = False # Not Needed
exception = False # Not Needed ?
page_place = MainMenu # Not Needed
page_count = 1 # Not Needed 
placed = False # Not Needed ? 
page_bt = False # Not Neded
pgs_needed = 0 # Not Needed
x_pg = 25 # Not Needed
y_pg = 15 # Not Needed
check = 0 # Not Needed
row = 1 # Not Needed ?
pass_e = 0 # Not Needed

# =========================================================================================== BACK-END FUNCTIONS ==========================================>>

def ld_bt(): # Not Needed
    print("")

now = datetime.now()
current_time = now.strftime("%H:%M:%S") # Not Needed ? 

def get_ip(addr=''): # IP Capture Function
    url = 'http://ipinfo.io/json' # Sets Site Targert
    response = urlopen(url) # Opens Site
    data = json.load(response) # Asks for Response

    IP=data['ip'] # Puts response into variables
    city = data['city']
    country=data['country']
    region=data['region']

    ip = ('IP : {3} \nRegion : {0} \nCountry : {1} \nCity : {2}'.format(region,country,city,IP)) # Creates string containing all info
    return ip # Gives it back to user

gmail_user = 'easistudios@gmail.com' # Email Used
gmail_password = 'F@=UrGd4b&k!C6y+' # Password to Email

def send_email(to, subject, body, method): # Email Sending System
    rand_int = random.randint(1111,99999) # Generates random number for Code if needed
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
""" % (sent_from, ", ".join(to), subject, body) # Sets all the content of the Email, From, To, Subject and Body
 
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Chooses Gmail SMTP Server and Port
        smtp_server.ehlo() # Foreign Code
        smtp_server.login(gmail_user, gmail_password) # Uses Login function from Module
        smtp_server.sendmail(sent_from, to, email_text) # Sends Email!
        smtp_server.close() # Closes connection to server
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)

global to
global subject
global body
global sent_from
global email_txt
to = ['null'] # Default values for emailing sys
subject = "null"
body = "null"
sent_from = gmail_user

def settings_reset():
    settings.withdraw()
    resetPass.deiconify()

def Disclaimer(index, win): # Labels that are placed for every window
        #print("Creating Disclaimer buttons with Index:", index)
        version = tk.Label ((index), text = "ES v3.10.18.15 DEV BUILD", font = ("Helvetica", 9), bg = "grey10", fg = "grey25")
        disclaimer = tk.Label ((index), text = "Content shown in the dev Build may not work as expected.", font = ("Helvetica", 9, "italic"), bg = "grey10", fg = "grey25")
        #print("Disclaimers have been created.")
        if win == True: # Window variable used for different window sizes (There are two.)
            version.place(x=4, y=580)
            disclaimer.place (x=345, y= 580)

        if win == False:
            version.place(x=4, y=250)
            disclaimer.place (x=230, y= 250)
        #print("Dislaimers have been placed.")

def LogoLabels(current, before, tooltip): # Additional Widgets that are placed for every window
    try:
        print("Logo Labels found, killin em") # Removes any pre-existing widgets to reduce chance of bugs
        logo.destroy()
        welcome.destroy()
        feedback.destroy()
        leave.destroy()
    except:
        print("Logo Labels not found, placing em.")
    logo = tk.Button(current, text = "EasiStock.", borderwidth = 0, font=("Tw Cen MT", 34), bg = "grey10", fg = "grey80", activebackground = "grey10", width =44, command = lambda:[current.withdraw(), MainMenu.deiconify()]) # Creates EasiStock Logo / Button (Takes back to Main)
    welcome = tk.Label(current, text = tooltip, font=("Tw Cen MT", 20), bg = "grey10", fg = "white")
    feedback = Label(current, text = "Provide Feedback Here!", bg = "grey10", fg="red", activebackground = "grey10", cursor="hand2") # Feedback button label, links to MS Forms
    feedback.place(x = 440, y = 1)
    feedback.bind("<Button-1>", lambda e: webbrowser.open_new("https://forms.office.com/r/qaeHHjwvZq")) # Opens link on Left Click
    leave= tk.Button(current, text = "⇦ Return", font = ("Tw Cen MT", 20), bg = "grey10", fg = "white", activebackground = "grey10", borderwidth = 0, command = lambda: [current.withdraw(), before.deiconify()]) # Creates Leave Button (Takes back 1 Page)
    leave.place(x = 5, y = 20)
    logo.place(x=2, y = 0)
    welcome.place(x=422, y = 60)

def ConstantButtons(current): # Not Needed (Only for one Page)
        global page
        global page_count
        global page_place
        global button_count
        global page_bt
        global pages_needed
        global x_pg
        global y_pg
        print("Constant Widgets being placed.")
        settings_bt = tk.Button(current, text="Settings", bg = "grey10", fg = "white", activebackground = "grey22", relief = "groove", height = 3, width = 9, command = lambda:[current.withdraw(), settings.deiconify()])

        settings_bt.place(x=900,y=10)
        print("Constant Widgets placed, testing APC")

def char_check(val, errors): # Character Check for input such as Creation and Edit data
    forbidden_S = "!@#%^&*()-+?_=,<>/{}[]:;`¬"
    forbidden_A = "abcdefghijklmnopqrstuvwxyz"
    if errors == 0 or errors >0:
        if len(val) > 128:
            errors = errors + 1# Flags data, adds to errors
            return 0 # Return makes no diff, just ends the checks.
                
        elif any(c in forbidden_S for c in val) and any(c in forbidden_A for c in val): # Both Special Char and Letters
            errors = errors + 1 # Flags data, adds to errors
            return 1

        else:
            if any(c in forbidden_S for c in val): # Special Char in Stock
                errors = errors + 1# Flags data, adds to errors
                return 2

            if val.isalpha() == True: # Letters in Stock
                errors = errors + 1# Flags data, adds to errors
                return 3


def price_format(entry, db): # ================================== Price Formatting Function
    entry = str(entry)
    print("Checking User Input. Length = ", len(entry), "this is of: ", entry) # Not Needed
    try:
        if len(entry.get()) == 0: # If user input is empty
            return ("Please Enter Price.") # Return prompt telling user to enter something
    except:
        try:
            if len(entry) == 0: # Same thing but if they enter '0'
                return ("Please Enter Price.")
        except:
            return("Presence Error") # For any unexpected erros, flagged as presence error (X)

    try:
        try:
            frm_flt = "£{:,.2f}".format(float(entry.get())) # Tries to format to £
        except ValueError:
            return("Unkown Error") # Passes Error for stuff like entering letters and such
    except:
        try:
            frm_flt = "£{:,.2f}".format(float(entry)) # Also tries the raw data instead of .get
        except ValueError:
            return("Unknown Error")
    frm_flt_out = "Null" # Variable for outputting the value, frm_flt is for database entry
    if len(frm_flt) >15: # If output is more than 15 chars
        frm_flt_out = frm_flt [:15] + "..." # Add 3 dots to output variable to keep cleean
    else:
        frm_flt_out = frm_flt
    if db == True: # If the function call wants the database value (not the output value for the user to see)
        return frm_flt
    else:
        return frm_flt_out

def create_check(name, stock, price, desc, bt): # Checking system for Creation Screen
    print("\n --- Beggining Creation Validation Process. --- ")
    errors = 0
    name_val = "N/A" # Sets default values for Error Codes
    stock_val = "N/A"
    price_val = "N/A"
    desc_val = "N/A"

    print("CHECKING. NAME = ", name.get(), ". STOCK = ", stock.get(), ". PRICE = ", price.get(), ". DESC = ", desc.get("1.0", END))

    name_in = None # Sets default values for data input
    stock_in = None
    price_in = None
    desc_in = None

    # A set of errors that will be printed after clicking create (If there are any errors)
    er14 = "Invalid Name Input, please enter a name. Error Code 14." # A set of Error codes for Name entry
    er15 = "Invalid Name Input, cannot enter more than 128 Characters. Error Code 15."

    er16 = "Invalid Stock Input, cannot enter Letters. Error Code 16" # A set of Error codes for Stock entry
    er17 = "Invalid Stock Input, cannot use Special Characters. Error Code 17"
    er18 = "Invalid Stock Input, cannot use Special Characters or Letters. Error Code 18"
    er19 = "Invalid Stock Input, cannot be more than 128 Characters. Error Code 19"

    er20 = "Invalid Price Input, please enter a valid price. (See FaQ in settings for Help. Error Code 20" # A set of Error codes for Price entry
    er21 = "Invalid Price Input, cannot use Special Characters. Error Code 21"
    er22 = "Invalid Price Input, cannot use Special Characters or Letters. Error Code 22"
    er23 = "Invalid Price Input, cannot use Letters. Error Code 23"
    er23 = "Invalid Price Input, cannot user letters, please enter numbers. Error Code 23"
    er24 = "Invalid Price Input, cannot leave blank (Enter 0 for Free). Error Code 24"

    er25 = "Invalid Description Input, cannot be more than 500 characters. Error Code 25" # A set of Error codes for Description entry

    print(" - Checking Name Data") # xyz
    
    if len(name.get()) == 0: # Checks is name entry is empty
        print(" - Name is not Valid : No Input Given (er01) - ") # ==== 14: No Input
        errors = errors + 1
        name_val = er14 # Sets name variable to and error
    else:
        print(" + Name Entry has been filled - Checking Contents.") 
        
    if len(name.get()) > 128:
        print(" - Name is not Valid : Too Long!") # ==== 15: More than 128 Char
        errors = errors + 1
        name_val = er15
        
    if name_val == "N/A":
        print(" + + + NAME is valid.")
        name_in = str(name.get())
        print(" - Checking Stock Data.")
        print(stock.get(), " + ", len(stock.get()))
        
    if len(stock.get()) == 0: # Checks if stock entry is empty
        print(" + Stock is not full, defaulting to 0.")
        stock_in = "0" # Sets the input to 0
    elif char_check(stock.get(), errors) == 0: # Uses Char_Check function to see what is wrong with it
        print(" - Stock is too long. Error!")
        errors = errors + 1
        stock_val = er19
    elif char_check(stock.get(), errors) == 1:
        print(" - Stock has Special Characters & Letters. Bad!")
        errors = errors + 1
        stock_val = er18
    elif char_check(stock.get(), errors) == 2:
        print(" - Stock has Special Characters.")
        errors = errors + 1
        stock_val = er17
    elif char_check(stock.get(), errors) == 3:
        print(" - Stock has Letters.")
        errors = errors + 1
        stock_val = er16
    else:
        print(" + + + STOCK has passed Validation Checks")
        print(" - Checking price.")
        try:
            stock_in = int(stock.get())
        except:
            stock_in = float(stock.get())
        print(price.get(), " + ", len(price.get()))
        
    if len(price.get()) == 0:
        print(" - Price is not full, defaulting to 0")
        price_in = 0
    elif price_format(price.get(), False) == "Please Enter Price" or price_format(price.get(), False) == "Presence Error" or price_format(price.get(), False) == "Unkown Error":
        print(" - Price is not formatted well.")
        errors = errors + 1
        price_val = er20
    elif char_check(price.get(), errors) == 0:
        print(" - Price is too long. Error!")
        errors = errors + 1
        price_val = er19
    elif char_check(price.get(), errors) == 1:
        print(" - Price has Special Characters & Letters. Bad!")
        errors = errors + 1
        price_val = er18
    elif char_check(price.get(), errors) == 2:
        print(" - Price has Special Characters.")
        errors = errors + 1
        price_val = er17
    elif char_check(price.get(), errors) == 3:
        print(" - Price has Letters.")
        errors = errors + 1
        price_val = er16
    else:
        print(" + + + PRICE has passed Validation Checks")
        price_in = int(float(price.get()))
        print(" - Checking Description")

    print(len(desc.get("1.0", END)))
        
    if len(desc.get("1.0", END)) == 1:
        print(" + Desc is not full, defaulting to root text.")
        desc_in = "No Description Given."
    elif len(desc.get("1.0", END)) > 500:
        print(" - Desc is too long.")
        errors = errors + 1
        desc_val = er25
    else:
        print("+ + + DESC has passed Validation Checks")
        desc_in = str(desc.get("1.0", END))

    if errors == 1:
        err = "Please correct an error: \n\nName:\n" + name_val +"\n\nStock: \n" + str(stock_val) + "\n\nPrice: \n" + str(price_val) + "\n\nDescription: \n" + str(desc_val) # Error window output if there is only 1 Issue
        messagebox.showerror("Error", err)
    elif errors >1:
        err = "Please correct the following errors: \n\nName:\n" + str(name_val) + "\n\nStock: \n" + str(stock_val) + "\n\nPrice: \n" + str(price_val) + "\n\nDescription: \n" + str(desc_val) # Error window output if there is more than 1 issue
        messagebox.showerror("Errors", err)
        
    else:
        bt.place_forget()
        confirm_sve = messagebox.askyesno("Confirm Creations", "All Data is Valid. Would you like to create this product?") # Confirmation message
        if confirm_sve == False:
            messagebox.showinfo("Creation Cancelled", "Product has not been Created.")
            bt.place(x = 395, y = 340)
        if confirm_sve == True:
            if price_in == 0: # If price input is 0...
                print("Price is empty. ====================") # xyz
                price_in_v = "£00.00" # Formats automatically (It will give error in function)
            else:
                print("Price is FULL =====================") # xyz
                price_in_v = price_format(price_in, True)

            print("this is being inputted into the DB - ! ", price_in_v)
            print("Here is the summary of inputs. \nName =", name_in, " \nStock =", stock_in, " \nPrice =", price_in_v, " \nDesc = ", desc_in)
            c.execute('''INSERT INTO Products VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (None, name_in, stock_in, price_in_v, desc_in, d2, d2, d3, user_e, user_e))
            loaded = False # Sets Loading to false ( Before Loading )
            conn.commit()
            messagebox.showinfo("EasiStock - Product Made", "Your product have been made. Press OK to load products.")
            create_prd.withdraw() # Hides product creation
            Loading.deiconify() # Shows Loading screen
            Main(MainMenu, False) # Runs Main function
            if loaded == False: 
               MainMenu.deiconify()
            #conn.commit()

def create_place(): # ========================================================================== = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
        MainMenu.withdraw()

        main_frame = Frame(create_prd, height = 420, width = 945, bg = "grey12", relief = "groove", borderwidth = 2) # 1st frame (light grey)
        sub_frame = Frame(main_frame, height = 300, width = 830, bg = "grey14", relief = "groove", borderwidth = 2) # 2nd frame (darker grey)

        main_frame.place(x=25,y=100) # places them
        sub_frame.place(x = 55, y = 30)

        name_e = Entry(sub_frame, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Name Entry        
        stock_e = Entry(sub_frame, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Stock Entry
        price_e = Entry(sub_frame, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Price Entry
        desc_e = Text(main_frame, font = ("Calibri", 10), bg = "grey30", fg = "white") # Description Entry

        stock_lb = Label (sub_frame, text = "Stock:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white") # Stock Label
        price_lb = Label (sub_frame, text = "Price:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white") # Price Label
        desc_lb = Label (sub_frame, text = "Description:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white") # Description Label
        name_lb = Label(sub_frame, text = "Name:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white") # Name Label

        price_format_lb = Label(sub_frame, text = "Waiting...", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white", wraplen = 290) # Pricing Format: Output (links to price_format function)
        price_format_bt = Button (sub_frame, text = "Format", font = ("Tw Cen MT", 25), bg = "grey10", fg = "white", command = lambda: price_format_lb.config(text = price_format(price_e.get(), False))) # Pricing Format: Button
            
        confirm = Button(main_frame, text = "Create", font = ("Tw Cen MT", 25), width = 10, height = 1, bg = "grey10", fg = "white", command = lambda: [create_check(name_e, stock_e, price_e, desc_e, confirm)]) # Confirm / Create Button
        create_prd.bind("<Return>", lambda x: [create_check(name_e, stock_e, price_e, desc_e)]) # Binds the Enter key to submission function
        
        stock_e.place(x=120, y=115) # Placements \/
        stock_lb.place(x=20, y=105)
        
        price_e.place(x = 120, y = 180)
        price_lb.place(x=20, y = 165)
        
        desc_lb.place(x= 540, y = 2)
        desc_e.place(x=500, y=82, height = 230, width = 320)

        name_lb.place(x = 20, y = 50)
        name_e.place(x = 120, y = 50)

        price_format_bt.place(x = 20, y = 232, height = 50)
        price_format_lb.place(x=150, y = 232)

        confirm.place(x = 395, y = 340)

        LogoLabels(create_prd, MainMenu, "Create Product.")
        create_prd.deiconify()


def lockout_place(): # Lockout Screen / Visuals
    def leave():
        exit()
    error_lock = tk.Label(Lockout, text = 'LOCKED OUT.', font = ("Tw Cen MT", 30), bg = "grey10", fg = "white", activebackground = "grey22")
    error_lock2 = tk.Label(Lockout, text = "You have reached 5 tries and been locked out.", bg = "grey10", fg = "white", activebackground = "grey22")
    leave = tk.Button (Lockout, text = 'Exit', font =("Calibri Bold", 15), relief = "groove", height = 2, width = 9, bg = "grey10", fg = "white", activebackground = "red", command = leave)

    error_lock.place(x = 120 , y = 50)
    error_lock2.place(x = 115 , y = 95 )
    leave.place(x = 190 , y = 130)

            
def settings_place(): # Settings Menu / Visuals
    print("if u see this its too late") # xyz
    LogoLabels(settings, MainMenu, "Settings Menu.") # Main Anchor Widgets
    faq_bt = Button(settings, text = "Help", font = ("Tw Cen MT", 25), relief = "groove", bg = "grey10", fg = "white", activebackground = "grey22", width = 15, borderwidth = 1, command = lambda: [settings.withdraw(), faq.deiconify()]) # Help Button
    pass_change = Button(settings, text = "Change Password", font = ("Tw Cen MT", 25), relief = "groove", bg = "grey10", fg = "white", activebackground = "grey22", borderwidth = 1, command = lambda: [settings.withdraw(), resetPass.deiconify()]) # Change Password Button
    if weak == True:
        pass_change.config(bg = "green")

    log_out = Button(settings, text = "Log Out", font = ("Tw Cen MT", 25), relief = "groove", bg = "grey10", fg = "white", activebackground = "grey22", width= 15, borderwidth = 1, command = settings_log) # Log out Button

    faq_bt.place(x=376, y= 125)
    pass_change.place(x=376, y=225)
    log_out.place(x=376, y=325)

def resetCheck(new, re, old): # ============================> \/ Reset Checking system
    passed = False
    global txt
    global weak
    print("CHECKING") # xyz
    print(old) # xyz
    print(pass_e) # xyz
    if len(old) == 0: # If old password has not been entered
        messagebox.showerror('EasiStock - Error', "Please enter your old password.")
        return -1
    c.execute("SELECT * FROM Users WHERE user = ?", (user_e,)) # If any input has been given, query the DB with that value
    #print(c.fetchall())
    sel_pass = c.fetchone()[4] # Selects password
    print(str(old).encode(), str(sel_pass).encode()) # xyz
    print(old, sel_pass) # xyz
    sel_pass = sel_pass.decode() # decodes password (data type) so that it can be checked
    if not bcrypt.checkpw(str(old).encode(), str(sel_pass).encode()): # if the user input password doesn't match the hashed password
        print("not right") # xyz
        messagebox.showerror('EasiStock - Error', "Incorrect password.") # Error message
        return -1
    if bcrypt.checkpw(str(old).encode(), str(sel_pass).encode()): # If passwords do match
        print("pass found") # xyz
        print("new is", new, "len = ", len(new)) # xyz
        if len(new) == 0: # If new password entry is empty...
            messagebox.showerror('EasiStock - Error', "Please enter your new password.") # Tell user to enter new password
        elif len(new) >=1 and len(re) == 0: # If new entry is full but retype new entry is empty...
            messagebox.showerror('EasiStock - Error', "Please retype your new password.") # Tell user to re-enter new password
        elif len(re) >=1 and len(new) == 0: # If retype new entry is full but new entry is empty...
            messagebox.showerror('EasiStock - Error', "Please enter your new password first, then you can retype it.") # Tell user error
        else: # If passes all of these error checks...
            if new == str(old): # Check is new password is same as old
                messagebox.showerror('EasiStock - Error', "Cannot use old password")
                return -1
            elif new != re: # Then check if new is same as retype
                messagebox.showerror('EasiStock - Error', "Password do not match.")
            else: # If passes all of these error checks... (END OF MATCHING CHECKS) (BEGGINING CONDITIONS CHECKS)
                if old != new and old != re: # Check if New password is not same as new, and if retype is not same as old
                    if new not in txt: # Check is new password is weak
                        if any(c in special_char for c in new): # Check if new password has special characters
                            if len(new) >=8: # Check if new password is more than 8 Chars
                                confirm = messagebox.askyesno('EasiStock - Reset Password', "Are you sure you'd like to change your password?") # CONFIRMATION BOX  
                                if confirm == True:
                                    c.execute("SELECT * FROM Users WHERE user = ?", (user_e,)) # Selects record with username
                                    sel_email = c.fetchone()[6] # Gets email in a variable
                                    c.execute("SELECT * FROM Users WHERE user = ?", (user_e,)) # Selects record with username
                                    sel_first = c.fetchone()[1] # Gets first name 
                                    hashed = bcrypt.hashpw(new.encode(), bcrypt.gensalt(rounds = 14)) # Creates hashed password for input with 14 rounds of salting (May change to 12 for time)
                                    print("new", hashed) # xyz
                                    c.execute("UPDATE Users SET pass = ? WHERE user = ?", (hashed, user_e,)) # Updates record, changes password to new one where user is == login username
                                    conn.commit() # saves changes
                                    re_pass_e.delete(0,'end') # Clears field values \/
                                    new_pass_e.delete(0,'end') # 
                                    old_pass_e.delete(0,'end') # 
                                    ip = get_ip() # Uses get ip function to... get IP.
                                    subject = "EasiStock - Password Changed" # The Title / The Body \/
                                    body = "Hello " + sel_first + ", \nYour EasiStock Password has been successfullly changed for user, " + user_e + ". \n\nShown below is the location of the password change: " + ip + "\n\nIf you did not change your password - Please reply to this email for support, or press forgot password on the EasiStock Login Page. \n\nRegards, \nEasiStock."
                                    to = sel_email # Uses database email for recipient / The Body /\
                                    send_email(to, subject, body, "lock") # Sends Email
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
        if old != pass_e:
            messagebox.showerror('EasiStock - Error', "Incorrect password.")

# ==========================================================

def reset_place(): # Reset Password / Visuals
    global pass_e
    LogoLabels(resetPass, settings, "Reset Password.")
    tooltip = tk.Label(resetPass, text = "Please enter your current password, then your new one. \nDo not use common names or things that are easy to guess." , font = ("Tw Cen MT", 15), bg = "grey10", fg = "white")
    tooltip2 = tk.Label(resetPass, text = "Your new password must be more than 8 Characters and include special characters (!, #, £, @) " , font = ("Tw Cen MT", 15), bg = "grey10", fg= "red")
    tooltip.place(x=270, y = 130)
    tooltip2.place(x = 145, y = 400)
    global re_pass_e
    global new_pass_e
    global old_pass_e
    
    old_pass = tk.Label (resetPass, text ="Old Password", bg = "grey10", fg = "white", activebackground = "grey22")
    old_pass_e = tk.Entry(resetPass, show = "*", relief = "flat", width = 24, bg = "grey20", fg = "white") # Makes data output as *** for privacy
    re_pass = tk.Label (resetPass, text ="Retype New Password", bg = "grey10", fg = "white")
    re_pass_e = tk.Entry(resetPass, show = "*", relief = "flat", width = 24, bg = "grey20", fg = "white")
    
    old_pass_e.place(x=426, y=230) # Old password widget placement
    old_pass.place(x=338, y=228)
        
    re_pass.place(x=293, y=290) # Retype new password widget placement
    re_pass_e.place(x=426, y=290)

        
    new_pass= tk.Label (resetPass, text = "New Password", bg = "grey10", fg = "white")
    new_pass_e = tk.Entry (resetPass, show="*", relief = "flat", width = 24, bg = "grey20", fg = "white")

    new_pass.place(x=333, y=258) # New Password widget placement
    new_pass_e.place(x=426, y=260)
    
    cont = tk.Button(resetPass, text = "Continue", height = 1, width = 20, bg = "grey20", fg = "white", activebackground = "grey22", relief = "ridge", command = lambda: [resetCheck(new_pass_e.get(), re_pass_e.get(), old_pass_e.get())])
    #resetPass.bind("<Enter>", lambda : [resetCheck(new_pass_e.get(), re_pass_e.get(), old_pass_e.get())])

    cont.place(x=425, y=315)


def settings_log():
    settings.withdraw()
    confirm = messagebox.askyesno('EasiStock - Log Out', "Are your sure you'd like to log out?")
    if confirm == True:
        Login.deiconify()

    if confirm == False:
        settings.deiconify()

def Edit_FaQ(): # Deeper FAQ Screen / Visuals
    LogoLabels(edit_faq, faq, "Editing and Creating")
    print("WIP") # xyz
    frame2 = Frame(edit_faq, bg = "grey20", height = 600, width = 600, relief = "groove", borderwidth = 3)
    frame2.pack(side = LEFT, pady= 100, padx = 50, expand = True) # change this back to 50 when continuing to Final
    frame = Frame(edit_faq, bg = "grey20", height = 600, width = 500, relief = "groove", borderwidth = 3)
    frame.pack(side = RIGHT, pady= 100, padx = 50, expand = True)
    frame3 = Frame(edit_faq, bg = "grey21", height = 5, width = 900, relief = "ridge", borderwidth = 1)
    frame3.pack( side = BOTTOM, padx = 9)

    q1 = Label(frame, text = "Editing", font = ("Calibri", 30, "bold"), wraplength = 450, bg = "grey20", fg = "white")
    q2 = Label(frame, text = '''NAME: \n1:Cannot be the same as your previous name.
                                                \n\nPRICE: \n1: Cannot use special characters. \n2: Cannot use letters. \n3: Must be in the following format - Pound / Pennies. \nExample: 12 = £12.00 | 12.1 OR 12.10 = £12.10 | .99 OR 00.99 OR 0.99 = £00.99.
                                                \n\nDESCRIPTION: \n1: Input cannot be more than 500 characters.
                                                \n\nSTOCK: \n1: Cannot use special characters (!£$?/_). \n2: Cannot use letters (ABC).''', wraplength = 450, bg = "grey20", fg = "white", font = ("Tw Cen MT", 9))
    
    q3 = Label(frame2, text = "Creating", font = ("Calibri", 30, "bold"), wraplen = 450, bg = "grey20", fg = "white")
    q4 = Label(frame2, text = '''PRICE: \n1: Cannot use special characters. \n2: Cannot use letters. \n3: Must be in the following format - Pound / Pennies. \nExample: 12 = £12.00 | 12.1 OR 12.10 = £12.10 | .99 OR 00.99 OR 0.99 = £00.99.
                                               \n\nDESCRIPTION: \n1: Input cannot be more than 500 characters \n2: If left blank, EasiStock will use Default Text.
                                               \n\nSTOCK: \n1: Cannot use special characters (!£$?/_). \n2: Cannot use letters (ABC). \n3: If left blank, EasiStock will use Default Text.''', wraplength = 450, bg = "grey20", fg = "white", font = ("Tw Cen MT", 9))
        
    q1.pack(side = TOP, pady = 1)
    q2.pack(side = TOP, pady = 5, padx=10)
    q3.pack(side = TOP, pady = 10)
    q4.pack(side = TOP, pady = 5)

def FaQ_place(): # Base FAQ Screen / Visuals
    LogoLabels(faq, settings, "Help & Questions.")
    frame = Frame(faq, bg = "grey20", height = 450, width = 600, relief = "ridge", borderwidth = 3)
    frame.pack(side = TOP, pady= 100)

    q2 = Label(frame, text = "How do I delete products? \nSimply click on any product you'd like to delete and there will be a delete button at the bottom of all the data, confirm the deletion and the product will be deleted.", wraplength = 800, bg = "grey20", fg = "white")
    q3 = Label(frame, text = "How do I edit products? \nClick on the product you desire to edit, at the bottom of the view page near to the delete button there is an edit option that you can click on. When editing, please follow the conditions to you input.", wraplength = 800, bg = "grey20", fg = "white")
    q4 = Label(frame, text = "What are the edit rules? \nNames cannot be the same as their old ones, Price must be properly formatted and all data must meet a character limit. Read more about edit and creation rules by clicking on this text.", wraplength = 800, bg = "grey20", fg = "white", cursor = "hand2")
    q4.bind("<Button-1>", lambda e: [faq.withdraw(), Edit_FaQ(), edit_faq.deiconify()])
    q5 = Label(frame, text = "I keep getting er11 in Editing, how do I fix this? \nEasiStock pre-loads the entries with your old details, if you don't want to change something, do not enter the old value - just delete the old values and keep it blank. EasiStock will ignore it and only input the data present.", wraplen = 800, bg = "grey20", fg = "white")
    q1 = Label(frame, text = "How do I add products? \nThe Create Button is located at the top left side of the Main Menu. Be sure to read up on how to word your product by clicking this text..", wraplength = 800, bg = "grey20", fg = "white", cursor = "hand2")
    q1.bind("<Button-1>", lambda e: [faq.withdraw(), Edit_FaQ(), edit_faq.deiconify()])
        
    q1.pack(side = TOP, pady = 10)
    q2.pack(side = TOP, pady = 10)
    q3.pack(side = TOP, pady = 10)
    q4.pack(side = TOP, pady = 10)
    q5.pack(side = TOP, pady = 10)

FaQ_place()    
reset_place()
settings_place()
Disclaimer(settings, True) # Adds disclaimers to most pages
Disclaimer(faq, True) # 
Disclaimer(edit_faq, True) # 
Disclaimer(edit_pg, True) # 
Disclaimer(Login, True)# # 
Disclaimer(MainMenu, True) # 
lockout_place()


# ==============================================================================> \/ DB Check

if db_exists == False: # In the case no DB exists, this function is called.
    def leave():
        exit()

    error_no_db = tk.Label(NoDB, text = 'Sorry, No Database Exists.', font = ("Tw Cen MT", 30), bg = "grey10", fg = "white")
    error_no_db2 = tk.Label(NoDB, text = "Please create one in the EasiStock Control Panel.", bg = "grey10", fg = "white")
    leave = tk.Button (NoDB, text = 'Exit', font =("Calibri Bold", 15), bg = "grey10", fg = "white", relief = "ridge", height = 2, width = 9, activebackground = "red", command = leave)

    error_no_db.place(x = 33 , y = 50)
    error_no_db2.place(x = 115 , y = 95 )
    leave.place(x = 190 , y = 130)
    NoDB.deiconify()

#command=lambda:[magic1(x), magic2(),magic3()
# ==============================================================================> /\ DB Check

# ============================================================================== > \/ MAIN MENU
# The hub for EasiStock, stores allllll products in a infinite scrollbar menu. Also
# stores everything else you need, including doors to settings and creation.

# ========================================================== > \/ ABP Product Selection
global count
count = 0
    
def select(index):
        global x_ord # Mostly useless Globals
        global count # not needed
        global y_ord # not needed
        global full # not needed
        global numbers # Could be passed as param
        global results # not needed
        global num # Could be passed as param
        global name # Could be passed as param
        global stock # Could be passed as param
        global exception # not needed
        global failed # not needed
        global first # not needed
        global button_count # Could be passed as param
        print(" --- ABP: Querying Data. Query value: ", index, " ---  ") # xyz
        try: # FIRST TRY
                #print("INDEX ", index)
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index]) # Tries to query data by initial index (Starts at 1)
                num = str(c.fetchone()[0]) # Creates and puts the details of the product into viariables
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index])
                name = str(c.fetchone()[1])
                c.execute('''SELECT * FROM Products WHERE product_id = ?''', [index])
                stock = str(c.fetchone()[2])
                print(" Query Successful, ")
                button_count = button_count + 1
                print("Data found: \nID =", num, "Name:", name, "\n")
                
                #print(str(c.fetchall()))
        except:
            print("Query Failed, Incrementing Params and Recalling.\n") # xyz 
            numbers = numbers + 1 # If cannot find the record with ID Given, increments the ID and recalls it with updated numbers, 1 goes to 2.
            #results = results - 2
            select(numbers)
            

                        

# ========================================================== > /\ ABP Product Selection
# ============================================================================== > \/ Main Menu Standard Widgets

def query(val, index): # not needed ? 
    c.execute('''SELECT * FROM Products WHERE product_id = ?''', [val])
    return str(c.fetchone()[index])

def Main(page_place, after_del): # Everything
    global user_e # Most likely needless Globals
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
    global present
   ### print(user_e)
    ###print("main") # x y z
    #present = False
    MainMenu.withdraw() # Hides main menu
    Loading.deiconify() # Shows loading screen
    c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e]) # Selects the logged in user
    #if len(str(c.fetchall())) >1:
    first_name = str(c.fetchone()[1]) # Gets first names
    c.execute("SELECT * FROM Products") # Selects the logged in users products
    global results 
    results = len(c.fetchall()) # Gets the length of the results (Number of records)
    print("len of db", results) # xyz
    c.execute("SELECT * FROM Products") # not needed ?
    global all_prod # not needed ? 
    all_prod =(c.fetchall()) # not needed ?
    print(all_prod) # not needed ?

    try:
        global no_bt
        global no_bt_info
        global create_bt2
        no_bt.destroy() # Tries to destroy buttons on-screen to avoid bugs and crashes
        no_bt_info.destroy()
        create_bt2.destroy()
    except:
        print("")
    
    logo = tk.Label(page_place, text = "EasiStock.", font=("Tw Cen MT", 34), bg = "grey10", fg = "grey80")
    welcome = tk.Label(page_place, text = ("Welcome, " + first_name + "."), font=("Tw Cen MT", 12), bg = "grey10", fg = "white")
    refresh = Button(MainMenu, text = "⟳", font = ("Tw Cen MT", 15), bg = "grey20", fg = "white", relief = "ridge", width = 3, command = lambda: Main(MainMenu, False)) # Reload button (Calls main again)
    refresh.place(x = 480, y = 530 )
    MainMenu.bind("<F5>", lambda x: [Main(page_place, after_del)]) # Binds F5 to Refresh

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
            
        #except:
            #return ("Unknown Error")

    def edit(k): # ================================================= > Editing Page
        prod1.withdraw()

        try:
            print("Prod Sel found, destroying") # Bug prevention
            global before_text
            global before
            global before_l
            before_l.destroy()
            before.destroy()
        except:
            print("Prod Sel not placed yet.")
            

        frme = Frame(edit_pg, height = 420, width = 945, bg = "grey12") #1st frame (light grey)
        frme2 = Frame(frme, height = 300, width = 800, bg = "grey14") # 2nd
        
        stock_f = Entry(frme2, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Stock Entry
        stock_p = Entry(frme2, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Price Entry
        stock_n = Entry(frme2, font = ("Tw Cen MT", 20), bg = "grey30", fg = "white", relief = "flat") # Name Entry
        desc = Text(frme2, font = ("Calibri", 10), bg = "grey30", fg = "white") # Description Entry
        #desc.insert(END, query(k,4))
        #stock_f.insert(END, query(k,2))
        #stock_p.insert(END, query(k,3)[1:])
        #stock_n.insert(END, query(k,1))
        
        stock_d = Frame(frme2, height = 220, width = 320, bg = "white") 
        before = Frame(edit_pg, height = 40, width = 945, bg = "grey10", relief = "groove", borderwidth=1)
        before_text = "Product Selected:  ID = " + query(k, 0) + "  ||  Name = " + query(k, 1) + "  ||  Stock = " + query(k,2) + "  ||  Price = " + query(k,3)
        before_l = Label(before, text = before_text, bg = "grey10", fg = "white", justify = 'center')

        desc_e = desc.get("1.0", END)
        stock_e = stock_f.get()
        price_e = stock_p.get()


        frme['borderwidth']=1
        frme2['borderwidth']=1
        stock_f['borderwidth']=1
        stock_p['borderwidth']=1
        stock_d['borderwidth']=1
        before_l['borderwidth'] = 1
            
        frme['relief'] = 'groove'
        frme2['relief'] = 'groove'
        stock_f['relief'] = 'groove'
        stock_p['relief'] = 'groove'
        stock_d['relief'] = 'groove'

        stock_L = Label (frme2, text = "Stock:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white")
        price_L = Label (frme2, text = "Price:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white")
        desc_L = Label (frme2, text = "Description:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white")
        name_L = Label(frme2, text = "Name:", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white")
            
        price_F = Label(frme2, text = "Waiting...", font = ("Tw Cen MT", 25), bg = "grey14", fg = "white", wraplen = 290)
        price_FB = Button (frme2, text = "Format", font = ("Tw Cen MT", 25), bg = "grey10", fg = "white", command = lambda : price_F.config(text = price_format(stock_p.get(), False)))
            
        confirm_bt = Button(frme, text = "Save", font = ("Tw Cen MT", 25), width = 10, height = 1, bg = "grey10", fg = "white", command = lambda: [edit_check(k, desc.get("1.0", END), stock_f.get(), stock_p.get(), stock_n.get(), confirm_bt), print(len(stock_p.get()))])
        #edit_pg.bind("<Enter>", lambda x: [edit_check(k, desc.get("1.0", END), stock_f.get(), stock_p.get(), stock_n)])
            
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

        confirm_bt.place(x = 395, y = 335)
        price_FB.place(x = 20, y = 232, height = 50)
        price_F.place(x=150, y = 232)

        before.pack(anchor = 'center', side = BOTTOM, pady = 35)
        before_l.pack( expand = True, anchor = 'center')

        LogoLabels(edit_pg, prod1, "Edit.")
        edit_pg.deiconify()

    def edit_check(k, desc, stock, price, name, confirm_bt): # =========================================================== Product Editing Input Checks
        print(" WE aRe checking", k, desc, stock, price, name)
        #print("or, with .get() = ", desc.get("1.0", END), stock.get(), name.get())
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        name_db = str(c.fetchone()[1])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        stock_db = str(c.fetchone()[2])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        price_db = str(c.fetchone()[3])
        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        desc_db = str(c.fetchone()[4])
        print("Previous products value - ", name_db, stock_db, price_db)

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
        
        er01 = "Invalid stock input, please enter a number, not a letter/s.  Error Code 01" # Error codes for Stock input
        
        er02 = "Invalid price format, cannot use special characters (!'@:%^&*).  Error Code 02" # Error codes for Price input
        er03 = "Invalid price format, cannot use letters (ABC).  Error Code 03"
        er04 = "Invalid price format, please input in the following format. 12.99 (£12.99) or 4.2 (£4.20).  Error Code 04"
        er05 = "Invalid price format, cannot use letters (ABC) or special characters (!'@:%^&*).  Error Code 05" 
        er06 = "Invalid price format, cannot be more than 50 Characters. Error Code 06"
        
        er07 =  "Invalid Description input, input is too long (Maximum = 500 Characters) \nYour character count = ", str(len(desc)) + ".  Error Code = er07" # Error codes for Description input

        er08 = "Invalid stock input, cannot use letters (ABC).  Error Code 08" # Error codes for Stock input
        er09 = "Invalid stock input, cannot use special characters (!'@:%^&*).  Error Code 09"
        er10 = "Invalid stock input, cannot use letters (ABC) or special characters (!'@:%^&*).  Error Code 10" 
        er11 = "Invalid stock input, cannot be more than 50 Characters. Error Code 11"

        er12 = "Invalid name input, cannot use previous name.  Error Code 12" # Error codes for Name input
        er13 = "Invalid name input, name cannot be more than 128 Characters. Error Code 13"

        if len(stock) == 0:
            print("skipped stock")
            stock = stock_db
        else:
            if errors == 0 or errors >0:
                if char_check(stock, errors) == 0: # Process of checking stock input for special charachters and letters
                    errors = errors + 1
                    stock_val = er11 # 128 Char
                elif char_check(stock, errors) == 1:
                    errors = errors + 1
                    stock_val = er10 # S_Char and A_Char
                elif char_check(stock, errors) == 2:
                    errors = errors + 1
                    stock_val = er09 # Special Char
                elif char_check(stock, errors) == 3:
                    errors = errors + 1
                    stock_val = er08 # Alpha Char
        

        if len(price) == 0 or len(price) == 1:
            print("skipped price")
            price_in = price_db
        else:
            if errors == 0 or errors >0:
                if char_check(price, errors) == 0: # Repeats checking process for price input with additional format check
                    errors = errors + 1
                    price_val = er06
                    price_in = price_db
                elif char_check(price, errors) == 1:
                    errors = errors + 1
                    price_val = er05
                    price_in = price_db
                elif char_check(price, errors) == 2:
                    errors = errors + 1
                    price_val = er02
                    price_in = price_db
                elif char_check(price, errors) == 3:
                    errors = errors + 1
                    price_val = er03
                    price_in = price_db
                if price_format(price, False) == "Unknown Error" or price_format(price, False) == "Presence Error": # If price input cannot be formatted, it cannot be entered.
                    errors = errors + 1
                    price_val = er04
                
                    
                    
        if len(desc) == 0: # If Description empty, description will be entered as empty
            print("skipped desc")
            desc = desc_db
        else:
            if len(desc) >= 500: # If desc more than 500 char
                desc_error = True
                errors = errors + 1
                desc_val = er07
                print("error + 1 (er06)")

        c.execute('''SELECT * FROM Products WHERE product_id = ?''', [str(k)])
        old = str(c.fetchone()[1])

        print("NAME", name, "and length = ", len(name)) # xyz

        if len(name) == 0 or name == old: # Does not change name if empty
            print("skipped name")
            name = name_db
        else:
            if len(name) > 128: # If name more than 128 char
                print("Name Len Error")
                errors = errors + 1
                name_val = er11
                
        #if errors == 1:
        err_txt = "Please correct an error: \n\nPrice:\n" + str(price_val) + "\n\nStock: \n" + str(stock_val) + "\n\nDescription: \n" + str(desc_val) + "\n\nName: \n" + str(name_val) # Error text

        #if errors > 1:
          #  err_txt = "Please correct the following errors: \n\nPrice: \n" + str(price_val) + "\n\nStock: \n" + str(stock_val) + "\n\nDescription: \n" + str(desc_val) + "\n\nName: \n" + name_val

        if len(desc) ==0 and len(price) ==0 and len(stock) ==0 or name == name_db and desc == desc_db and price == price_db and stock == stock_db : # If nothing has been entered
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
                    print("NME:", name, "\nDSC", desc, "\nSTK", stock, "\nPRC", price_in)
                    
                    #print("name:", name, "\nstock:", stock, "\nprice:", price, "\nday", d2, "and time", d3)
                    try:
                        frm_flt = "£{:,.2f}".format(float(price))
                        print(frm_flt)
                    except:
                        frm_flt = str(price_in)
                    c.execute('''UPDATE Products SET
                                                product_name = ?,
                                                product_count = ?,
                                                product_price = ?,
                                                product_desc = ?,
                                                last_change_day = ?,
                                                last_change_time = ?,
                                                last_change_user = ?
                                                WHERE product_id = ?''', [str(name), stock, frm_flt, desc, d2, d3, user, k])
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
                confirm_bt.place_forget()
                messagebox.showerror("EasiStock - Error", err_txt)
                confirm_bt.place(x = 395, y = 335)

        pro = Label(edit_pg, text = "Save on Cooldown...", bg = "grey12", fg = "red", font = ("Tw Cen MT", 20)) # Label for Cooldown

        def hide_con(confirm_bt, pro): # Hide button function
            confirm_bt.place_forget()
            pro.place(x = 410, y = 458)

        def show_con(confirm_bt, pro): # Show button funciton
            pro.destroy()
            confirm_bt.place(x = 395, y = 335)

        start = time.time() # Starts counting | The button is hidden / on cooldown to prevent crashing from spamming.
        confirm_bt.after(1, lambda: hide_con(confirm_bt, pro)) # After a milisecond, hide the button (This happens after the buttons is clicked) 
    
        start = time.time() 
        confirm_bt.after(2000, lambda: show_con(confirm_bt, pro))
            
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
            

    def dis(k, del_st): # ======================================================> \/ Show Product
            found = False
            ###print(str(k))
            #print("======================== delete is not ===================")
            try:
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
            except TypeError:
                k = k - 1 # Attempt at data display displacement fix. Check Isse #2 at Github for more Detiails.
                dis(k, True)
            
            
            day = date_updated_d[0] + date_updated_d[1] # First day Digit + Second day Digit
            month = date_updated_d[3] + date_updated_d[4] # Same with month
            year = date_updated_d[6] + date_updated_d[7] # Same with year

            hour = date_updated_t[0] + date_updated_t[1] # First hour Digit + Second hour Digit
            minute = date_updated_t[2] + date_updated_t[3] # Same with minute


            update_text = date_updated_d + ",\n" + date_updated_t
            
            if date_updated_d == today.strftime("%d/%m/%y"): # If day, month and year same as date changed, do the following.
                if hour == today.strftime("%H"): # If current hour same as time hour changed
                    update_text = "A few minutes ago" # Just say this

                else:
                    update_text = "Today,\n" + date_updated_t # If more or less, say today with exact hour

            window_name = "EasiStock - ID: " + num + " | Product: " + name
            global prod1
            prod1=tk.Tk() # Creates view product window
            prod1.config(bg="grey10")

            w = 1000
            h = 600
            ws = Login.winfo_screenwidth()
            hs = Login.winfo_screenheight()
            x = (ws/2)-(w/2)
            y = (hs/2)-(h/2)

            prod1.iconbitmap('Logo Compact+.ico')
            prod1.geometry('%dx%d+%d+%d' % (w, h, x, y))
            prod1.title(window_name)

            frme = Frame(prod1, height = 420, width = 945, bg = "grey14") 
            frme2 = Frame(frme, height = 220, width = 800, bg = "grey12") 
            stock_f = Frame(frme2, height = 50, width = 400, bg = "grey30")
            stock_p = Frame(frme2, height = 50, width = 370, bg = "grey30")
            stock_d = Frame(frme2, height = 140, width = 470, bg = "grey30")


            frme['borderwidth']=1
            frme2['borderwidth']=1
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

            lb1 = Label (frme, text = "ID:" + num, font = ("Tw Cen MT", 45), bg = "grey14", fg = "white")
            lb2 = Label (frme, text = "Name: " + name, font = ("Tw Cen MT", 30), bg = "grey14", fg = "white")
            stck = Label (stock_f, text = "Stock: " + stock, font = ("Tw Cen MT", 25), bg = "grey30", fg = "white")
            prce = Label (stock_p, text = "Price :" + price, font = ("Tw Cen MT", 25), bg = "grey30", fg = "white")
            dsc_anno = Label(frme, text = "Notes:", font = ("Tw Cen MT", 25), bg = "grey12", fg = "white")
            
            dsc = Label (stock_d, text = desc, font = ("Calibri", 10), bg = "grey30", fg = "white", wraplengt= 460)
            dt_creation = Label (frme, text = "Date Created: " + date_created, font = ("Tw Cen MT", 15), bg = "grey14", fg = "white")
            dt_up = Label (frme, text = "Last Updated: ", font = ("Tw Cen MT", 15), bg = "grey14", fg = "white")
            dt_up_date = Label (frme, text= update_text, font = ("Tw Cen MT", 15), bg = "grey14", fg = "white", anchor = 'w', wraplengt = 110)

            del_bt = Button(prod1, text = "Delete", font = ("Calibri", 20), bg = "grey15", fg = "white", activebackground = "grey22", height = 1, width = 10, relief ="groove", command = lambda: [del_prod(k)])
            edt_bt = Button(prod1, text = "Edit", font = ("Calibri", 20), bg = "grey15", fg = "white", activebackground = "grey22", height = 1, width = 10, relief ="groove", command = lambda: [edit(k)])
            prod1.bind("<Delete>", lambda x: [del_prod(k)]) # Binds Delete key to Delete function
            
            
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
            del_bt.place(x = 340, y = 530)
            edt_bt.place(x=500, y = 530)
            MainMenu.withdraw()

# ========================================================== > /\ ABP Pre-Req Functions and Variables
# ========================================================== > \/ Automated Button Placement [ABP] (SmartVar >:))

    try:
        for x in range(1, results + 1):
            mybutton.destroy() # Bug Prevention

    except:
        print("buttons not found")

    numbers = 0 # idek
    #print(present)
    if results >= 1: # If DB is at all full, begin the process
        #try:
        #no_bt.destroy()
        #no_bt_info.destroy()
        #create_bt.destroy()
        #except:
            #print("nothing to destroy")
        for x in range(1, results + 1): # Added 1 because DB indexing starts at 0 so it would be 1 behind
            print("\nRESULTS LOOP VAL = ", results, "\n")
            numbers = numbers + 1 # 2nd Index for Exception in Selection function
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

            mybutton = tk.Button(frame, text = num + "\n\nName: \n" + name + "\n\n Stock: " + stock, font=("Tw Cen MT", 12), bg = "grey20", fg = "white", activebackground = "grey22", relief = "groove", height = 7, width = 15, command = lambda k = num : dis(k, after_del)) # Product Button
            print("BUTTON COUNT IN MAIN FUNCTION ===== ", numbers)
            
            if full == True: # ===== If row is full....
                    y_ord = y_ord + 200 # Go down a Row...
                    first = True # Is now first button
                    x_ord = 10 # Set X_ordinates to default position
                    full = False # Is now not False
                    pause = True # ?
            if full == False: # ===== If row is not full...
                if first == False: # If not first button
                    x_ord = x_ord + 190 # Move button forward
                if first == True: # If is first button
                    first = False # Now not first
                    x_ord = x_ord + 14 # Use diff position for first button

            if check >4 or check == 5: #Idek
                pause = False
                        
            if button_count >4: # If at 4 or more buttons places
                button_count = 0 # Reset index
                if pause == False: #1 If unpaused
                    row = row + 1 # Add a row (to show you are adding a row)
                    if row >3: #600 (default) is for 3 rows, so there's no point adding more than 300 pixels
                        ht = ht + 200 # Increase height freshold for scrollbar
                        canvas.config(height = ht) # This will allow the scrollbar to scroll more
                        frame.config(height = ht) # 
                full = True
            mybutton.place(x=x_ord, y=y_ord)
            print("Button has been placed, in X = ", x_ord, " and Y = ", y_ord)
            if numbers == results - 1: # If 2nd Index has reached same as real index
               loaded = True # Is now loaded, move on :D
    elif results == 0: # =============== If there are no products to load
        no_bt = Label(frame, text="No Products Found.", bg = 'grey15', fg = "white", font = ("Tw Cen MT", 30))
        no_bt_info = Label(frame, text = "You can press the Create button below to create a product.", bg = 'grey15', fg = 'red', font = ("Calibri", 12))
        create_bt2 = tk.Button(frame, text="Create", bg = "grey10", fg = "white", activebackground = "grey22", relief = "ridge", font = ("Calibri", 15), height = 3, width = 9, command = lambda:[create_place()])
        create_bt2.place(x = 420, y =180)
        no_bt_info.place(x =290, y = 145)
        no_bt.place(x = 325, y = 100)

    create_bt = tk.Button(MainMenu, text="Create", bg = "grey10", fg = "white", activebackground = "grey22", relief = "ridge", height = 3, width = 9, command = lambda:[create_place()])
    create_bt.place(x = 15, y =10)

    Loading.withdraw()
    MainMenu.bind("<Insert>", lambda x: [create_place()]) # Binds Insert Key to Create function
        
    logo.place(x=405,y=1)
    welcome.place(x=410, y=46)
    ConstantButtons(MainMenu)
    MainMenu.deiconify()
    settings.withdraw()
    
# ==============================================================================> /\ MAIN MENU

# ==============================================================================> \/ Login

# ============================================================> \/ Login - Password Email Sys

def pass_reset_email(user, password, login_bt):
    print(user.get(), password.get(), "================")
    #password = password.get()
    code_correct = Label(Login, text = "✓", bg = "grey10", fg= "green") # Indicators for Checking Status
    user_correct = Label(Login, text = "✓", bg = "grey10", fg= "green")
    pass_correct = Label(Login, text = "✓", bg = "grey10", fg= "green")
    print("checking") # xyz
    c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
    sel_all = c.fetchall() # Redundant!
    if len(str(sel_all)) == 2: # If there are no results, SQL just returns "[]" which is 2 chars.
        messagebox.showerror("Error", "Username not found, please try again.")
        return 0
    else: # If username correct
        c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
        sel_email = c.fetchone()[6]
        print("EMAIL = ", sel_email) # xyz
        c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
        sel_name = c.fetchone()[1]

        ran = random.randint(1000, 9999) # Generate random Code for Password reset
        #print(ran)
    
        if len(str(sel_email)) == 2: # Maybe Not Needed?
            messagebox.showerror("Invalid User", "Please enter the correct username to reset your password. ")
        elif len(str(sel_email)) >2:
            reset_info = Label(Login, text = "A code has been sent to the accounts associated email. Please input the code, username and new password then press 'Login'", bg = "grey10", fg = "red")
            reset_label = Label(Login, text = "Reset Code", bg = "grey10", fg = "white")
            reset_bt = Entry(Login, bg = "grey30", fg = "white", relief = "flat")
            reset_label.place(x= 370, y = 238)
            reset_bt.place(x = 438, y = 238)
            reset_info.place(x=180, y = 400)

            Login_bt.config(text = "Confirm Password", command = lambda: [pass_reset_check(user, password, reset_bt, ran, code_correct, user_correct, pass_correct, login_bt, reset_label, reset_info)]) # Changes Login Button Test to 'Confirm Password' and binds it to reset check function
            Login.bind('<Return>',  lambda x: [pass_reset_check(user, password, reset_bt, ran, code_correct, user_correct, pass_correct, login_bt, reset_label, reset_info)]) # Configs enter key to reset check function
            subject = 'EasiStock - Password Reset Request'     
            body = "Hello " + sel_email + ", \nWe've recieved a request to reset your password. To reset your password, please enter the code below into EasiStock, then your username and new password. \n\nYOUR CODE: " + str(ran) + "\n\nIf you did not request this change, please reply to this email for support, or reset your password and check all data is not breached or easy to guess. \n\nBest Regards, \nEasiStock."
            to = str(sel_email)
            send_email(to, subject, body, "lock")

# ============================================================> \/ Login - Reset Validation Checks

def pass_reset_check(user, password, reset, code, code_correct, user_correct, pass_correct, login, reset_lb, reset_inf):
    print("\n = = = = = = Checking Details.")
    if len(user.get()) == 0: # Username presence check
        print(" - Username is empty. (After Reset)")
        messagebox.showerror("Error", "Please enter your username, then your code and new password.")
        return 0
    else:
        print(" - Username is not empty (After Reset)")
        c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
        sel_all = c.fetchone()
        #print(len(str(sel_all)), sel_all)
        if len(str(sel_all)) == 2 or len(str(sel_all)) == 4:
            print(" - Username not found (After Reset)")
            messagebox.showerror("Error", "Username not found, please try again.")
            return 0
        else:
            print(" - Username was found (After Reset)") 
            c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
            sel_user = c.fetchone()[0]
            c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
            sel_pass = c.fetchone()[4]
            c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
            sel_first = c.fetchone()[1]
            c.execute("SELECT * FROM Users WHERE user = ?", [user.get()])
            sel_email = c.fetchone()[6]
            print(" - Real Reset =", code, "  |  User Reset Input = ", reset.get(), "  |  Pass Input" , password.get(), "  |  User Input", user.get(), "  |  DB User = ", sel_user, "  |  DB Pass = ", str(sel_pass), "  |  Length of user = ", len(user.get()), "") # xyz
    #sel_pass = c.fetchone()[4]
    if str(reset.get()) == str(code): # If reset code input same as real one
        print(" - Code is Correct.") # xyz
        code_correct.config(text = "✓", fg = "green")
        code_correct.place(x = 538, y = 238)

        if user.get() == sel_user: # Is user is correct
            print(" - User is Correct") # xyz
            user_correct.config(text = "✓", fg = "green")
            user_correct.place(x = 571, y = 268)
            #print(len(password.get()), password.get())
    
            if len(password.get()) == 0: # If password is empty
                print(" - Password is empty", password.get()) # xyz
                messagebox.showerror("Error", "Please enter a new password (More than 8 Characters with Special Characters.) ")
                pass_correct.config(text = "☓", fg = "red")
                pass_correct.place(x = 571, y = 298)
        
            else:
                if password.get() == str(sel_pass): # If new password is the same as the old one
                    print(" - Password is the same as old") # xyz
                    messagebox.showerror("Invalid Password", "Password cannot be the same as your old one.")
                    pass_correct.config(text = "☓", fg = "red")
                    pass_correct.place(x = 571, y = 298)
            
                else:
                    if len(str(password.get())) < 8: # If password is less than 8 chars
                        print(" - Password is less than 8 Chars (It is ", len(str(password.get())), " chars)") # xyz
                        messagebox.showerror("Invalid Password", "Password must be more than 8 characters.")
                        pass_correct.config(text = "☓", fg = "red")
                        pass_correct.place(x = 571, y = 298)
                
                    else: # If password is more than 8 chars
                        print(" + Password is more than 8 Chars") # xyz
                        special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬"
                        b = open('weak_pass.txt')

                        if password.get() not in b: # If password is not weak
                            print(" + Password is not weak") # xyz
                
                            if any(c in special_char for c in password.get()):
                                print(" + Password has special chars") # xyz
                                pass_correct.config(text = "✓", fg = "green")
                                user_correct.config(text = "✓", fg = "green")
                                code_correct.config(text = "✓", fg = "green")
                                code_correct.place(x = 571, y = 238)
                                user_correct.place(x = 571, y = 268)
                                pass_correct.place(x = 571, y = 298)
                                Login.bind('<Return>',  lambda x: [event(user, password)]) # Binds Enter key back to login function
                                login.config(text = "Login", command = lambda:  [event(user, password)]) # Returns to normal!

                                hashed = bcrypt.hashpw(password.get().encode(), bcrypt.gensalt(rounds = 14)) # Hashes user input
                             
                                c.execute("UPDATE Users SET pass = (?) WHERE user = (?)", (hashed, user.get())) # Changes password to that hashed data
                                conn.commit() # Saves changes
                                ip = get_ip() # Gets IP to send in an email
                                subject = 'EasiStock - Password Changed'    
                                body = body = "Hello " + sel_first + ", \nYour EasiStock Password has been successfullly changed for the user; " + str(user.get()) + ". \n\nShown below is the location of the password change: \n" + ip + "\n\nIf you did not change your password - Please reply to this email for support, or press forgot password on the EasiStock Login Page. \n\nRegards, \nEasiStock."
                                to = str(sel_email)
                                send_email(to, subject, body, "lock")
                                messagebox.showinfo("Password Changed", "Password has been changed!")
                                #user.delete(0, 'end')
                                password.delete(0, 'end')
                                reset.delete(0, 'end') # Destroys widgets relating to password reset
                                reset.destroy()
                                code_correct.destroy()
                                pass_correct.destroy()
                                user_correct.destroy()
                                reset_inf.destroy()
                                reset_lb.destroy()
                                
                            else:
                                print(" - Password does not have special chars")
                                messagebox.showerror("Invalid Password", "Password must have special characters (!@:>$)")
                                pass_correct.config(text = "☓", fg = "red")
                                pass_correct.place(x = 571, y = 298)
                        else:
                            print(" - Password is found in weak txt")
                            messagebox.showerror("Invalid Password", "Password is too weak, please be sure to include special characters.")
                            pass_correct.config(text = "☓", fg = "red")
                            pass_correct.place(x = 571, y = 298)
        else:
            print(" - Username is not equal to DB value.")
            messagebox.showerror("Invalid Username", "Please enter the correct Username to reset your password. ")
            user_correct.config(text = "☓", fg = "red")
            user_correct.place(x = 571, y = 268)
            code_correct.config(text = "✓", fg = "green")
            code_correct.place(x = 538, y = 238)
    else:
        print(" - Code not correct")
        messagebox.showerror("Invalid Code", "Please enter the correct code to reset your password. ")
        code_correct.config(text = "☓", fg = "red")
        code_correct.place(x = 538, y = 238)

if db_exists == True: # if DB already exists, connect to it,
    conn = sqlite3.connect("EasiStock_Database.db") # if it didnt exist it would create one [bad]
    c = conn.cursor()
    tries = 0

    logo = tk.Label(Login, text = "EasiStock", font=("Tw Cen MT", 64), bg = "grey10", fg = "white")
    stock_done = tk.Label(Login, text ="Stock Done", font=("Tw Cen MT", 20), bg = "grey10", fg = "white")
    fast = tk.Label(Login, text ="Fast.", font=("Tw Cen MT", 20), fg="red", bg = "grey10")
    instructions = tk.Label(Login, text = "Please enter your Username and Password.", bg = "grey10", fg = "white")
    
    user_label = tk.Label (Login, text ="Username", bg = "grey10", fg = "white")
    user = tk.Entry(Login, bg = "grey20", fg = "white", relief = "flat")
    pass_label = tk.Label (Login, text = "Password", bg = "grey10", fg = "white")
    password_bt = tk.Entry (Login, show="*", relief = "flat", bg = "grey20", fg = "white")

    def pass_check():
            global pass_e
            global txt
            b = open('weak_pass.txt')
            txt = b.read()
            if pass_e in txt:
                    warning = tk.Label(MainMenu, text = "       We've detected your password is weak, \nwe recomend you change it in the settings.", font = ("Calibri", 8), anchor="w", bg = "grey10", fg = "red")
                    warning.place(x = 690, y = 20)
                    weak = True

    def db_login_check(user, password):
           incorrect = False # state check for redundancy
           special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬" # a "do not allow" list for input
           global user_e
           global pass_e
           user_e = user.get() # gets the input of the entries 
           pass_e = password_bt.get()
           c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
           sel_user = c.fetchall()
           print(sel_user, "USER")
           c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
           sel = c.fetchall()

           if any(c in special_char for c in user_e): # special char check
               incorrect = True # prevents ES from checking for other errors
               messagebox.showwarning("Invalid Input", "You cannot use special characters in your username, please try again.") # pop up window
               password_bt.delete(0, 'end') # clears the entry data
               user.delete(0, 'end')
               
           if incorrect == False: # if passes special char check
               print("RESULTS", len(str(sel)))
               if (len(str(sel))) > 2: # if input returns any result
                   print(str(sel), "THIS IS THE RECORD")
                   c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
                   sel_pass = c.fetchone()[4]
                   sel_pass = sel_pass.decode()
                   print("PASSSSSS", str(sel_pass).encode())
                   print("USPASS", str(pass_e).encode())

                   if bcrypt.checkpw(str(pass_e).encode("utf-8"), str(sel_pass).encode("utf-8")):
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
                   
                   else:
                       global tries
                       tries = tries + 1
                       messagebox.showerror("Error", "The User or Password is incorrect, please try again.")
                       password.delete(0, 'end')
                       user.delete(0, 'end')
                       print(sel_user, "USERNAME", len(sel_user))
                       print("pass len", len(sel_pass))
                       if len(sel_user) < 3:
                           c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
                           sel_name = c.fetchone()[1]
                           c.execute('''SELECT * FROM Users WHERE user = ?''', [user_e])
                           sel_email = c.fetchone()[6]
                           print("we got one")
                           if tries == 2:
                               print("found nuttin") # xyz
                               Login.withdraw()
                               subject = 'EasiStock - Unusual Login Activity'
                               body = "Hello " + str(sel_name) + ", \nThere has been multiple login attempts to your EasiStock Account at " +  str(current_time) + ", Today. Shown below is the location of the login attempt: \n\n" + get_ip() + "\n\nIf you'd like to change your password, please click forget password (WIP) on the EasiStock program and you will be sent a OTP (One-Time-Password) to change your password. \n\nBest Regards, \nEasiStock."
                               to = sel_email
                               send_email(to, subject, body, "lock")
                               Lockout.deiconify()

               else:
                    tries = tries + 1
                    messagebox.showerror("Error", "The User or Password is incorrect, please try again.")
                    password.delete(0, 'end')
                    user.delete(0, 'end')
                    if tries == 5:
                       Login.withdraw()
                       Lockout.deiconify()

                           
           if len(sel) > 4:
               tries = tries + 1
               messagebox.showerror("Error", "The User or Password is incorrect, please try again.")
               password.delete(0, 'end')
               user.delete(0, 'end')
               if tries == 5:
                   Login.withdraw()
                   Lockout.deiconify()

    def event(user, pss):
        db_login_check(user,pss)
    def pres_check(user):
        if len(user.get()) == 0:
            messagebox.showerror("Error", "Please input your username to reset your password.")
        else:
            pass_reset_email(user, password_bt, Login_bt)

    Login_bt = tk.Button(Login, text = "Login", height = 1, width = 20, bg = "grey20", fg = "white", activebackground ='grey80', relief = "ridge", command = lambda: db_login_check(user, password_bt))
    reset_pass = Button(Login, text = "Forgot Password", height = 1, width = 20, bg = "grey20", fg = "white", activebackground= "grey80", relief = "ridge", command  = lambda: [pres_check(user)])
    Login.bind('<Return>',  lambda x: [event(user, password_bt)])

    logo.place(x=340,y=100)
    stock_done.place(x=405, y=190)
    fast.place(x=534, y=190)
    user.place(x=438, y=270)
    user_label.place(x=376, y=268)
    password_bt.place(x=438, y=300)
    pass_label.place(x=378, y=300)
    Login_bt.place(x=425, y=325)
    reset_pass.place(x=425, y = 355)

    Login.deiconify()

# ==============================================================================> /\ Login

hold = input("Press Enter to Begin.")

