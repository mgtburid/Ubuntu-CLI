def outoverwrite(x):
    x = x.split(">")                                    #splits user input so there are parts [0]. [1]
    x[0] = x[0].replace("echo ", "")                    #removes "echo" in the STDOUT
    x[1] = x[1].replace(" ", "")                        #removes blank space before the filename
    file = open(x[1], "w")                              #gets file in the append mode
    file.write(x[0]+"\n")                               #\n adds a new line after appending

def outappend(x):
    x = x.split(">>")                                   #splits user input so there are parts [0]. [1]
    x[0] = x[0].replace("echo ", "")                    #removes "echo" in the STDOUT
    x[1] = x[1].replace(" ", "")                        #removes blank space before the filename
    file = open(x[1], "a")                              #[1] is everything that comes after >/>>
    file.write(x[0]+"\n")                               #[0] is everything that comes before >/>>
