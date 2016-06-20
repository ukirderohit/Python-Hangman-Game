import loginwork

loginwork.menu()
status = loginwork.user()
if status == 'Success':
    print "Game starts in hangman.py"