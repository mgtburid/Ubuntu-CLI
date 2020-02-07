def work(x):
    x = x.split("cat ")                 #"cat " is a delimiter for the whole command dividing the line on two parts
    f = open(x[1], "r")                 #the second part is a filename or path (in the future)
    print(f.read())                     #outputs the content of the specified file
