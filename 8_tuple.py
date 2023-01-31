"""
tuple
"""
t1=(12,56,90)
print(t1)
#t1[0]=34
print(t1)
l1=list(t1)
l1.append(35)
print(l1)
t1=tuple(l1)
print(t1)

t1_up=(i+5 for i in t1)
t1=t1_up
print(tuple(t1_up))
