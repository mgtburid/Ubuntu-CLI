import redirection                                      #importing the file responsible
                                                        #for redirections to other files
echow = "echo"
append = ">>"
overwrite = ">"

def split(x):                                           #responsible for usual echo's output
    x = x.split("echo ")
    x = x[1]
    print(x)

def work(x):
    if (echow in x and append not in x and overwrite not in x):     #makes sure there are
        split(x)                                                    #no redirections etc.
    elif (echow in x and append in x):
        redirection.outappend(x)                        #redirection.py append function
    elif (echow in x and overwrite in x):
        redirection.outoverwrite(x)                     #redirection.py overwrite function
