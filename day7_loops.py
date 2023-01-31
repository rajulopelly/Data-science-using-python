"""
Loops
while
for
"""
"""
s=0
i=1
while(i<=5):
    s=s+i
    i=i+1
print("sum=",s)

j=5


while(j>=1):
    print(j)
    j=j-1
"""
#print 1 to 5,but after reaching 3,exit the loop
"""
i=1
while(i<=5):
    if(i==3):
        break
    print(i)
    i=i+1
j=1
#print 1 to 10 numbers excpet 4
while(j<=10):
    
    if(j==4):
        j=j+1
        continue
    print(j)
    j=j+1
    """
"""
1.sum of even numbers in between 1 to 10
2.sum of odd numbers in between 1 to 10
3.sum of odd numbers except 5 in a given range
4.find ncr and npr
5.find sum of first and last digit in a given number(ex:243.output:2+3)
"""
"""
i=1
s=0
while(i<=10):
    if(i==6):
        i=i+1
        continue
    if(i%2==0):
        print(i)
        s=s+i
    i=i+1
"""
#factorial of given number
"""
num=int(input("enter the number:"))
f=1
print("sum=",s)
"""

"""
for var in range(start,end,step)

for k in range(6):
    print(k)
"""
"""
nested loop(loop within the loop)

num=int(input("enter number:"))
for k in range(num,num+1):
    for j in range(1,11):
        print("%d*%d=%d"%(k,j,k*j))
"""
for k in range(1,4):
    for j in range(1,k+1):
        print(j,end=" ")
    print("\n")
"""
To print alphabets
"""
c='A'
print(ord(c))
for k in range(1,4):
    c1=ord(c)
    for j in range(1,k+1):
        print(chr(c1),end=" ")
        c1=c1+1
    print("\n")

