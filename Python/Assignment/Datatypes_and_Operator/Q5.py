a = 100
b = 200

lsit1 = [1,2,3]

list2 = [1,2,3]

print("ID of a : ",id(a))
print("ID of b : ",id(b))

print(a is b)
print(a is not b) 

print("Id of list1 :" ,id(lsit1))
print("Id of list1 :" ,id(list2))
print(lsit1 is list2)
print(lsit1 is not list2)