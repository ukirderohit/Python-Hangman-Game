"""=============================================================================
# Script Name	: loginwork.py
# Author			: Rohit Shankarrao Ukirde
# Created			: 15th June 2016
# Last Modified	: 18th June 2016

# Description		: This will go through Login, has Command Line Interface 
Password is hidden from user
This file authenticates the user data from csv file
============================================================================="""

import re
import os
import string
import csv
import getpass #to hide characters for password ,Which will get the password while displaying nothing


def menu(): 
    """This is Login Menu"""
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
    """Registration Menu - This automates according to the user input"""
    global choice 
    choice = int(raw_input("Enter your Choice Please : "))
    if choice == 1:
        """New Sign-UP here"""
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
            passwd = getpass.getpass("Enter your Password  :")
            plen = len(passwd)
            if plen < 8:
                continue
            repasswd = getpass.getpass("Re-Enter your Password :   ")
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
                        """CSV file is handled here"""
                        writerds = csv.writer(csvfile)
                        writerds.writerow([firstname,lastname,emailid,phoneno,username,passwd])
                        csvfile.close()
                        return 'Success'
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
        """Login Here"""
        os.system('cls')
        print("")
        print("")
        print(" Welcome to Hangman !! ")
        print("")
        while True:
            username1 = raw_input("Enter your Username : ")
            passwd1 = getpass.getpass("Enter your password : ")
            FileOpen = open("hangman.csv","rb")
            FileRead = csv.reader(FileOpen, delimiter = ',')
            FileRead.next() #skip first line
            text=[]
            text1=[]
            for row in FileRead:
                text = row[4]
                text1 = row[5]
                if (text in username1) and (text1 in passwd1) :
                    return 'Success'
                    return False
                else:
                    i=0
            if i==0:
                i=1
                print "Incorrect username and Password"
                
                continue
    elif choice == 3:
        """Exit"""
        print("Good bye !!!! ")
        exit()
    elif choice > 3:
        """IF choice entered more than 3 it will exit"""
        print("Invalid choice !!!!  Program is terminating ")

# menu()
# user()