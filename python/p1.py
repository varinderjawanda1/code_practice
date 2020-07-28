#Ints and concatenation
int1 = 4
int2 = 2
int3 = int1 + int2
print int3
int4 = int1 - int2
print int4
int5 = int1 * int2
print int5
int6 = int1/int2
print int6

#strings and concatenation

string1 = 'Varinder'
print string1
string2 = 'Jawanda'
print string2
print string1 + string2
string3 = 'Jot'
print string3
string4 = 'Jawanda'
print string4
# for some reason below print is not printing values
print 3*("""int3 + int4 + int5 + int6 \nstring3 + string4\n""")

#list and concatenation and nesting

list = [1, 2, 3]
print list[1]
newlist = list + [4, 5, 6]
print newlist[:]
newlist.append(7)
print newlist[:]
newlist2 = [11, 12,13]
newlist3 = [newlist, newlist2]
print newlist3[:]

#if then else

if int6 <= 0:
    print int6
else:
    print int2

