
class Odam:
    holati=True
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Work is dunder")
    def outPut(self):
        print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}")

# odam1=Odam("Ali",23,"Erkar")
# odam1.outPut()
class Shifokor(Odam):
    def __init__(self,name,age,gender,dori):
        super().__init__(name, age, gender)
        self.dori=dori

    def outPut(self):
        print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}\nDori : {self.dori}")
shifokr1=Shifokor("Alisa",22,"ayol","Parasetamol")
shifokr1.outPut()
print(shifokr1.holati)



# class MyClass7 :
#     myDict={}
#     def add_element(self,key,val):
#         self.myDict[key]=val
#         print(self.myDict)
#     def update(self,key,val):
#         self.myDict[key]=val
#         print(self.myDict)
#
# MyClass7.add_element(MyClass7,"Ali","+998901234567")
# MyClass7.add_element(MyClass7,"Guzal","+998976543218")
# MyClass7.update(MyClass7,"Ali","+998991234567")




















