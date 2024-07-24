class kb:
    name="kumar"
    course="python"
    degree="BSc.CSIT"
    def __init__(self):
        print("Hey i am a constructor and i dont need any function call to get evoked")# dunder method(_ _)
    def getinfo(self):# self is a passed parameter so it can be anything like (a),(b),(ab),......
        print(f"The preffered language is {self.course} and the degree pursuing is {self.degree}")
        #if we wanna add a function that we dont need to pass any paremeter then we use '@staticmethod'
    @staticmethod
    def stat():
        print("Hi I am static and no parameter was passed")
kumar=kb()
# kumar.salary=1500000
kumar.course="Js"#It gives preference to object instance(attribute) over class class attribute
print(kumar.course)#here course is class attribute
# print(kumar.salary)#here salary is object 
kumar.getinfo()# which is equivalent to kb.getinfo(kumar)
kumar.stat()

