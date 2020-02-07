import echo                                             #redirection module is not imported
                                                        #because it is imported in echo module
import cat

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
    echo.work(x)                                        #work function in echo module is called here
    if "cat" in x:                                      #lets cat module work
        cat.work(x)
    elif "sudo su" in x:                                #lets the user enter root mode. However, this
        x = str(input(usrnm+hst+hstnm+rmode))           #implementation is to be reworked yet
        echo.work(x)
    elif "exit" in x:                                   #stops the entire project or exists the rmode
        break
