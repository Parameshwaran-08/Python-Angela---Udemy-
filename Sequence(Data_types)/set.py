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

sett = {1,2,5}
print(sett)
print(type(sett))


sett.add(3)
print(sett)

sett.remove(5)
print(sett)

# sett.remove(9)    # Remove will give error if the element not in set
# print(sett)

sett.discard(9)  # discard will not give error like remove
print(sett)

# print(sett.pop())  # pops elements randomly bcoz of set unorderedness

# print(sett.clear())  #clears the set

# del sett  - #deletes the set

for i in sett:
    print(i)
    
sett2 = {i*2 for i in sett if i%2 !=0}
print(sett2)

sett.update(sett2)   #like extend in lists
print(sett)

set3 = sett.union(sett2)
print(set3)

x={1,2,3}
y={4,5,6,3}
x.intersection_update(y)
z=x.intersection(y)
print(x)
print(z)

m={1,2,3}
n={4,5,6,3}
m.symmetric_difference_update(n)
o=m.symmetric_difference(n)
print(m)
print(o)

l={1,True}  #(1 and true , 0 and false are considered duplicates)
print(l)