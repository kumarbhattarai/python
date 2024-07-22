print("Hello world")
# To print multi-line
print(''' 
        this 
        is 
        a 
        multi-line
        code''')
# module
# pip install pyttsx3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Proceeding")
# engine.runAndWait()


# import os

# def list_directory_contents(path='E:\\sigma'):
#     try:
#         # Get the list of files and directories
#         with os.scandir(path) as entries:
#             for entry in entries:
#                 print(entry.name)
#     except FileNotFoundError:
#         print(f"The directory '{path}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # List contents of the specified directory
# list_directory_contents('E:\\sigma')


# import os
# directive = 'E:\\sigma'
# contents = os.listdir(directive)
# for item in contents:
# print(item)


# print(True or False)
# print(True and False)
# print(not(True))
# a="kumar"
# print(type(a))
# print(type(False))
# x=123
# y=float(x)
# print(type(x))
# print(x)
# print(y)
# print(type(y))
# x="121"
# y=float(x)
# print(type(x))
# print(type(y))
# p=input("Enter first number")
# q=input("Enter second number")
# print(p+q)#it concatinates as input take string
# p=int(p)
# q= int(q)
# print("The sum is",p+q)



name="kumar"
print(name[0:2]) #prints the name from array 0 to 1
print(name[0:5:2])#skips 2 letters
print(len(name))
print(name.endswith('r'))
print(name.capitalize())#.upper and .lower to make the whole word capital or small
print(name.find("r"))
print(name.replace("kumar","euresh"))
print("This is a escape \"sequence\;")
print("Good evening "+name+". What a lovely night to learn python")
#now it can be written as
print(f"Good evening {name}. What a lovely night to learn python ")
letter='''
    dear nam,
    you've been selected for furthur proceeding
    date
'''
print(letter.replace("nam","kumar").replace("date","7th jan 2025"))
# name[2]='t' It'll show error as we can't manipulate string . so we have list(immutable). 
fruits=["Apple","mango","9.80",1,2.5,False,"banana"]
# fruits[1]="papaya" #lists are mutable
# fruits[3]="string_cast"
# print(fruits[1])
# print(fruits[3])
# print(fruits[2])
# print(fruits[1:5])
fruits.append("kumar")
print(fruits)
#In string while operating some string functions a whole new string is made but in case of list the existing list is updated
l=[1,5,3,56,23,1] 

l.sort()
l.reverse()
fruits.insert(6,"NaN") #inserts NaN at 6th position
fruits.pop(6)#removes the value from the index 6
fruits.remove(1)#remove 1 if there is from the list
print(fruits)
print(l)
m=(1,3,"KB")
print(type(l))
print(type(m))
a=(1)#integer data type
a=(1,)#tuple data type


# method of tuple
m.count(3) #counts the number of 3 in the tuple a
print(m.index(1)) #gives the index at which there is 1
print(m+a)#concatenates 2 tuples and make another and then it prints
print(m*3)#prints tuple m 3 times
print(2 in m)#checks if there is 2 in my tuple
print(m[0:2])#slicing in tuple makes a whole new tuple as it is immutable
