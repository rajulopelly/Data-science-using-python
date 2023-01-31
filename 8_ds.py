"""
Data structure
"""
l1=[2,3,4]
l1.pop()
print(l1)
"""
implement stack using list functions
i.e insert 10 elements dynamically onto the stack
and delete 4 elements

st=[]
n=int(input("enter the range:"))
for i in range(n):
    st.append(int(input("enter element:")))
print(st)

for j in range(3):
    st.pop()
print(st)
"""

#queue(FCFS)
queue=[2,5]
queue[0]=45
print(queue[0])
queue.insert(1,6)
print(queue)
#queue.pop()
queue.insert(3,8)
print(queue)
"""
queue.insert(1,6)
queue.insert(0,25)
print(queue)
"""



