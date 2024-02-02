"""   
     Contents :
          1) Accessing the elements
          2) Change/Update/Remove the elements
          3) Add/remove/delete the elements
          4) Looping the datatype (both loops)
          5) Comprehension (not for tuples)
          6) Sorting
          7) Copying
          8) Joining
          8) Duplicate removal (if needed)
          9) Using datatype in-built methods
          10) Unpacking and addition of tuples

"""

tup = (1,2,3)
print(tup)

print(type(tup))

print(tup[:])

print(tup[0:1])

tup1=(1,)
print(tup1)
print(type(tup1))

tup1 =list(tup1)
tup1.append(2)  #same for remove,delete,pop
tup1=tuple(tup1)
print(tup1)

tupl = (2,3,1,4)
list(tupl).sort()
print(tupl)

tupp = ("a","b","c")
tupe = tuple([i for i in list(tupp)])
print(tupp)
print(tupe)

alphabets = ("a","b","c")
a,b,c=alphabets  #unpacking tuple
print(a)
print(b)
print(c)

d= tupp+alphabets
print(d)
print(d.count("a"))
print(d.index("a"))