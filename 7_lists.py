"""
s1=input("enter data:")
l1=len(s1)-1
rev=" "
while(l1>=0):
    rev=rev+s1[l1]
    l1=l1-1
print("reverse=",rev)
"""
#Lists
l1=[]
l2=[101,102,103]
l3=["sree","sri","Ram"]
l4=[5400,50000,5600.450,35400,250]
print(type(l4))
"""
for k in l4:
    print(type(k))
list functions
append()
extend()
insert()
index()
sort()
min()
max()
reverse()
copy()
count()
"""
#l1.append(l2)
print(l1)
l1.extend(l2)
l1.extend(l3)
print(l1)
l1.insert(0,"Raj")
print(l1)
print(l1.index("Raj"))

print(l1.count("Sree"))
l1.reverse()
print(l1)
print("Raj" in l1)

sal=[45000,34500,1200,65300]
"""
1.find min element
2.find max element
3.add 500 to each element and print it as list
4.find sum of sal who are getting more than 20000
"""
m=sal[0]
for v in range(len(sal)):
    if(m>sal[v]):
        m=sal[v]
print("minimu=",m)
"""
for k in range(len(sal)):
    sal[k]=sal[k]+500
print(sal)
"""
sal_up=[i+1000 for i in sal if i<2000]
print(sal_up)






    









