def leapyr(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            print("yes")
    elif n%4!=0:
        print ("no")
    else:
        print("invalid")
