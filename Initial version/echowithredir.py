# echo with redirection functionality

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
hst = User.host                                         #an @ delimiter
hstnm = User.hostname                                   #is entered manually from the keyboard
umode = User.umode
rmode = User.rmode                                      #superuser mode. Currently not used

x = str(input(usrnm+hst+hstnm+umode))
if (echo.echow in x and echo.append in x):
    x = x.split(">> ")                                  #splits user input so there is a part [0]
    x[0] = x[0].replace("echo ", "")                    #gets rid from "echo" in the STDOUT
    file = open(x[1], "a")                              #with the command itself and a part [1]
    file.write(x[0]+"\n")                               #where it should be put
elif (echo.echow in x and echo.overwrite in x):
    x = x.split("> ")                                   #same here, yet it overwrites not appends
    x[0] = x[0].replace("echo ", "")
    file = open(x[1], "w")
file.write(x[0]+"\n")
