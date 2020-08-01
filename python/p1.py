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
x = len(y)
def a():
    print y
    for i in range(x):
        if i %  2:
            return y[i]