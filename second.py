# dictionary

# obj={}#empty set
obj = {
    "kumar":100,
    "euresh":65,
    "list":[1,2,3]
}
print(obj,type(obj))
print(obj["kumar"])#100(value) is asiigned to the key "kumar" so it will be printed
#O(1) time complexity of python dictionary. dict is mutable.
obj["kumar"]="eur"
print(obj["kumar"])
print(obj.items())#in tuples form
print(obj.keys())
print(obj.values())
obj.update({"euresh":99}) #updates the value of euresh 
# print(obj.get("ku"))#returns none
# print(obj["ku"])#returns error


# sets



# s=set() empty set 
s={1,2,42,32,1,1,1,1,"kb"} #set doesn't print duplicate values
print(s)#order is not maintained in set
# s.add(5,6)#this cant be done
s.add(5)#only one element at a time
print(s) #set is immutable and cant be accessed   by index
s.remove(2)
print(s)
s1={3,5,9,43,53}
print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
l=["kumar","euresh"]
name=input("Enter your name ")
if(name in l):
    print(f"{name} is in list")
    print("This'll also execute in if")
else:
    print("Not in list")
print("list contains")
print(l) 