x=[1,3,"kb",9.23]
i=0
while(i<len(x)):
    print(x[i])
    i+=1
for i in range(10,50,5): #start,end,stepsize  or simply for i in range(10) (goes from 0 t 9)
    if(i==45):
        break
    print(f"{i} ",end="")
    #in python if we wanna hold a certain task(loop,) we can use pass snd leave it empty