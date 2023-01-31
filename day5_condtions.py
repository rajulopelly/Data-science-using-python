"""
conditional statements
if

if(cond):
    statements
    
if else
elif
nested
"""
n1=6.2
n2=5.4
if(n1>n2):
    print(n1," is greater")
else:
    print(n2," is greater")

"""
Assignments
1.to check whether the number is even
2.To check whether the number is odd
3.To check whether the number is positive
4.To check whether the number is negative
5.To check whether the number is divisible by both 5 and 11
"""

num=int(input("enter the number "))
if(num%5==0 and num%11==0):
    print(num," is divisible by both 5 and 11")
else:
    print(num," is not divisible by both 5 and 11")
"""
find the denomination of(2000,500,200,100,50) given amount
ex:2650
no.of 2000rs. notes=1
no.of 500 notes=1
no.of 100 notes=1
no of 50rs.notes=1
"""
amnt=int(input("enter the amount "))
if(amnt>=2000):
    note2k=int(amnt/2000)
    amnt=amnt-note2k*2000
    print("no.of 2k notes=",note2k)
print("remaining amount=",amnt)
