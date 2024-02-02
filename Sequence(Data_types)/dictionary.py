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

dic = {"a":1,"b":2,"c":3,"d":[4,5,6]}
print(dic)

print(dic["d"])
print(dic.get("d"))


print(dic.keys())
print(type(dic.keys()))

print(dic.values())
print(type(dic.values()))

print(dic.items())
print(type(dic.items()))


if "a" in dic:
    print("yes")
    
if "b" in dic.keys():
    print("yes")
    
if 3 in dic.values():
    print("yes")
    

dic["f"]="6"
print(dic)

dic.update({"e":5})
print(dic)


dic["e"]=7
print(dic)

dic.update({"f":8})
print(dic)


dic.pop("e")
print(dic)

dic.popitem()
print(dic)

del dic["d"]
print(dic)



for i in dic:
    print(i)

for i in dic:
    print(dic[i])
    
for i in dic.keys():
    print(i)
    
for i in dic.values():
    print(i)
    
for i in dic.items():
    print(i)
    

dic2 = dic   #it changes if dic is changed
print(dic2)

dic["e"]=4
print(dic2)

dic3 = dict(dic)         #dict and copy does not change if main dic is changed 
dic4 = dic.copy()

dic["f"]=5
print(dic)

print(dic3)
print(dic4)


lap = {
    "dell" : {"model": "i5","year" : 2022},
    "acer" : {"model" : "i7","year" : 2023}
}
print(lap)

dic = {{"1":1,"2":2},{"3":3,"4":4}} #we cannot create elements in dict as dicts it should be key-value pair
print(dic) # it creates unhashable type error


numeric = {
           "numbers":1,
           "float":1.4,
           "complex":1+5j
           }

sequence = {
            "list":[1,2,3],
            "tuple":(1,2,3),
            "set":{1,2,3},
            "dict":{'a':1,'b':2,'c':3}
}

data_types = {
    "non sequence": numeric,
    "sequence" : sequence
}

print(data_types)
print(data_types["sequence"]["dict"]["b"])
print(data_types["non sequence"]["complex"])


cities =("bangalore","chennai")
states = ("karnataka","tamilnadu")
dic = {i:k for i,k in zip(states,cities) if k == "chennai"}
print(dic)   


names = ["alice","paramesh","bog","bob"]

y = {name:len(name) if len(name)>4 else "short" for name in names }
print(y)


ages = {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 35}
u = {name:age if age<=30 else "old" for name,age in ages.items() }
print(u)

p = {name:age for name,age in ages.items() if age<=30}
print(p)
