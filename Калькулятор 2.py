a = float (input("NUM 1 \n"))
b = float (input("NUM 2 \n"))
w = float (input("NUM 3 \n"))
c = input("RAW \n")
r = 0
if c=="+":
    r=a+b+w
elif c=="-":
    r=a-b-w
elif c=="*":
    r=a*b*w
elif c=="/":
    r=a/b/w
print (r)