# main indents = 80 col |  sub indents = 60 col |  description = 83 col (text) ###
import datetime
import time
import sqlite3
import string
from datetime import datetime
from os import system

# ==============================================================================> /\ Module Imports

# ==============================================================================> \/ Variables and other
# this is where all variables are defined and ready to be utilised by any function so
# long as they are globalised, by having all variants in one section, they are easy
# to manage and cleaner :)

system("title " + "EasiStock Database Creation Tool")

conn = sqlite3.connect("EasiStock_Database.db")

c = conn.cursor()

global d1
global d2
today = datetime.now()
d1 = today.strftime("%d/%m/%y")
d2 = today.strftime("%d/%m/%y")
d3 = today.strftime("%H : %M : %S")


# ==========================================================> \/ Password checking and/or creation (SmartVar Technology)
# A method to keep password databases secure and sturdy, will try
# an initial selection to see if it exists, if not (exception) it then
# creates the table along with a root record as usual.

try: # tries initially to select all records from the table, "Users"
    c.execute('''
                    SELECT * FROM Users
                    ''')
    conn.commit()
    sel = c.fetchall() # a shortened variables to fetch results

except: # if a database doesn't exist, it should raise an error, if so, it creates an entity
    c.execute('''
                    CREATE TABLE IF NOT EXISTS Users (
                    [user] TEXT PRIMARY KEY, 
                    [f_name] TEXT NOT NULL,
                    [l_name] TEXT NOT NULL,
                    [reg_date] BLOB NOT NULL,
                    [pass] TEXT NOT NULL)
                    ''') # TEXT = Is simply letters, 
    conn.commit() # saves the changes

    values = [("21DoniLa", "larry", "doni", "21-05-12", "pass1"), # this is an array of values that /will/ be used with the variable below
              ("15DedgjJa", "Jason", "Dedgj", "15-05-12", "pass2")] 
    insertion = ('''INSERT INTO Users VALUES (?, ?, ?, ?, ?)''') # by splitting parameters into seperate variables, it allows for multiple values to be insterted at a time

    conn.executemany(insertion, values) # executemany combines these in order to make the params work
    conn.commit()



# ==========================================================> \/ Smart-Var Techology - Product Presence Check
# A method to keep python variables persistent across executions.
# Tries to validate existence and changed variable states
# depending on the outcome of said command.

try:
    c.execute("SELECT * FROM Products")
    is_crt = True # Statement of if DB has been Created -------------------------|
    is_add = True # A debug variable to check if anything has been added.|
    is_del = False # Presence check, if true, has been deleted. ---------------|

except:
    is_crt = False
    is_add = False
    is_del = True

# =================================> \/ Rest of Variables

is_admin = False
sel_con = False
admin_tries = 3

# =============> \/ User Reg Variables

min_num = False # Conditions for whether or not user input has passed said validation checks |
max_num = False # -------------------------------------------------------------------------------------------|
user_first = False # Conditions for whether or not the user inpuit has fully passed validation |
user_last = False # -----------------------------------------------------------------------------------------|

year = datetime.today() # captures the day for use in user creation |
today = year.strftime("%y") # ----------------------------------------------------|


# ==============================================================================> \/ MAIN
# The main hub for non admin users, contains ability to Creat, View and delete
# database which require little skill or knowledge, appropiate for mid - level
# or single-manned businesses.

def Main():
    global is_admin 
    q1 = input ("\n\n1 - Create Database \n2 - View Database \n3 - Delete Database \n4 - Advanced\n5 - Quick Exit \n") # Ask user for permission to create database.

    if q1 == "1": # 1 - Create Database
        if is_crt == False: # Initially checks if db has been created |
            db_creation() # ----------- Smart-Var Technology--------------|
        if is_crt == True: # If it has, it returns error message ---------|
            print("Sorry, a database already exists")
            Main()


    if q1 == "2": # 2 - View Database
        if is_crt == False: 
            print("Sorry, no database exists.") 
            Main()
        if is_crt == True: 
            db_view()

    if q1 =="3": # 3 - Delete Database
        if is_crt == False:
            print("Sorry, there is no database to delete.")
            Main()
        if is_crt == True:
            db_del()

    if q1 == "4": # 4 - Admin Panel 
        if is_admin == True:
            admin_menu()
        if is_admin == False:
            login_admin()

    if q1 == "5": # 5 - Quick Exit 
        exit()

    else:
        print("Invalid Text, please try again.") # Basic error check.
        Main()

# ==============================================================================> \/ Create

def db_creation():
    global is_crt
    global is_del
    global is_add


    print("\nCreating Table...")
    time.sleep(0.5)
    
    c.execute('''
                    CREATE TABLE IF NOT EXISTS Products (
                    [product_id] INTEGER PRIMARY KEY,
                    [product_name] BLOB NOT NULL,
                    [product_count] INTEGER NOT NULL,
                    [product_price] BLOB NOT NULL,
                    [product_desc] BLOB,
                    [date_made] INTEGER NOT NULL,
                    [last_change_day] INTEGER NOT NULL,
                    [last_change_time] INTEGER NOT NULL)
                    ''')
    conn.commit()
    is_crt = True
    is_del = False
    
    print("\nTable has been created.")
    print("Adding Root Record")
    time.sleep(1)

    values = [(None, "Root Record", "255", "£5.00", "Root Record Description Test, very good product!", d1, d2, d3), # this is an array of values that /will/ be used with the variable below
            (None, "Root Record2", "255", "£5.00", "Root Record Description Test, very bad product!", d1, d2, d3)]

    insertion = ('''INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?, ?, ?)''')

    conn.executemany(insertion, values) # executemany combines these in order to make the params work
    conn.commit()
    
    print("\nRoot Record has been added.")
    time.sleep(0.5)
    print("\nRetrieving table.")
    time.sleep(0.5)
    is_add = True
    db_view()

# ============================================================================== > \/ Viewing DB

def db_view():

    c.execute('''SELECT * FROM Products''')

    sel = c.fetchall()

    if len(sel) == 0:
        print("No Products found, please contact EasiStock Staff or Reset the program.\n\n\n")

    if len(sel) >= 1:
        for row in sel:
            print(row)

    menu_return()

# ============================================================================== > \/ Deleting DB

def db_del():
    global is_crt
    global is_del
    global is_add
    confirmation = input ("Are you sure you'd like to delete your database? Any data removed cannot be retrieved. \n1 - Yes \n2 - No")

    if confirmation == "1":
        print("\nDeleting Database...")
        time.sleep(1)
        c.execute("DROP table Products")
        conn.commit()
        is_del = True
        is_crt = False
        is_add = False
        print ("\nDeleted!")
        time.sleep(0.5)
        menu_return()
    if confirmation == "2":
        print("Deletion Cancelled.")
        time.sleep(0.4)
        menu_return()

    else:
        print("Invalid input, please try again.")
        db_del()

# ============================================================================== > \/ Admin Login

def  login_admin():
    global is_admin
    global admin_tries
    login = input("\n\nTo enter the Admin Panel, please enter the Admin Password, or press 0 to return to the main menu. \n")

    if admin_tries == 0: # Checks tries first, if it was first user would have one more trie before being locked out.
        print("You have been locked out.")
        time.sleep(1)
        exit()

    if login == "test": # password 0.0
        print("Password Accepted.\n")
        is_admin = True # Used to remember login.
        admin_menu()

    if login == "0":
        print("Returning to main menu")
        Main()

    else:
        print("\nIncorrect password,")
        admin_tries = admin_tries - 1 # Subtracts one from the tries variable, then loops back |
        print("You have ", admin_tries, "tries left.") # -----------------------------------------------------------|
        login_admin() # ----------------------------------------------------------------------------------------------------|

# ============================================================================== > Admin Menu
        
def admin_menu():
    print("Welcome to the Admin Panel.")
    q1 = input ("\n1 - View Users \n2 - Register User  \n3 - Reset Passwords \n4 - Remove Users \n5 - Return to Main Menu \n6 - Quick Exit")
    
    if q1 == "1": # 1 - View Users
        db_sel_users()

    if q1 == "2": # 2 - Register Users
        db_reg_user_FNAME()

    if q1 =="3": # 3 - Reset Users
        db_user_reset()

    if q1 == "4": # 4 - Remove Users
        db_user_delete()

    if q1 == "5": # 5 - Main Menu
        Main()

    if q1 == "6": # 6 - Quick Exit
        exit()

    else:
        print("Invalid Text, please try again.") 
        admin_menu()


# ============================================================================== > \/ View Users

def db_sel_users():
    print("")
    c.execute('''SELECT user, f_name, l_name FROM Users''')

    sel = c.fetchall()

    if len(sel) == 0:
        print("\nNo Users found.\n")
        question = input("Would you like to create a user? \n1 - Yes \n2 - No\n")

        if question == "1":
            db_reg_user_FNAME()

        if question == "2":
            menu_return()

        else:
            print("Invalid input, please try again\n")
            db_sel_users()

    if len(sel) >= 1:
        print("")
        for row in sel:
            print(row)

    print("")
    menu_return()
# ============================================================================== > \/ REGISTATION: L NAME

def db_reg_user_LNAME(First_Name):
    global user_last

    last_name = input ("\nPlease input your Last Name, or enter 0 to return to the main menu. \n ").split()
    last_name = last_name[0]
    
    if last_name == "0":
        menu_return()

    reg_checks(last_name, db_reg_user_FNAME)

    if user_first == True:
        user_reg_db(First_Name, last_name, year) # Feeds info to other function, ready to generate username.
        


# ============================================================================== > \/ REGISTRATION:  F NAME

def db_reg_user_FNAME():
    global user_first
    print("Welcome to the ES User Registration Form.")
    time.sleep(1)
   
    first_name = input ("\nPlease input your First Name, or enter 0 to return to the main menu.\n").split()
    first_name = first_name[0]

    
    if first_name == "0":
        menu_return()

    reg_checks(first_name, db_reg_user_FNAME) # Initiate checking system.

    if user_first == True: # After going through checks, uses variables to determine results.
        db_reg_user_LNAME(first_name) # Proceeds to last name input.

# ============================================================================== > \/ REG CHECKS

def reg_checks(user_input, return_function):
    global user_first
    global user_last
    special_char = "!@#$%^&*()-+?_=,<>/{}[]:;`¬" # Provides a "do not use" list for checking.

    if user_input == "0":
        menu_return()

    if any(c in special_char for c in user_input): # If user input contains stuff from "do not use" list.
        print("Invalid input, you cannot use any special character (! * ; : _ @ . . . ")
        return_function()

    if len(user_input) < 4: # =========> \/ Min Char check
            print("Invalid input, Usernames must be more than 4 characters long.")
            min_num_con = True
            return_function()

    if len(user_input) > 30: # ========> \/ Max Char check
            print("Invalid input, Usernames must be below 30 characters.")
            max_num_con = True
            return_function()

    if min_num == False and max_num == False:# =====> Concluding check
        if user_first == True: # Smart-Var Tech: checks if first name has already been done.
            user_last = True

        if user_first == False:
            user_first = True

# ============================================================================== > \/ REGISTRATION : DB CHECK
                
def user_reg_db(first_name, last_name, year):
    number = 0

    FName = (first_name[0] + first_name[1]) # Example; the input "Jason " is shortened to " Ja "
    year_str = str(year) # Makes the date a string so that it can be shortened
    year_format = (year_str[2] + year_str[3]) # Formats it so 2021-DD-MM turns to just 21.
    
    Username = year_format + last_name.capitalize() + FName.capitalize() # Adds the year (21) with the Last Name (Dedgjonaj) and First Name Formatted (Ja) to make \21DedgjonajJa\

    print("\nYour generated username is", Username, ".")
    confirm_user = input ("Would you like to make changes? \n1 - Yes \n2 - No\n")

    if confirm_user == "1":
        print("\nReturning to creation.")
        db_reg_user_FNAME()

    if confirm_user == "2":
        try:
            values = [(Username, first_name.capitalize(), last_name.capitalize(), year, "password")]
            sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?)"

            conn.executemany(sql, values)
            conn.commit()
            print("\nUser has been registered!")
            db_sel_users()

        except:
            print("")
            number = number + 1 # Fluid Numbering System, loops until the edited username will not clash with data
            exception(first_name, last_name, year, number)

# ============================================================================== > \/ REGISTRATION: DB CHECK - EXCEPTION

def exception (first_name, last_name, year, number):
    
    FName = (first_name[0] + first_name[1] + str(number)) # Example; the input "Jason " is shortened to " Ja " with addtional Copy Number
    year_str = str(year) # Makes the date a string so that it can be shortened
    year_format = (year_str[2] + year_str[3]) # Formats it so 2021-DD-MM turns to just 21.
    Username = year_format + last_name.capitalize() + FName.capitalize()

    print("Sorry, this username is already taken, creating new username")

    try:
            values = [(Username, first_name, last_name, year, "password")]
            sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?)"

            conn.executemany(sql, values)
            conn.commit()
            print("User has been registered! Your username is", Username)
            db_sel_users()

    except:
        number = number + 1
        exception(first_name, last_name, year, number)

# ============================================================================== > \/ Password Reset

def db_user_reset():

    Selection = input ("Please input the FIRST NAME of the User. Or press 0 to return to the main menu.\n")

    if Selection == "0":
        menu_return()

    else:
        c.execute("SELECT user, f_name, l_name FROM Users WHERE f_name LIKE ?", [f"%{Selection}%"]) # Looks for all records that contain the user input, doesn't need to be exact

        sel = c.fetchall()
        for row in sel:
            print(row)

        if len(sel) == 0: # If there are no results, the input was wrong.
            print("\nSorry, no user exists with that name, please check spelling and try again. \n")
            db_user_reset()

        if len(sel) > 1: # If there are more than 1 results, it will need a full username to refine selection.
            Selection2 = input("\nPlease enter the FULL USERNAME of the User\n")

            c.execute("SELECT user, f_name, l_name FROM Users WHERE user = ?", [Selection2])

            sel = c.fetchall()
            for row in sel:
                print(row)

            if len(sel) == 0: 
                print("No results found. Please check spelling, capitalization and try again.")
                db_user_reset()

            if len(sel) == 1: # If there is one result, there is only one user to reset, needs confirmation. 
                confirmation = input("\nIs this the user you'd like to reset? \n1 - Yes \n2 - No\n")
    
                if confirmation == "1":
                    c.execute('''UPDATE Users
                                    SET pass = "password"
                                    WHERE user = ?''', [Selection2])
                    conn.commit()
                    print("\nUser Reset")
                    menu_return()

                if confirmation == "2":
                    print("\nReturning to reset menu.")
                    db_user_reset()

        if len(sel) == 1:
            confirmation2 = input("\nIs this the user you'd like to reset? \n1 - Yes \n2 - No\n")

            if confirmation2 == "1":
                c.execute('''UPDATE Users
                                SET pass = "password"
                                WHERE user = ?''', [Selection2])
                conn.commit()
                print("\n\nUser reset.")
                menu_return()

            if confirmation2 == "2":
                print("\nReturning to reset menu.")
                db_user_reset()

# ============================================================================== > \/ Delete Users

def db_user_delete():

    Selection = input ("\nPlease input the FIRST NAME of the user you'd like to DELETE. Or press 0 to return to the main menu.\n")

    if Selection == "0":
        menu_return()

    if Selection == "":
        print("Please enter a First Name next time.")
        db_user_delete()

    else:
        print("")
        c.execute("SELECT user, f_name, l_name FROM Users WHERE f_name LIKE ?", [f"%{Selection}%"])

        sel = c.fetchall()
        for row in sel:
            print(row)

        if len(sel) == 0:
            print("Sorry, no username exists with that name, please check spelling and try again. \n")
            db_user_delete()

        if len(sel) > 1:
            Selection2 = input("\nPlease input the FULL USERNAME of the user you'd like to DELETE. Please note capitalization applies.\n")

            if Selection2 == "":
                print("Please enter a Username next time.")
                db_user_delete()

            else:
                c.execute("SELECT user, f_name, l_name FROM Users WHERE user = ?", [Selection2])

                sel = c.fetchall()
                for row in sel:
                    print(row)

                if len(sel) == 0:
                    print("No results found. Please check spelling, capitalization and try again.")
                    db_user_delete()

                if len(sel) >= 1:
                    confirmation = input("\nIs this the user you'd like to DELETE? Confirming will delete the user.\n1 - Yes \n2 - No\n")

                    if confirmation == "1":
                        c.execute('''DELETE FROM Users
                                        WHERE user = ? ''', [Selection2])
                        conn.commit()
                        print("\nUser deleted.")
                        menu_return()

                    if confirmation == "2":
                        print("\nReturning to deletion menu.")
                        db_user_delete()
                
                    else:
                        print("\nSorry, please try again.")
                    db_user_delete()

        if len(sel) == 1:
            confirmation2 = input("\nIs this the user you'd like to DELETE? Confirming will delete the user.\n1 - Yes \n2 - No\n")

            if confirmation2 == "1":
                c.execute('''DELETE FROM Users
                                WHERE f_name LIKE ? ''', [f"%{Selection}%"]) # Since we don't have username data, we use the first name data to delete.
                conn.commit()
                print("\nUser deleted.")
                menu_return()

            if confirmation2 == "2":
                print("\nReturning to deletion menu.")
                db_user_delete()
                
            else:
                print("\nSorry, please try again.")
                db_user_delete()

        else:
            print("\nSorry, please try again.")
            db_user_delete()

    
# ============================================================================== > \/ Menu Redirect

def menu_return():
    global is_admin

    if is_admin == True:
        menu_choice = input ("1 - Main Menu \n2 - Admin Menu\n")
        
        if menu_choice == "1":
            print("Returning to Main Menu...\n")
            Main()

        if menu_choice == "2":
            print ("Returning to Admin Menu\n")
            admin_menu() 

        else:
            print("Invalid input, please try again.\n")
            menu_return()

    if is_admin == False:
        print("Returning to main menu...\n")
        Main()
            
        

print("Welcome to the EasiStock Control Panel") # welcome message
print("Public Build v1.0.2")
time.sleep(1)
Main()

