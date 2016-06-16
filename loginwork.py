import re
import os
import string
import csv

def database():
    global data
    global d,secdata
    data = [['admin','admin']]  #default creditinals
    secdata = ['12345']
    d = []

def menu():  
    print(" ****  Welcome to Login Portal **** ")
    print("")  
    print("1.New Client")
    print("2.Existing Client")
    print("3.Exit")
    print("")
	
	
def user():
    global choice 
    choice = int(raw_input("Enter your Choice Please : "))
    if choice == 1:
        while True:
            os.system('cls')
            print(" ************************************************** ")
            print("          !!! Welcome to Registration !!!      ")
            print(" ************************************************** ")
            firstname = raw_input("First Name :    ")
            lastname = raw_input("Last Name :    ")
            emailid = raw_input("Email :    ")
            phoneno = int(raw_input("Phone Number :    "))
            print(" @@@@ Username should be greater than 8 character @@@@ ")
            print("")
            username = raw_input("  Enter your Username :    ")
            length = len(username)
            if length < 8:
                continue
            print("")
            print(" @@@@ Password should greater than 8 character @@@@ ")
            passwd = raw_input("Enter your Password  :     ")
            plen = len(passwd)
            if plen < 8:
                continue
            repasswd = raw_input("Re-Enter your Password :   ")
            match = re.search(repasswd,passwd)
            if match:
                print("         !!! Password Matched !!!      ")
                with open("Book1.csv", "ab") as csvfile:
					writerds = csv.writer(csvfile)
					writerds.writerow([firstname,lastname,emailid,phoneno,username,passwd])
					csvfile.close()
					menu()# Game should start here
					return False
					
            else:
                print(" @@@@ password did not matched @@@@ ")
                os.system('cls')
                continue
            print("")
database()
menu()
user()