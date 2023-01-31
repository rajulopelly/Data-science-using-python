"""
1.find factorial of given number
2.find ncr
3.find npr
def fact(n):
    f=1
    while(n!=0):
        f=f*n
        n=n-1
    return f
#funciton call
n=int(input("enter n:"))
r=int(input("enter r:"))
#print(fact(num))
#ncr=n!/(n-r)!*r!
res=fact(n)//(fact(n-r)*fact(r))
print(res)
"""
#passing an array through the function
sal=[45000,45600,25400,12500,5400,43500]
def salGr20k(s):
    s1=[]
    for k in s:
        if(k>20000):
            s1.append(k)
    return s1
#function call

print(salGr20k(sal))

"""
1.find prime number using function
2.find prime numbers in a given range
3.find prime digits in a given number
4.find perfect number in a given number
"""


        

    






