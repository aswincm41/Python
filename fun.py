#local variable
def f():
    a="spectrum"
    print(a)
f()

def f():
    s="kerala"
    print(s)
f()

def f():
    a="kochi"
    print(a)
f()

def f():
    s=20
    print(s)
f()

#global variable
def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is "+x)

def ifunc():
    global a
    a="god's own country"
ifunc()
print("kerala" +a)

def gfunc():
    global a,b
    a=10
    b=5
gfunc()
print(a+b)







