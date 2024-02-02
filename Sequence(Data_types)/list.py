"""   
     Contents :
          1) Accessing the elements
          2) Change/Update/Remove the elements
          3) Add/remove/delete the elements
          4) Looping the datatype (both loops)
          5) Comprehension
          6) Sorting
          7) Copying
          8) Joining
          8) Duplicate removal (if needed)
          9) Using datatype in-built methods

"""


lis = [1,2,2,3,3,4,4,4,4,5]
for i in lis[:]:
    if lis.count(i)>1:
        del lis[i]
print(lis)


print(list(set(lis)))


new_lis = []
for i in lis:
    if i not in new_lis:
        new_lis.append(i)
print(new_lis)


index = 0
while i not in new_lis:
    new_lis.append(lis[index])
    index+=1
print(new_lis)


length = len(lis)
index = 0
while index < length-1:
    count = lis.count(index)
    if count>1:
        for _ in range(count-1):
            del lis[index]
    index+=1
print(lis)


# INSERTION SORT (using while loop)

lis = [2,1,5,3,7,10,9,11,6,99999]
index = 0
while index < len(lis)-1:  #(0 to n-1)
    pos = index+1
    while pos < len(lis): #(1 to n)
        if lis[index]>lis[pos]:
            lis[index],lis[pos]=lis[pos],lis[index]
        pos +=1 
    index+=1
print(lis)


# BUBBLE SORT (using while loop)

lis = [2,1,5,3,3]
index = 0
while index < len(lis)-1:
    pos = 0 
    while pos < (len(lis)-index-1):
        if lis[pos]>lis[pos+1]:
            lis[pos],lis[pos+1]=lis[pos+1],lis[pos]
        pos+=1
    index+=1
print(lis)


nums=[1,2,3,4,5,6,7,8,9,10]
even_nums = [num for num in nums if num != 5]
print(even_nums)


# Matrix using comprehension

mat = [[k for k in range(1,4)] for i in range(3)]
print(mat)


a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)


a= ["s","b","c"]
c=""
for i in a:
    c+=i
print(c)


b= "".join(a)
print(b)


c= "".join([str(i) for i in a])
print(c)


lis = [1,2,3,4,5]
print(lis)


print(lis[0:-3])


lis[2]=25
print(lis)


lis.append(6)
print(lis)


lis.remove(25)
print(lis)


del lis[0]
print(lis)


lis.insert(0,1)
print(lis)


lis.insert(2,3)
print(lis)


del lis[-1]
print(lis)


for i in lis:
    print(i,end = " ")
print()


for i in lis:
    print(lis.index(i),end=" ")
print()

for i in lis:
    print(f"Num : {i }, Count : {lis.count(i)}")
    
lis2= lis[:]
print(lis2)

lis3 = lis.copy()
print(lis3)

lis.reverse()
print(lis)

lis.reverse()
print(lis)

print(lis[::-1])
print("\n")


# INSERTION SORT (using for loop)

k = [2,4,3,5,1,6]
# k.sort()
# print(k)

for i in range(len(k)-1):
    for m in range(i+1,len(k)):
        if k[i]>k[m]:
            k[i],k[m]=k[m],k[i]
print(k)