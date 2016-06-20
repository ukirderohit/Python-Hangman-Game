"""=============================================================================
# Script Name	: hangman.py
# Author			: Rohit Shankarrao Ukirde
# Created			: 15th June 2016
# Last Modified	: 20th June 2016

# Description		: This program will run first then it will direct to Login, 
after authenticating user it will run. It has Command Line Interface
============================================================================="""

import loginwork

loginwork.menu()
status = loginwork.user()
if status == 'Success':
    print "Game starts in hangman.py"