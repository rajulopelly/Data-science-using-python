"""
Anonymous function
"""
"""
def primeDigits(num):
    while(num>0):
        f=0
        r=num%10
        for c in range(2,r):
            if(r%c==0):
                f=1
                break
        if(f==0):
            print(r," is a prime")
        else:
            print(r," is not a prime")
        num=num//10
num=int(input("Enter the number:"))
primeDigits(num)
"""
#addition of three numbers
def addT(n1,n2,n3):
    return n1+n2+n3

print(addT(2,3,4))

ad=lambda n1,n2,n3:n1+n2+n3
print(ad(2,3,4))


#fahrenheit to celsius and vice versa without lambda function
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)
F=map(fahrenheit, temp)
#f1=(102.35,97.24,98.54,100.98989)
#C=map(celsius,f1)
print(list(F))	#print object generator at 0x999
f_t=map(lambda T:(float(9)/5)*T + 32,temp)
print(list(f_t))

"""
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "EinfÃ¼hrung in Python3, Bernd Klein",3,24.99]]
Write a Python program, which returns a list with tuple.
Each tuple consists of a  order number and
the product of the price per items and the quantity.
The product should be increased by 10,- €
if the value of the order is less than 100.00 €.
Write a Python program using lambda and map.

"""











