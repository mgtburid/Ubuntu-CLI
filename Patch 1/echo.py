# project's core

import redirection                                      #importing the file responsible
                                                        #for redirections to files
class echo:
    echow = "echo"
    append = ">>"
    overwrite = ">"

class User:
    name = str(input("Enter the username: "))           #accepts input from a keyboard
    host = "@"                                          #delimiter between usrnm and hstnm
    hostname = str(input("Enter the hostname: "))       #accepts input from a keyboard
    umode = "~$ "                                       #regular user mode marker
    rmode = "# "                                        #root user mode marker

usrnm = User.name                                       #is entered manually from the keyboard
hst = User.host                                         #a @ delimiter
hstnm = User.hostname                                   #is entered manually from the keyboard
umode = User.umode
rmode = User.rmode                                      #superuser mode. Currently not used

while True:                                             #makes code run forever
    x = str(input(usrnm+hst+hstnm+umode))
    
    if (x == "exit" or x == "Exit"):
        break
    elif (echo.echow in x and echo.append in x):
        redirection.outappend(x)                        #redirection.py append function
    elif (echo.echow in x and echo.overwrite in x):
        redirection.outoverwrite(x)                     #redirection.py overwrite function
