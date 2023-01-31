"""
1.Ask the user to enter rate per hour in integer and number of hours.
A security agency pays to their staff as per the tariff given below:
	Hours					Rate
For first 48 hours in a week			Rs. K per hour
For next 8 hrs in a week 			Rs.1.25K per hour
For further hours in a week 			Rs.1.5K per hour

2.The school office collects the monthly fee(including tution fee and miscellaneous fee)
of the students as per the given tariff:
Calss			Tution Fee			Miscellaneous Fee
Std I- std V		Rs.800				15% of Tution Fee
Std VI- std X		Rs.1000			20% of Tution Fee
Std XI- std XII	Rs.1200			25% of Tution Fee
Write a program to accept the class at the time of payment. display the total fee collected.

k=int(input("enter rate:"))
hrs=int(input("enter hrs:"))
if(hrs<=48):
    tot_price=k*hrs
elif(hrs>48 and hrs<=56):
    tot_price=48*k+(hrs-48)*1.25*k
elif(hrs>56):
    tot_price=48*k+(hrs-48)*1.25*k+(hrs-56)*1.50*k
print("total payment:",tot_price)
"""
"""
#nested if
n1=int(input("enter num1 "))
n2=int(input("enter num2 "))
n3=int(input("enter num3 "))
if(n1>n2):
    if(n1>n3):
        print(n1," is greater")
    else:
        print(n3," is greater")
elif(n2>n3):
    print(n2," is greater")
else:
    print(n3," is greater")
    """
n1=int(input("enter num1 "))
n2=int(input("enter num2 "))
n3=int(input("enter num3 "))
if(n1>n2 and n1>n3):
    print(n1," is greater")
elif(n2>n1 and n2>n3):
    print(n2," is greater")
elif(n3>n1 and n3>n2):
    print(n3," is greater")
else:
    print("all r equal")



