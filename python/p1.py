#exercise 1

x = raw_input("Enter first number:")
y = raw_input("Enter second number:")

x = int(x)
y = int(y)

a = x * y
b = x + y

if a <= 1000:
    print a
else:
    print b

#exercise 2

y = int(raw_input("Enter last number of range:"))

for a in range(y):
    b = a - 1
    c = b + a
    if c > 0:
        print c

#exercise 3

y = str(raw_input("Enter your name:"))
def evenReturn(y):
#    print y
    x = len(y)
#    print x
    for i in range(x):
        if i % 2:
            print y[i]
evenReturn(y)

#exercise 4
n = int(raw_input("Enter alter number:"))
def alterString (y, n):
    x = len(y)
    a = x - n
    print y [a:]

alterString(y,n)

# exercise 5

#x = [int (y) for y in raw_input("Enter values:")]

#print x

#exercise 6

y = "Tom is nice person. Tom help people. Tom lives in USA"
y = str(y)
x = y.count(Tom)
print x

