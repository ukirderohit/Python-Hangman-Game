import re
import os
import string

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
            print(" @@@@ Username should be greater than 8 character @@@@ ")
            print("")
            username = raw_input("  Enter your Username :    ")
            length = len(username)
            if length < 8:
                continue
            print("")
            print(" @@@@ Password should greater than 8 character @@@@ ")
            passwd = raw_input("  Enter your Password  :     ")
            plen = len(passwd)
            if plen < 8:
                continue
            repasswd = raw_input("  Re-Enter your Password :   ")
            match = re.search(repasswd,passwd)
            if match:
                print("         !!! Password Matched !!!      ")
                
            else:
                print(" @@@@ password did not matched @@@@ ")
                os.system('cls')
                continue
            print("")
            print("  Security code should must be greater than 4 character ")
           
            security = raw_input(" Enter your Security code to recover or reset password : ")
            s  = len(security)
            if s > 4:
                data.append([username,passwd])
                secdata.append(security)
                d.append([username,passwd])
            else:
                print(" The length is not greater than 4 character ")
                continue
            for i in data:
                t = i
            print("")
            print(" ------------------------------------------------ ")
            print("        The Username is : ", t[0])
            print("        The password is : ", t[1])
            print(" ------------------------------------------------- ")
            print("")
            conf = int(raw_input(" For confirmation press 1 :  "))
           
            if conf == 1:
                print("     !!!!!!!!!       Regristration successful    !!!!!!!")
                print("")
                print("")
                
                
            else:
                data.remove([username,passwd])
                d.remove([username,passwd])
                continue 
            

            if [username,passwd] in data:
                os.system('cls')
                break
        while True:
            print(" ********************************************** ")
            print("              Login Portal    ")
            print(" ********************************************** ")
            print("")
            username = raw_input("Please Enter your Username : ")
            passwd = raw_input("Please Enter your password : ")
            print("")
            if [username,passwd] in data:
                print("")
                print(" -------------------------------- ")
                print("        Welcome  " , username.upper())
                print(" -------------------------------- ")
                break
            else:
                print(" @@    Invalid Creditinals     try again... @@ ")
                print("")
                attempt = int(raw_input("For reset password press 1 and to @@@try again.. press 2 : "))
                os.system('cls')
                if attempt == 1:
                    security = raw_input("Enter your security number : ")
                    if security in secdata:
                        new_passd = raw_input("Enter your new Password : ")
                        data.append([username,new_passd])
                        print(" Password Updated Successfully ")
                        break
                
                    else:
                        print(" Security code is wrong your account is blocked ") 
                        break

    elif choice == 2:
        print(" Welcome to Login !! ")
        print("")
        while True:
            username = raw_input("Enter your Username : ")
            passwd = raw_input("Enter your password : ")
            if [username,passwd] in data:
                print("Welcome ", username.upper())
                break
            else:
                print(" Invalid creditinals @@try again .. " )
                user = int(raw_input("To reset your password press 1 and to try again press 2: "))
                os.system('cls')
                if user == 1:
                    security = raw_input("Enter your security number : ")
                    if security in secdata:
                        new_passd = raw_input("Enter your new Password : ")
                        data.append([username,new_passd])
                        print(" Password Updated Successfully ")
                        break
                    else:
                        continue
    elif choice == 3:
        print("Good bye !!!! ")
        exit()
    elif choice > 3:
        print("Invalid choice !!!!  Program is terminating ")
                





    

        
                 
    



database()
menu()
user()
