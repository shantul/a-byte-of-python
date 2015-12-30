def func():
    global x, y

    x = 2
    y = x

    print "x is", x
    print "changed local x to", x

    print "y is", y


func()

print y
print "global x is now", x
