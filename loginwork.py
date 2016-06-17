'''=============================================================================
Rohit Shankarrao Ukirde
This file authenticates the user data from csv file
============================================================================='''

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
    print("")
    print("")
    print("")
    print(" ****  Welcome to Hangman **** ")
    print("")  
    print("")
    print("1.New - SignUp Here")
    print("2.Login")
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
            firstname = raw_input("First Name :")
            lastname = raw_input("Last Name :")
            emailid = raw_input("Email :")
            phoneno = int(raw_input("Phone Number :"))
            print(" @@@@ Username should be greater than 8 character @@@@ ")
            print("")
            username = raw_input("  Enter your Username :")
            length = len(username)
            if length < 8:
                continue
            print("")
            print(" @@@@ Password should greater than 8 character @@@@ ")
            passwd = raw_input("Enter your Password  :")
            plen = len(passwd)
            if plen < 8:
                continue
            repasswd = raw_input("Re-Enter your Password :   ")
            match = re.search(repasswd,passwd)
            if match:
                print("         !!! Password Matched !!!      ")
                conf = int(raw_input(" For confirmation press 1 :  "))
                if conf == 1:
                    print("")
                    print("")
                    print("     !!!!!!!!!       Regristration successful    !!!!!!!")
                    print("")
                
                    with open("hangman.csv", "ab") as csvfile:
                        writerds = csv.writer(csvfile)
                        writerds.writerow([firstname,lastname,emailid,phoneno,username,passwd])
                        csvfile.close()
                        menu()# Game should start here
                        return False
                else:
                    menu()
                    return False
					
            else:
                print(" @@@@ password did not matched @@@@ ")
                os.system('cls')
                continue
            print("")
    elif choice == 2:
        os.system('cls')
        print("")
        print("")
        print(" Welcome to Hangman !! ")
        print("")
        while True:
            username1 = raw_input("Enter your Username : ")
            passwd1 = raw_input("Enter your password : ")
            FileOpen = open("hangman.csv","rb")
            FileRead = csv.reader(FileOpen, delimiter = ',')
            FileRead.next() #skip first line
            text=[]
            text1=[]
            for row in FileRead:
                text = row[4]
                text1 = row[5]
                if (text in username1) and (text1 in passwd1) :
                    print "Success"
                    
                    menu()
                    user()
                    return False
                else:
                    i=0
            if i==0:
                i=1
                print "Incorrect username and Password"
                
                continue
database()
menu()
user()