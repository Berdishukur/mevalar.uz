class Texnika:
    def __init__(self,brand, model, type):
        self.brand=brand
        self.model=model
        self.type=type
    def info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nType : {self.type}")
# texnika1=Texnika("07","Juguli","Mexanika")
# texnika1.info()
class Nootebooks(Texnika):
    def __init__(self,brand, model, type, video_card, ram, display):
        super().__init__(brand,model,type)
        self.video_card=video_card
        self.ram=ram
        self.display=display

    def more_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nType : {self.type}\nVido_Card : {self.video_card}\nRam : {self.ram}\nDesplay :{self.display}")
nootebook1=Nootebooks("Core","Acer","10-avlod","256","8","True")
nootebook1.more_info()













#
# class Odam:
#     holati=True
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print("Work is dunder")
#     def outPut(self):
#         print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}")
#
# # odam1=Odam("Ali",23,"Erkar")
# # odam1.outPut()
# class Shifokor(Odam):
#     def __init__(self,name,age,gender,dori):
#         super().__init__(name, age, gender)
#         self.dori=dori
#
#     def outPut(self):
#         print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}\nDori : {self.dori}")
# # shifokr1=Shifokor("Alisa",22,"ayol","Parasetamol")
# # shifokr1.outPut()
# # print(shifokr1.holati)
# class Jangchi(Odam):
#     def __init__(self,name,age,gender,qurol):
#         super().__init__(name, age, gender)
#         self.qurol=qurol
#
#     def outPut(self):
#         print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}\nQurol : {self.qurol}")

# jangchi1=Jangchi("Akobir",25,"Erkak","Qalqon")
# jangchi1.outPut()

# class SuperOdam(Shifokor,Jangchi):
#     def __init__(self,name,age,gender,dori,qurol):
#         super().__init__(name, age, gender,dori,qurol)
#
#     def outPut1(self):
#         print(f"Ism : {self.name}\nJinsi : {self.gender}\nYosh : {self.age}\nQurol : {self.qurol}\nDori : {self.dori}")
#
# s1=SuperOdam("Sevinch",22,"ayol","As","Qilich")
# print(s1.holati)













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




















