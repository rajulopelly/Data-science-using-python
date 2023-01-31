"""
dictionary
keys()
get()
update()
copy()
items()
zip()
"""
d1={"sno":[2,3,4],"sname":["sree","sri","Rock"],3:[21,34.5,89.45]}
print(d1.keys())

#Accessing dictionary elements
print(d1["sno"])

for k in d1:
    print(k,":",d1[k])
#manipulation of dictionary
d1["addr"]=["Hyd","Sec","Pune"]
print(d1)
#To delete key and values
del d1[3]
print(d1.get("sno"))

for k,v in d1.items():
    print(k,":",v)
d1.update({"phone":[7878,9090,57657,435]})
d1.update({"phone":987})
print(d1)

username=("user1","user2")
pwds=["pwd12","pwd23"]

d_users=zip(username,pwds)
print(dict(d_users))

l1=[2,3,4]
d_l={i:i*i for i in l1}
print(d_l)















