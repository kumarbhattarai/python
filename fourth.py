f=open("test.txt",'rb')
# f.write("This is a latest write mode")
data=f.read()
print(data)
# lines=f.readlines()#It returns list 
# print(lines,type(lines))
# line=f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
f.close()
        
        
        # with statement

with open("test.txt") as f:
    print(f.read())
    #no need to close the file